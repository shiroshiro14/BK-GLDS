import json


class factory:
    def __init__(self):
        self.speaker = open('./JSON-file/bk-iot-speaker.JSON')
        self.gas = open('./JSON-file/bk-iot-gas.JSON')
        self.relay = open('./JSON-file/bk-iot-relay.JSON')
        self.pressure = open('./JSON-file/GLDS-pressure.JSON')
        self.time = open('./JSON-file/bk-iot-time.JSON')

    def update_json(self, id, value):
        self.terminate()
        self.write_speaker = open('./JSON-file/bk-iot-speaker.JSON','w')
        self.write_gas = open('./JSON-file/bk-iot-gas.JSON','w')
        self.write_relay = open('./JSON-file/bk-iot-relay.JSON','w')
        self.write_pressure = open('./JSON-file/GLDS-pressure.JSON','w')
        self.write_time = open('./JSON-file/bk-iot-time.JSON','w')
        
        factory_speaker = json.load(self.speaker)
        factory_gas = json.load(self.gas)
        factory_relay = json.load(self.relay)
        factory_pressure = json.load(self.pressure)
        factory_time = json.load(self.time)
        if id == factory_speaker['id']:
            factory_speaker['data'] = value 
        elif id == factory_gas['id']:
            factory_gas['data'] = value
        elif id == factory_relay['id']:
            factory_relay['data'] = value
        elif id == factory_pressure['id']:
            factory_pressure['data'] = value          
        elif id == factory_time['id']:
            factory_time['data'] = value    

    def terminate(self):
        self.speaker.close()
        self.gas.close() 
        self.relay.close() 
        self.pressure.close() 
        self.time.close()
