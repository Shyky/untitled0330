import os


# aapt Toolkit v1.0
def execute(command):
    """Execute the command with shell"""
    reader = os.popen(command)
    result = reader.read()
    reader.close()
    return result


class ApkInfo:
    """Apk file information"""

    def __init__(self, package, label, icon, version, sdk_version):
        self.package = package
        self.label = label
        self.version = version
        self.icon = icon
        self.sdk_version = sdk_version

    def package_name(self):
        return self.package

    def application_label(self, label):
        self.label = label

    def version_name(self, version):
        self.version = version

    def sdk_version(self, sdk_version):
        self.sdk_version = sdk_version

    def __str__(self):
        return "package = " + self.package + " , label = " + self.label \
               + " , version = " + self.version + " , icon = " + self.icon + " , sdk_version = " + self.sdk_version


def aapt_list(file_name):
    command = "aapt l " + file_name
    return execute(command)


def aapt_dump(apk_file_name):
    command = "aapt d " + apk_file_name
    return execute(command)


def aapt_dump_badging(apk_file_name):
    command = "aapt d badging " + apk_file_name
    result = execute(command)
    print result
    package_name = result[result.find("package: name='") + len("package: name='"):result.find("' versionCode=")]
    application_label = result[
                        result.find("application-label:'") + len("application-label:'"):result.find(
                            "'\napplication-icon-160:")]
    version_name = result[
                   result.find("versionName='") + len("versionName='"):result.find("' platformBuildVersionName=")]
    icon = result[
           result.find("icon='") + len("icon='"):result.find("'\napplication-debuggable")]
    sdk_version = result[
                  result.find("sdkVersion:'") + len("sdkVersion:'"):result.find("'\ntargetSdkVersion:")]
    apk_info = ApkInfo(package_name, application_label, icon, version_name, sdk_version)
    return apk_info


os.system("aapt")
print aapt_list("base.apk")
print aapt_dump("base.apk")
print aapt_dump_badging("base.apk")
