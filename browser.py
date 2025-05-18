import gi
import os
import sys
import urllib.request
import hashlib

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")

from gi.repository import Gtk, WebKit2

# === GitHub auto-update ===
REPO_URL = "https://raw.githubusercontent.com/pullchocks/umbranet/main/browser.py"

def hash_file(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def check_for_update():
    print("🔍 Checking for browser.py updates...")
    local_hash = hash_file("browser.py")

    try:
        response = urllib.request.urlopen(REPO_URL)
        remote_content = response.read()
        remote_hash = hashlib.sha256(remote_content).hexdigest()

        if local_hash != remote_hash:
            print("⬇️  Update found. Updating browser.py...")
            with open("browser.py", "wb") as f:
                f.write(remote_content)
            print("✅ Updated. Please relaunch.")
            sys.exit(0)
        else:
            print("✅ browser.py is up to date.")
    except Exception as e:
        print(f"⚠️  Update check failed: {e}")

check_for_update()

# === Browser App ===
class PrivateBrowser(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Umbranet Browser")
        self.set_default_size(1000, 700)

        self.web_context = WebKit2.WebContext.get_default()
        self.webview = WebKit2.WebView.new_with_context(self.web_context)

        self.set_private_mode(True)
        self.set_javascript_enabled(True)
        self.set_cookie_policy(False)
        self.set_proxy(use_tor=False)

        scrolled = Gtk.ScrolledWindow()
        scrolled.add(self.webview)
        self.add(scrolled)

        self.add_header_bar()
        self.webview.load_uri("https://example.com")

    def set_private_mode(self, enabled):
        settings = self.webview.get_settings()
        settings.set_property("enable-private-browsing", enabled)

    def set_javascript_enabled(self, enabled):
        settings = self.webview.get_settings()
        settings.set_property("enable-javascript", enabled)

    def set_cookie_policy(self, block_all):
        mgr = self.web_context.get_cookie_manager()
        policy = WebKit2.CookieAcceptPolicy.NEVER if block_all else WebKit2.CookieAcceptPolicy.ALWAYS
        mgr.set_accept_policy(policy)

    def set_proxy(self, use_tor):
        proxy_settings = WebKit2.NetworkProxySettings.new(
            "socks5h://127.0.0.1:9050" if use_tor else "direct", []
        )
        self.web_context.set_network_proxy_settings(
            WebKit2.NetworkProxyMode.DEFAULT, proxy_settings
        )

    def add_header_bar(self):
        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Umbranet"

        js_button = Gtk.ToggleButton(label="JS")
        js_button.set_active(True)
        js_button.connect("toggled", self.toggle_js)

        tor_button = Gtk.ToggleButton(label="Tor")
        tor_button.set_active(False)
        tor_button.connect("toggled", self.toggle_tor)

        cookie_button = Gtk.ToggleButton(label="Cookies")
        cookie_button.set_active(True)
        cookie_button.connect("toggled", self.toggle_cookies)

        header.pack_start(js_button)
        header.pack_start(cookie_button)
        header.pack_end(tor_button)

        self.set_titlebar(header)

    def toggle_js(self, button):
        enabled = button.get_active()
        self.set_javascript_enabled(enabled)
        self.webview.reload()

    def toggle_tor(self, button):
        self.set_proxy(use_tor=button.get_active())
        self.webview.reload()

    def toggle_cookies(self, button):
        self.set_cookie_policy(block_all=not button.get_active())
        self.webview.reload()

if __name__ == "__main__":
    app = PrivateBrowser()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
