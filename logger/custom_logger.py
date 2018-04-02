import inspect
import logging

def customLogger(logLevel):

	loggerName = inspect.stack()[1][3]
	logger = logging.getLogger(loggerName)

	logger.setLevel(logging.DEBUG)

	fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='w')
	fileHandler.setLevel(logLevel)

	formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(funcName)20s() -%(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

	fileHandler.setFormatter(formatter)
	logger.addHandler(fileHandler)

	return logger
