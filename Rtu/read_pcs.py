import threading
import time
import redis
from pyModbusTCP.client import ModbusClient
from read_structure import StData


class ReadPcs(threading.Thread):
    def __init__(self, _host="localhost", _port=502):
        super().__init__()
        self.client = ModbusClient(host=_host,port=_port)
        self.redis = redis.Redis(host="localhost", port=6379)
        self.map = StData.data

    def redis_to_write(self,key, value):
        self.redis.hset("pcs",key,value)

    def redis_to_read(self,key):
        try:
            _get_redis = self.redis.hget("pcs",key)
            return _get_redis
        except (ValueError,TypeError):
            return None

    def modbus_to_read(self,start_addr,count):
        try:
            read = self.client.read_holding_registers(start_addr,count)
            return read
            # print(f"Holding Registers  {start_addr}: {read}")
        except (ValueError,TypeError):
            return []

    def modbus_to_write(self,start_addr,value):
        try:
            self.client.write_single_register(start_addr,value)
        except Exception as e:
            print(e)

    def run(self):
        while True:
            try:
                for key, size, index, scale in self.map:
                    data = self.modbus_to_read(index,1)
                    value = data[0] * scale
                    self.redis_to_write(key,value)
            except Exception as e:
                print(e)


if __name__ == "__main__":  #직접 실행시에만 동작하고 import 되었을때는 실행 x
    read_pcs=ReadPcs() #객체 생성 Read_PCS의 인스턴스
    t = threading.Thread(target=read_pcs.run,args=())
    t.start()


