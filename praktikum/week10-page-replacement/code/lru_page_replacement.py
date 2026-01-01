# LRU Page Replacement Simulation

def lru_page_replacement(reference_string, frame_size):
    memory = []
    recent_use = {}
    page_faults = 0

    print("=== LRU PAGE REPLACEMENT ===")

    for time, page in enumerate(reference_string):
        if page in memory:
            print(f"Page {page} -> Memory {memory} (Hit)")
        else:
            page_faults += 1
            if len(memory) < frame_size:
                memory.append(page)
            else:
                # cari halaman yang paling lama tidak digunakan
                lru_page = min(memory, key=lambda x: recent_use[x])
                memory[memory.index(lru_page)] = page
            print(f"Page {page} -> Memory {memory} (Fault)")

        recent_use[page] = time

    print(f"\nTotal Page Fault LRU: {page_faults}")

if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_size = 3

    lru_page_replacement(reference_string, frame_size)
