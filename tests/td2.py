from arduino import Commands, Arduino
from time import sleep
from motors import Motors
from mission import Mission
import time
board = Arduino()
board.connect()
move = Motors()
mission = Mission()
mission.startMission()



start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
move.position(20,200)
there=int(move.getAtPosition())
print("initial position status is :")
print(there)
print("now moving to requested position")
while (there==0):
	print("waiting for desination, status is:")
	sleep(0.2)
	there=int(move.getAtPosition())
	print(there)
print("Arrived there")
print("--- %s seconds ---" % (time.time() - start_time))
print("now going to rotate and see how that goes")
move.rotate(-90,200)
print("initial position status is :")
there=int(move.getAtPosition())
print(there)
print("now turning by requested amount")
while (there==0):
	print("waiting for desination, status is:")
	sleep(0.2)
	there=int(move.getAtPosition())
	print(there)
print("--- %s seconds ---" % (time.time() - start_time))
sleep(1)
move.position(-20,200)
print("now moving position -20")
print("--- %s seconds ---" % (time.time() - start_time))
print("test completed")
