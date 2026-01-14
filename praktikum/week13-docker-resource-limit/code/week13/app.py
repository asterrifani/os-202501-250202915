#!/usr/bin/env python3
"""
Program uji untuk mengamati dampak resource limit
Menguji CPU dan memori allocation
"""

import time
import sys
import psutil
import os

def print_system_info():
    """Menampilkan informasi sistem"""
    print("=" * 50)
    print("INFORMASI SISTEM")
    print("=" * 50)
    print(f"CPU Count: {psutil.cpu_count()}")
    print(f"Total Memory: {psutil.virtual_memory().total / (1024**3):.2f} GB")
    print(f"Available Memory: {psutil.virtual_memory().available / (1024**3):.2f} GB")
    print("=" * 50)
    print()

def cpu_intensive_task(duration=10):
    """
    Task yang menggunakan CPU secara intensif
    Args:
        duration: durasi dalam detik
    """
    print(f"[CPU TEST] Memulai komputasi intensif selama {duration} detik...")
    start_time = time.time()
    counter = 0
    
    while time.time() - start_time < duration:
        # Komputasi matematika intensif
        for i in range(1000):
            _ = i ** 2 * 3.14159 / 2.71828
        counter += 1
        
        # Update progress setiap detik
        elapsed = time.time() - start_time
        if int(elapsed) != int(elapsed - 0.1):
            cpu_percent = psutil.cpu_percent(interval=0.1)
            mem_percent = psutil.virtual_memory().percent
            print(f"  Progress: {int(elapsed)}s | CPU: {cpu_percent}% | Memory: {mem_percent}%")
    
    print(f"[CPU TEST] Selesai. Total iterasi: {counter:,}")
    print()

def memory_allocation_test(max_mb=200, step_mb=50):
    """
    Test alokasi memori bertahap
    Args:
        max_mb: maksimal memori yang akan dialokasikan (MB)
        step_mb: step alokasi per iterasi (MB)
    """
    print(f"[MEMORY TEST] Mengalokasikan memori hingga {max_mb} MB...")
    print(f"Step alokasi: {step_mb} MB per iterasi")
    print()
    
    allocated_data = []
    current_mb = 0
    
    try:
        while current_mb < max_mb:
            # Alokasikan memori (1 MB = 1024 * 1024 bytes)
            chunk_size = step_mb * 1024 * 1024
            data = bytearray(chunk_size)
            allocated_data.append(data)
            
            current_mb += step_mb
            
            # Informasi penggunaan memori
            mem_info = psutil.virtual_memory()
            print(f"  Allocated: {current_mb} MB | "
                  f"Used: {mem_info.percent}% | "
                  f"Available: {mem_info.available / (1024**2):.0f} MB")
            
            time.sleep(1)
        
        print(f"\n[MEMORY TEST] Berhasil mengalokasikan {current_mb} MB")
        print("Menahan alokasi selama 5 detik...")
        time.sleep(5)
        
    except MemoryError:
        print(f"\n[MEMORY TEST] MemoryError! Tidak cukup memori pada {current_mb} MB")
        print("Container mungkin terkena limit memori")
    except Exception as e:
        print(f"\n[MEMORY TEST] Error: {e}")
    finally:
        # Cleanup
        del allocated_data
        print("[MEMORY TEST] Memori dibersihkan")
    
    print()

def mixed_workload_test():
    """Test kombinasi CPU dan memory"""
    print("[MIXED TEST] Menjalankan workload kombinasi...")
    
    data = []
    for i in range(5):
        print(f"\n  Iterasi {i+1}/5:")
        
        # Alokasi memori kecil
        chunk = bytearray(20 * 1024 * 1024)  # 20 MB
        data.append(chunk)
        print(f"    - Allocated 20 MB")
        
        # CPU work
        start = time.time()
        for j in range(10000):
            _ = j ** 2 * 3.14159
        elapsed = time.time() - start
        print(f"    - CPU work: {elapsed:.3f}s")
        
        # Status
        mem = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=0.1)
        print(f"    - CPU: {cpu}% | Memory: {mem.percent}%")
    
    print("\n[MIXED TEST] Selesai")
    print()

def main():
    print("\n")
    print("╔" + "═" * 48 + "╗")
    print("║" + " DOCKER RESOURCE LIMIT TEST ".center(48) + "║")
    print("╚" + "═" * 48 + "╝")
    print()
    
    # Tampilkan info sistem
    print_system_info()
    
    # Test 1: CPU Intensive
    print("\n" + "─" * 50)
    print("TEST 1: CPU INTENSIVE WORKLOAD")
    print("─" * 50)
    cpu_intensive_task(duration=10)
    
    # Test 2: Memory Allocation
    print("─" * 50)
    print("TEST 2: MEMORY ALLOCATION")
    print("─" * 50)
    memory_allocation_test(max_mb=200, step_mb=50)
    
    # Test 3: Mixed Workload
    print("─" * 50)
    print("TEST 3: MIXED WORKLOAD")
    print("─" * 50)
    mixed_workload_test()
    
    print("=" * 50)
    print("SEMUA TEST SELESAI")
    print("=" * 50)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)