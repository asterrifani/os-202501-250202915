import csv
import os

print("=== SIMULASI CPU SCHEDULING FCFS ===\n")

# Path otomatis (dataset.csv satu folder dengan week9.py)
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "dataset.csv")

print("Membaca file:", file_path, "\n")

processes = []
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        processes.append({
            "process": row["Process"],
            "arrival": int(row["ArrivalTime"]),
            "burst": int(row["BurstTime"])
        })

# FCFS
processes.sort(key=lambda x: x["arrival"])

current_time = 0

print("proses\tArrival\tBurst\tWaiting\tTurnaround")
print("-------------------------------------------")

for p in processes:
    if current_time < p["arrival"]:
        current_time = p["arrival"]

    waiting = current_time - p["arrival"]
    turnaround = waiting + p["burst"]

    print(f"{p['process']}\t{p['arrival']}\t{p['burst']}\t{waiting}\t{turnaround}")

    current_time += p["burst"]




