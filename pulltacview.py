import os
import math

data = {}
last_values = {}
object_types = {}
object_names = {}

def deg_to_meters(lat):
    # Convert degrees to radians
    lat_rad = math.radians(lat)

    # Earth radius in meters (approximate value)
    earth_radius = 6371000

    # Calculate the distance in meters
    distance_meters = earth_radius * lat_rad

    return distance_meters


with open('/Users/maxwesterman/Desktop/DynamicsProject1MissileMay31/Tacview/data_file.txt', 'r') as file:
    current_time = None
    start_processing = False

    for line in file:
        line = line.strip()

        if line.startswith("#") and line[1:].split()[0].replace('.', '', 1).isdigit():
            start_processing = True  

        if start_processing:
            if line.startswith("#"):
                current_time = line[1:]
            elif not line.startswith("0"):
                values = line.split(',')
                if len(values) < 2:
                    continue
                obj_id = values[0]
                parameters = values[1].split('|')[:3]

                # Save the parameters as the last known value for the obj_id
                last_values[obj_id] = parameters

                if "Type=Air+FixedWing" in line:
                    object_types[obj_id] = "Air+FixedWing"
                    name_position = line.find(",Name=")
                    if name_position != -1:
                        name_end_position = line.find(",", name_position + 6)
                        if name_end_position == -1:
                            name_end_position = len(line)
                        object_names[obj_id] = line[name_position + 6:name_end_position]
                
                if "Importance=1" in line:
                    player_id = obj_id
                    player_values = line.split('|')
                    # Extract the first two values as lat and long
                    player_lat = deg_to_meters(float(player_values[0].split('=')[1]))
                    player_long = deg_to_meters(float(player_values[1]))

                if obj_id in object_types:
                    if current_time:
                        parameters.append(current_time)

                    if obj_id in data:
                        data[obj_id].extend(parameters)
                    else:
                        data[obj_id] = parameters


previous_lat = None
previous_long = None
previous_alt = None
previous_time = None

for obj_id, parameters in data.items():
    with open(f'{obj_id}.txt', 'w') as file:
        previous_lat = None
        previous_long = None
        previous_alt = None
        previous_time = None
        
        for i in range(0, len(parameters), 4):
            lat = parameters[i].replace("T=", "") if parameters[i] else previous_lat
            long = parameters[i + 1] if parameters[i + 1] else previous_long
            alt = parameters[i + 2] if parameters[i + 2] else previous_alt
            time = parameters[i + 3] if parameters[i + 3] else previous_time

            try:
                lat_float = deg_to_meters(float(lat))
                long_float = deg_to_meters(float(long))
                alt_float = float(alt)
                time_float = float(time)
                if time_float > 40:
                    file.write(','.join([str(lat_float-player_lat), str(long_float-player_long), str(alt_float), str(time_float)]) + '\n')
            except ValueError:
                continue  # Skip the line if any value cannot be converted to a number

            # Save the current values as the previous values for the next iteration
            previous_lat = lat
            previous_long = long
            previous_alt = alt
            previous_time = time

