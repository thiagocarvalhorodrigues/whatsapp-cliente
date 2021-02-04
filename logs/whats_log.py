import logging
import os

dir_path = os.getcwd()

def funcao_debug(debug):
    logging.basicConfig(filename=dir_path + '\\logs\\whats.log', filemode="w", format='%(levelname)s %(asctime)s %(message)s',datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.StreamHandler()
    logging.getLogger('').addHandler(logger)
    arquivo_debug = logging.debug(debug)

    return arquivo_debug

def funcao_info(info):
    logging.basicConfig(filename=dir_path + '\\logs\\whats.log', filemode="w", format='%(levelname)s %(asctime)s %(message)s',datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.StreamHandler()
    logging.getLogger('').addHandler(logger)
    arquivo_info = logging.info(info)

    return (arquivo_info)

def funcao_warning(warning):
    logging.basicConfig(filename=dir_path + '\\logs\\whats.log', filemode="w", format='%(levelname)s %(asctime)s %(message)s',datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.StreamHandler()
    logging.getLogger('').addHandler(logger)
    arquivo_warning = logging.warning(warning)

    return arquivo_warning

def funcao_error(error):
    logging.basicConfig(filename=dir_path + '\\logs\\whats.log', filemode="w", format='%(levelname)s %(asctime)s %(message)s',datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.StreamHandler()
    logging.getLogger('').addHandler(logger)
    arquivo_error = logging.error(error)

    return arquivo_error

def funcao_critical(critical):
    logging.basicConfig(filename=dir_path + '\\logs\\whats.log', filemode="w", format='%(levelname)s %(asctime)s %(message)s',datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.StreamHandler()
    logging.getLogger('').addHandler(logger)
    arquivo_critical = logging.critical(critical)

    return arquivo_critical






