🚀 Launching Umbranet...
🔍 Checking for browser.py updates...
✅ browser.py is up to date.
libEGL warning: failed to open /dev/dri/renderD128: Permission denied

libEGL warning: failed to open /dev/dri/card0: Permission denied


** (browser.py:495): WARNING **: 23:54:15.216: webkit_settings_set_enable_private_browsing is deprecated and does nothing, use #WebKitWebView:is-ephemeral or #WebKitWebContext:is-ephemeral instead

** (browser.py:495): CRITICAL **: 23:54:15.216: WebKitNetworkProxySettings *webkit_network_proxy_settings_new(const char *, const char *const *): assertion 'URL(String::fromUTF8(defaultProxyURI)).isValid()' failed
Traceback (most recent call last):
  File "/home/pullchocks/umbranet/browser.py", line 122, in <module>
    app = PrivateBrowser()
          ^^^^^^^^^^^^^^^^
  File "/home/pullchocks/umbranet/browser.py", line 55, in __init__
    self.set_proxy(use_tor=False)
  File "/home/pullchocks/umbranet/browser.py", line 78, in set_proxy
    proxy_settings = WebKit2.NetworkProxySettings.new(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: constructor returned NULL
Traceback (most recent call last):
  File "C:\Users\johna\OneDrive\Desktop\Umbranet_Installer\umbranet_installer.py", line 140, in <module>
    main()
  File "C:\Users\johna\OneDrive\Desktop\Umbranet_Installer\umbranet_installer.py", line 120, in main
    install_umbranet()
  File "C:\Users\johna\OneDrive\Desktop\Umbranet_Installer\umbranet_installer.py", line 79, in install_umbranet
    wsl_run("cd ~/umbranet && DISPLAY=$DISPLAY python3 browser.py")
  File "C:\Users\johna\OneDrive\Desktop\Umbranet_Installer\umbranet_installer.py", line 63, in wsl_run
    subprocess.run(["wsl", "-d", WSL_DISTRO, "--", "bash", "-c", command], check=True)
  File "C:\Users\johna\AppData\Local\Programs\Python\Python312\Lib\subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['wsl', '-d', 'Debian', '--', 'bash', '-c', 'cd ~/umbranet && DISPLAY=$DISPLAY python3 browser.py']' returned non-zero exit status 1.
PS C:\Users\johna\OneDrive\Desktop\Umbranet_Installer>