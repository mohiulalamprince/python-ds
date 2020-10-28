import pandas as pd
import time
from datetime import datetime
import sys

url1 = "https://www.worldometers.info/coronavirus/"

while (True):
    try:
        data1 = pd.read_html(url1)

        str_time = str(time.time()) 
        
        file_log_writer = open("/Users/prince/data/corona/" + "log.txt", "a")
        data1[0].to_csv("/Users/prince/data/corona/" + str_time + ".csv", sep=',')

        str_log = str_time + "\t\t" + str(datetime.now()) + "\n"
        print (str_log)
        
        file_log_writer.write(str_log)
        file_log_writer.close()
    except Exception as e:
        print ("Exception " + str(e))
    except:
        print("Unexpected error:", sys.exc_info()[0])

