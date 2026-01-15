
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD "Scheduling (FCFS/SJF)"

---

## Identitas
- **Nama**  : Aster Rifani  
- **NIM**   : 250202915  
- **Kelas** : 1IKRB

---

## Pendahuluan (Introduction)
### A. Latar Belakang
   Dalam sistem operasi modern,banyak proses yang dapat berada dalam keadaan siap untuk dieksekusi secara bersamaan.Kondisi ini menuntut adanya menkanisme pengaturan yang tepat agar pengguna CPU menjadi efisien dan adil.

   Penjadwalan CPU berperan penting untuk menentukan urutan eksekusi proses sehingga kinerja sistem dapat dioptimalkan, khususnya dalam meminimalkan *waiting time* dan *turnaround time*.

   Algoritma penjadwalan CPU memiliki karakteristik yang berbeda-beda.Algoritma **First Come First Served (FCFS)** merupakan algoritma yang paling mudah dan sederhana untuk diimplementasikan, namun sering kali kurang efisien ketika terdapat proses dengan waktu eksekusi yang panjang. Sebaliknya, Algoritma **Shortest Job First (SJF)** mampu meningkatkan efisiensi dengan mengeksekusi proses berdurasi pendek mampu meningkatkan efisiensi dengan mengeksekusi proses berdurasi pendek terlebih dahulu, tetapi berpotensi menimbulkan masalah *starvation* pada proses berdurasi panjang.

   Oleh karena itu, diperlukan pemahaman dan pengujian langsung terhadap kedua algoritma tersebut agar dapat diketahui perbedaan kinerja serta kondisi penggunaan yang paling sesuai.Praktikum ini dilakukan untuk membandingkan algoritma FCFS dan SJF melalui perhitungan dan analisis parameter kinerja sistem.
### B. Tujuan
Tujuan dari praktikum ini adalah:
   > Mempelajari konsep dasar penjadwalan CPU menggunakan algoritma FCFS dan SJF.

   > Menghitung nilai *waiting time* dan *turnaround time* pada masing-masing algoritma.

   > Membadingkan kinerja algoritma FCFS dan SJF.

   > Mengetahui kelebihan dan kekurangan masing-masing algoritma penjadwalan.

---

## Metode (Methods)
### A. Data Proses
   | Proses | Burst Time | Arrival Time |
   |--------|------------|--------------|
   |   P1   |      6     |       0      |
   |   P2   |      8     |       1      |
   |   P3   |      7     |       2      |
   |   P4   |      3     |       3      |
### B. Langkah Eksperimen
   1. Mengurutkan proses sesuai dengan aturan algoritma :
      - FCFS : berdasarkan *arrival time*.
      - SJF : berdasarkan *burst time* terpendek.
   2. Menghitung :
      - Waiting Time (WT) = waktu mulai eksekusi - arrival time
      - Turnaround Time (TAT) = WT + burst time
   3. Menghitung nilai rata-rata WT dan TAT.
   4. Membuat tabel hasil dan Gantt Chart.

---

## Hasil (Results)
### A. Hasil FCFS
![Screenshot hasil](screenshots/tabel%20FCFS%20.png)
   - Rata-rata Waiting Time (WT): **8,75**
   - Rata-rata Turnaround Time (TAT): **14,75**
   - Gantt Chart FCFS :
   ```
    |  P1  |     P2     |    P3    | P4 |
   0       6            14         21   24
   ```
### B. Hasil SJF
![Screenshot hasil](screenshots/tabel%20SJF.png)
   - Rata-rata Waiting Time (WT): **6,25**
   - Rata-rata Turnaround Time (TAT): **12,25**
### C. Perbandingan antara **SJF** dan **FCFS*
![Screenshot hasil](screenshots/tabel%20FCFS%20vs%20SJF.png)
 | **Algoritma** | **Avg Waiting Time** | **Avg Turnaround Time** | **Kelebihan** | **Kekurangan** |
   |---|---|---|---|---|
   | FCFS | 8,75 |14,75| Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
   | SJF | 6,25 | 12,25 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

---
## Pembahasan (Discussion)
   Berdasarkan hasil percobaan, algoritma SJF menghasilkan nilai rata-rata *waiting time* dan *turnaround time* yang lebih kecil dibandingkan FCFS. Hal ini terjadi karena SJF memprioritaskan proses dengan *burst time* pendek sehingga antrean proses dapat diselesaikan lebih cepat.

   Namun, SJF memiliki kelemahan berupa potensi *starvation* pada proses dengan waktu eksekusi panjang, terutama jika sistem terus menerima proses pendek. Sebaliknya, FCFS lebih menjamin keadilan karena setiap proses dijalankan sesuai urutan kedatangan, meskipun efisiensinya lebih rendah.

---

## Kesimpulan
   1. Algoritma SJF lebih dibandingkan dengan Algoritma FCFS berdasarkan nilai rata-rata WT dan TAT.
   2. FCFS lebih unggul dalam kesederhanaan dan keadilan.
   3. Pemilihan algoritma harus disesuaikan dengan kebutuhan sistem.

---

## Quiz
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi? 
   **Jawaban:**  Format IMRAD menyusun laporan secara sistematis mulai dari latar belakang, metode, hasil, hingga analisis. Struktur ini memudahkan pembaca dan dosen untuk memahami tujuan praktikum, menilai ketepatan metode, serta mengevaluasi hasil dan pembahasan secara objektif dan konsisten.
2. Apa perbedaan antara bagian **Hasil** dan **Pembahasan**? 
   **Jawaban:**  Bagian Hasil menyajikan data atau temuan praktikum secara objektif dalam bentuk tabel, grafik, atau perhitungan, tanpa interpretasi. Sedangkan Pembahasan berisi analisis dan interpretasi hasil, penjelasan alasan terjadinya hasil tersebut, serta perbandingan dengan teori atau ekspektasi.
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?
   **Jawaban:**  Sitasi dan daftar pustaka penting untuk menunjukkan bahwa laporan didukung oleh sumber ilmiah yang valid, menghindari plagiarisme, serta meningkatkan kredibilitas dan keabsahan laporan praktikum.

---
## Daftar Pustaka
   Silberschatz, A., Galvin, P., Gagne, G. Operating System Concepts, 10th Ed.

   Tanenbaum, A. Modern Operating Systems, 4th Ed.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
