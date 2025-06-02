from sensor import Sensor, SensorArray

def load_SensorArray():
    print("Loading SensorArray...")

    print("Initializing sensors...")
    s = Sensor(14, 13)  # Example sensor initialization
    print(f"Sensor initialized on pins")
    print(f"Distance: {s.distance_in_cm} cm")

    s.calibrate()  # Example calibration
    print(f"Sensor calibrated: {s.distance_to_floor_in_cm} cm")
    s.measure()  # Example measurement
    print(f"Sensor value: {s.length_in_cm} cm")

    

    return sa