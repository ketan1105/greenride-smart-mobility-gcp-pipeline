import json
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()
locations = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Pune"]
status_list = ["completed", "cancelled", "error"]

def generate_event():
    start_time = datetime.utcnow() - timedelta(minutes=random.randint(10, 60))
    end_time = start_time + timedelta(minutes=random.randint(10, 30))
    
    return {
        "station_id": f"STN-{random.randint(1000, 1100)}",
        "location": random.choice(locations),
        "start_time": start_time.isoformat() + "Z",
        "end_time": end_time.isoformat() + "Z",
        "energy_kwh": round(random.uniform(10, 40), 2),
        "price": round(random.uniform(100, 300), 2),
        "status": random.choice(status_list)
    }

if __name__ == "__main__":
    for _ in range(10):
        print(json.dumps(generate_event()))
