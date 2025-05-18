import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2


class PrivateBrowser:
    def __init__(self):
        self.window = Gtk.Window(title="Umbranet")
        self.window.set_default_size(1000, 700)
        self.window.connect("destroy", Gtk.main_quit)

        self.web_context = WebKit2.WebContext.get_default()
        self.webview = WebKit2.WebView.new_with_context(self.web_context)
        self.webview.set_ephemeral(True)  # Enable private browsing

        self.scroller = Gtk.ScrolledWindow()
        self.scroller.add(self.webview)
        self.window.add(self.scroller)

        self.set_proxy(use_tor=True)

        self.webview.load_uri("https://www.duckduckgo.com")
        self.window.show_all()

    def set_proxy(self, use_tor=True):
        if use_tor:
            try:
                proxy_settings = WebKit2.NetworkProxySettings.new("socks", ["socks5://127.0.0.1:9050"])
                self.web_context.set_network_proxy_settings(
                    WebKit2.NetworkProxyMode.CUSTOM,
                    proxy_settings
                )
            except Exception as e:
                print(f"⚠️ Failed to set proxy: {e}")
        else:
            # Disable proxy
            self.web_context.set_network_proxy_settings(
                WebKit2.NetworkProxyMode.DEFAULT,
                None
            )


if __name__ == "__main__":
    app = PrivateBrowser()
    Gtk.main()
