import sys
from flask import Flask, render_template,request
from exception import CustomException
from flask_mysqldb import MySQL
import pymysql
import pandas as pd
import os
import logging
#import pickle
import numpy as np

host = "localhost"
user = "root"
password = "arp570afx984"
db = "mydb"

def read_sql_data():
    logging.info("reading sql database")
    try:
        mydb = pymysql.connect(
            host=host,
            user = user,
            password=password,
            db=db
        )
        logging.info("Connection established",mydb)
        df = pd.read_sql_query("select * from students",mydb)
        print(df.head())
        return df
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)