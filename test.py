#! /usr/bin/env python2
# Small test client for rtl_tcp
# Simeon Miteff <simeon.miteff@gmail.com>
# Thu Sep 27 09:28:55 SAST 2012
import socket
import struct
import time

SET_FREQUENCY = 0x01
SET_SAMPLERATE = 0x02
SET_GAINMODE = 0x03
SET_GAIN = 0x04
SET_AGC_MODE = 0x08
SET_TUNER_GAIN_INDEX = 0x0d
SET_FREQENCYCORRECTION = 0x05
SET_IF_GAIN_R = 0x21
SET_NOTCH = 0x24

class RtlTCP(object):
    def __init__(self):
        self.remote_host = "10.34.0.237"
        self.remote_port = 4951
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.remote_host, self.remote_port))
        #self.__send_command(SET_SAMPLERATE, 2048000)
    def tune(self, freq):
        self.__send_command(SET_FREQUENCY, freq)
    def gain(self, gainlevel):
        self.__send_command(SET_GAIN, gainlevel)
    def gainmode(self, gainmode):
        self.__send_command(SET_GAINMODE, gainmode)
    def agcmode(self, agcmode):
        self.__send_command(SET_AGC_MODE, agcmode)
    def tunergain(self, tunergain):
        self.__send_command(SET_TUNER_GAIN_INDEX, tunergain)
    def ifgain(self, ifgain):
        self.__send_command(SET_IF_GAIN_R, ifgain)
    def notch(self, sn):
        self.__send_command(SET_NOTCH, sn)
    def setting(self, value, setting):
        self.__send_command(setting, value)
    def __send_command(self, command, parameter):
        cmd = struct.pack(">BI", command, parameter)
        self.conn.send(cmd)

if __name__=="__main__":
    sdr = RtlTCP()
    #sdr.gainmode(1)
    #sdr.agcmode(1)
    #sdr.gain(2)
    # -29
    #sdr.tunergain(-1)
    sdr.notch(1)
    #sdr.setting(0,0x22)
    #sdr.ifgain(1)