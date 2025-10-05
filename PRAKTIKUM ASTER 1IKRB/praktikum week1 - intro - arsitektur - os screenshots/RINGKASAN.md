# RINGKASAN
- Perbedaan monolithic kernel, microkernel, & layered architecture
- Contoh OS nyata yang menggunakan masing-maasing model
- Analisis: model yang paling relevan untuk sistem modern
### Perbedaan Monoithic Kernel, Microkernel, & Layered Architecture
#### - Monolithic Kernel
Seluruh layanan sistem operasi (manajemen proses, manajemen memori, file system, device driver, dan networking) berjalan dalam ruang alamat kernel (kernel space)dengan mode hak akses tertinggi (supervisor mode).
#### - Microkernel
Kernel dikurangi seminimal mungkin, hanya mencakup fungsi-fungsi inti(manajemen komunikasi antar-proses/IPC, penjadwalan dasar, dan manajemen memori level rendah).Layanan sistem operasi lainnya (seperti file system, device driver, dan networking)diimplementasikan sebagai proses pengguna (user-level servers)diluar kernel.
#### - Layered Architecture
Arsitektur ini mengatur sistem operasi ke dalam lapisan-lapisan (layers),di mana setiap lapisan hanya dapat menggunakan fungsi dan layanan yang disediakan oleh lapisan yang lebih rendah.
Lapisan 0 adalah perangkat keras (hardware), dan laypisan N adalah antarmuka pengguna (user interfce). Dan tujuannya untuk mempermudah desain, implementasi, dan debugging.
### Contoh OS nyata yang menggunakan masing-masing model
A.Monolithic Kernel : Linux & UNIX
B.Microkernel : MINIX & macOS
C.Layered Architecture : The OS
### Analisis: model yang paling relevan untuk sistem modern
Model sistem operasi (OS) yang paling relevan untuk sistem modern bergantung pada jenis perangkat dan tujuan penggunaanny, dengan:
 - *Windows* menjadi pilihan dominan PC umum,
 - *macOS* untuk ekosistem Apple,
 - *Linux* untuk server dan kustomisasi,
 - serta *Android* untuk perangkat seluler seperti smartphone dan tablet.
