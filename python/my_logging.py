#Creating your own logging with file handler and stream handler

#import logging module from standard library
import logging


os.remove("my_log.txt") # first delete the my_log file if exists
logger = logging.getLogger(__name__)  #creating your logger name "__main__"
logger.setLevel(logging.DEBUG)   

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
stream_handler = logging.StreamHandler(sys.stdout) #Stream handler is used to print the output to a standard output unlike file
stream_handler.setLevel(logging.INFO). 
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("my_log.txt", mode='a')    #File handler is used to print log message to a file based on log level
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)


logger.addHandler(stream_handler)
logger.addHandler(file_handler)


logger.debug("This is debug go to stdout")
try:
    a = 10/0
except ZeroDivisionError:
    logger.error("This is error")     #we can also use logger.exception if we want more information 
else:
    logger.info("this is info")
    
    
    
#output stdoutput 
#2018-08-12 11:26:13,247:ERROR:This is error
#[Finished in 0.347s]
#my_log.txt
#2018-08-12 11:26:13,247:ERROR:This is error



