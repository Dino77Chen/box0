# -*- coding:utf-8 -*-

import pickle


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
my_log = log_def(file_path, "check.log", "I")
do_log = log_def(file_path, "check_do.log", "I")


def file_open(file_path_name, flag):
    try:
        n_file = open(file_path_name, flag)
        return n_file
    except FileNotFoundError:
        return -1


final_flag = True

lf = file_open(file_path + 'file_list.dump', 'rb')
if lf == -1:
    my_log.error("list file NotFound")
    final_flag = False
    exit(-1)
file_list = pickle.load(lf)
total_file = file_list.pop(0)
total_file_count = total_file[0]
lf.close()

for i in range(total_file_count):
    dump_file_name = file_path + str(i) + '_' \
        + str(file_list[i][0]) + '_' \
        + str(file_list[i][1]) + '.dump'
    do_log.info(dump_file_name)
    df = file_open(dump_file_name, 'rb')
    if df == -1:
        my_log.error("file NotFound: " + dump_file_name)
        final_flag = False
        break

    do_log.info("load dump file start")
    my_matrix = pickle.load(df)
    do_log.info("load dump file end")

    txt_file_name = file_path + str(i) + '_' \
        + str(file_list[i][0]) + '_' \
        + str(file_list[i][1]) + '.txt'
    tf = file_open(txt_file_name, 'r')
    if tf == -1:
        my_log.error("txt file NotFound" + txt_file_name)
        final_flag = False
        break

    do_log.info("read txt file start")
    line = tf.readline()
    l_line = line.split("|")
    l_line.pop()  # delete '\n'
    l_line = list(map(int, l_line))
    matrix = [l_line]
    while True:
        line = tf.readline()
        if len(line) == 0:
            break
        l_line = line.split("|")
        l_line.pop()  # delete '\n'
        l_line = list(map(int, l_line))
        # python2 l_line = map(int, l_line)
        matrix.append(l_line)
    do_log.info("read txt file end")

    do_log.info("diff matrix start")
    if my_matrix != matrix:
        my_log.error("matrix in dump : " + str(my_matrix))
        my_log.error("matrix in text : " + str(matrix))
        final_flag = False
    else:
        my_log.info("." + dump_file_name)
        my_log.info("." + txt_file_name)
    do_log.info("diff matrix end")

    df.close()
    tf.close()

if final_flag:
    my_log.info("All Right! \n")
else:
    my_log.error("Something Wrong! \n")
