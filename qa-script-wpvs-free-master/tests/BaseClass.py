import inspect
import logging
import os

import pytest

from config import TestData
from utilities.helper import get_test_run_id


@pytest.mark.usefixtures("setUp")
class BaseClass:

    run_id = get_test_run_id('WPVSF')
    print('\n------ New Test Run with ID', run_id, 'is created ------\n')
    print('Running test on site ', TestData.BASE_URL)
    print('\n', 'Collecting Tests')

    def getLogger(self):
        # loggerName = inspect.stack()[1][3]
        # logger = logging.getLogger(loggerName)
        # fileHandler = logging.FileHandler('logfile.log')
        # formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        # fileHandler.setFormatter(formatter)
        # logger.addHandler(fileHandler)
        # logger.setLevel(logging.INFO)
        # fileHandler.close()
        # if os.path.exists("logfile.log"):
        #     os.remove("logfile.log")
        # return logger
        pass
