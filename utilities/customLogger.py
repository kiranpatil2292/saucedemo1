import inspect
import logging
import os


class LogGen():
    @staticmethod
    def loggen():
        # path = os.path.abspath(os.curdir) + "\\logs\\automation.log"
        # logging.basicConfig(filename=path,
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # logger = logging.getLogger()
        # logger.setLevel(logging.DEBUG)
        # return logger

        # name = inspect.stack()[1][3]
        logger = logging.getLogger()
        file = logging.FileHandler(os.path.abspath(os.curdir) + "\\logs\\automation.log")
        Format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        file.setFormatter(Format)
        logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger
