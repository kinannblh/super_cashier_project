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


## Penjelasan Functions

1. init ()
</br>Method untuk inisiasi class Transaction
</br>self.transaction (dict): Data akan disimpan dalam bentuk dictionary 

2. add_items (nama_item, jumlah_item, harga_per_item)
</br>Method untuk menambah item ke dalam daftar pesanan
</br>Parameters:
    </br>nama_item (str, key) = nama item yang dibeli, merupakan key dalam dictionary
    </br>jumlah_item (int) = jumlah item yang dibeli
    </br>harga_per_item (int) = harga satuan item yang dibeli

3. update_item_name (nama_item, update_nama_item)
 </br>Method untuk mengubah nama item yang sudah dimasukkan ke dalam daftar pesanan
    </br>Parameters:
    </br>nama_item (str)= nama item sebelum diganti, key lama
    </br>nama_item_baru (str)= nama item baru, key baru

4. update_item_qty (nama_item, update_jumlah_item)
</br>Method untuk mengubah jumlah item yang sudah yang sudah dimasukkan ke dalam daftar pesanan
    </br>Parameters:
    </br>nama_item (str, key): nama item yang akan diubah jumlahnya
    </br>update_jumlah_item (int): jumlah baru dari item yang dibeli 

5. update_item_price (nama_item, update_harga_item)
</br>Method untuk mengganti harga item pada item yang sudah dimasukkan dalam daftar pesanan
    </br>Parameters:
    </br>nama_item (string, key) = nama item yang ingin diubah harganya 
    </br>update_harga_item (int) = harga baru dari item

6. delete_item (nama_item)
</br>Method untuk menghapus data nama item tertentu yang sudah dimasukkan ke dalam daftar pesanan
    </br>Parameters:
    </br>nama_item (str) = nama item yang datanya ingin dihapus

7. reset_transaction()
</br>Method untuk menghapus seluruh data yang sudah dimasukkan ke dalam daftar pesanan

8. check_order()
</br>Method untuk mengecek kesalahan pada input data dan menghasilkan semua data pesanan

9. total_price()
</br>Method untuk menghitung harga total yang harus dibayar

## Test Case
Dapat dilihat pada notebook Test_Case_Super_Cashier.ipynb
