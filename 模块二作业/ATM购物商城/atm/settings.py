import os
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logger_consume = logging.getLogger('consume')
logger_operation = logging.getLogger('operation')

logger_consume.setLevel(logging.INFO)
logger_operation.setLevel(logging.INFO)

consume_log_file_path = BASE_DIR + '/logs/consume.log'
operation_log_file_path = BASE_DIR + '/logs/operation.log'

consume_fh = logging.FileHandler(consume_log_file_path)
consume_fh.setLevel(logging.INFO)
consume_ch = logging.StreamHandler()
consume_ch.setLevel(logging.ERROR)

operation_fh = logging.FileHandler(operation_log_file_path)
operation_fh.setLevel(logging.INFO)
operation_ch = logging.StreamHandler()
operation_ch.setLevel(logging.ERROR)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

consume_fh.setFormatter(formatter)
consume_ch.setFormatter(formatter)

operation_fh.setFormatter(formatter)
operation_ch.setFormatter(formatter)

logger_consume.addHandler(consume_fh)
logger_consume.addHandler(consume_ch)

logger_operation.addHandler(operation_fh)
logger_operation.addHandler(operation_ch)




