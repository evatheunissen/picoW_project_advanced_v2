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
    elif cmd.startswith("measure"):
        sensor_id = 2 # Default value: MIDDLE
        sc = cmd.split()
        if len(sc) > 1:
            try:
                si = int(sc[1])
                if 0 <= si < len(sa.sensors):
                    sensor_id = si
                else:
                    print(f"Invalid sensor ID {si}, has to be between 0 and {len(sa.sensors) - 1}. Using default sensor (MIDDLE).")
            except ValueError:
                print(f"Invalid sensor ID {sc[1]}, has to be an integer. Using default sensor (MIDDLE).")
        sensor: Sensor = sa.sensors[sensor_id]
        sensor.measure()
        print(f"Sensor {sensor_id} length value: {sensor.length_in_cm} cm")
    elif cmd.startswith("calibrate"):
        sensor_id = 2 # Default value: MIDDLE
        sc = cmd.split()
        if len(sc) > 1:
            try:
                si = int(sc[1])
                if 0 <= si < len(sa.sensors):
                    sensor_id = si
                else:
                    print(f"Invalid sensor ID {si}, has to be between 0 and {len(sa.sensors) - 1}. Using default sensor (MIDDLE).")
            except ValueError:
                print(f"Invalid sensor ID {sc[1]}, has to be an integer. Using default sensor (MIDDLE).")
        sensor: Sensor = sa.sensors[sensor_id]
        sensor.calibrate()
        print(f"Sensor {sensor_id} calibration value: {sensor.distance_to_floor_in_cm} cm")
    elif cmd == "complete measure":
        sa.measure()
        print(f"Maximum length value: {sa.max_length} cm (Sensor ID: {sa.max_length_id})")
    elif cmd == "complete calibrate": # calibrated = False will never be !!! -> calibration 0 gives error -> default value is max_distance_in_cm
        sa.calibrate()
        if sa.front_back_diff != -1 and sa.left_right_diff != -1: # -1 error value -> diff can be -1 !!!
            print(f"Front-Back difference: {sa.front_back_diff} cm")
            print(f"Left-Right difference: {sa.left_right_diff} cm")
        else:
            print("Cannot calculate Front-Back and Left-Right difference.")
        for sensor in sa.sensors:
            print(f"Sensor {sensor.id} calibration value: {sensor.distance_to_floor_in_cm} cm")
    elif cmd.startswith("shots"):
        sc = cmd.split()
        if len(sc) > 1:
            try:
                shots = int(sc[1])
                if shots < 1:
                    print("Number of shots must be at least 1.")
                else:
                    for sensor in sa.sensors:
                        sensor.num_of_shots = shots
                        print(f"Set sensor {sensor.id} shots to {shots}.")
            except ValueError:
                print(f"Invalid number of shots '{sc[1]}', must be an integer greater than 0.")
        else:
            print("Please specify the number of shots.")
    elif cmd == "help":
        print("Available commands:")
        print("  measure [sensor_id] - Measure length for a specific sensor (default is MIDDLE).")
        print("  calibrate [sensor_id] - Calibrate a specific sensor (default is MIDDLE).")
        print("  measure all - Measure lengths for all sensors and determine maximum length.")
        print("  calibrate all - Calibrate all sensors and calculate axis differences.")
        print("  shots [number] - Set the number of shots for each sensor.")
        print("  exit - Exit the program.")

