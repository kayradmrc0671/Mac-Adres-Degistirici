#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("CODER:BY SOULFLY.PY")
print("İnstagram:@soulfly.py")

os.system("apt-get install figlet")
os.system("apt-get install macchanger")
os.system("clear")
os.system("figlet MAC değiştirme BY SOULFLY.PY")

print("""
MAC DEĞİŞTİRME PROGRAMINA HOŞ GELDİNİZ

1) MAC ADRESİ RANDOM ŞEKİLDE BELİRLE
2) MAC ADRESİNİ KENDİ ELİNLE BELİRLE
3) MAC ADRESİNİ ORİJİNALE DÖNDÜR
""")

islemno = raw_input("İşlem No Girin: ")

if(islemno=="1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
print("\033[92mYENİ MAC ADRESİNİZ RANDOM BELİRLENDİ.")

if(islemno=="2"):
	macadres = raw_input("YENİ MAC ADRESİNİZİ GİRİNİZ:")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac" + macadres + "eth0")
	os.system("ifconfig eth0 up")
print("\033[92mYENİ MAC ADRESİNİZİ ELLE BELİRLEDİNİZ")

if(islemno=="1"):
	os.system("ifconfig eth0 down")
	os.system("ifconfig -p eth0")
	os.system("ifconfig eth0 up")
print("\033[92mMAC ADRESİNİZ ORJİNALE DÖNDÜ")