import hashlib
import sys

def banner():
    print("-" * 50)
    print(" BASİT HASH HESAPLAYICI - GITHUB PROJEM")
    print("-" * 50)

def hesapla(metin):
    # Metni 'byte' türüne çevirmemiz lazım (encode)
    metin_byte = metin.encode('utf-8')

    # MD5 Hesaplama (Eski ama bilinmeli)
    md5_hash = hashlib.md5(metin_byte).hexdigest()
    
    # SHA-256 Hesaplama (Güncel standart)
    sha256_hash = hashlib.sha256(metin_byte).hexdigest()

    print(f"\n[+] Girilen Metin: {metin}")
    print(f"[+] MD5 Hash    : {md5_hash}")
    print(f"[+] SHA-256 Hash: {sha256_hash}")
    print("-" * 50)

if __name__ == "__main__":
    banner()
    
    # Kullanıcıdan veri alalım
    try:
        kullanici_metni = input("Hashlenecek metni girin: ")
        if kullanici_metni:
            hesapla(kullanici_metni)
        else:
            print("Boş veri girdiniz!")
    except KeyboardInterrupt:
        print("\nÇıkış yapılıyor...")