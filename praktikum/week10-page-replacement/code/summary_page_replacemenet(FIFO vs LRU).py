# Summary Page Replacement (FIFO vs LRU)

def fifo(reference_string, frame_size):
    memory = []
    pointer = 0
    faults = 0

    for page in reference_string:
        if page not in memory:
            faults += 1
            if len(memory) < frame_size:
                memory.append(page)
            else:
                memory[pointer] = page
                pointer = (pointer + 1) % frame_size
    return faults


def lru(reference_string, frame_size):
    memory = []
    recent_use = {}
    faults = 0

    for time, page in enumerate(reference_string):
        if page not in memory:
            faults += 1
            if len(memory) < frame_size:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda x: recent_use[x])
                memory[memory.index(lru_page)] = page
        recent_use[page] = time
    return faults

if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_size = 3

    fifo_faults = fifo(reference_string, frame_size)
    lru_faults = lru(reference_string, frame_size)

    print("=== HASIL AKHIR SIMULASI ===")
    print(f"FIFO Page Fault : {fifo_faults}")
    print(f"LRU  Page Fault : {lru_faults}")

    if fifo_faults < lru_faults:
        print("Algoritma FIFO lebih efisien pada simulasi ini.")
    elif lru_faults < fifo_faults:
        print("Algoritma LRU lebih efisien pada simulasi ini.")
    else:
        print("FIFO dan LRU memiliki efisiensi yang sama.")
