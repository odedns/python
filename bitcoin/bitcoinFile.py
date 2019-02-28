from datetime import date, datetime, timedelta
import json

def create_file(stats_dict) :
    filename = "bitFile_" + datetime.today().strftime("%Y%m%d-%H%M%S")
    file_object = open(filename, "w")  # "r" is the default mode.
    str = json.dumps(stats_dict)

    file_object.write(str)




