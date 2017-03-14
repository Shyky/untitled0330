# -*- coding: UTF-8 -*-
import os


def catch_android_device_http_log(dir_name):
    command = "adb logcat -d -v threadtime"
    reader = os.popen(command)
    m_action = ""
    url = ""
    method = ""
    param = ""
    param_format = ""

    find_str_url = "完成执行网络请求 --> 请求接口地址（URL）："
    find_str_method = "完成执行网络请求 --> 请求方式："
    find_str_param = "完成执行网络请求 --> 请求参数："
    find_str_param_format = "完成执行网络请求 --> 请求参数格式："
    find_str_response = "完成执行网络请求 --> 响应数据："

    # 死循环开始
    while True:
        line = reader.readline()

        if line.find("完成执行网络请求 --> ") != -1:
            print line

        # # 跳过
        # if line.find("action=app_show_word") != -1:
        #     continue

        if line.find(find_str_url) != -1:
            url = line[line.rfind(find_str_url) + len(find_str_url): len(line)]

        if line.find(find_str_method) != -1:
            method = line[line.rfind(find_str_method) + len(find_str_method): len(line)]

        if line.find(find_str_param) != -1:
            param = line[line.rfind(find_str_param) + len(find_str_param): len(line)]
            # "m_action="
            m_action = line[line.rfind("action=") + len("action="): len(line)]

        if line.find(find_str_param_format) != -1:
            param_format = line[line.rfind(find_str_param_format) + len(find_str_param_format): len(line)]

        if line.find(find_str_response) != -1:
            response = line[line.rfind(find_str_response) + len(find_str_response): len(line)]

            # 使用str.rstrip()方法删除空格
            # "w"是覆盖模式
            fo = open(dir_name + "\\" + m_action.rstrip() + ".txt", "w")
            fo_2 = open(dir_name + "\\" + m_action.rstrip() + ".all.txt", "w")
            fo_2.write("请求接口地址（URL）：\n\n\t" + url + "\n请求方式：\n\n\t" + method + "\n请求参数：\n\n\t" +
                       param + "\n请求参数格式：\n\n\t" + param_format + "\n响应数据：\n\n\t" + response)
            # 写入内容
            fo.write(response.rstrip())
            # 关闭文件
            fo.close()
            fo_2.close()

        if line == "":
            break

    # 死循环结束
    reader.close()


# Run
print "----------------------------------------", "Android HTTP Log Catch Tool v1.0", \
    "----------------------------------------"
input_str = ""
while True:
    input_str = raw_input("请输入APP名称：")
    if input_str.rstrip() != "":
        break

save_dir = "D:\\" + input_str + " app http response"
# 目录不存在才创建
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

while True:
    catch_android_device_http_log(save_dir)
