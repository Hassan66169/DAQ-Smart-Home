from my_masterclass import *       # Make sure to Import class to avoid Error !
import time
x=0
HumanPresence = 1
Temperature = 29

# ==================== Thingspeak =========================================

w_key = 'ESRH8DHQX652MI6O' #'Your Write key goes here '
r_key = 'LNABE72V7RL5LSEA' #'your read key goes here '
channel_id = 1975953 #83234                              # replace with channel id
while True:
    ob = Thingspeak(write_api_key=w_key, read_api_key=r_key, channel_id=channel_id)
    ob.post_cloud(value1=x,value2=Temperature)
    time.sleep(50)
    Data = ob.read_cloud(result=1)                # change result=number of data you want
    print(Data)
    (LED, Fan) = Data
    print(LED, Fan)
    if x==0:
        x=1
    else:
        x=0
    
        
        
    
