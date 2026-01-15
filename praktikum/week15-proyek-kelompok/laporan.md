
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama Anggota Kelompok:**  
1. Erlin Dwi Cahyanti   (250202911)
2. Ani Ngismatul Hawa   (250202914)
3. Aster Rifani         (250202915)
4. Dyah Retno Wulandari (250202934)
5. Lutfi Khoerunnisa    (250202947)
- **Kelas** : [1IKRB]

---

## 1. Pendahuluan
### A. Latar Belakang
Sistem Operasi (Operating System) memiliki peran penting dalam mengelola sumber daya komputer seperti CPU, memori, dan proses. Pada proyek ini dilakukan simulasi dua konsep utama Sistem Operasi, yaitu:
- CPU Scheduling (FCFS dan SJF)
- Modul Page Replacement (FIFO)
Simulasi dibuat menggunakan bahasa pemrograman Java berbasis terminal dan dijalankan di dalam Docker untuk memastikan environment yang reproducible. Proyek dikerjakan menggunakan Git kolaboratif dengan pembagian branch per fitur. Mini Simulasi Sistem Operasi merupakan studi komprehensif yang mengintegrasikan tiga pilar utama infrastruktur TI modern. Pertama, Manajemen Memori melalui perbandingan algoritma FIFO dan LRU untuk mengoptimalkan efisiensi page replacement . Kedua, Scheduling yang mengatur antrean proses agar sistem berjalan responsif. Ketiga, Containerization (Docker) yang digunakan untuk mensimulasikan limitasi sumber daya CPU dan RAM secara nyata, memastikan aplikasi berjalan stabil di lingkungan terisolasi tanpa mengganggu host utama.

---

## 2. Tujuan
Tujuan dari proyek ini, berdasarkan panduan praktikum, adalah sebagai berikut:

> Bekerja dalam tim: Kemampuan berkolaborasi dalam kelompok dengan pembagian tugas yang jelas antara peran Lead, Developer, dan QA.

> Menggabungkan konsep: Mampu mengintegrasikan setidaknya dua konsep inti dari Sistem Operasi (misalnya pengaturan CPU dan penggantian halaman memori) ke dalam satu program yang sama.

> Mengelola kode: Menggunakan Git untuk mengelola kode dengan baik, termasuk pembuatan dan penggabungan branch secara rapi.

> Memastikan aplikasi bisa dijalankan: Menggunakan Docker agar aplikasi dapat dijalankan dengan lancar di berbagai lingkungan.

> Membuat dokumentasi dan presentasi: Membuat dokumentasi yang terstruktur serta menyampaikan hasil pengujian aplikasi melalui presentasi yang jelas.

---

## 3. Arsitektur Aplikasi
### A. Desain Arsitektur Umum
Arsitektur umum Mini Simulasi Sistem Operasi ini dibangun di atas tiga lapisan integrasi yang menghubungkan logika algoritma dengan lingkungan eksekusi modern. Pada lapisan inti, Logika Manajemen Memori dan Penjadwalan berfungsi sebagai otak sistem yang memproses antrean data menggunakan algoritma seperti FIFO atau LRU serta mengatur prioritas tugas. Logika ini kemudian dibungkus dalam Lapisan Kontainerisasi (Docker), yang bertindak sebagai lingkungan terisolasi untuk mengatur batas penggunaan sumber daya fisik, seperti membatasi kapasitas CPU dan RAM agar simulasi tidak mengonsumsi seluruh daya host.

Aliran datanya dimulai dari input proses yang dijadwalkan oleh unit scheduling, lalu dialokasikan ke unit memory management untuk dipetakan ke dalam slot memori yang tersedia, sementara seluruh aktivitas tersebut dipantau secara real-time melalui metrik performa kontainer.
## 4. Deskripsi Modul
Aplikasi simulasi Sistem Operasi ini dibagi menjadi beberapa modul terpisah untuk menjaga struktur kode tetap rapi, mudah dipahami, dan mudah dikembangkan. Setiap modul merepresentasikan satu konsep atau fungsi utama dalam Sistem Operasi.
#### 4.1 Modul CPU Scheduling
- Nama Modul: scheduling
- File Utama: FCFS.java, SJF.java, Process.java
- Deskripsi:
Modul CPU Scheduling bertanggung jawab untuk mensimulasikan penjadwalan proses pada CPU menggunakan algoritma First Come First Serve (FCFS) dan Shortest Job First (SJF – non-preemptive).
- Fungsi Utama:
   - Membaca data proses dari file process.csv
   - Mengurutkan proses sesuai algoritma yang dipilih
- Menghitung:
   - Waiting Time
   - Turnaround Time
   - Rata-rata Waiting Time
   - Menampilkan hasil dalam bentuk tabel ASCII di terminal
- Input:
Dataset proses (PID, Arrival Time, Burst Time)
- Output:
   - Tabel hasil per proses
   - Ringkasan metrik penjadwalan
#### 4.2 Modul Page Replacement
- Nama Modul: paging
- File Utama: FIFO.java, LRU.java
- Deskripsi:
Modul Page Replacement digunakan untuk mensimulasikan penggantian halaman pada memori utama dengan algoritma FIFO (First In First Out) dan LRU (Least Recently Used).
- Fungsi Utama:
   - Membaca urutan referensi halaman dari file pages.txt
   - Menerima input jumlah frame dari pengguna melalui CLI
   - Menentukan page hit dan page fault
   - Menghitung fault rate
- Input:
   - Jumlah frame
   - Dataset referensi halaman
- Output:
   - Total page reference
   - Jumlah page fault
   - Jumlah page hit
   - Fault rate (%)
### C. Alur Data
1. Input & Penjadwalan (Scheduling): Data atau proses masuk ke dalam sistem dan diatur urutan eksekusinya oleh unit scheduling. Di sini, sistem menentukan kapan sebuah proses mendapatkan giliran untuk diproses oleh CPU.

2. Alokasi Memori (Memory Management): Setelah proses dijadwalkan, sistem akan mengakses data di memori. Pada tahap ini, algoritma FIFO atau LRU bekerja untuk memutuskan data mana yang harus tetap berada di 3 slot frame dan data mana yang harus diganti jika terjadi page fault .

3. Eksekusi Terisolasi (Containerization): Seluruh proses komputasi ini berjalan di dalam Kontainer Docker. Docker memastikan bahwa simulasi hanya menggunakan sumber daya sesuai limit yang ditentukan, misalnya CPU maksimal 50% dan RAM 256 MiB.

4. Monitoring & Output: Hasil akhir berupa jumlah fault dan hit ditampilkan sebagai output, sementara beban kerja sistem dipantau secara real-time melalui metrik performa (CPU/RAM Usage) untuk memvalidasi stabilitas arsitektur.


---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
