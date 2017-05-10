# **Nas Auto mapper**

Windows Nas auto mapper is a simple systray and GUI screen app for windows. It is coded with Python 2.7 and PyQt5.
It fixes the lack of auto remapping network folders after rebooting windows, and are focued on mapping NAS via there DNS name.

Installer does not depend on either python or Qt installations.



[![](https://img.shields.io/badge/Twitter--blue.svg?maxAge=2592000)](https://twitter.com/zadow28) ![Python version](https://img.shields.io/badge/python-2.7-brightgreen.svg?maxAge=2592000) ![PyQ5t](https://img.shields.io/badge/PyQt5-5.6-orange.svg) ![npm](https://img.shields.io/npm/l/express.svg?maxAge=2592000) [![](https://img.shields.io/badge/Donate-Paypal-blue.svg?maxAge=2592000)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=8KXM6W2JVRUWL)[![](https://img.shields.io/badge/Latest release--red.svg?maxAge=2592000)](https://github.com/techbliss/NAS_DNS_AUTOMAPPER/releases/tag/releases)

# **Screens**

**System tray**

![systray](https://cloud.githubusercontent.com/assets/3592375/18998381/cbffc7ba-8738-11e6-973f-51f3f6dd6b2d.png)

**Gui**


<img width="426" alt="mapper" src="https://cloud.githubusercontent.com/assets/3592375/25897558/a761e61e-3588-11e7-808b-ff1a12d859f0.png">

# **Usage**

App will show in windows system tray menu.
left click icon to setup new server at forst launch, or when changing server.
right click for other options.
**Dont type https://, just type dns name like screenshot of GUI**

# **Installer**

Simply install the installer, and find it under system tray menu.
Remember to setup server at first launch.

# **Run with Python code without installer**
# **Build installer yourself**
*Tools needed*

[Inno Install](http://www.jrsoftware.org/isinfo.php)

[PyInstaller](https://github.com/pyinstaller/pyinstaller)

from repo folder type

`pyinstaller --window --icon=app.ico WebDav.py icons.py`


**Find build under dist.**

from **PyQt5** folder copy platforms from **PyQt5\plugins\**


to **dist\WebDavMain**

also copy the **ffmpeg** folder with **subfolders** build folder

to **dist\WebDavMain**

Use supplied innosetup script to build. and install

# **Todo**
Adope prompts for password


# **Credits**

[![](https://img.shields.io/badge/Iconfinder free icons--red.svg?maxAge=2592000)](https://www.iconfinder.com)

 *@Fearless for the batch script.*

[](https://github.com/mrfearless)


**Donaters**

Many thanks to [![](https://img.shields.io/badge/Jetbrains-Company-blue.svg?maxAge=2592000)](https://www.jetbrains.com/) for donating a opensource licence.


![icon_upsource](https://cloud.githubusercontent.com/assets/3592375/20355736/9f4a6842-ac22-11e6-9901-9055ae8f1a69.png)![icon_pycharm](https://cloud.githubusercontent.com/assets/3592375/20355738/9f4f9bfa-ac22-11e6-8e1b-e49ba71b672c.png)




