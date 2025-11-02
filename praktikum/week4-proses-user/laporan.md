
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Aster Rifani  
- **NIM**   : 250202915  
- **Kelas** : 1IKRB

---

## Tujuan 
> Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
> Menampilkan daftar proses yang sedang berjalan dan statusnya.  
> Menggunakan perintah untuk membuat dan mengelola user.  
> Menghentikan atau mengontrol proses tertentu menggunakan PID.  
> Menjelaskan kaitan antara manajemen user dan keamanan sistem.  

---

## Dasar Teori
Sistem operasi berperan sebagai penghubung antara pengguna dan perangkat keras komputer dengan mengelola sumber daya seperti prosesor, memori, serta perangkat input dan output. Salah satu fungsi utamanya adalah pengelolaan proses, yaitu entitas yang merepresentasikan program yang sedang dieksekusi beserta semua informasi yang diperlukan untuk menjalankannya. Setiap proses memiliki identitas unik dan dapat berada pada beberapa keadaan seperti berjalan, menunggu, atau berhenti. Mekanisme manajemen proses meliputi pembuatan, penjadwalan, komunikasi antarproses, serta penghentian proses untuk menjamin efisiensi dan stabilitas sistem.

Dalam lingkungan multiuser seperti Linux, sistem operasi juga menjalankan fungsi manajemen pengguna untuk memastikan keamanan dan keteraturan akses terhadap sumber daya. Setiap pengguna memiliki identitas berupa user ID dan group ID yang menentukan hak akses terhadap file, direktori, maupun layanan sistem. Pemisahan antara pengguna biasa dan administrator (root) diterapkan untuk mencegah penyalahgunaan wewenang dan menjaga integritas sistem. Melalui pengaturan hak akses dan otorisasi, sistem dapat membatasi tindakan pengguna terhadap komponen penting, sehingga tercipta lingkungan kerja yang aman dan terkendali.

Linux menyediakan berbagai perintah yang digunakan untuk memantau serta mengelola proses dan pengguna. Perintah `ps` menampilkan daftar proses yang sedang berjalan, `top` menampilkan aktivitas proses secara dinamis, dan `kill` digunakan untuk mengirim sinyal ke proses tertentu agar dihentikan. Selain itu, perintah `adduser` digunakan untuk menambahkan akun pengguna baru beserta pengaturan awalnya. Penggunaan perintah-perintah ini memungkinkan administrator untuk mengawasi kinerja sistem, mengatur prioritas proses, serta menjaga kestabilan operasi. Melalui kombinasi antara manajemen proses dan manajemen pengguna, sistem operasi Linux mampu menciptakan lingkungan yang efisien, aman, dan terstruktur dalam menjalankan berbagai aplikasi secara bersamaan.


---

## Langkah Praktikum
1. 1. **Setup Environment**
   - Menggunakan CloudShell.  
   - Memastikan sudah login sebagai user non-root.  
   - Menyiapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   -  Menjalankan perintah berikut:
   `whoami`
   `id`
   `groups`
   - Menjelaskan setiap output dan fungsinya.  
   - Membuat user baru (jika memiliki izin sudo):
     `sudo adduser praktikan`
     `sudo passwd praktikan`
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   - Menjalankan:
   `ps aux | head -10`
   `top -n 1`
   - Menjelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Menyimpan tangkapan layar `top` ke:
   `praktikum/week4-proses-user/screenshots/top.png`

4. **Eksperimen 3 – Kontrol Proses**
   - Menjalankan program latar belakang:
     `sleep 1000 &`
     `ps aux | grep sleep`
   - Mencatat PID proses `sleep`.  
   - Menghentikan proses:
     `kill <PID>`
   - Memastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   - Menjalankan:
   `pstree -p | head -20`
   - Mengamati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Mencatat hasilnya dalam laporan.

6. **Commit & Push**
   `git add .`
   `git commit -m "Minggu 4 - Manajemen Proses & User"`
   `git push origin main`

---

## Kode / Perintah
- Hasil observasi seluruh perintah dimasukkan ke dalam `laporan.md`.  
- Screenshot hasil eksekusi disimpan di folder `screenshots/`.  
- Laporan lengkap tersimpan di `laporan.md`. 
- Eksperimen 1 :  `whoami`
                  `id`
                  `groups`
                  `sudo adduser praktikan`
                  `sudo passwd praktikan`
- Eksperimen 2 :  `ps aux | head -10`
                  `top -n 1`
   Menyimpan tangkapan layar `top` ke:
   `praktikum/week4-proses-user/screenshots/top.png`
- Eksperimen 3 :  `sleep 1000 &`
                  `ps aux | grep sleep`
                  `kill <PID>`
                  `ps aux | grep sleep`
- Eksperimen 4 :  `pstree -p | head -20`
- Commit & Push : `git add .`
                  `git commit -m "Minggu 4 - Manajemen Proses & User"`
                  `git push origin main`

---

## Hasil Eksekusi
1. Eksperimen 1 – Identitas User

  * Menjalankan Perintah `whoami`,`id`,& `groups`
   ![Screenshot Eksperimen 1](screenshots/Eksperimen%201.a.png)

   a. `whoami` : 

         - Output : asterrifani0624
         - Fungsi : memastikan identitas user aktif terutama ketika bekerja dengan hak akses berbeda (misalnya setelah menggunakan `sudo` atau `su`).

   b. `id` : 

         - Output : uid=1000(asterrifani0624) gid=1000(asterrifani0624) groups=1000(asterrifani0624),4(adm),27(sudo),996(docker)
         - Fungsi : untuk mengecek hak akses dan grup 
         keanggotaan seorang user di sistem.

   c. `groups` :

         - Output : asterrifani0624 adm sudo docker 
         - Fungsi :  menampilkan daftar grup yang dimiliki oleh user saat ini dalam format lebih sederhana dibanding `id`.
   * Membuat User Baru 
   ![Screenshot Eksperimen 1](screenshots/Eksperimen%201.b.png)

      Percobaan selanjutnya adalah menambahkan pengguna baru dengan nama praktikan menggunakan perintah berikut:
      `sudo adduser praktikan`
      Sistem kemudian menampilkan proses penambahan user baru, termasuk pembuatan grup baru dengan nama yang sama, penentuan UID/GID, serta permintaan pengisian password dan data tambahan seperti nama lengkap dan nomor telepon.
      Setelah proses selesai, user praktikan berhasil ditambahkan ke sistem dengan direktori home /home/praktikan.
      Untuk mengatur atau mengganti password user tersebut dapat digunakan perintah:
      `sudo passwd praktikan`
   * Uji Login User Baru

      Setelah user baru berhasil dibuat, dilakukan pengujian login menggunakan perintah:
      `$ su - praktikan`
      Jika login berhasil, prompt terminal akan berubah menjadi:
      `praktikan@cloudshell:-$`
      Hal ini menandakan bahwa sesi telah berpindah ke akun praktikan, dengan direktori home dan lingkungan kerja yang terpisah dari user sebelumnya.

2. Eksperimen 2 – Monitoring Proses

   * Penjelasan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.   

   | Kolom | Arti/Fungsi |
   | :--- | ---  |
   | PID	 |Identitas unik proses yang diberikan oleh kernel. Proses dengan PID kecil seperti 1 (bash) dan 9 (syslogd) biasanya merupakan proses sistem yang berjalan sejak awal.|
   | USER |Menunjukkan pemilik proses, misalnya root untuk proses sistem, dan asterri+ untuk proses milik pengguna biasa.|
   | %CPU |Menampilkan persentase penggunaan CPU oleh proses. Nilai 0.0 menunjukkan proses tidak sedang aktif menggunakan CPU.|
   | %MEM |	Menampilkan persentase penggunaan memori fisik (RAM). Semakin besar nilainya, semakin banyak sumber daya yang digunakan.|
   | COMMAND |	Menunjukkan nama program atau perintah yang dijalankan, seperti bash, dockerd, containerd, atau node.|
   * Tangkapan Layar top n- 1
   ![Screenshot Eksperimen 3](screenshots/Eksperimen%202.png)

3. Eksperimen 3 -  Kontrol Proses

   ![Screenshot Eksperimen 3](screenshots/Eksperimen%203.png)

   Proses sleep dengan `PID 1364` berhasil dijalankan di latar belakang dan dapat diverifikasi keberadaannya menggunakan kombinasi perintah `ps` dan `grep`. Hal ini menunjukkan bahwa sistem Linux memberikan fasilitas bagi pengguna untuk menjalankan dan memantau proses secara paralel tanpa mengganggu aktivitas terminal utama.
   Perintah `kill` merupakan salah satu mekanisme dasar kontrol proses di Linux. Dengan menggunakan PID sebagai identitas unik, pengguna dapat menghentikan proses tertentu tanpa memengaruhi proses lain yang sedang berjalan.
   Secara default, `kill` mengirimkan sinyal SIGTERM, namun jika proses tidak merespons, pengguna dapat menggunakan sinyal lain seperti:
   `kill -9 <PID>` → mengirim sinyal SIGKILL, menghentikan proses secara paksa.
   `kill -15 <PID>` → sinyal default untuk penghentian normal.
   Setelah menjalankan `kill 1364`, proses `sleep 1000` berhenti dengan normal, terbukti dari pesan “Terminated” dan tidak munculnya lagi proses tersebut pada hasil `ps aux | grep sleep`.

4. Eksperimen 4 – Analisis Hierarki Proses
   ![Screenshots Eksperimen 4](screenshots/Eksperimen%204.png)
```   
 systemd(1)
├─ sshd(502)
│  └─ bash(508)
│     └─ pstree(1360)
├─ cron(300)
├─ dbus-daemon(250)
├─ dockerd(248)
│  └─ containerd(303)
└─ systemd-journald(170)
```
   Perintah `pstree -p` menampilkan hierarki proses dalam bentuk pohon.
   Dari hasil percobaan, dapat diidentifikasi bahwa:
   * Proses utama (induk) pada sesi Cloud Shell ini adalah `bash(1)`.
   * Beberapa proses turunan penting seperti `dockerd`, `containerd`, `python`, dan `node` berperan dalam menjalankan layanan sistem dan editor.

---

## Analisis
   1. Identitas User
   
   Perintah `whoami`, `id`, dan `groups` menunjukkan bahwa pengguna aktif adalah `asterrifani0624`.
   `id` memberikan informasi lengkap tentang UID, GID, dan grup yang dimiliki user, sedangkan groups menyajikan daftar grup secara lebih ringkas.
   Penambahan user baru (praktikan) berhasil dilakukan dan dapat diuji melalui perintah `su - praktikan`, menandakan sistem memberikan kontrol penuh terhadap hak akses dan sesi pengguna.

   2. Monitoring Proses
   
   Kolom penting seperti PID, USER, %CPU, %MEM, dan COMMAND membantu memantau aktivitas proses di sistem.
   PID kecil biasanya menunjukkan proses sistem, sedangkan proses yang dijalankan pengguna memiliki PID lebih besar.
   Monitoring proses memberikan informasi tentang konsumsi sumber daya sistem (CPU dan RAM) serta kepemilikan proses.

   3. Kontrol Proses
   
   Sistem Linux memungkinkan pengguna menjalankan proses di latar belakang (`sleep`) dan memantau keberadaannya.
   Perintah `kill` memungkinkan penghentian proses baik secara normal (`SIGTERM`) maupun paksa (`SIGKILL`).
   Hal ini menunjukkan kemampuan manajemen proses secara fleksibel tanpa mengganggu aktivitas terminal utama.

   4. Hierarki Proses

   Perintah `pstree -p` menampilkan hubungan induk-anak antarproses.
   Di Cloud Shell, proses induk utama adalah `bash(1)` sementara proses turunan meliputi `dockerd`, `containerd`, `python`, dan `node`.
   Struktur ini berbeda dengan sistem Linux lokal, yang biasanya memiliki `systemd(1 se)`bagai proses induk.Analisis hierarki proses membantu memahami alur eksekusi proses dan interaksi antarproses di lingkungan Linux.

---

## Kesimpulan
   Berdasarkan percobaan yang dilakukan, dapat disimpulkan bahwa Linux memberikan kemampuan yang baik untuk mengelola identitas pengguna, memantau, dan mengontrol proses. Pengguna aktif dapat diverifikasi menggunakan perintah `whoami`, `id`, dan `groups`, serta sistem memungkinkan penambahan user baru dengan hak akses yang terkontrol. Monitoring proses memperlihatkan penggunaan sumber daya seperti CPU dan memori, sedangkan perintah `kill` memungkinkan penghentian proses secara normal maupun paksa. Analisis hierarki proses melalui `pstree` menunjukkan hubungan induk-anak antarproses, di mana di Cloud Shell proses induk utama adalah `bash(1)`, sementara di Linux lokal biasanya `systemd(1)`. Secara keseluruhan, percobaan ini menunjukkan bahwa Linux menyediakan lingkungan yang transparan, fleksibel, dan efisien dalam manajemen user dan proses.

---

## Quiz
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux? 
   **Jawaban:**  
   Proses `init` atau `systemd` adalah proses pertama yang dijalankan oleh kernel saat booting dan memiliki PID 1. Fungsi utamanya adalah menjadi induk dari semua proses lain di sistem, memulai layanan-layanan sistem, mengatur runlevel atau target, serta menangani proses-proses daemon. `systemd` merupakan versi modern dari `init` yang menyediakan manajemen layanan lebih efisien, parallel startup, logging terintegrasi, dan kontrol proses yang lebih baik.
2. Apa perbedaan antara `kill` dan `killall`?  
   **Jawaban:**   
   * `kill` digunakan untuk mengirim sinyal ke proses tertentu berdasarkan `PID`. Contohnya: `kill 1234` mengirim sinyal ke proses dengan `PID 1234`.
   * `killall` digunakan untuk mengirim sinyal ke semua proses yang memiliki nama tertentu. Contohnya: `killall firefox` menghentikan semua proses dengan nama firefox sekaligus
3. Mengapa user `root` memiliki hak istimewa di sistem Linux? 
   **Jawaban:** 
    User `root` memiliki hak istimewa karena merupakan administrator sistem. Root dapat mengakses semua file, mengubah konfigurasi sistem, menginstal atau menghapus program, serta menjalankan perintah yang dibatasi untuk user biasa. Hak istimewa ini diperlukan agar sistem dapat dikelola secara penuh dan aman, namun penggunaannya harus hati-hati untuk mencegah kerusakan sistem atau risiko keamanan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
   laptop yang rusak.
- Bagaimana cara Anda mengatasinya?
   ganti laptop baru.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
