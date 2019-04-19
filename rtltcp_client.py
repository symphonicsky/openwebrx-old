import socket
import struct
import time

SET_FREQUENCY = 0x01
SET_GAINMODE = 0x03
SET_GAIN = 0x04
SET_TUNER_GAIN_INDEX = 0x0d

class client(object):
    def __init__(self):
        self.remote_host = "localhost"
        self.remote_port = 4951
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.remote_host, self.remote_port))
    def set_freq(self, freq):
        self.__send_command(SET_FREQUENCY, freq)
    def tunergain(self, tunergain):
        self.__send_command(SET_TUNER_GAIN_INDEX, tunergain)
    def __send_command(self, command, parameter):
        cmd = struct.pack(">BI", command, parameter)
        self.conn.send(cmd)