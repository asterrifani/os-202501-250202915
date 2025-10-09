
# Laporan Praktikum Minggu 1
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Aster Rifani 
- **NIM**   : 250202915 
- **Kelas** : 1IKRB

---

## Tujuan
> Mengetahui peran sistem operasi dalam arsitektur komputer.
> Mengindentifikasi komponen utama OS (kernel, system call, device komputer, device driver, file sistem).
> Membandingkan model arsitektur OS (monolithic kernel, microkernel, layered architecture).
> Menggambar diagram sederhana arsitekture OS menggunakan alat bantu digital.

---

## Dasar Teori
Operating System Architecture 
 Operating system architecture merupakan struktur desain yang menentukan bagaimana sistem operasi dibangun dan bagian-bagiannya saling berkomunikasi untuk mengelola seluruh aktivitas komputer.
 
  Terdapat perbedaan dalam jenis arsitektur sistem operasi, antara lain:
 1. _Monolithic Kernel_: seluruh layanan sistem operasi (manajemen proses,manajemen memori,file system,device driver,dan networking) berjalan dalam ruangan kernel (kernel space)dengan mode hak akses teringgi (supervisor mode).
 2. _Micro Kernel_: kernel dikurangi seminim mungkin, hanya mencakup fungsi-fungsi inti (manajemen komunikasi antar-proses/IPC, penjadwalan dasar,dan manjemen memori level rendah).Layanan sistem operasi lainnya (seperti file system, device driver, dan networking)diimplementasikan sebagai proses pengguna (user-level servers)diluar kernel.
 3. _Layered Architecture_: arsitektur ini mengatur sistem operasi ke dalam lapisan-lapisan (layers), di mana setiap lapisan hanya dapat menggunakan fungsi dan layanan yang disediakan oleh lapisan yang lebih rendah.Lapisan 0 adalah perangkat kers (hardware), dan lapisan N adalah antarmuka pengguna (user interface).Dan tujuannya untuk mempermudah desain, implementasi, dan debugging.
  
  Contoh OS yang nyata menggunakan masing masing model :
 1. Monolithic Kernel: LINUX & UNIX
 2. Microkernel: MINIX & macOS
 3. Layered Architecture: The OS

---

## Langkah Praktikum
1. Membaca materi pengantar tentang komponen OS.  
2. Perintah yang dijalankan.
```bash
uname -a
whoami
lsmod | head
dmesg | head
```
3. Membuat diagram arsitektur menggunakan alat bantu digital (**draw.io**).  
4. Commit messege:
 
  hasil laporan 
```bash
praktikum/week1 - intro - arsitektur - os/laporan.md
```
  hasil diagram
 ```bash
praktikum/week1 - intro - arsitektur os/screenshots/diagram-os.png
 ```

---

## Kode / Perintah
```bash
git add.
git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
git push origin main
```
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Screenshot hasil percobaan atau diagram:
![Tugas Diagram](TugasDiagram.PNG)

---

## Analisis
- Makna dari percobaan atau membuat diagram tersebut adalah untuk mengetahui hubungan antara _User → System Call → Kernel → Hardware_ 
- Hubungan antara Kernel, system Call, dan Arsitektur OS, yaitu:
 
  1. Kernel merupakan pelaksana fungsi utama OS.
  2. System Call merupakan mekanisme komunikasi antara _user mode → kernel mode_.
  3. Arsitektur OS menentukan bagaimana kernel dan system call diorganisasikan dan dijalankan dalam sistem.
  
  Jadi,fungsi kernel dan system call bekerja sesuai pola yang ditetapkan arsitektur OS.
- Perbedaan antara Linux dan Windows terjadi karena perbedaan arsitektur kernel, system call, format file,dan lingkungan eksekusi.   

---

## Kesimpulan
 Berdasarkan hasil praktikum yang telah dilakukan, dapat disimpulkan bahwa sistem operasi memiliki peran penting sebagai dalam arsitektur komputer. Sistem operasi bertanggung jawab dalam mengatur penggunaan sumber daya komputer agar setiap komponen dapatbekerja secara efisien dan terkoordinasi.
 
 Melalui perbandingan model OS,dapat diketahui bahwa monolithic kernel memiliki performa yang lebih tinggi karena seluruh layanan berjalan di ruang kernel, microkernel lebih aman dan modular karena layanan berjalan di ruang pengguna,sedangkan layered architecture menawarkan struktur yang terorganisir berdasarkan lapisan fungsi.

 Pembuatan diagram arsitektur menggunakan alat bantu digital membantu memperjelas hubungan antara user, system call, kernel, hardware. Dan memperkuat pemahaman tentang cara kerja sistem operasi dalam arsitektur komputer. 

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.
2. 
   **Jawaban:** Manajemen proses, Manajemen memori, & Manajemen I/O.  
3. Jelaskan perbedaan antara _kernel mode_ dan _user mode_.
   
   **Jawaban:** Perbedaan antara _kernel mode_ dan _user mode_ terletak pada tingkat hak akses terhadap sumber daya sistem.Pada _kernel mode_, memiliki akses penuh, memungkinkan sistem operasi menjalankn instruksi yang bersifat istimewa yaitu mengelola memori serta berinteraksi langsung dengan perangkat keras.Sebaliknya _user mode_ memiliki program aplikasi berjalan dengan hak akses terbatas dan tidak dapat langsung mengakses perangkat keras atau menjalankan instruksi istimewa (semua operasi semacam itu harus dilakukan melalui system call ke sistem operasi.
4. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
   
   **Jawaban:** 1.Monolithic Kernel : UNIX, LINUX, MS-DOS, & BSD.  
                2.Microkernel : MINIX & MACH.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

  Bagian yang paling menantang pada minggu ini yaitu cara menyelesaikan tugas dan pengunggahan tugas.   
- Bagaimana cara Anda mengatasinya?

   Dengan cara mencari dan melihat tutorial serta bertanya kepada teman.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
