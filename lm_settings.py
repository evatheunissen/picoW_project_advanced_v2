from sensor import Sensor, SensorArray

def load_SensorArray():
    print("Loading SensorArray...")

    sa = SensorArray()

    sa.add(Sensor(14, 13)) # FRONT
    sa.add(Sensor(20, 21)) # LEFT
    sa.add(Sensor(10, 11)) # MIDDLE
    sa.add(Sensor(8, 7)) # RIGHT
    sa.add(Sensor(3, 2)) # BACK

    return sa