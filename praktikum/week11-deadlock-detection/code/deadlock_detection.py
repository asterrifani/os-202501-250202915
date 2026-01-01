import csv

def detect_deadlock(processes, allocation, request):
    deadlock = []

    for p in processes:
        for other in processes:
            if p != other and request[p] == allocation[other]:
                deadlock.append(p)
                break
    return deadlock


# ===== MEMBACA BACA DATASET CSV =====
processes = []
allocation = {}
request = {}

with open("dataset_deadlock.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = row["Process"]
        processes.append(p)
        allocation[p] = row["Allocation"]
        request[p] = row["Request"]


# ===== EKSEKUSI =====
result = detect_deadlock(processes, allocation, request)

print("Proses Dadlock yang Terdeteksi :")
for p in processes:
    status = "Deadlock" if p in result else "No Deadlock"
    print(f"{p} : {status}")

if len(result) == len(processes):
    print("\nSystem is in DEADLOCK condition")
else:
    print("\nSystem is SAFE")


