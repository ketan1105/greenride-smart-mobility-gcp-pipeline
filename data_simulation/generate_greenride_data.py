import random
import csv
import uuid
from datetime import datetime, timedelta

# Configuration
NUM_RECORDS = 500
VEHICLE_TYPES = ['E-Bike', 'E-Scooter', 'E-Car']
CITIES = ['Bangalore', 'Delhi', 'Mumbai', 'Pune', 'Hyderabad']
FARE_BASE = {'E-Bike': 5, 'E-Scooter': 7, 'E-Car': 10}

# Generate random trip data
def generate_trip_data():
    trip_data = []
    for _ in range(NUM_RECORDS):
        trip_id = str(uuid.uuid4())
        user_id = random.randint(1000, 5000)
        city = random.choice(CITIES)
        vehicle_type = random.choice(VEHICLE_TYPES)
        distance_km = round(random.uniform(0.5, 25.0), 2)
        duration_min = round(distance_km * random.uniform(1.5, 3.5), 2)
        co2_saved_kg = round(distance_km * random.uniform(0.1, 0.25), 2)
        fare_amount = round(distance_km * FARE_BASE[vehicle_type], 2)
        trip_time = datetime.now() - timedelta(days=random.randint(0, 60), minutes=random.randint(0, 1440))

        trip_data.append([
            trip_id,
            user_id,
            city,
            vehicle_type,
            distance_km,
            duration_min,
            co2_saved_kg,
            fare_amount,
            trip_time.strftime('%Y-%m-%d %H:%M:%S')
        ])
    return trip_data

# Write to CSV
def write_csv(filename, rows):
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'trip_id',
            'user_id',
            'city',
            'vehicle_type',
            'distance_km',
            'duration_min',
            'co2_saved_kg',
            'fare_amount',
            'trip_time'
        ])
        writer.writerows(rows)

if __name__ == '__main__':
    data = generate_trip_data()
    write_csv('greenride_trips.csv', data)
    print(f"✅ Generated greenride_trips.csv with {NUM_RECORDS} records.")

