
# Laporan Praktikum Minggu [2]
Topik: "Struktur System Call dan Fungsi Kernel"

---

## Identitas
- **Nama**  : Aster Rifani 
- **NIM**   : 250202915  
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
>    Menjelaskan konsep dan fungsi system call.

>    Mengidentifikasi jenis-jenis system call dan fungsinya.

>    Mengamati alur perpindahan mode user ke kernel saat system call terjadi.

>    Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## Dasar Teori
  Menurut Silberschatz, Galvin, dan Gagne (2018), system call merupakan antarmuka utama antara _program pengguna (user programs)_ dan kernel sistem operasi. Tanpa mekanisme ini, aplikasi di ruang pengguna akan memiliki akses langsung terhadap perangkat keras atau memori sistem, yang dapat menimbulkan risiko serius terhadap integritas dan kerahasiaan data.System call bertindak sebagai "penjaga gerbang" (gatekeeper) yang mengontrol setiap permintaan dari aplikasi ke sumber daya kernel, seperti berkas, jaringan, atau memori.
  
  Dengan demikian, system call menjadi komponen penting dalam model keamanan OS berbasis proteksi lapisan (layered protection). Kernel hanya menjalankan fungsi-fungsi yang sah dan terverifikasi, sehingga mencegah program jahat mengakses area memori kernel atau melakukan operasi berbahaya seperti manipulasi tabel proses. Tanenbaum dan Bos (2015) menekankan bahwa kontrol ini merupakan inti dari _mekanisme isolasi_ antara pengguna dan sistem, di mana setiap system call harus melewati proses validasi hak akses (permission checking) sebelum dijalankan. Oleh karena itu, system call bukan hanya sarana komunikasi teknis, tetapi juga _mekanisme pertahanan utama_ terhadap eksploitasi sistem.
  
  Transisi dari _user mode_ ke _kernel mode_ merupakan titik kritis dalam arsitektur keamanan sistem operasi. Berdasarkan Tanenbaum & Bos (2015), sistem operasi modern memastikan keamanan transisi ini dengan menggunakan _instruksi perangkat keras khusus_ seperti trap atau interrupt. Saat program pengguna memanggil system call, CPU secara otomatis berpindah ke kernel mode melalui jalur yang telah ditentukan oleh _Interrupt Descriptor Table (IDT)_ atau mekanisme serupa.
  
  Selama proses ini, alamat instruksi dan konteks pengguna disimpan, lalu kontrol dialihkan hanya ke bagian kode kernel yang aman dan diawasi. Kernel juga memeriksa parameter yang dikirim oleh pengguna, untuk memastikan tidak ada upaya menyusup ke ruang memori kernel (misalnya melalui pointer manipulation)._Silberschatz et al. (2018)_ menambahkan bahwa OS modern menerapkan privilege levels dan memory protection unit (MMU) untuk memastikan bahwa kode pengguna tidak dapat menulis ke area kernel, bahkan jika terjadi kesalahan atau serangan. Hanya setelah pemeriksaan selesai dan hak akses valid, kernel mengeksekusi fungsi yang diminta, kemudian mengembalikan kontrol ke mode pengguna.
  
  Contoh System Call Umum di Linux :
 1. **read()** dan **write()** – untuk membaca dan menulis data pada berkas atau perangkat I/O.
 2. **open()** dan **close()** – untuk membuka dan menutup berkas.
 3. **fork()** – membuat proses baru dengan menyalin proses induk.
 4. **exec()** – mengeksekusi program baru dalam proses yang ada.
 5. **wait()** – menunggu proses anak selesai.
 6. **exit()** – mengakhiri proses dengan aman.
 7. **getpid()** – memperoleh ID proses saat ini.
 
  Semua system call ini bekerja melalui transisi terkontrol antara ruang pengguna dan kernel, memastikan keamanan, isolasi, serta stabilitas sistem.

---

## Langkah Praktikum
1. Setup Environtmen
   - Menggunakan Clud Shell untuk Terminal Linux.
   - Pastikan perintah ``strace`` dan ``man`` sudah terinstal.
   - Konvigurasi Git
2. Eksperimen 1-Analisis System Call
     Menjalankan perintah:
       ``strace ls``
3. Eksperimen 2-Menelusuri System Call File I/O
     Menjalankan perintah:
       ``strace -e trace=open,read,write,close cat /etc/passwd``
4. Eksperimen 3-Mode User vs Kernel
     Menjalankan perintah:
       ``dmesg | tail -n 10``
               atau
       ``sudo dmesg``
5. Diagram Alur Syscall
    - Membuatkan diagra yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
    - Menggunakan draw.io
    - Simpan di:
      ``praktikum/week2-syscall-structure-/screenshots/syscall-diagram.png``
6. Commit & Push
    ``git add .
      git commit -m "Minggu 2 - Structure System Call dan Kernel Interaction"
      git push origin main ``
---

## Kode / Perintah
- Hasil observasi system call dimasukkan ke dalam:
``laporan.md.``
- File screenshots hasil observasi disimpan di:
``screenshots/syscall_ls.png.``
- Diagram alursystemcall disimpan di:
``screenshots/syscall-diagram.png.``
- Laporan lengkap berada di:
``laporan.md.``

---

## Hasil Eksekusi
Hasil percobaan observasi system call:
### 1. Eksperimen 1 - Analisis System Call (Menjalankan perintah " Strace ls ")
![Terminal Linux 1](TerminalLinux1.PNG)
| No | System Call                        | Fungsi |
|----|------------------------------------|--------|
| 1. | `execve ( " /usr/bin/ls",["ls"]..")` | panggilan system call pertama untuk mengeksekusi Linux. |
| 2. | `brk (null)` | Mengtur batas akhir diheap memori.digunakan untuk manajemen memori.|
| 3. | `mmap (...)` | Memetakan area memori ke dalam ruang alamat proses.Digunakan untuk keprluan internal seperti stack atau pustaka dinamis. |
| 4. | `acces("/etc/ld.so.preload" R_OK)` | Mengecek apakah file preload ada dan data bisa dibaca.File ini bisa digunakan untuk preload library secara paksa. |
| 5. | `openat(AT_FDCWD, "/etc/ld.so.cache",O_RDONLY O_CLOEXEC)` | Membuka file cache pustaka dinamis untuk dibaca,agar sistem bisa menemukan lokasi pustaka (.so) yang dibutuhkan oleh program. |
| 6. | `fstat(3...)` | Mengambil informasi status dari file descriptor 3,yaitu file yang baru dibuka. |
| 7. | `mmap(..)` | Memetakan isi file ke memori agar bisa dibaca lebih efisien. |
| 8. | `openat(AT_FDCWD, "/lib/x86-linux-gnu/libselinux.so.1",...)` | Menutup file descriptor 3 setelah selesai membaca. |
| 9. | `openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libselinux.so.1", ...)` | Membuka pustaka dinamis (libselinux),salah satu library yang dibutuhkan(ls). |
| 10. | `read(3,...)` | Membaca isi awal file (libselinux.so.1) untuk memverifikasi bahwa itu adalah file ELF (Executable and Linkable Format). |
### 2. Eksperimen 2 - Menelusuri System Call File I/O (Menjalankan Perintah " strace -e trace=open, read, write, close cat /etc/psswd ")
![Terminal Linux 2](TerminalLinux2.PNG)

 Menganalisis bagaimana file dibuka,dibaca,dan ditutup oleh kernel.
  1. Membuka file [open()/openat()]
      Kernel menemukan dan memverifikasi file, lalu memberi file descriptor.
  2. Membaca isi file [read()]
      Kernel salin isi file ke buffer program.
  3. Menampilkan isi file [write()]
      Kernel kirim data ke layar atau terminal.
  4. Menutup file [close()]
      Kernel mengakhiri akses dan lepas file descriptor.
### 3. Eksperimen 3 - Mode User vs Kernel (Menjalnkan Perintah " dmesg | tail -n 10 ")
![Terminal Linux 3](TerminalLinux3.PNG)

 Perbedaan output ini dengan output dari program biasa,yaitu:
  Output dari dmesg berasal dari log kernel yang mencatat aktivitas sistem inti seperti deteksi hardware, 
driver, dan konfigurasi booting. Sedangkan output dari program biasa seperti cat atau ls berasal dari user space, 
yang menunjukkan hasil kerja program atau isi file. Jadi keduanya punya sumber yang berbeda — dmesg dari kernel, program 
biasa dari proses user.

Hasil diagram:
![Diagram2](Diagram2.PNG)

---

## Analisis
Percobaan ini bertujuan memahami bagaimana system call dan mekanisme transisi user mode ke kernel mode bekerja dalam sistem operasi. Melalui perintah ``strace`` pada instruksi seperti ``ls`` dan ``cat /etc/passwd``, terlihat bahwa setiap perintah pengguna memicu serangkaian system call seperti ``open()``, ``read()``, ``write()``, dan ``close()``. Misalnya, saat ``cat /etc/passwd`` dijalankan, kernel membuka file, membaca isinya, menulis hasil ke layar, lalu menutupnya. Hal ini menunjukkan bahwa program pengguna tidak berinteraksi langsung dengan perangkat keras, melainkan melalui system call yang berfungsi sebagai jembatan aman antara aplikasi dan kernel.

Menurut _Silberschatz, Galvin, dan Gagne (2018)_, system call adalah mekanisme resmi untuk meminta layanan kernel secara terkontrol, memastikan keamanan dan isolasi antar proses. Hasil percobaan juga memperlihatkan melalui _dmesg_ bahwa kernel berjalan pada mode istimewa, sedangkan aplikasi berada di user mode. Transisi dari user ke kernel mode terjadi ketika CPU mengeksekusi trap untuk menjalankan fungsi kernel. Proses ini menjamin bahwa kode pengguna tidak dapat memodifikasi kernel secara langsung, sebagaimana dijelaskan oleh _Tanenbaum dan Bos (2015)_, yang menekankan pentingnya pemisahan hak akses untuk menjaga stabilitas dan keamanan sistem.

Dari sisi arsitektur, Linux menggunakan _monolithic kernel_ sehingga seluruh layanan inti seperti manajemen proses, file, dan memori berada di ruang kernel. Hal ini membuat system call dapat diamati secara langsung menggunakan strace. Sebaliknya, Windows menggunakan _hybrid kernel_, di mana sebagian layanan berjalan di user space, sehingga aktivitas system call tidak terlihat langsung tanpa alat tambahan seperti Process Monitor. Meskipun berbeda, keduanya mengikuti prinsip yang sama: system call menjaga agar interaksi antara aplikasi dan sistem dilakukan secara aman. Dengan demikian, hasil percobaan ini membuktikan teori bahwa system call dan mekanisme user–kernel mode merupakan inti dari keamanan, kontrol, dan stabilitas sistem operasi modern.  

---

## Kesimpulan
Dari hasil percobaan dapat disimpulkan bahwa system call berperan penting sebagai penghubung aman antara program pengguna dan kernel. Setiap perintah yang dijalankan di terminal melewati proses validasi di kernel untuk menjaga keamanan dan stabilitas sistem. 

Transisi antara user mode dan kernel mode memastikan bahwa aplikasi tidak dapat mengakses perangkat keras atau memori secara langsung. Perbandingan antara Linux dan Windows menunjukkan perbedaan arsitektur, tetapi keduanya tetap mengandalkan prinsip dasar yang sama: system call adalah mekanisme inti untuk mengontrol akses dan melindungi sistem operasi dari gangguan atau kesalahan pengguna.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?
   **Jawaban:**  Sebagai penghubung antara program pengguna dan kernel agar program bisa memakai layanan sistem, seperti membaca file atau membuat proses, dengan cara yang aman.
2. Sebutkan 4 kategori system call yang umum digunakan.  
   **Jawaban:**
    1. Process control:
                      mengatur proses
                      (misal ``fork``, ``exec``)
    2. File management: 
                      mengelola file 
                      (misal ``open``, ``read``, ``write``, ``close``)
    3. Device management:
                     mengakses perangkat I/O
                     (misal: ``read``, ``write``)
    4. Information & communication:
                     mendapat info sistem atau komunikasi antarproses 
                     (misal ``getpid``, ``pipe``)
4. Mengapa system call tidak bisa dipanggil langsung oleh user program?  
   **Jawaban:**  Karena untuk keamanan dan stabilitas sistem — user program tidak boleh langsung mengakses kernel agar tidak merusak atau mengganggu sistem operasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  bagi saya yang paling menantang pada minggu ini yaitu untuk memahami cara-cara terminal.  
- Bagaimana cara Anda mengatasinya?
  dengan bantuan teman satu kelas dan AI saya bisa mengerjakan di tugas minggu ini.  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
