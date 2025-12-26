
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Aster Rifani  
- **NIM**   : 250202915  
- **Kelas** : 1IKRB

---

## Tujuan
> Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  

> Menjalankan program dengan dataset uji yang 
diberikan atau dibuat sendiri.  

> Menyajikan output simulasi dalam bentuk tabel atau grafik.  

> Menjelaskan hasil simulasi secara tertulis.  

---

## Dasar Teori
Simulasi CPU scheduling merupakan metode untuk memodelkan proses penjadwalan CPU dalam sistem operasi menggunakan program komputer. Simulasi ini bertujuan untuk membantu memahami bagaimana sistem operasi mengatur penggunaan CPU oleh berbagai proses serta mempermudah analisis kinerja penjadwalan melalui perhitungan waktu eksekusi proses.

Algoritma First Come First Served (FCFS) adalah salah satu algoritma penjadwalan CPU yang paling sederhana. Pada algoritma ini, proses akan dieksekusi berdasarkan urutan kedatangan ke dalam sistem. Proses yang datang lebih awal akan memperoleh jatah CPU terlebih dahulu dan dijalankan hingga selesai tanpa adanya interupsi.

Dalam simulasi CPU scheduling FCFS, parameter yang digunakan meliputi arrival time dan burst time. Berdasarkan parameter tersebut, sistem menghitung waiting time dan turnaround time untuk setiap proses. Simulasi ini mudah diimplementasikan dan sesuai untuk pembelajaran, namun memiliki keterbatasan seperti kemungkinan terjadinya convoy effect dan waktu tunggu rata-rata yang tinggi. 

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Membuat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Menjalankan program menggunakan dataset uji.  
   - Memastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Menyimpan hasil eksekusi (screenshot).

4. **Analisis**

   - Menjelaskan alur program.  
   - Membandingkan hasil simulasi dengan perhitungan manual.  
   - Menjelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```
---

## Kode / Perintah
- Kode program simulasi di folder `code/`.
- Dataset uji di `code/reference_string.txt`.
- Screenshot hasil simulasi di `screenshots/`.
- Laporan lengkap di `laporan.md`.

---

## Hasil Eksekusi
![Screenshot](screenshots/Screenshot%202025-12-26%20121827.png)

---

## Analisis
Berdasarkan hasil percobaan algoritma *First Come First Served (FCFS)*, proses dieksekusi sesuai urutan waktu kedatangan sehingga proses yang datang lebih awal akan diproses terlebih dahulu tanpa memperhatikan lama waktu eksekusinya. Akibatnya, proses dengan *burst time* besar dapat menyebabkan proses lain menunggu lebih lama, sehingga nilai *waiting time* dan *turnaround time* meningkat pada proses yang datang belakangan. Hal ini menunjukkan bahwa meskipun FCFS mudah diimplementasikan, algoritma ini kurang efisien untuk sistem dengan variasi waktu proses yang besar karena dapat menimbulkan efek *convoy*.


---

## Kesimpulan
Berdasarkan hasil praktikum simulasi CPU scheduling menggunakan algoritma First Come First Served (FCFS), dapat disimpulkan bahwa simulasi berhasil menggambarkan cara kerja penjadwalan CPU berdasarkan urutan kedatangan proses. Hasil perhitungan waiting time dan turnaround time yang diperoleh dari simulasi sesuai dengan perhitungan manual, sehingga implementasi algoritma dapat dinyatakan benar. Algoritma FCFS mudah diimplementasikan dan cocok untuk pembelajaran konsep dasar penjadwalan CPU, namun memiliki keterbatasan seperti waktu tunggu rata-rata yang tinggi dan potensi terjadinya convoy effect.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
   **Jawaban:** Simulasi diperlukan untuk memodelkan cara kerja algoritma scheduling secara nyata tanpa harus menjalankannya pada sistem operasi sebenarnya. Melalui simulasi, proses perhitungan waktu eksekusi, waiting time, dan turnaround time dapat diuji secara otomatis sehingga mengurangi kesalahan perhitungan manual serta mempermudah analisis kinerja algoritma.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
   **Jawaban:** Pada dataset kecil, hasil simulasi dan perhitungan manual biasanya sama. Namun, pada dataset yang besar, perhitungan manual berisiko tinggi terjadi kesalahan dan membutuhkan waktu lama, sedangkan simulasi tetap akurat, konsisten, dan cepat. Simulasi juga memudahkan pengolahan data dalam jumlah besar tanpa meningkatkan kompleksitas pengerjaan.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan. 
   **Jawaban:** Algoritma First Come First Served (FCFS) lebih mudah diimplementasikan dibandingkan algoritma lain seperti SJF. FCFS hanya memerlukan pengurutan proses berdasarkan waktu kedatangan tanpa perhitungan tambahan, sedangkan SJF membutuhkan proses seleksi burst time terpendek yang lebih kompleks.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  kurang semangat dalam mengerjakan tugas.
- Bagaimana cara Anda mengatasinya?  butuh penyemangat.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
