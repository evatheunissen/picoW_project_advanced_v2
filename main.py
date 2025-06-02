import sys
from machine import Pin
from sensor import Sensor, SensorArray

sa = SensorArray()
sa.add(Sensor(14, 13)) # FRONT
sa.add(Sensor(20, 21)) # LEFT
sa.add(Sensor(10, 11)) # MIDDLE
sa.add(Sensor(8, 7)) # RIGHT
sa.add(Sensor(3, 2)) # BACK

# sa.calibrate()

while True:
    cmd = input("> ")
    if cmd == "exit":
        sys.exit(0)
    elif cmd == "measure":
        sensor: Sensor = sa.sensors[0]
        sensor.measure()
        print(f"Sensor value: {sensor.length_in_cm} cm")
