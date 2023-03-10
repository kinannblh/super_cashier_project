# -*- coding: utf-8 -*-
"""Cashier

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MgNn3pKwvagBx_BszLJbBdfnzsvCj2Sx
"""

from tabulate import tabulate
import pandas as pd

class Transaction:

  def __init__ (self):
    '''
    Method untuk inisiasi class Transaction

    self.transaction (dict) = dictionary tempat penyimpanan data
    '''
    self.transaction = dict()

  def add_item(self, nama_item, jumlah_item, harga_per_item):
    '''
    Method untuk menambah item ke dalam daftar pesanan

    Parameters:
    nama_item (str, key) = nama item yang dibeli, merupakan key dalam dictionary
    jumlah_item (int) = jumlah item yang dibeli
    harga_per_item (int) = harga satuan item yang dibeli
    '''       

    #mengecek tipe data integer
    if isinstance (jumlah_item, int) == False:
       print(f"Tidak dapat menambahkan item {nama_item}. Jumlah item harus berupa angka.")

    elif isinstance (harga_per_item, int) == False:
         print(f"Tidak dapat menambahkan item {nama_item}. Harga item harus berupa angka.")

    else:
      #memastikan input data bernilai positif
      if jumlah_item <= 0:
         print(f"Tidak dapat menambahkan item {nama_item}. Jumlah item harus bernilai positif.")
      else:
        pass
        
        if harga_per_item <= 0:
           print(f"Tidak dapat menambahkan item {nama_item}. Harga item harus bernilai positif.")
      
        else:
         harga_total = jumlah_item*harga_per_item
         self.transaction.update({nama_item: [jumlah_item, harga_per_item, harga_total]})
         print(f"Item {nama_item} sejumlah {jumlah_item} seharga Rp{harga_per_item} per item berhasil ditambahkan.")

  def update_item_name(self, nama_item, nama_item_baru):
    '''
    Method untuk mengubah nama item yang sudah dimasukkan ke dalam daftar pesanan

    Parameters:
    nama_item (str)= nama item sebelum diganti, key lama
    nama_item_baru (str)= nama item baru, key baru
    '''
    temp = self.transaction[nama_item]
    self.transaction.pop(nama_item)
    self.transaction.update({nama_item_baru: temp})
    print(f"Item {nama_item} berhasil diubah menjadi {nama_item_baru}.")
    print(" ")
    
    #menampilkan daftar pesanan
    data = pd.DataFrame(self.transaction).T
    headers = ['Item', 'Jumlah Item', 'Harga per item', 'Total Harga']
    print("Berikut adalah daftar pesanan Anda:")
    print(" ")
    print(tabulate(data, headers))
  
  def update_item_qty(self, nama_item, update_jumlah_item):
    '''
    Method untuk mengubah jumlah item yang sudah yang sudah dimasukkan ke dalam daftar pesanan

    Parameters:
    nama_item (str, key): nama item yang akan diubah jumlahnya
    update_jumlah_item (int): jumlah baru dari item yang dibeli 
    '''
    #mengecek tipe data integer
    if isinstance (update_jumlah_item, int) == False: 
       print(f"Tidak dapat mengubah jumlah item {nama_item}. Jumlah item harus berupa angka.")

    else:
      #memastikan input data bernilai positif
      if update_jumlah_item <= 0:
         print(f"Tidak dapat mengubah jumlah item {nama_item}. Jumlah item harus bernilai positif.")
      else:
        self.transaction[nama_item][0] = update_jumlah_item
        self.transaction[nama_item][2] = update_jumlah_item*self.transaction[nama_item][1]
        print(f"Jumlah item {nama_item} berhasil diubah menjadi {update_jumlah_item} item.")
        print(" ")

        #menampilkan daftar pesanan
        data = pd.DataFrame(self.transaction).T
        headers = ['Item', 'Jumlah Item', 'Harga per item', 'Total Harga']
        print("Berikut adalah daftar pesanan Anda:")
        print(" ")
        print(tabulate(data, headers))

  def update_item_price(self, nama_item, update_harga_item):
    '''
    Method untuk mengganti harga item pada item yang sudah dimasukkan dalam daftar pesanan

    Parameters:
    nama_item (string, key) = nama item yang ingin diubah harganya 
    update_harga_item (int) = harga baru dari item
    '''
    #mengecek tipe data integer
    if isinstance (update_harga_item, int) == False: 
       print(f"Tidak dapat mengubah harga item {nama_item}. Harga item harus berupa angka.")

    else:
      #memastikan data harga item bernilai positif
      if update_harga_item <= 0:
         print(f"Tidak dapat mengubah harga item {nama_item}. Harga item harus bernilai positif.")
      else:
        self.transaction[nama_item][1] = update_harga_item
        print(f"Harga item {nama_item} berhasil diubah menjadi Rp{update_harga_item}")
        print(" ")

        #menampilkan daftar pesanan
        data = pd.DataFrame(self.transaction).T
        headers = ['Item', 'Jumlah Item', 'Harga per item', 'Total Harga']
        print("Berikut adalah daftar pesanan Anda:")
        print(" ")
        print(tabulate(data, headers))

  def delete_item(self, nama_item):
    '''
    Method untuk menghapus data nama item tertentu yang sudah dimasukkan ke dalam daftar pesanan

    Parameters:
    nama_item (str) = nama item yang datanya ingin dihapus
    '''
    try:
      self.transaction.pop(nama_item)
      print(f"{nama_item} berhasil dihapus dari daftar pesanan.")
      print(' ')
      
      #menampilkan daftar pesanan
      data = pd.DataFrame(self.transaction).T
      headers = ['Item', 'Jumlah Item', 'Harga per item', 'Total Harga']
      print("Berikut adalah daftar pesanan Anda:")
      print(" ")
      print(tabulate(data, headers))
    
    except KeyError:
      print(f"{nama_item} tidak terdapat dalam daftar pesanan.")
  
  def reset_transaction(self):
    '''
    Method untuk menghapus seluruh data yang sudah dimasukkan ke dalam daftar pesanan
    '''
    self.transaction.clear()
    print("Daftar pesanan berhasil dikosongkan.")

  def check_order(self):
    '''
    Method untuk mengecek kesalahan pada input data dan menghasilkan semua data pesanan
    '''
    
    for key, value in self.transaction.items():
        nama_item = key
        jumlah_item = value[0]
        harga_per_item = value[1]
    
    #mengecek daftar pesanan apakah kosong atau tidak
    if(len(self.transaction) == 0):
      print("Anda belum memasukkan item ke daftar pesanan.")
      print(" ")        
    
    else:
      #mengecek tipe data integer
      if isinstance (jumlah_item, int) == False:
         print("Jumlah item harus berupa angka!")

      elif isinstance (harga_per_item, int) == False:
         print("Harga item harus berupa angka!")

      else:
        #menampilkan daftar pesanan
        data = pd.DataFrame(self.transaction).T
        headers = ['Item', 'Jumlah Item', 'Harga per item', 'Total Harga']
        print("Berikut adalah daftar pesanan Anda:")
        print(" ")
        print(tabulate(data, headers))

  def total_price(self):
    '''
    Method untuk menghitung harga total yang harus dibayar
    '''
    #menampilkan daftar pesanan
    if(len(self.transaction) == 0):
      print("Anda belum memasukkan item ke daftar pesanan.")    
    else:
      data = pd.DataFrame(self.transaction).T
      headers = ['Item', 'Jumlah Item', 'Harga per item', 'Total Harga']
      print(tabulate(data, headers))

    #menghitung harga total dengan menambahkan seluruh harga total pada daftar pesanan
    harga_total = 0
    for harga in self.transaction:
        harga_total += self.transaction[harga][2]

    #branching diskon sesuai dengan persyaratan minimal belanja
    if harga_total > 500_000:
       diskon = 0.1
       harga_akhir = harga_total - (diskon * harga_total)
       print(' ')
       print(f"Total belanja Anda sebesar Rp{harga_total}.")
       print(f"Anda mendapatkan diskon sebesar {diskon * 100} %.")
       print(f"Anda hanya perlu membayar sebesar Rp{harga_akhir}.")

    
    elif harga_total > 300_000:
         diskon = 0.08
         harga_akhir = harga_total - (diskon * harga_total)
         print(' ')
         print(f"Total belanja Anda sebesar Rp{harga_total}.")
         print(f"Anda mendapatkan diskon sebesar {diskon * 100} %.")
         print(f"Anda hanya perlu membayar sebesar Rp{harga_akhir}.")

    elif harga_total > 200_000:
         diskon = 0.05
         harga_akhir = harga_total - (diskon * harga_total)
         print(' ')
         print(f"Total belanja Anda sebesar Rp{harga_total}.")
         print(f"Anda mendapatkan diskon sebesar {diskon * 100} %.")
         print(f"Anda hanya perlu membayar sebesar Rp{harga_akhir}.")

    else:
         harga_akhir = harga_total
         print(' ')
         print(f"Total belanja Anda sebesar Rp{harga_akhir}.")