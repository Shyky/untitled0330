# -*- coding: UTF-8 -*-
import os

# ADB ToolKit v1.0
command_adb = "adb"
command_aapt = "aapt"
command_adb_shell = command_adb + " shell"
command_adb_shell_pm = command_adb_shell + " pm"


def execute(command):
    """Execute the command with shell"""
    reader = os.popen(command)
    result = reader.read()
    reader.close()
    return result


def adb_devices():
    """List connect Android devices"""
    command = command_adb + " devices"
    result = execute(command)
    devices = result.split("\n")
    for item in devices:
        if item.startswith("List of devices"):
            devices.remove(item)
        if item.startswith("\n"):
            devices.remove(item)
    return devices


def adb_wait_for_device():
    command = command_adb + " wait-for-device"
    os.system(command)


def adb_install(apk_file_name, override=None):
    """Install the apk into Android device"""
    if override:
        command = command_adb + " install -r " + apk_file_name
    else:
        command = command_adb + " install " + apk_file_name
    result = execute(command)
    return result


def adb_uninstall(package_name, keep_data=None):
    if keep_data:
        command = command_adb + " uninstall -k " + package_name
    else:
        command = command_adb + " uninstall " + package_name
    os.system(command)


def adb_pull(remote_file_or_dir_name, local_dir_name=""):
    """Pull file from Android device"""
    command = command_adb + " pull " + remote_file_or_dir_name + " " + local_dir_name
    result = execute(command)
    return result


def adb_push(local_file_name, remote_dir_name):
    """Push file into Android device"""
    command = command_adb + " push " + local_file_name + " " + remote_dir_name
    result = execute(command)
    return result


def adb_shell_pm_list_packages():
    """List installed packages"""
    command = command_adb_shell_pm + " list packages"
    result = execute(command)
    packages = result.replace("package:", "").replace("\r", "").split("\n")
    return packages


def adb_shell_pm_path(package_name):
    """Show the specify package location"""
    command = command_adb_shell_pm + " path " + package_name
    result = execute(command)
    return result[len("package:"):len(result)]


def adb_logcat():
    command = command_adb + " logcat -d -v threadtime"
    reader = os.popen(command)
    m_action = ""
    # 死循环开始
    while True:
        line = reader.readline()
        print line
        if line.find("完成执行网络请求 --> 请求参数：") != -1:
            m_action = line[line.rfind("m_action=") + len("m_action="): len(line)]
            print m_action

        if line.find("完成执行网络请求 --> 响应数据：") != -1:
            response = line[line.rfind("完成执行网络请求 --> 响应数据：") +
                            len("完成执行网络请求 --> 响应数据："): len(line)]

            # 使用str.rstrip()方法删除空格
            # "w"是覆盖模式
            fo = open("D:\\temp_apk\\dresslily app http response\\" + m_action.rstrip() + ".txt", "w")
            # 写入内容
            fo.write(response.rstrip())
            # 关闭文件
            fo.close()

        if line == "":
            break

    # 死循环结束
    reader.close()
    # return result

    # result = execute(command)
    # return result


# Test
# print adb_shell_pm_list_packages()
# path = adb_shell_pm_path("com.android.providers.telephony")
# print path
# print adb_pull(path)

while True:
    adb_logcat()
