# FIFO Page Replacement Simulation

def fifo_page_replacement(reference_string, frame_size):
    memory = []
    pointer = 0
    page_faults = 0

    print("=== FIFO PAGE REPLACEMENT ===")

    for page in reference_string:
        if page in memory:
            print(f"Page {page} -> Memory {memory} (Hit)")
        else:
            page_faults += 1
            if len(memory) < frame_size:
                memory.append(page)
            else:
                memory[pointer] = page
                pointer = (pointer + 1) % frame_size
            print(f"Page {page} -> Memory {memory} (Fault)")

    print(f"\nTotal Page Fault FIFO: {page_faults}")

if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_size = 3

    fifo_page_replacement(reference_string, frame_size)
