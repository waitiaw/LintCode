import threading
import redis
from pyModbusTCP.client import ModbusClient
import pandas as pd
from read_structure import StData

class PandasData(threading.Thread):
    def __init__(self,data):
        super().__init__()
        self.df = pd.DataFrame(data,columns=['name','type','addr','scale'])
        self.redis = redis.Redis(host="localhost", port=6379)
        self.client = ModbusClient(host="localhost", port=502)

    def add_column(self,col1,col2):
        self.df['value'] = self.df[col1] * self.df[col2]

    def add_modbus_column(self,col,gain):
        self.df['value'] = self.df[col] * gain

    def modbus_read(self,start_addr,count):
        modbus_values = self.client.read_holding_registers(start_addr,count)
        return modbus_values

    def redis_read(self,name,value):
        try:
            self.redis.hset("Test",name, value)
        except Exception as e:
            print(e)

    def make_data(self):
        if 'gain' in self.df.columns:
            self.add_column('scale','gain')
        else :
            for cnt in range(len(self.df)):
                start = self.df['addr'].iloc[cnt]
                modbus_gain = self.modbus_read(start,1)
                self.add_modbus_column('scale',modbus_gain)

        self.df = self.df[['name','value']]
        pd.set_option('display.max_rows', None)

    def display_data(self):
        self.make_data()
        print(self.df)
        for i in range(len(self.df)):
            _name = self.df['name'].iloc[i]
            _value = str(self.df['value'].iloc[i])
            try:
                self.redis_read(_name,_value)

            except Exception as e:
                print(e)


if __name__ == "__main__":
    new_data = PandasData(StData.data)
    t = threading.Thread(target= new_data.display_data(),args=())
    t.start()