import serial
import time

class MHZ14A():
    packet = [0xFF,0x01,0x86,0x00,0x00,0x00,0x00,0x00,0x79]
    zero = [0xff, 0x87, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf2]
    def __init__(self,ser="/dev/ttyTHS1"):
        self.serial = serial.Serial(ser,9600,timeout=1)
        time.sleep(5)
    def get(self):
        self.serial.write(bytearray(self.packet))
        res = self.serial.read(size=9)
        res = bytearray(res)
        checksum = 0xff & (~(res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7])+1)
        if res[8] == checksum:
            ppm = (res[2]<<8)|res[3]
            temp = res[4]
            return ppm
        else:
            print (hex(checksum))
            return -1
    def close(self):
        self.serial.close
def main():
	co2 = MHZ14A("/dev/ttyTHS1")
	try:
		print("CO2 PPM is "+str(co2.get()))
		ppm = int(co2.get())
		if ppm <= 450 :
			print("매우 좋음")
		elif ppm > 450 and ppm <= 1000:
			print("좋음")
		elif ppm > 1000 and ppm <= 2000:
			print("보통")
		elif ppm > 2000 and ppm < 5000:
			print("나쁨")
		elif ppm > 5000:
			print("매우 나쁨")

	except:
		print("err")
		co2.close()
if __name__ == '__main__':
	while  True :
		main()
