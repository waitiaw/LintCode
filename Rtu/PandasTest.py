import threading
import redis
import pandas as pd
from RtuStructure import RtuData

class PandasData:
    def __init__(self,data):
        self.df = pd.DataFrame(data,columns=['name','type','addr','scale','gain'])
        self.redis = redis.Redis(host="localhost", port=6379)

    def add_column(self,total,col1,col2):
        self.df[total] = self.df[col1] * self.df[col2]

    def redis_read(self,name,value):
        try:
            self.redis.hset("Test",name, value)
        except Exception as e:
            print(e)

    def make_data(self):
        self.add_column('value','scale','gain')
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
    new_data = PandasData(RtuData.data)
    t = threading.Thread(target= new_data.display_data(),args=())
    t.start()