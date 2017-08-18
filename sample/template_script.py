from importlib.machinery import SourceFileLoader
logger = SourceFileLoader("LoggerHandler", "../lib/logger_handler.py").load_module()
conf_handler = SourceFileLoader("confHandler", "../lib/conf_handler.py").load_module()
import time
import os

###############################################################################
##  insert description about the script here
###############################################################################

appname = 'template_script'

def main(logger):

    #set up conf
    config = conf_handler.ConfHandler('../conf/test.ini')
    section = 'test_section'
    test_value = config.get(section,'test_key')
    
    #run
    logger.info('******************************************************',False)
    logger.info('**************** ' + appname + ' starting .. ***************',False)
    logger.info('******************************************************',False)
    time_start = time.time()

    logger.info('*********** WRITE CODE HERE ****************')

    logger.info('Value loaded from conf: ' + test_value,False)
    
    str_time = str(time.time() - time_start)
    logger.info(appname + ' finished in ' + str_time[:str_time.index('.')+3] + ' secs..',False)
    logger.info('------------------------------------------------------------',False)    


if __name__ == "__main__":

    #set up logger
    logger = logger.LoggerHandler(appname)
    
    try:
        main(logger)
    except Exception as e:
        logger.fatal(str(e))
        
    #close logger
    logger.close()
