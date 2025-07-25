import random
import uuid
import json
from datetime import datetime, timedelta
import os

NUM_TRIPS = 500
NUM_STATIONS = 10

stations = [
    {"station_id": f"S{i+1}", "name": f"Station {i+1}", "lat": round(28.5 + random.random(), 6), "lon": round(77 + random.random(), 6)}
    for i in range(NUM_STATIONS)
]

def generate_trip_data():
    trip_data = []
    for _ in range(NUM_TRIPS):
        start_station = random.choice(stations)
        end_station = random.choice([s for s in stations if s["station_id"] != start_station["station_id"]])
        
        start_time = datetime.now() - timedelta(days=random.randint(0, 30), minutes=random.randint(0, 1440))
        duration = timedelta(minutes=random.randint(5, 60))
        end_time = start_time + duration
        
        trip_data.append({
            "trip_id": str(uuid.uuid4()),
            "start_station_id": start_station["station_id"],
            "end_station_id": end_station["station_id"],
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "distance_km": round(random.uniform(1.0, 15.0), 2),
            "fare_amount": round(random.uniform(10.0, 150.0), 2),
            "user_type": random.choice(["subscriber", "casual"])
        })
    return trip_data

def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    os.makedirs("data_simulation/output", exist_ok=True)
    save_to_json(stations, "data_simulation/output/stations.json")
    save_to_json(generate_trip_data(), "data_simulation/output/trips.json")
    print("✅ Data generated successfully.")
