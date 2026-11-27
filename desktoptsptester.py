import time

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return ((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2) ** 0.5

def zap(cities):
    """Sort and connect cities based on the nearest x and y values and calculate the total distance."""
    if not cities:
        print("No cities to process. Please check the input data.")
        return []

    start_time = time.time()  # Start time at the beginning of the code
    # Sort cities by x, then y in ascending order
    cities_sorted = sorted(cities, key=lambda city: (city['x'], city['y']))
    sorted_path = []
    total_distance = 0
    current_city = cities_sorted[0]
    sorted_path.append(current_city)
    remaining_cities = cities_sorted[1:]  # List of cities left to visit

    while remaining_cities:
        # Find the closest city by comparing x then y
        closest_city = min(remaining_cities, key=lambda city: calculate_distance(current_city, city))
        total_distance += calculate_distance(current_city, closest_city)
        # Check if the closest city is in the remaining cities before trying to remove it
        if closest_city not in remaining_cities:
            # This shouldn't happen with correct data, skip this iteration
            continue
        # Attempt to remove the closest city
        index = remaining_cities.index(closest_city)
        sorted_path.append(closest_city)
        del remaining_cities[index]
        current_city = closest_city
        # If we've processed all remaining cities, break out of the loop
        if not remaining_cities:
            break
        # Placeholder for potential future code or logic checks
        pass

    end_time = time.time()  # End time after sorting
    # Ensure the first city is also placed at the end to form a loop
    if sorted_path:
        total_distance += calculate_distance(sorted_path[-1], sorted_path[0])
        sorted_path.append(sorted_path[0])
    end_time2 = time.time()  # End time after adding first to last in sorted path
    # Function to format time with seconds and milliseconds
    def format_time(timestamp): 
          seconds = int(timestamp)
          milliseconds = int((timestamp - seconds) * 1000)
          return f"{seconds}s {milliseconds:03d}ms"
    print(f"Sorting Time: {format_time(end_time- start_time)}\n"
          f"After Sorted Adjusted Last to First: {format_time(end_time2 - start_time)}")
    print(f"Total Calculated Distance: {total_distance} units")
    return sorted_path
# Example USA States data
usa_states = [
    {'x': -97.0, 'y': 35.0, 'name': 'Oklahoma', 'size_x': 69.0, 'size_y': 47.0},
    {'x': -98.0, 'y': 31.0,  'name': 'Texas', 'size_x': 268.0, 'size_y': 278.0},
    {'x': -88.0, 'y': 41.0,  'name': 'Illinois', 'size_x': 57.0, 'size_y': 55.0},
    {'x': -81.0, 'y': 27.0,  'name': 'Florida', 'size_x': 53.0, 'size_y': 58.0},
    {'x': -119.0, 'y': 36.0,  'name': 'California', 'size_x': 163.0, 'size_y': 156.0},
    {'x': -86.0, 'y': 40.0,  'name': 'Indiana', 'size_x': 36.0, 'size_y': 35.0},
    {'x': -93.0, 'y': 45.0,  'name': 'Minnesota', 'size_x': 87.0, 'size_y': 84.0},
    {'x': -105.0, 'y': 39.0,  'name': 'Colorado', 'size_x': 104.0, 'size_y': 103.0},
    {'x': -81.0, 'y': 38.0,  'name': 'West Virginia', 'size_x': 24.0, 'size_y': 31.0},
    {'x': -77.0, 'y': 39.0,  'name': 'Maryland', 'size_x': 12.0, 'size_y': 32.0},
    {'x': -92.0, 'y': 34.0,  'name': 'Arkansas', 'size_x': 53.0, 'size_y': 55.0},
    {'x': -81.0, 'y': 34.0,  'name': 'South Carolina', 'size_x': 32.0, 'size_y': 33.0},
    {'x': -83.0, 'y': 32.0,  'name': 'Georgia', 'size_x': 59.0, 'size_y': 60.0},
    {'x': -80.0, 'y': 35.0,  'name': 'North Carolina', 'size_x': 54.0, 'size_y': 55.0},
    {'x': -74.0, 'y': 40.0,  'name': 'New Jersey', 'size_x': 9.0, 'size_y': 21.0},
    {'x': -71.0, 'y': 42.0,  'name': 'Massachusetts', 'size_x': 10.0, 'size_y': 27.0},
    {'x': -122.0, 'y': 47.0,  'name': 'Washington', 'size_x': 71.0, 'size_y': 70.0},
    {'x': -70.0, 'y': 45.0,  'name': 'Maine', 'size_x': 35.0, 'size_y': 34.0},
    {'x': -149.0, 'y': 64.0,  'name': 'Alaska', 'size_x': 665.0, 'size_y': 663.0},
    {'x': -157.0, 'y': 21.0,  'name': 'Hawaii', 'size_x': 11.0, 'size_y': 10.0},
    {'x': -86.0, 'y': 39.0,  'name': 'Indiana', 'size_x': 36.0, 'size_y': 35.0},
    {'x': -95.0, 'y': 30.0,  'name': 'Louisiana', 'size_x': 52.0, 'size_y': 50.0},
    {'x': -92.0, 'y': 35.0,  'name': 'Mississippi', 'size_x': 48.0, 'size_y': 50.0},
    {'x': -117.0, 'y': 34.0,  'name': 'Nevada', 'size_x': 110.0, 'size_y': 107.0},
    {'x': -108.0, 'y': 33.0,  'name': 'New Mexico', 'size_x': 121.0, 'size_y': 122.0},
    {'x': -83.0, 'y': 42.0,  'name': 'Ohio', 'size_x': 45.0, 'size_y': 44.0},
    {'x': -96.0, 'y': 44.0,  'name': 'South Dakota', 'size_x': 77.0, 'size_y': 75.0},
    {'x': -85.0, 'y': 35.0,  'name': 'Tennessee', 'size_x': 42.0, 'size_y': 41.0},
    {'x': -120.0, 'y': 44.0,  'name': 'Oregon', 'size_x': 98.0, 'size_y': 96.0},
    {'x': -84.0, 'y': 43.0,  'name': 'Michigan', 'size_x': 97.0, 'size_y': 96.0},
    {'x': -73.0, 'y': 43.0,  'name': 'New York', 'size_x': 55.0, 'size_y': 54.0},
    {'x': -75.0, 'y': 41.0,  'name': 'Pennsylvania', 'size_x': 46.0, 'size_y': 47.0},
    {'x': -77.0, 'y': 38.0,  'name': 'Virginia', 'size_x': 43.0, 'size_y': 44.0},
    {'x': -86.0, 'y': 33.0,  'name': 'Alabama', 'size_x': 52.0, 'size_y': 53.0},
    {'x': -88.0, 'y': 33.0,  'name': 'Mississippi', 'size_x': 48.0, 'size_y': 49.0}
]

# Example data for other cities
cities = [
    {'name': 'City0', 'x': 710, 'y': 168},
    {'name': 'City1', 'x': 737, 'y': 137},
    {'name': 'City2', 'x': 761, 'y': 101},
    {'name': 'City3', 'x': 661, 'y': 125},
    {'name': 'City4', 'x': 707, 'y': 185},
    {'name': 'City5', 'x': 612, 'y': 126},
]

# Execute the 'zap' function to sort and connect cities based on their coordinates
result = zap(usa_states)
# result = zap(cities)

if result:
    # Extract key points from the sorted path
    first_city = result[0]
    second_to_last_city = result[-2]
    last_city = result[-1]

    # Log the results for analysis
    print(f"Array Sorted: {result} Length Of: {len(result)}")
    print(f"First starting point: {first_city}")
    print(f"Second-to-last starting point: {second_to_last_city}")
    print(f"Last starting point: {last_city}")
