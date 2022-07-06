import os
import time 
import random

barDarah1 =   ['■■■■■■■■■■', '■■■■■■■■■□', '■■■■■■■■□□', '■■■■■■■□□□', '■■■■■■□□□□', '■■■■■□□□□□', '■■■■□□□□□□', '■■■□□□□□□□', '■■□□□□□□□□', '■□□□□□□□□□', '□□□□□□□□□□']
barDarah2 =  ['■■■■■■■■■■', '□■■■■■■■■■', '□□■■■■■■■■', '□□□■■■■■■■', '□□□□■■■■■■', '□□□□□■■■■■', '□□□□□□■■■■', '□□□□□□□■■■', '□□□□□□□□■■', '□□□□□□□□□■', '□□□□□□□□□□']

a = 0
b = 0

darah1 = (barDarah1[a])
darah2 = (barDarah2[b])

awakening1 = 0
awakening2 = 0
shield1 = 0
shield2 = 0

#tampilan
pesan = "       Memilih Serangan..."
m = " "
n = " "
aa = "  "
bb = "  "
lanjut = 0

def hapusLayar():
    os.system('cls' if os.name == 'nt' else 'clear')

def kembaliKeMenu():
    global a, b, darah1, darah2, awakening1, awakening2, shield1, shield2
    global pesan, m, n, aa, bb, lanjut

    a = 0
    b = 0

    darah1 = (barDarah1[a])
    darah2 = (barDarah2[b])

    awakening1 = 0
    awakening2 = 0
    shield1 = 0
    shield2 = 0

    #tampilan
    pesan = "       Memilih Serangan..."
    m = " "
    n = " "
    aa = "  "
    bb = "  "
    lanjut = 0
    input("Tekan Enter Untuk Kembali")
    menu()

def menu():
    hapusLayar()

    print("=" * 32)
    print("""
          Suwit Onlen
        Tapi Gak Onlen
""")
    print("=" * 32)
    print("""
[1] Play
[2] Cara Bermain
[3] Keluar
""")

    pilihMenu = int(input("Silahkan Pilih Menu : "))
    if pilihMenu == 1:
        play()
    elif pilihMenu == 2:
        caraBermain()
    elif pilihMenu == 3:
        exit()
    else:
        menu()
    
def tampilanPlay():
    hapusLayar()

    print("=" * 32)
    print(f"""      {n}{n}{n}             {m}{m}{m}
  {aa}  YOU{n}     V     {m}COM  {bb}
      {n}{n}{n}             {m}{m}{m}""")
    print(f"  {darah1}       {darah2}")
    print("=" * 32)
    print("""
1. BATU  2. GUNTING  3. KERTAS
""")
    tampilanPesan()

def tampilanPesan():
    print("-" * 32, "\n")
    print(f"{pesan}", "\n")
    print("-" * 32)

def play():
    global darah1, darah2, a, b, aa, bb, pesan, lanjut, m, n
    global awakening1, awakening2, shield1, shield2

    tampilanPlay()

    serang = int(input("Silahkan Pilih Serangan : "))
    komputer = random.choice([1, 2, 3])

    if a >= 7:
        rage = random.randrange(1, 101)
        if rage <= 50:
            awakening1 = 1
            shield1 = 0
            n = "*"
        elif rage <= 80:
            a -= 2
            aa = "+2"
            darah1 = (barDarah1[a])
            awakening1 = 0
            shield1 = 0
            n = "+"
        elif rage <= 100:
            shield1 = 1
            awakening1 = 0
            n = "#"
    elif a <= 6:
        awakening1 = 0
        shield1 = 0
        n = " "
    
    if b >= 7:
        rage = random.randrange(1, 101)
        if rage <= 50:
            awakening2 = 1
            shield2 = 0
            m = "*"
        elif rage <= 80:
            b -= 2
            bb = "+2"
            darah2 = (barDarah2[b])
            awakening2 = 0
            shield2 = 0
            m = "+"
        elif rage <= 100:
            shield2 = 1
            awakening2 = 0
            m = "#"
    elif b <= 6:
        awakening2 = 0
        shield2 = 0
        m = " "

    if serang == 1:
        lanjut = 1
        pesan = "\t      BATU"
        tampilanPlay()
        time.sleep(1)
        pesan = "\t Lawan Memilih..."
        tampilanPlay()
        time.sleep(2)

        if komputer == 1:
            lanjut = 1
            pesan = "\t     BATU"
            tampilanPlay()
            time.sleep(1)
            pesan = "\t BATU V BATU"
            tampilanPlay()
            time.sleep(2)
            pesan = "\t     SERI"
            tampilanPlay()
            time.sleep(1)
            pesan = "       Memilih Serangan..."
            lanjut = 0
            aa = "  "
            bb = "  "
        elif komputer == 2:
            lanjut = 1
            pesan = "\t    GUNTING"
            tampilanPlay()
            time.sleep(1)
            pesan = "\t BATU V GUNTING"
            tampilanPlay()
            time.sleep(2)
            pesan = "\t  BATU MENANG"
            tampilanPlay()
            time.sleep(1)
            pesan = "       Memilih Serangan..."
            lanjut = 0
            damage2()
        elif komputer == 3:
            lanjut = 1
            pesan = "\t    KERTAS"
            tampilanPlay()
            time.sleep(1)
            pesan = "\t BATU V KERTAS"
            tampilanPlay()
            time.sleep(2)
            pesan = "\t KERTAS MENANG"
            tampilanPlay()
            time.sleep(1)
            pesan = "       Memilih Serangan..."
            lanjut = 0
            damage1()
    elif serang == 2:
        lanjut = 1
        pesan = "\t     GUNTING"
        tampilanPlay()
        time.sleep(1)
        pesan = "\t Lawan Memilih..."
        tampilanPlay()
        time.sleep(2)

        if komputer == 1:
            lanjut = 1
            pesan = "              BATU"
            tampilanPlay()
            time.sleep(1)
            pesan = "         GUNTING V BATU"
            tampilanPlay()
            time.sleep(2)
            pesan = "           BATU MENANG"
            tampilanPlay()
            time.sleep(1)
            pesan = "       Memilih Serangan..."
            lanjut = 0
            damage1()
        elif komputer == 2:
            lanjut = 1
            pesan = "            GUNTING"
            tampilanPlay()
            time.sleep(1)
            pesan = "       GUNTING V GUNTING"
            tampilanPlay()
            time.sleep(2)
            pesan = "             SERI"
            tampilanPlay()
            time.sleep(1)
            pesan = "       Memilih Serangan..."
            lanjut = 0
            aa = "  "
            bb = "  "
        elif komputer == 3:
            lanjut = 1
            pesan = "            KERTAS"
            tampilanPlay()
            time.sleep(1)
            pesan = "       GUNTING V KERTAS"
            tampilanPlay()
            time.sleep(2)
            pesan = "        GUNTING MENANG"
            tampilanPlay()
            time.sleep(1)
            pesan = "       Memilih Serangan..."
            lanjut = 0
            damage2()
    elif serang == 3:
        lanjut = 1
        pesan = "\t     KERTAS"
        tampilanPlay()
        time.sleep(1)
        pesan = "\t Lawan Memilih..."
        tampilanPlay()
        time.sleep(2)

        if komputer == 1:
            lanjut = 1
            pesan = "            BATU"
            tampilanPlay()
            time.sleep(1)
            pesan = "        KERTAS V BATU"
            tampilanPlay()
            time.sleep(2)
            pesan = "        KERTAS MENANG"
            tampilanPlay()
            time.sleep(1)
            pesan = "       Memilih Serangan..."
            lanjut = 0
            damage2()
        elif komputer == 2:
            lanjut = 1
            pesan = "            GUNTING"
            tampilanPlay()
            time.sleep(1)
            pesan = "        KERTAS V GUNTING"
            tampilanPlay()
            time.sleep(2)
            pesan = "         GUNTING MENANG"
            tampilanPlay()
            time.sleep(1)
            pesan = "       Memilih Serangan..."
            lanjut = 0
            damage1()
        elif komputer == 3:
            lanjut = 1
            pesan = "           KERTAS"
            tampilanPlay()
            time.sleep(1)
            pesan = "       KERTAS V KERTAS"
            tampilanPlay()
            time.sleep(2)
            pesan = "             SERI"
            tampilanPlay()
            time.sleep(1)
            pesan = "       Memilih Serangan..."
            lanjut = 0
            aa = "  "
            bb = "  "
    else:
        tampilanPlay()
    
    time.sleep(2)


    if a >= 10:
        pesan = "\t  KAMU KALAH"
        lanjut = 1

    if b >= 10:
        lanjut = 1
        pesan = "\t  KAMU MENANG"
    
    if lanjut == 0:
        play()
    else:
        tampilanPlay()
        kembaliKeMenu()

def damage1():
    global darah1, a, aa, bb
    attack = random.randrange(1, 101)

    if attack <= 50:
        bb = "  "
        if awakening2 == 1:
            if shield1 == 1:
                a += 0
                aa = "-0"
            else:
                a += 2
                aa = "-2"
        else:
            if shield1 == 1:
                a += 0
                aa = "-0"
            else:
                a += 1
                aa = "-1"
    elif attack <= 80:
        bb = "  "
        if awakening2 == 1:
            if shield1 == 1:
                a += 0
                aa = "-0"
            else:
                a += 4
                aa = "-4"
        else:
            if shield1 == 1:
                a += 0
                aa = "-0"
            else:
                a += 2
                aa = "-2"
    elif attack <= 100:
        bb = "  "
        if awakening2 == 1:
            if shield1 == 1:
                a += 0
                aa = "-0"
            else:
                a += 6
                aa = "-6"
        else:
            if shield1 == 1:
                a += 0
                aa = "-0"
            else:
                a += 3
                aa = "-3"
    
    if a > 10:
        a = 10
    
    darah1 = (barDarah1[a])

def damage2():
    global darah2, b, bb, aa
    attack = random.randrange(1, 101)

    if attack <= 50:
        aa = "  "
        if awakening1 == 1:
            if shield2 == 1:
                b += 0
                bb = "-0"
            else:
                b += 2
                bb = "-2"
        else:
            if shield2 == 1:
                b += 0
                bb = "-0"
            else:
                b += 1
                bb = "-1"
    elif attack <= 80:
        aa = "  "
        if awakening1 == 1:
            if shield2 == 1:
                b += 0
                bb = "-0"
            else:
                b += 4
                bb = "-4"
        else:
            if shield2 == 1:
                b += 0
                bb = "-0"
            else:
                b += 2
                bb = "-2"
    elif attack <= 100:
        aa = "  "
        if awakening1 == 1:
            if shield2 == 1:
                b += 0
                bb = "-0"
            else:
                b += 6
                bb = "-6"
        else:
            if shield2 == 1:
                b += 0
                bb = "-0"
            else:
                b += 3
                bb = "-3"
    
    if b > 10:
        b = 10
    
    darah2 = (barDarah2[b])

def caraBermain():
    hapusLayar()

    print("=" * 32)
    print("""
          Cara Bermain
   Suwit Onlen Tapi Gak Onlen
""")
    print("=" * 32)
    print("""
1. Player akan melawan komputer

2. Masing-masing diberikan 10
   darah

3. Player akan memilih antara
   Batu, Gunting, atau Kertas

4. Kemudian komputer memilih
   secara acak

5. Setelah salah satu menang
   (suwit) maka akan di random
   jumlah serangannya (1/2/3)

6. Jika salah satu darah kurang
   dari sama dengan tiga, maka
   akan di random pilihan :

(*)Awakening 50% (2x serangan)
(+)Regen 30% (+2 Darah)
(#)Shield 20% (Kebal Serangan)

7. Permainan selesai, jika ada
   yang kehabisan darah
""")
    print("-" * 32)
    input("Tekan Enter Untuk Kembali")
    menu()

menu()