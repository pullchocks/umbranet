import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class PrivateBrowser(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Private WebKit Browser")
        self.set_default_size(1000, 800)

        # Default toggle states
        self.js_enabled = False
        self.cookies_enabled = False
        self.private_mode = True
        self.tor_enabled = False

        self.init_ui()
        self.create_webview()
        self.load_page()

    def init_ui(self):
        header = Gtk.HeaderBar(title="Privacy Browser")
        header.set_show_close_button(True)
        self.set_titlebar(header)

        # JS toggle
        self.js_switch = Gtk.Switch()
        self.js_switch.set_active(self.js_enabled)
        self.js_switch.connect("notify::active", self.on_toggle)
        header.pack_start(Gtk.Label(label="JavaScript"))
        header.pack_start(self.js_switch)

        # Cookies toggle
        self.cookie_switch = Gtk.Switch()
        self.cookie_switch.set_active(self.cookies_enabled)
        self.cookie_switch.connect("notify::active", self.on_toggle)
        header.pack_start(Gtk.Label(label="Cookies"))
        header.pack_start(self.cookie_switch)

        # Private toggle
        self.private_switch = Gtk.Switch()
        self.private_switch.set_active(self.private_mode)
        self.private_switch.connect("notify::active", self.on_toggle)
        header.pack_end(Gtk.Label(label="Private"))
        header.pack_end(self.private_switch)

        # Tor toggle
        self.tor_switch = Gtk.Switch()
        self.tor_switch.set_active(self.tor_enabled)
        self.tor_switch.connect("notify::active", self.on_toggle)
        header.pack_end(Gtk.Label(label="Tor"))
        header.pack_end(self.tor_switch)

    def create_webview(self):
        self.web_context = WebKit2.WebContext.get_default()

        if self.tor_enabled:
            self.web_context.set_network_proxy_settings(
                WebKit2.NetworkProxyMode.MANUAL,
                {
                    "http": "socks5://127.0.0.1:9050",
                    "https": "socks5://127.0.0.1:9050"
                }
            )
        else:
            self.web_context.set_network_proxy_settings(WebKit2.NetworkProxyMode.DEFAULT, {})

        if self.private_mode:
            manager = WebKit2.WebsiteDataManager.new_ephemeral()
        else:
            manager = WebKit2.WebsiteDataManager.new()

        self.web_context.set_website_data_manager(manager)

        self.webview = WebKit2.WebView.new_with_context(self.web_context)
        self.settings = self.webview.get_settings()
        self.settings.set_enable_javascript(self.js_enabled)
        self.settings.set_enable_plugins(False)
        self.settings.set_enable_webgl(False)
        self.settings.set_enable_html5_local_storage(self.cookies_enabled)
        self.settings.set_enable_html5_database(self.cookies_enabled)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)
        self.add(scrolled_window)

    def load_page(self):
        self.webview.load_uri("https://check.torproject.org")

    def on_toggle(self, switch, gparam):
        # Read toggle states
        self.js_enabled = self.js_switch.get_active()
        self.cookies_enabled = self.cookie_switch.get_active()
        self.private_mode = self.private_switch.get_active()
        self.tor_enabled = self.tor_switch.get_active()

        # Recreate webview with updated settings
        self.remove(self.webview.get_parent())
        self.create_webview()
        self.load_page()
        self.show_all()

if __name__ == "__main__":
    app = PrivateBrowser()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
