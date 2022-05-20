import json


class factory:
    def __init__(self):
        self.speaker = open('./JSON-file/bk-iot-speaker.JSON')
        self.gas = open('./JSON-file/bk-iot-gas.JSON')
        self.relay = open('./JSON-file/bk-iot-relay.JSON')
        self.pressure = open('./JSON-file/GLDS-pressure.JSON')
        self.time = open('./JSON-file/bk-iot-time.JSON')
        # self.factory_speaker = json.load(self.speaker)
        # self.factory_gas = json.load(self.gas)
        # self.factory_relay = json.load(self.relay)
        # self.factory_pressure = json.load(self.pressure)
        # self.factory_time = json.load(self.time)

    def terminate(self):
        self.speaker.close()
        self.gas.close() 
        self.relay.close() 
        self.pressure.close() 
        self.time.close()
