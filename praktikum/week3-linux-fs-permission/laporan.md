
# Laporan Praktikum Minggu [3]
Topik: Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Aster Rifani
- **NIM**   : 250202915  
- **Kelas** : 1IKRB

---

## Tujuan  
> Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.

> Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.

> Menjelaskan hasil output dari perintah Linux dasar.

---

## Dasar Teori
   Setiap file dan direktori di Linux memiliki kepemilikan yang terdiri dari tiga bagian: user (pemilik), group (kelompok pengguna), dan others (pengguna lain). Kepemilikan ini menentukan siapa yang memiliki hak akses terhadap file tersebut. Pengguna dan administrator dapat mengubah kepemilikan menggunakan perintah `chown` dan `chgrp`.

   Linux mengatur hak akses file melalui tiga jenis izin:
   1. read (r)
   2. write (w)
   3. execute (x)

   Hak akses ini berlaku untuk user, group, dan others secara terpisah. Izin tersebut dapat dilihat dengan ls -l dan diubah menggunakan chmod, baik dengan format simbolik maupun oktal.

   Ownership menentukan siapa yang berhak mengakses file, sementara permission menentukan tindakan apa yang boleh dilakukan. Kombinasi keduanya menjadi dasar kontrol akses yang menjaga keamanan dan stabilitas sistem file Linux, serta mencegah akses tidak sah.

---

## Langkah Praktikum
1. Setup Environment
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di  dalam direktori repositori Git praktikum:
praktikum week3-linux-fs-permission/
2. Eksperimen 1 –Navigasi Sistem File 
Menjalankan perintah berikut:

   `pwd`
   `ls -l`
   `cd /tmp`
   `ls -a`
3. Eksperimen 2 – Membaca File Jalankan perintah:

   `cat /etc/passwd | head -n 5`
4. Eksperimen 3 – Permission & Ownership 
Buat file baru:

  - `echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt`
  - Ubah pemilik file (jika memiliki izin sudo):
   `sudo chown root percobaan.txt
ls -l percobaan.txt`
5. Eksperimen 4 – Dokumentasi
   screenshot hasil terminal dan simpan di:
   `praktikum/week3-linux-fs-permission/screenshots/`
6. Commit & Push

   `git add .
   git commit -m "Minggu 3 - Linux File   System & Permission"
   git push origin main`

---

## Kode / Perintah
1. Hasil observasi perintah Linux dimasukkan ke dalam `laporan.md.`
2. Screenshot hasil eksekusi disimpan di `screenshots/.`
3. Laporan lengkap tersimpan di `laporan.md.`
4. Eksperimen 1:`pwd`
   `ls -l`
   `cd /tmp`
   `ls -a`
5. Eksperimen 2:
   `cat /etc/passwd | head -n 5`
6. Eksperimen 3:
   `echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt`
   `sudo chown root percobaan.txt
ls -l percobaan.txt`
7. Eksperimen 4:
   `praktikum/week3-linux-fs-permission/screenshots/`
8. Commit & Push:
   `git add .
   git commit -m "Minggu 3 - Linux File   System & Permission"
   git push origin main`

---

## Hasil Eksekusi
![Screenshot](![alt text](image.png))
### 1. Eksperimen 1-Navigasi Sistem File
| **Perintah** | **Hasil Output** |**Keterangan Singkat**|
|:---:|:---:|:---:|
|`pwd`|`/home/asterrifani0624`|Direktori aktif: /home/asterrifani0624. Tidak menampilkan isi folder atau file tersembunyi.|
|`ls -l`|`drwxrwxr-x 2 asterrifani0624 asterrifani0624 4096 Oct 23 10:35 praktkum-week-3`|Menampilkan isi lengkap folder home, ada file dan direktori, ukuran dan permission. Folder praktkum-week-3 sudah berhasil dibuat.|
|`cd /tmp`|(Prompt berubah ke `tmp`)|Direktori aktif berubah ke /tmp.|
|`ls -a`|Menampilkan file dan folder tersembunyi di `/tmp`, termasuk file sementara dan file konfigurasi.|Direktori aktif: `/tmp.` Isi lengkap dengan file biasa dan tersembunyi (., .., dan banyak file prefiks `tmp.`).|
### 2. Eksperimen 2-Membaca File
   ``asterrifani0624@cloudshell:/tmp$ cat /etc/passwd | head -n 5 root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync``
   |**Perintah**|**Keterangan**|
   |:---:|:---:|
   |`cat/etc/passwd head -n 5`|Perintah cat /etc/passwd | head -n 5 menampilkan 5 baris pertama dari file `/etc/passwd`, yang berisi informasi akun pengguna di sistem Linux. Informasi tersebut meliputi username, user ID (UID), group ID (GID), direktori home, dan shell yang digunakan saat login.(`root`,`daemon`,`bin`,`sys`,dan `sync`)|
### 3. Eksperimen 3-Permission & Ownership
   ``asterrifani0624@cloudshell:~$ echo "Hello Aster Rifani - 250202915" > percobaan.txt
asterrifani0624@cloudshell:~$ ls -l percobaan.txt
-rw-rw-r-- 1 asterrifani0624 asterrifani0624 31 Oct 23 11:48 percobaan.txt
asterrifani0624@cloudshell:~$ chmod 600 percobaan.txt
asterrifani0624@cloudshell:~$ ls -l percobaan.txt
-rw------- 1 asterrifani0624 asterrifani0624 31 Oct 23 11:48 percobaan.txt
asterrifani0624@cloudshell:~$ sudo chown root percobaan.txt
asterrifani0624@cloudshell:~$ ls -l percobaan.txt
-rw------- 1 root asterrifani0624 31 Oct 23 11:48 percobaan.txt
asterrifani0624@cloudshell:~$ sudo cat percobaan.txt
Hello Aster Rifani - 250202915``
   - Analisi Perbedaan Sebelum dan Sesudah `chmod`:
      1. Sebelum `chmod`

         Setelah membuat file `percobaan.txt`, hak akses file dengan perintah : `ls -l percobaan.txt`
         
         Diperoleh dengan hasil : `-rw-rw-r-- 1 asterrifani0624 asterrifani0624 31 Oct 23 11:48 percobaan.txt`
         Hak akses `rw-rw-r--` yang berarti pemilik dan grup dapat membaca dan menulis, sedangkan pengguna lain hanya dapat membaca.
      2. Sesudah `chmod 600 percobaan.txt`

         Perintah chmod 600 percobaan.txt dijalankan untuk mengubah hak akses file menjadi: `-rw-------`

         Hasil cek dengan `ls -l percobaan.txt`: `-rw------- 1 asterrifani0624 asterrifani0624 31 Oct 23 11:48 percobaan.txt`
         Artinya hanya pemilik file yang dapat membaca dan menulis, sementara grup dan pengguna lain tidak memiliki akses apapun.
      3. Setelah Mengubah Pemilik File dengan `sudo chown root percobaan.txt`

         Setelah mengganti pemilik file menjadi root dengan perintah:`sudo chown root percobaan.txt`

         Saya cek kembali dengan: `ls -l percobaan.txt`

         Didapatkan hasil:`-rw------- 1 root asterrifani0624 31 Oct 23 11:48 percobaan.txt`
         Setelah menjalankan perintah `sudo chown root percobaan.txt`, pemilik file berubah menjadi root sehingga hanya pengguna `root` yang memiliki hak akses membaca dan menulis file tersebut, sementara pengguna lain, termasuk pemilik sebelumnya, tidak dapat mengakses file tersebut.

---

## Analisis
   **Eksperimen 1**
      Eksperimen ini bertujuan memahami bagaimana menavigasi dan melihat isi sistem file Linux, termasuk bagaimana melihat direktori saat ini, isi direktori dengan detail, berpindah lokasi, dan melihat file tersembunyi.
   **Eksperimen 2**
      Eksperimen ini memperlihatkan cara membaca isi file teks (dalam hal ini file konfigurasi sistem `/etc/passwd` yang berisi informasi akun pengguna). Penggunaan `head -n 5` membatasi output hanya pada 5 baris pertama agar lebih mudah dipahami.
   **Eksperimen 3**
      Eksperimen ini menjelaskan konsep dasar pengelolaan hak akses (permissions) dan kepemilikan (ownership) file pada Linux. Dengan `chmod`, hak akses file dapat dibatasi agar hanya pemilik yang bisa mengakses. Dengan `chown`, kepemilikan file dapat dialihkan ke user lain (misal root), sehingga akses file juga bergantung pada siapa pemiliknya. Ini penting untuk keamanan dan pengelolaan sistem file.

---

## Kesimpulan
Manajemen file di Linux melibatkan kemampuan untuk menavigasi sistem file dengan menggunakan perintah seperti `pwd` untuk mengetahui direktori saat ini, `ls` untuk melihat isi direktori, dan cd untuk berpindah antar folder. Selain itu, perintah `ls -a` memungkinkan pengguna melihat file tersembunyi, sehingga memudahkan dalam mengelola dan memahami struktur direktori di sistem Linux. Pemahaman dasar tentang cara membaca file menggunakan perintah `cat` dan `head` juga penting untuk memeriksa isi file teks, terutama file konfigurasi sistem.

Di sisi lain, manajemen permission dan kepemilikan file sangat krusial untuk menjaga keamanan dan kontrol akses di Linux. Dengan menggunakan perintah `chmod`, pengguna dapat mengatur hak akses file agar hanya pemilik atau grup tertentu yang dapat membaca, menulis, atau mengeksekusi file tersebut. Perintah `chown` memungkinkan penggantian pemilik file, yang berdampak langsung pada siapa yang memiliki kontrol penuh atas file tersebut. Kombinasi pengaturan permission dan ownership membantu melindungi file dari akses yang tidak diinginkan dan menjaga integritas sistem.

---

## Quiz
1. Apa fungsi dari perintah `chmod`? 
   **Jawaban:**  Perintah `chmod` (change mode) digunakan untuk mengubah hak akses (permission) file atau direktori di sistem Linux/Unix. Dengan `chmod`, kamu bisa mengatur siapa saja yang boleh membaca (read), menulis (write), atau mengeksekusi (execute) sebuah file atau direktori.
2. Apa arti dari kode permission `rwxr-xr--`? 
   **Jawaban:**  Kode permission `rwxr-xr--` terdiri dari tiga bagian (masing-masing tiga karakter) yang mewakili hak akses untuk:

   - Pemilik (owner): `rwx` → dapat membaca (read), menulis (write), dan mengeksekusi (execute) file/direktori.

   - Grup (group): `r-x` → dapat membaca dan mengeksekusi,    tapi tidak bisa menulis.

   - Lainnya (others): `r--` → hanya bisa membaca saja.
3. Jelaskan perbedaan antara `chown` dan `chmod`
   **Jawaban:**  `chmod` mengatur apa yang boleh dilakukan terhadap file, sedangkan `chown` mengatur siapa yang punya file tersebut.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
 laptop nya ngelag 
- Bagaimana cara Anda mengatasinya?  
 dengan bersabar
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
