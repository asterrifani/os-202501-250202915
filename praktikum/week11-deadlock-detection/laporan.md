
# Laporan Praktikum Minggu 11
Topik:  Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Aster Rifani
- **NIM**   : 290202915  
- **Kelas** : 1ikrb

---

## Tujuan
> Membuat program sederhana untuk mendeteksi deadlock.

> Menjalankan simulasi deteksi deadlock dengan dataset uji.

> Menyajikan hasil analisis deadlock dalam bentuk tabel.

> Memberikan interpretasi hasil uji secara logis dan sistematis.

> Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
Deadlock merupakan sebuah kondisi pada sistem operasi yang terjadi akibat dua atau lebih proses saling menunggu sumber daya yang sedang digunakan oleh proses lain,sehingga tidak ada satu pun proses yang dapat melanjutkan eksekusinya. Kondisi ini umumnya terjadi karena terpenuhinya empat syarat deadlock, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait.

Deteksi deadlock dilakukan dengan memantau keadaan sistem untuk mengidentifikasi adanya siklus ketergantungan antara pross dan sumber daya. Pendekatan ini menggunakan algoritma deeksi yang menganalisis alokasi dan permintaan sumber daya untuk menentukan apakah sistem berada dalam kondisi deadlock. Setelah terdeteksi, sistem dapat mengambi tindakan pemulihan,seperti menghentikan proses tertentu atau mlepaskan sumber daya,agar sistem dapat kembali berjalan normal.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```


---

## Kode / Perintah
- Kode program deteksi deadlock di folder `code/`.  
- Dataset uji di `code/dataset_deadlock.csv`.  
- Screenshot hasil eksekusi di folder `screenshots/`. 

---

## Hasil Eksekusi
![Screenshot](screenshots/Screenshot%202026-01-01%20134334.png)

---

## Analisis
Tabel hasil deteksi deadlock :
| Proses | Status   |
| ------ | -------- |
| P1     | Deadlock |
| P2     | Deadlock |
| P3     | Deadlock |

Berdasarkan hasil simulasi, seluruh proses berada dalam kondisi deadlock karena setiap proses memegang satu resource dan menunggu resource lain yang sedang digunakan oleh proses lain, sehingga tidak ada proses yang dapat melanjutkan eksekusi. Proses P1 memegang R1 dan menunggu R2, P2 memegang R2 dan menunggu R3, serta P3 memegang R3 dan menunggu R1, yang membentuk circular wait P1 → P2 → P3 → P1. Kondisi ini memenuhi keempat syarat deadlock, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait, sehingga sistem dinyatakan berada dalam kondisi deadlock.

---

## Kesimpulan
Berdasarkan hasil simulasi deteksi deadlock, sistem teridentifikasi berada dalam kondisi deadlock karena adanya ketergantungan melingkar antar proses dalam penggunaan resource.

Algoritma deteksi deadlock berhasil mengidentifikasi proses-proses yang terlibat deadlock sesuai dengan teori deadlock, sehingga dapat disimpulkan bahwa simulasi berjalan dengan benar dan efektif dalam mendeteksi kondisi deadlock pada sistem operasi.

---

## Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?  
   **Jawaban:**  
   - *Deadlock prevention* mencegah deadlock dengan menghilangkan salah satu syarat deadlock sejak awal.
   - *Deadlock avoidance* menghindari deadlock dengan memastikan sistem selalu berada dalam kondisi aman sebelum resource dialokasikan.
   - *Deadlock detection* membiarkan deadlock terjadi lalu mendeteksinya dan melakukan pemulihan.
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   **Jawaban:**  karena tidak semua deadlock dapat dicegah atau dihindari sebelumnya, sehingga sistem perlu mengenali deadlock yang telah terjadi agar dapat melakukan tindakan pemulihan dan menjaga sistem tetap berjalan.
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?  
   **Jawaban:**  
   - Kelebihan:
      Pendekatan deteksi deadlock lebih fleksibel karena sistem tidak perlu mencegah atau menghindari deadlock sejak awal, sehingga penggunaan resource dapat lebih efisien.

   - Kekurangan:
      Pendekatan ini memerlukan mekanisme tambahan untuk mendeteksi dan memulihkan deadlock, serta berisiko mengganggu proses yang sedang berjalan saat dilakukan pemulihan.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
