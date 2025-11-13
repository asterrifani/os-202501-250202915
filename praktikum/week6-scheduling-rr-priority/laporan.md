
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling  

---

## Identitas
- **Nama**  : Aster Rifani 
- **NIM**   : 250202915  
- **Kelas** : 1IKRB

---

## Tujuan
> Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.

> Menyusun tabel hasil perhitungan dengan benar dan sistematis.

> Membandingkan performa algoritma RR dan Priority.  

> Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.

> Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
   ***Penjadwalan CPU (CPU Scheduling)*** adalah salah satu fungsi utama dalam sistem operasi yang bertujuan untuk menentukan proses mana yang akan mendapatkan alokasi waktu CPU pada saat tertentu. Karena hanya satu proses yang dapat menggunakan CPU pada suatu waktu, maka sistem operasi perlu mengatur proses-proses yang sedang menunggu agar dapat dieksekusi secara efisien dan adil.

   ***Round Robin (RR)*** merupakan salah satu algoritma penjadwalan yang paling umum digunakan dalam sistem time-sharing atau multitasking. Prinsip dasar algoritma ini adalah memberikan setiap proses jatah waktu eksekusi yang sama, yang disebut *time quantum*.

   ***Priority Scheduling*** adalah algoritma penjadwalan yang menentukan urutan eksekusi proses berdasarkan tingkat prioritas yang dimilikinya. Setiap proses diberikan nilai prioritas, dan CPU akan dialokasikan kepada proses dengan prioritas tertinggi terlebih dahulu.

---

## Langkah Praktikum
1. **Menyiapkan Data Proses**
   Menggunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Menggunakan *time quantum (q)* = 3.  
   - Menghitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Mngurutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Melakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Membuat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Mengubah *quantum* menjadi 2 dan 5.  
   - Mengamati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Membuat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Menyimpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Membuat tabel perbandingan sebagai berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```

---

## Kode / Perintah
1. Hasil perhitungan dan analisis dimasukkan ke `laporan.md`.  
2. Screenshot tabel atau Gantt Chart disimpan di folder `screenshots/`.  
3. Laporan lengkap berada di `laporan.md`. 
4. Melakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```

---

## Hasil Eksekusi
1. **Eksperimen 1 – Round Robin (RR)**
![Screenshot](screenshots/Tabel%20Perhitungan%20Round%20Robin%20(RR).png)
   Sisa burst time dicatat setiap kali proses selesai menjalankan time quantum. Data ini digunakan untuk menentukan proses mana yang masih perlu dijalankan pada putaran berikutnya.

   - Sisa Burst time tiap putaran sebagai berikut :

   | Proses | Burst Time Awal | Sisa Burst Time setelah Putaran 1 | Sisa Burst Time Setelah Putaran 2 | Sisa Burst Time setelah Putaran 3 |
   |---|---|---|---|---|
   | P1 | 5 | 2 | 0 | - |
   | P2 | 3 | 0 | - | - |
   | P3 | 8 | 5 | 2 | 0 |
   | P4 | 6 | 3 | 0 | - |

   - Gantt Chart
    ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
    0    3    6    9    12   14   17   20   22 
    ```

2. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
![Screenshot hasil](screenshots/Tabel%20Perhitungan%20Priority%20Schedulling.png)
   Algoritma ini memilih proses berdasarkan prioritas, proses dengan prioritas lebih tinggi (angka kecil) mendapatkan layanan lebih cepat. Pada percobaan ini P1 dieksekusi paling dulu karena tiba di waktu 0 dan termasuk prioritas tinggi relatif (2). P2 tiba setelah P1 tetapi memiliki prioritas 1 (tertinggi) — namun karena non-preemptive, P2 baru dieksekusi setelah P1 selesai.

   - Gantt Chart
    ```
     | P1 | P2 | P4 | P3 |
    0    5    8   14   22
    ```
3. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Round Robin (q=3)
      Gantt Chart :
     ```
      | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 | P3 |
     0    2    4    6    8   10   12   14   16   18   20   22
     ```
   - Round Robin (q=5)
      Gantt Chart :
     ```
      | P1 | P2 | P3 | P4 | P3 |
     0    5    8    13   18   21   22
     ```
4. **Eksperimen 4 – Dokumentasi**
   Tabel perbandingan antara Round Robin & Priority Scedulling :

   | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | 8,5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

---

## Analisis
   Dengan demikian,hasil eksperimen dapat menunjukkan bahwa :
   -  **Priority Scheduling** memberikan waktu rata-rata (waiting time dan turnaround time) yang lebih rendah karena eksekusi difokuskan pada proses penting.
   -  **Round Robin (RR)** lebih unggul dari sisi keadilan dan responsivitas, terutama pada sistem dengan banyak proses interaktif.

---

## Kesimpulan
   Berdasarkan hasil eksperimen penjadwalan CPU menggunakan algoritma Round Robin (RR) dan Priority Scheduling, dapat disimpulkan bahwa:

   1. **Round Robin (RR)** memberikan keadilan yang lebih baik karena setiap proses mendapatkan jatah waktu eksekusi secara bergiliran. Algoritma ini cocok untuk sistem interaktif dan multitasking, meskipun performanya sangat bergantung pada besar kecilnya nilai time quantum.

   2. **Priority Scheduling** mampu menghasilkan waktu rata-rata eksekusi yang lebih cepat pada proses penting, namun berpotensi menimbulkan starvation bagi proses dengan prioritas rendah.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling? 
   **Jawaban:**  *Round Robin* lebih menekankan keadilan serta pembagian waktu yang merata.Sedangkan,*Priority Schedulling* menekankan urutan berdasarkan tingkat kepentingan proses.
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?
   **Jawaban:**  Jika nilai quantum kecil maka dapat membuat sistem sering berpindah proses/tidak efisien.Sedangkan kalau terlalu besar nilai quantum nya akan mengakibatkan proses lain menunggu lama/kurang responsif.
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?  
   **Jawaban:**  Karena cara kerjanya yang memprioritaskan proses dengan prioritas tinggi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Motor rusak.
- Bagaimana cara Anda mengatasinya?  Dengan sabar dan memakai motor yang lain.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
