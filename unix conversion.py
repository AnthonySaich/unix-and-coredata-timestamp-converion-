import time
from time import mktime
import datetime
from datetime import datetime
epoch = time.time()


def epochtimetodate():
    epochtimetodate = (float(input("what epoch time do you want to know ")))
    date = time.strftime('%d-%m-%y %H:%M:%S', time.localtime(epochtimetodate))

    print(date)
    main()


def mac():
    coredata_timestamp = (float(input("What mac time do you want convert?")))
    coredata_start_date = datetime(2001, 1, 1, 0, 0, 0, 0, tzinfo=None)
    coredata_start_unix = int(mktime(coredata_start_date.timetuple()))
    unix_timestamp = coredata_start_unix + coredata_timestamp
    date = time.strftime('%d-%m-%y %H:%M:%S', time.localtime(unix_timestamp))
    print (date)
    
    main()
    
    

def main():
    print(epoch)
    menu = input ("""What would like to chose
1 = Unix to human readable
2 = MAC os to human readable 
                  """)
    
    
    if menu == "1":
        epochtimetodate()
    elif menu == "2":
        mac()
        
    pass
    main()
main()


    

