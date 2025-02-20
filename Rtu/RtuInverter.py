import threading
import redis
from RtuStructure import RtuData

class RtuDevice(threading.Thread):
    def __init__(self):
        super().__init__()
        self.redis = redis.Redis(host="192.168.0.144",port=6379)
        self.map = RtuData.data

    def redis_read(self,name,value):
        try:
            self.redis.hset("Rtu",name, value)
        except Exception as e:
            print(e)

    def run(self):
        while True:
            try:
                for _name, _type, _addr, _scale, _gain in self.map:
                    _value = _scale * _gain
                    self.redis_read(_name,_value)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    r1 = RtuDevice()
    t = threading.Thread(target=r1.run,args=())
    t.start()


