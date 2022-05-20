import json
speaker = open('./JSON-file/bk-iot-speaker.JSON','r')
test  = json.load(speaker)
speaker.close()
speaker = open('./JSON-file/bk-iot-speaker.JSON','w')
test = json.load(speaker)
test['data'] = 10000
