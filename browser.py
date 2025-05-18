#!/usr/bin/env python3
# 🚀 Launching Umbranet...

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2


class PrivateBrowser:
    def __init__(self):
        print("🪟 Initializing Umbranet window...")
        self.window = Gtk.Window(title="Umbranet")
        self.window.set_default_size(1000, 700)
        self.window.connect("destroy", Gtk.main_quit)

        print("🌐 Setting up web context...")
        self.web_context = WebKit2.WebContext.get_default()

        print("🧭 Creating web view...")
        self.webview = WebKit2.WebView.new_with_context(self.web_context)

        if hasattr(self.webview, "set_ephemeral"):
            print("🛡️ Enabling ephemeral (private) mode...")
            self.webview.set_ephemeral(True)
        else:
            print("⚠️ Ephemeral mode not supported in this WebKit version.")

        self.scroller = Gtk.ScrolledWindow()
        self.scroller.add(self.webview)
        self.window.add(self.scroller)

        print("🔧 Applying proxy settings...")
        self.set_proxy(use_tor=False)  # Change to True to enable Tor proxy

        print("🌍 Loading homepage...")
        self.webview.load_uri("https://www.duckduckgo.com")

        print("✅ Showing window.")
        self.window.show_all()

    def set_proxy(self, use_tor=True):
        if use_tor:
            proxy_uri = "socks5://127.0.0.1:9050"
            try:
                print("🧅 Setting Tor proxy...")
                proxy_settings = WebKit2.NetworkProxySettings.new("socks", [proxy_uri])
                self.web_context.set_network_proxy_settings(
                    WebKit2.NetworkProxyMode.CUSTOM,
                    proxy_settings
                )
                print("✅ Tor proxy applied.")
            except Exception as e:
                print(f"⚠️ Failed to set Tor proxy: {e}")
        else:
            print("🚫 Disabling proxy (default settings)...")
            self.web_context.set_network_proxy_settings(
                WebKit2.NetworkProxyMode.DEFAULT,
                None
            )


if __name__ == "__main__":
    print("🚀 Launching Umbranet browser...")
    app = PrivateBrowser()
    Gtk.main()
