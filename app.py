from src.AIproject.logger import logging
from src.AIproject.exception import CustomException
import sys


if __name__=="__main__":
    logging.info("The executio has started")
 
    try:
        100/0
        
    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e,sys)
    
    