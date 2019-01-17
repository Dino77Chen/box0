# -*- coding:utf-8 -*-

import os
import datetime


def list_path(path):
    this_list = os.listdir(path)
    for this_one in this_list:
        if os.path.isfile(path + this_one):
            file_time = os.path.getmtime(path + this_one)
            file_time = datetime.datetime.utcfromtimestamp(file_time)
            now_time = datetime.datetime.now()
            delta_time = (now_time - file_time).seconds
            if delta_time > 300:
                cmdstr = "dir " + path + this_one
                print(cmdstr)
                os.system(cmdstr)


list_path("my_files/")
