
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Aster Rifani  
- **NIM**   : 250202915  
- **Kelas** : 1IKRB

---

## Tujuan
> Mengimplementasikan algoritma page replacement FIFO dalam program.

> Mengimplementasikan algoritma page replacement LRU dalam program.

> Menjalankan simulasi page replacement dengan dataset tertentu.

> Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.

> Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
   Manajemne memori virtual merupakan mekanisme sistem operasi untuk memngatur penggunaan memori utama dengan membagi memori ke dalam *page*. Ketika *page* yang dibutuhkan tidak tersedia di dalam memori utama, maka akan terjadi *page fault* sehingga sistem operasi harus melakukan proses *page replaceent*.

   Algoritma *page replacement* digunakan untuk menentukan *page* yang akan diganti. FIFO mengganti *page* yang pertama masuk ke memori, sedangkan LRU mengganti *page* yang paling lama tidak digunakan, yang umumnya memberikan performa lebih baik.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
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
   1. Hasil eksekusi fifo page replacement:
![Screenshot](screenshots/Screenshot%202026-01-01%20082908.png)
   2. Hasil eksekusi lru page replacement:
   ![Screenshot](screenshots/Screenshot%202026-01-01%20083249.png)
   3. Summary page replacement fifo vs lru :
   ![Screenshot](screenshots/Screenshot%202026-01-01%20083734.png)

---

## Analisis
   1. Tabel FIFO
      | No | Page | Kondisi | Frame 1 | Frame 2 | Frame 3 |
      | -- | ---- | ------- | ------- | ------- | ------- |
      | 1  | 7    | Fault   | 7       | –       | –       |
      | 2  | 0    | Fault   | 7       | 0       | –       | 
      | 3  | 1    | Fault   | 7       | 0       | 1       |
      | 4  | 2    | Fault   | 2       | 0       | 1       | 
      | 5  | 0    | Hit     | 2       | 0       | 1       |
      | 6  | 3    | Fault   | 2       | 3       | 1       |
      | 7  | 0    | Fault   | 2       | 3       | 0       |
      | 8  | 4    | Fault   | 4       | 3       | 0       |
      | 9  | 2    | Fault   | 4       | 2       | 0       |
      | 10 | 3    | Fault   | 4       | 2       | 3       |
      | 11 | 0    | Fault   | 0       | 2       | 3       |
      | 12 | 3    | Hit     | 0       | 2       | 3       |
      | 13 | 2    | Hit     | 0       | 2       | 3       |
      Total Page Fault FIFO : 10

   2. Tabel LRU
      | No | Page | Kondisi | Frame 1 | Frame 2 | Frame 3 |
      | -- | ---- | ------- | ------- | ------- | ------- |
      | 1  | 7    | Fault   | 7       | –       | –       |
      | 2  | 0    | Fault   | 7       | 0       | –       |
      | 3  | 1    | Fault   | 7       | 0       | 1       |
      | 4  | 2    | Fault   | 2       | 0       | 1       |
      | 5  | 0    | Hit     | 2       | 0       | 1       |
      | 6  | 3    | Fault   | 2       | 0       | 3       |
      | 7  | 0    | Hit     | 2       | 0       | 3       |
      | 8  | 4    | Fault   | 4       | 0       | 3       |
      | 9  | 2    | Fault   | 4       | 0       | 2       |
      | 10 | 3    | Fault   | 4       | 3       | 2       |
      | 11 | 0    | Fault   | 0       | 3       | 2       |
      | 12 | 3    | Hit     | 0       | 3       | 2       |
      | 13 | 2    | Hit     | 0       | 3       | 2       |
      Total Page Fault LRU : 9
   
   3. Tabel Perbandingan
      | Algoritma | Jumlah Page Fault | Keterangan |
      | --------- | ----------------- | ---------- |
      | FIFO | 10 | Mengganti halaman paling awal masuk |
      | LRU | 9 | Mengganti halaman yang paling tidak dipakai |


---

## Kesimpulan
Berdasarkan praktikum yang dilakukan, dapat disimpulkan bahwa mekanisme *page replacement* sangat berpengaruh terhadap kinerja manajemen memori virtual dalam sistem operasi. Algoritma FIFO mudah diimplementasikan namun dapat menghasilkan jumlah *page fault* yang lebih tinggi, sedangkan algoritma LRU cenderung lebih efisien karena mempertimbangkan riwayat penggunaan *page*. Dengan demikian, pemilihan algoritma *page replacement* yang tepat dapat meningkatkan efisiensi penggunaan memori dan performa sistem secara keseluruhan.


---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?
   **Jawaban:**  FIFO mengganti page yang pertama kali masuk ke memori tanpa melihat seberapa sering atau terakhir page tersebut digunakan, sedangkan LRU mengganti page yang paling lama tidak digunakan berdasarkan riwayat akses.
2. Mengapa FIFO dapat menghasilkan *Belady’s Anomaly*?
   **Jawaban:**  FIFO dapat mengalami Belady’s Anomaly karena penambahan jumlah frame memori tidak selalu menurunkan jumlah page fault. Hal ini terjadi karena FIFO tidak mempertimbangkan pola penggunaan page, sehingga page yang masih sering dibutuhkan dapat tergantikan.
3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
   **Jawaban:**  LRU mempertimbangkan prinsip lokalitas, yaitu page yang baru digunakan cenderung digunakan kembali. Oleh karena itu, LRU biasanya menghasilkan jumlah page fault yang lebih sedikit dibanding FIFO.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
