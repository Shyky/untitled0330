# set encoding
# -*- coding: UTF-8 -*-
from Tkinter import *

import adb

top = Tk()
top.title = "Android调试控制台"

# frame_left_top = Frame(width=380, height=270, bg='white')

lb_connected_devices = Listbox()
lb_installed_packages = Listbox()
lb_package_locations = Listbox()
# bn_uninstall = Button("Uninstall")

connect_devices = adb.adb_devices()
installed_packages = adb.adb_shell_pm_list_packages()

for item in connect_devices:
    lb_connected_devices.insert(0, item)
for item in installed_packages:
    lb_installed_packages.insert(0, item)
    # lb_package_locations.insert(0, adb.adb_shell_pm_path(item))

# 将小部件放置到主窗口中
# frame_left_top.grid(row=0, column=0, padx=2, pady=5)
lb_connected_devices.pack()
lb_installed_packages.pack()
lb_package_locations.pack()
# bn_uninstall.pack()

# 进入消息循环
top.mainloop()
