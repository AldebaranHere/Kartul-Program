# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:24:53 2022

@author: hp
Subject: Karya Tulis Informatika
"""
import math

pi = 3.1415

print("Masukkan 1 untuk menghitung kubus.")
print("Masukkan 2 untuk menghitung balok.")
print("Masukkan 3 untuk menghitung prisma segitiga.")
print("Masukkan 4 untuk menghitung piramida alas persegi.")
print("Masukkan 5 untuk menghitung silinder.")
print("Masukkan 6 untuk menghitung kerucut.")
print("Masukkan 7 untuk menghitung bola.")
print("=====================MOHON DIBACA=====================")
print("Keterangan: Masukkan nilai panjang, lebar, dan lain sebagainya dalam satuan cm") 

def tigadimensi():
    pemulai = int(input("Masukkan pilihan di sini: "))
                  
    if pemulai == 1:
        panjang = float(input("Masukkan nilai panjang: "))
        volume_kubus = panjang ** 3
        luas_permukaan_kubus = 6 * (panjang ** 2)
        print(f'Volume Kubus: {volume_kubus} cm³')
        print(f'Luas Permukaan Kubus: {luas_permukaan_kubus} cm²')
        
    elif pemulai == 2:
        panjang = float(input("Masukkan nilai panjang: "))
        lebar = float(input("Masukkan nilai lebar: "))
        tinggi = float(input("Masukkan nilai tinggi: "))
        volume_balok = panjang * lebar * tinggi
        luas_permukaan_balok = (panjang * lebar * 2) + (lebar * tinggi * 2) + (tinggi * panjang * 2)
        print(f'Volume Balok: {volume_balok} cm³')
        print(f'Luas Permukaan Balok: {luas_permukaan_balok} cm²')
    
    elif pemulai == 3:
        a = float(input("Masukkan nilai panjang sisi segitiga pertama: "))
        b = float(input("Masukkan nilai panjang sisi segitiga kedua: "))
        c = float(input("Masukkan nilai panjang sisi segitiga ketiga: "))
        t = float(input("Masukkan nilai tinggi prisma: "))
        
        s = (a+b+c)/2
        
        luas_segitiga = math.sqrt(s*(s-a)*(s-b)*(s-c))
        
        volume_prisma_segitiga = luas_segitiga * t
        luas_permukaan_prisma_segitiga = 2*luas_segitiga + 2*s*t
        
        print(f'Volume Prisma Segitiga: {volume_prisma_segitiga} cm³')
        print(f'Luas Permukaan Prisma Segitiga: {luas_permukaan_prisma_segitiga} cm²')
    
    elif pemulai == 4:
        panjang = l = float(input("Masukkan nilai panjang: "))
        lebar = w = float(input("Masukkan nilai lebar: "))
        tinggi = h = float(input("Masukkan nilai tinggi: "))
        volume_piramida_alas_persegi = l * w * h / 3
        luas_permukaan_piramida_alas_persegi = l * w + (l * math.sqrt(((lebar/2)) ** 2 + (tinggi ** 2))) + (w * math.sqrt((((l/2)) ** 2) + (h ** 2)))
        print(f'Volume Piramida Alas Persegi: {volume_piramida_alas_persegi} cm³')
        print(f'Luas Permukaan Piramida Alas Persegi: {luas_permukaan_piramida_alas_persegi} cm²')
    
    elif pemulai == 5:
        r = float(input("Masukkan nilai radius: "))
        h = float(input("Masukkan tinggi silinder: "))
        volume_cylinder = pi * (r ** 2) * h
        surface_area_cylinder = 2 * pi * r * (h + r)
        print(f'Volume Silinder: {volume_cylinder} cm³')
        print(f'Luas Permukaan Silinder: {surface_area_cylinder} cm²')
    
    elif pemulai == 6:
        r = float(input("Masukkan nilai radius: "))
        h = float(input("Masukkan nilai tinggi: "))
        volume_kerucut = pi * (r ** 2) * (h / 3)
        luas_permukaan_kerucut = pi * r * (r + (((h ** 2) + (r ** 2)) ** (1 / 2)))
        print(f'Volume Kerucut: {volume_kerucut} cm³')
        print(f'Luas Permukaan Kerucut:  {luas_permukaan_kerucut} cm²')
    
    elif pemulai == 7:
        
        r = float(input("Masukkan nilai radius: "))
        volume_bola = (4 / 3) * pi * (r ** 3)
        luas_permukaan_bola = 4 * pi * (r ** 2)
        print(f'Volume Bola: {volume_bola} cm³')
        print(f'Luas Permukaan Bola: {luas_permukaan_bola} cm²')
    
    print("===PROGRAM SELESAI===")    
    print("Masukkan 1 untuk memakai ulang program ini")
    print("Masukkan apapun selain 1 untuk berhenti memakai program ini")
    
    konfirmasi = input("Masukkan di sini: ")
    
    if konfirmasi == "1":
        tigadimensi()
    else:
        print("Terima kasih sudah menggunakan program ini.")
        pass
    
tigadimensi()