import logging

def set_logger(logger_name=None):
    '''
    This methods configures and outputs the centralized logger
    So each module does not need to warry about this
    '''
    
    logger = logging.getLogger(logger_name)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)
    
    return logger
    