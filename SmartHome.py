from my_masterclass import *       # Make sure to Import class to avoid Error !
import time
import cv2

thres = 0.5 # Threshold to detect object
nms_thres = 0.5

classNames= []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
# print(len(classNames))
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getobjects(img, draw=True, objects = []):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold = nms_thres)
    # print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId-1]
            if className in objects:
                objectInfo.append([box, className]) 
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,className.upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    return img, objectInfo


x=0
# HumanPresence = 1
Temperature = 30

# ==================== Thingspeak =========================================

w_key = 'ESRH8DHQX652MI6O' #'Your Write key goes here '
r_key = 'LNABE72V7RL5LSEA' #'your read key goes here '
channel_id = 1975953 #83234                              # replace with channel id

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    # cap.set
    while True:
        success,img = cap.read()
        result,objectInfo = getobjects(img,False,objects = ['person'])
        NumberofHuman = len(objectInfo)
        print(NumberofHuman)
        # cv2.imshow("Output",img)
        #cv2.waitKey(1)

        ob = Thingspeak(write_api_key=w_key, read_api_key=r_key, channel_id=channel_id)
        ob.post_cloud(value1=NumberofHuman,value2=Temperature)
        time.sleep(50)
        Data = ob.read_cloud(result=1)                # change result=number of data you want
        print(Data)
        (LED, Fan) = Data
        print(LED, Fan)

    
        
        
    
