import os

command_adb = "adb"
command_adb_shell = command_adb + " shell"
command_adb_shell_pm = command_adb_shell + " pm"

# aapt
command_aapt = "aapt"


def list_devices():
    # List connect Android devices
    command = command_adb + " devices"
    os.system(command)


def list_packages():
    # List installed packages
    command = command_adb_shell_pm + " list packages"
    os.system(command)


def dumpsys_package(package_name):
    # Show the specify package's information
    command = command_adb_shell + " dumpsys package " + package_name
    reader = os.popen(command)
    result = reader.read()
    version_name = result[result.find("versionName=") + len("versionName="): result.find("dataDir=")]
    resource_path = result[result.find("resourcePath=") + len("resourcePath="): result.find("nativeLibraryPath=")]
    print "------ package information ------\n"
    print package_name + "\t" + "dd" + "\t" + version_name.rstrip() + "\t" + resource_path.rstrip()
    print result
    reader.close()


def show_package_path(package_name):
    command = command_adb_shell_pm + " path " + package_name
    os.system(command)


def get_package_path(package_name):
    command = command_adb_shell_pm + " path " + package_name
    reader = os.popen(command)
    result = reader.read()
    reader.close()
    return result[8:len(result)]


def pull_file_from_device(file_name_or_dir, save_dir):
    command = command_adb + " pull " + file_name_or_dir + " " + save_dir
    os.system(command)


def push_file_into_device(file_or_dir_name, save_dir):
    command = command_adb + " push " + file_or_dir_name + " " + save_dir
    os.system(command)


def adb_logcat():
    command = command_adb + " logcat"
    os.system(command)


def aapt_dabging(apk_path):
    command = command_aapt + " d badging " + apk_path
    os.system(command)

    reader = os.popen(command)
    result = reader.read()
    reader.close()
    start = result.find("application-label:'") + 1
    print "start", start
    application_label = result[start:20]
    print "-->", application_label


print "-------------------------------- ADB Toolkit v1.0 --------------------------------"
print "1.List connect Android devices\t2.List installed packages"
menu = raw_input()
if menu == "1":
    list_devices()
else:
    list_packages()

    dumpsys_package("com.android.music")
    apk_path = get_package_path("com.android.music")
    print apk_path
    pull_file_from_device(apk_path, "E:\\xx")
    # rfind method from the end to find
    apk_file_name = apk_path[apk_path.rfind("/") + 1:len(apk_path)]
    aapt_dabging(apk_file_name)
    adb_logcat()
