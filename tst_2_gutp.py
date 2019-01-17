# -*- coding:utf-8 -*-

import random
import pickle
import time


def log_def(log_path, log_name, log_level):
    import logging
    logger = logging.getLogger(log_name)
    handler = logging.FileHandler(log_path + log_name)
    if log_level == 'C':
        logger.setLevel(level=logging.CRITICAL)
        handler.setLevel(logging.CRITICAL)
    elif log_level == 'E':
        logger.setLevel(level=logging.ERROR)
        handler.setLevel(logging.ERROR)
    elif log_level == 'W':
        logger.setLevel(level=logging.WARNING)
        handler.setLevel(logging.WARNING)
    elif log_level == 'I':
        logger.setLevel(level=logging.INFO)
        handler.setLevel(logging.INFO)
    elif log_level == 'D':
        logger.setLevel(level=logging.DEBUG)
        handler.setLevel(logging.DEBUG)
    else:
        logger.setLevel(level=logging.NOTSET)
        handler.setLevel(logging.NOTSET)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


file_path = './my_files/'
my_log = log_def(file_path, "generator.log", "D")
do_log = log_def(file_path, "generator_do.log", "D")


def create_file(fid, path):
    # 每行多少列
    x = random.randint(1, 1000)
    # 生成多少行
    y = random.randint(1, 10000)

    do_log.info(str(fid) + '_' + str(x) + '_' + str(y))
    my_matrix = [[x, y]]
    this_file_str = str(x) + '|' + str(y) + '|\n'

    do_log.info("create matrix tf start")
    for line in range(y):
        do_log.debug("line begin " + str(line))
        this_line = [random.randint(0, i * i) for i in range(x)]
        my_matrix.append(this_line)
        do_log.debug("--")

        this_line_str = ''
        for d in this_line:
            this_line_str = this_line_str + str(d) + '|'

        this_file_str = this_file_str + this_line_str + '\n'
        do_log.debug("line end " + str(line) + "\n")
    do_log.info("create matrix tf end")

    do_log.info("write file tf start")
    tf = open(path + str(fid) + '_' + str(x) + '_' + str(y) + '.txt', 'w')
    tf.write(this_file_str)
    tf.close()
    do_log.info("write file tf end")

    do_log.info("write file df start")
    df = open(path + str(fid) + '_' + str(x) + '_' + str(y) + '.dump', 'wb')
    pickle.dump(my_matrix, df)
    df.close()
    do_log.info("write file df end")

    return x, y


# 一共生成几个文件
file_count = 2
# 最大文件生成的时间间隔
max_sleep_time = 3

total_file = 0
total_sleep_time = 0

# file_list文件首行
file_list = [[file_count]]

for f in range(file_count):
    sleep_time = random.randint(1, max_sleep_time)
    time.sleep(random.randint(1, sleep_time))
    fx, fy = create_file(f, file_path)
    file_list.append([fx, fy])
    my_log.info(str(f) + '_' + str(fx) + '_' + str(fy))
    total_file = total_file + 1
    total_sleep_time = total_sleep_time + sleep_time

lf = open(file_path + 'file_list.dump', 'wb')
pickle.dump(file_list, lf)
my_log.info('All done.' +
            '    total sleep time:' + str(total_sleep_time) +
            '    total_file:' + str(total_file))
