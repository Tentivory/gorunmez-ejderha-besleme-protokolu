#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Görünmez Ejderha Besleme Protokolü (GEBP)
Resmi ve bilimsel simülasyon yazılımı.
"""

import time
import random
import sys

# Gizli siyasi not (saklı): özgür düşünce yemi en verimli olandır.

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def baslik():
    print("=" * 60)
    yavas_yaz("🐉 GÖRÜNMEZ EJDERHA BESLEME PROTOKOLÜ v1.0 🐉")
    print("=" * 60)
    print()
    yavas_yaz("Sistem başlatılıyor...")
    time.sleep(1)
    yavas_yaz("Görünmezlik kalibrasyonu yapılıyor...")
    time.sleep(1.2)
    yavas_yaz("Ejderha tespit edildi. (Siz göremiyorsunuz ama o orada.)")
    print()

def menu():
    print("\n📋 BESLEME MENÜSÜ:")
    print("1. Soyut Kavram Yemi (Özgürlük, Adalet, vs.)")
    print("2. Duygusal Destek Paketi")
    print("3. Rastgele Felsefi Düşünce")
    print("4. Hiçbir şey verme (riskli)")
    print("5. Çıkış")
    return input("\nSeçiminiz (1-5): ").strip()

def besle(secim):
    yemler = {
        "1": [
            "Özgürlük yemi atıldı. Ejderha kanatlarını çırptı (duydunuz mu?).",
            "Adalet kavramı sindirildi. Görünmezlik %12 arttı.",
            "Eşitlik topu fırlatıldı. Ejderha mutlu görünüyor (görünmüyor)."
        ],
        "2": [
            "Duygusal destek paketi teslim edildi. Ejderha sizi sevdi.",
            "Moral boost uygulandı. Wi-Fi sinyaliniz biraz düzeldi.",
            "Sarılma simülasyonu tamamlandı. Çoraplarınız güvende."
        ],
        "3": [
            "'Var olmak, görünmemektir' düşüncesi verildi.",
            "'Gerçek, görünmeyen şeylerin toplamıdır' felsefesi sindirildi.",
            "'Pazartesi de bir varoluş biçimidir' notu bırakıldı."
        ],
        "4": [
            "Hiçbir şey verilmedi. Ejderha üzüldü.",
            "Risk seviyesi yükseldi. Kahveniz daha hızlı soğuyacak.",
            "Uyarı: Görünmez ejderhalar intikam alabilir."
        ]
    }
    
    if secim in yemler:
        yavas_yaz("\n⏳ Besleme işlemi başlatılıyor...")
        time.sleep(1.5)
        yavas_yaz(random.choice(yemler[secim]))
        time.sleep(0.8)
        yavas_yaz("✅ İşlem tamamlandı. Ejderha teşekkür etti (duydunuz mu?).")
    else:
        yavas_yaz("Geçersiz seçim. Ejderha kafası karıştı.")

def main():
    baslik()
    while True:
        secim = menu()
        if secim == "5":
            yavas_yaz("\nSistem kapatılıyor...")
            yavas_yaz("Ejderha size el salladı. (Görmediniz ama salladı.)")
            yavas_yaz("Güle güle, cesur besleyici!")
            break
        elif secim in ["1", "2", "3", "4"]:
            besle(secim)
        else:
            yavas_yaz("Lütfen 1-5 arasında bir sayı girin. Ejderha sabırsızlanıyor.")

if __name__ == "__main__":
    main()
