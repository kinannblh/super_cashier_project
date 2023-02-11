# Super Cashier Project

## Latar belakang
Super Cashier App module adalah sistem kasir swalayan (self-service) sebuah supermarket. Pelanggan dapat memasukkan daftar belanja secara mandiri sehingga pelanggan dari berbagai kota berbeda juga dapat berbelanja di supermarket tersebut.
</br> Modul ini dibuat dengan menerapkan Object Oriented Programming, try-except, dan clean code.

## Objektif dan Feature Requirements
### Objektif
Pelanggan dapat memasukkan sendiri nama item, jumlah item, dan harga item ke dalam daftar pesanan. Output berupa daftar pesanan yang di dalamnya terdapat daftar nama item, jumlah item, harga per item, dan harga serta harga akhir yang harus dibayarkan oleh pelanggan.

### Feature Requirements
Modul ini memiliki beberapa feature requirements dengan flow berikut:
1. Pelanggan membuat ID transaksi
2. Pelanggan memasukkan nama ite, jumlah item, dan harga per item.
3. Jika terdapat kesalahan input, pelanggan dapat
</br> a. Mengubah nama item
</br> b. Mengubah jumlah item
</br> c. Mengubah harga item
4. Jika terdapat pembatalan transaksi, pelanggan dapat: 
</br> a. Menghapus salah satu nama item dimana saat menghapus item tersebut, jumlah dan harga item juga akan terhapus
</br> b. Menghapus seluruh transaksi/reset transaksi
5. Jika transaksi sudah selesai tetapi pelanggan ingin melihat kembali data item yang dimasukkan, pelanggan akan melihat:
</br> a. Jika tidak terdapat kesalahan input, akan muncul pesan "Pemesanan sudah benar." atau pesan semacamnya
</br> b. Jika terdapat kesalahan input, akan muncul pesan "Terdapat kesalahan input data." atau pesan semacamnya
</br> c. Output daftar pesanan
6. Pelanggan dapat melihat total harga yang harus dibayarkan. Terdapat beberapa persyaratan untuk mendapatkan diskon:
</br> a. Jika transaksi mencapai Rp200.000, pelanggan mendapat diskon 5%
</br> b. Jika transaksi mencapai Rp300.000, pelanggan mendapat diskon 8%
</br> c. Jika transaksi mencapai Rp500.000, pelanggan mendapat diskon 10%

## Flowchart

![Flowchart cashier (1)](https://user-images.githubusercontent.com/108425666/218265692-0999beea-c56a-4799-b383-08fa3c0202c1.jpeg)



