
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
