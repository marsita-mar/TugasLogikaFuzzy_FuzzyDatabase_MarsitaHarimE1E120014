
import mysql.connector as mysql
import pandas as pd
import numpy as np


mydb=mysql.connect(
    host="localhost",
    user="root",
    passwd=""
)


mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)


mydb.database="fuzzy_db"
mycursor.execute("SHOW TABLES")
data=mycursor.fetchall()
print(data)


mycursor.execute("SELECT * FROM tb_emp")
data=mycursor.fetchall()
df=pd.DataFrame(data,columns=['Id','Nama','Usia','Masa Kerja','Gaji'])
print(df)


mycursor.execute("SELECT * FROM tb_kriteria")
data=mycursor.fetchall()
df=pd.DataFrame(data,columns=['Id','Nama Kriteria','Bawah','Tengah','Atas','Kelompok','Keterangan'])
print(df)


mycursor.execute("SELECT usia FROM tb_emp")
kUsia=mycursor.fetchall()
print(kUsia)


mycursor.execute("SELECT bawah FROM tb_kriteria WHERE id=1")
kbawah = mycursor.fetchall()

mycursor.execute("SELECT tengah FROM tb_kriteria WHERE id=1")
ktengah = mycursor.fetchall()

mycursor.execute("SELECT atas FROM tb_kriteria WHERE id=1")
katas = mycursor.fetchall()

print(kbawah, ktengah, katas)

muda = []
for i in kUsia:
    x = i
    a = kbawah[0]
    b = ktengah[0]
    c = katas[0]

    if x < a or x > c:
        miu = 0
    elif a <= x and x <= b:
        miu = (np.subtract(x, a)) / (np.subtract(b, a))
    elif b < x and x <= c:
        miu = (np.subtract(c, x)) / (np.subtract(c, b))

    print("Miu Umur Muda = ", miu)
    muda.append(miu)

print("\n", muda)


mycursor.execute("SELECT bawah FROM tb_kriteria WHERE id=2")
kbawah = mycursor.fetchall()

mycursor.execute("SELECT tengah FROM tb_kriteria WHERE id=2")
ktengah = mycursor.fetchall()

mycursor.execute("SELECT atas FROM tb_kriteria WHERE id=2")
katas = mycursor.fetchall()

print("\n", kbawah, ktengah, katas)
paruhbaya = []

for i in kUsia:
    x = i
    a = kbawah[0]
    b = ktengah[0]
    c = katas[0]

    if x < a or x > c:
        miu = 0
    elif a <= x and x <= b:
        miu = (np.subtract(x, a)) / (np.subtract(b, a))
    elif b < x and x <= c:
        miu = (np.subtract(c, x)) / (np.subtract(c, b))

    print("Miu Umur paruhbaya = ", miu)
    paruhbaya.append(miu)

print("\n", paruhbaya)


mycursor.execute("SELECT bawah FROM tb_kriteria WHERE id=3")
kbawah = mycursor.fetchall()

mycursor.execute("SELECT tengah FROM tb_kriteria WHERE id=3")
ktengah = mycursor.fetchall()

mycursor.execute("SELECT atas FROM tb_kriteria WHERE id=3")
katas = mycursor.fetchall()

print("\n", kbawah, ktengah, katas)
tua = []

for i in kUsia:
    x = i
    a = kbawah[0]
    b = ktengah[0]
    c = katas[0]

    if x < a or x > c:
        miu = 0
    elif a <= x and x <= b:
        miu = (np.subtract(x, a)) / (np.subtract(b, a))
    elif b < x and x <= c:
        miu = (np.subtract(c, x)) / (np.subtract(c, b))

    print("Miu Umur Tua = ", miu)
    tua.append(miu)

print("\n", tua)

#Data Derajat Keanggotaan Usia (All)
mycursor.execute("SELECT nama FROM tb_emp")
data=mycursor.fetchall()
fixU=list(zip(data,muda,paruhbaya,tua))
df=pd.DataFrame(fixU,columns=['Nama Karyawan','Muda','paruhbaya','Tua'])
print(df)

#Derajat Keanggotaan Masa Kerja
mycursor.execute("SELECT masakerja FROM tb_emp")
kMasa=mycursor.fetchall()
print(kMasa)

# Derajat Keanggotaan Masa Kerja (Baru)
# Bawah
mycursor.execute("SELECT bawah FROM tb_kriteria WHERE id=4")
kbawah = mycursor.fetchall()
# Tengah
mycursor.execute("SELECT tengah FROM tb_kriteria WHERE id=4")
ktengah = mycursor.fetchall()
# Atas
mycursor.execute("SELECT atas FROM tb_kriteria WHERE id=4")
katas = mycursor.fetchall()

print(kbawah, ktengah, katas)

baru = []
for j in kMasa:
    x = j
    a = kbawah[0]
    b = ktengah[0]
    c = katas[0]

    if x < a or x > c:
        miu = 0
    elif a <= x and x <= b:
        miu = (np.subtract(x, a)) / (np.subtract(b, a))
    elif b < x and x <= c:
        miu = (np.subtract(c, x)) / (np.subtract(c, b))

    print("Miu Masa Kerja Baru = ", miu)
    baru.append(miu)

print("\n", baru)

# Derajat Keanggotaan Masa Kerja (Lama)
# Bawah
mycursor.execute("SELECT bawah FROM tb_kriteria WHERE id=5")
kbawah = mycursor.fetchall()
# Tengah
mycursor.execute("SELECT tengah FROM tb_kriteria WHERE id=5")
ktengah = mycursor.fetchall()
# Atas
mycursor.execute("SELECT atas FROM tb_kriteria WHERE id=5")
katas = mycursor.fetchall()

print("\n", kbawah, ktengah, katas)
lama = []

for j in kMasa:
    x = j
    a = kbawah[0]
    b = ktengah[0]
    c = katas[0]

    if x < a or x > c:
        miu = 0
    elif a <= x and x <= b:
        miu = (np.subtract(x, a)) / (np.subtract(b, a))
    elif b < x and x <= c:
        miu = (np.subtract(c, x)) / (np.subtract(c, b))

    print("Miu Masa Kerja Lama = ", miu)
    lama.append(miu)

print("\n", lama)

#Data Derajat Keanggotaan Masa Kerja (All)
mycursor.execute("SELECT nama FROM tb_emp")
data=mycursor.fetchall()
fixU=list(zip(data,baru,lama))
df=pd.DataFrame(fixU,columns=['Nama Karyawan','Baru','Lama'])
print(df)

#Derajat Keanggotaan Gaji
mycursor.execute("SELECT gaji FROM tb_emp")
kGaji=mycursor.fetchall()
print(kGaji)

# Derajat Keanggotaan Gaji (Rendah)
# Bawah
mycursor.execute("SELECT bawah FROM tb_kriteria WHERE id=6")
kbawah = mycursor.fetchall()
# Tengah
mycursor.execute("SELECT tengah FROM tb_kriteria WHERE id=6")
ktengah = mycursor.fetchall()
# Atas
mycursor.execute("SELECT atas FROM tb_kriteria WHERE id=6")
katas = mycursor.fetchall()

print(kbawah, ktengah, katas)

rendah = []
for k in kGaji:
    x = k
    a = kbawah[0]
    b = ktengah[0]
    c = katas[0]

    if x < a or x > c:
        miu = 0
    elif a <= x and x <= b:
        miu = (np.subtract(x, a)) / (np.subtract(b, a))
    elif b < x and x <= c:
        miu = (np.subtract(c, x)) / (np.subtract(c, b))

    print("Miu Gaji Rendah = ", miu)
    rendah.append(miu)

print("\n", rendah)

# Derajat Keanggotaan Gaji (Sedang)
# Bawah
mycursor.execute("SELECT bawah FROM tb_kriteria WHERE id=7")
kbawah = mycursor.fetchall()
# Tengah
mycursor.execute("SELECT tengah FROM tb_kriteria WHERE id=7")
ktengah = mycursor.fetchall()
# Atas
mycursor.execute("SELECT atas FROM tb_kriteria WHERE id=7")
katas = mycursor.fetchall()

print("\n", kbawah, ktengah, katas)
sedang = []

for k in kGaji:
    x = k
    a = kbawah[0]
    b = ktengah[0]
    c = katas[0]

    if x < a or x > c:
        miu = 0
    elif a <= x and x <= b:
        miu = (np.subtract(x, a)) / (np.subtract(b, a))
    elif b < x and x <= c:
        miu = (np.subtract(c, x)) / (np.subtract(c, b))

    print("Miu Gaji Sedang = ", miu)
    sedang.append(miu)

print("\n", sedang)

# Derajat Keanggotaan Gaji (Tinggi)
# Bawah
mycursor.execute("SELECT bawah FROM tb_kriteria WHERE id=8")
kbawah = mycursor.fetchall()
# Tengah
mycursor.execute("SELECT tengah FROM tb_kriteria WHERE id=8")
ktengah = mycursor.fetchall()
# Atas
mycursor.execute("SELECT atas FROM tb_kriteria WHERE id=8")
katas = mycursor.fetchall()

print("\n", kbawah, ktengah, katas)
tinggi = []

for k in kGaji:
    x = k
    a = kbawah[0]
    b = ktengah[0]
    c = katas[0]

    if x < a or x > c:
        miu = 0
    elif a <= x and x <= b:
        miu = (np.subtract(x, a)) / (np.subtract(b, a))
    elif b < x and x <= c:
        miu = (np.subtract(c, x)) / (np.subtract(c, b))

    print("Miu Gaji Tinggi = ", miu)
    tinggi.append(miu)

print("\n", tinggi)

#Data Derajat Keanggotaan Gaji (All)
mycursor.execute("SELECT nama FROM tb_emp")
data=mycursor.fetchall()
fixU=list(zip(data,rendah,sedang,tinggi))
df=pd.DataFrame(fixU,columns=['Nama Karyawan','Rendah','Sedang','Tinggi'])
print(df)

#Data Karyawan Dan Derajat Keanggotaan (All)
#Id
mycursor.execute("SELECT id FROM tb_emp")
idK=mycursor.fetchall()
#Nama Karyawan
mycursor.execute("SELECT nama FROM tb_emp")
nama=mycursor.fetchall()
#Usia
mycursor.execute("SELECT usia FROM tb_emp")
usia=mycursor.fetchall()
#Masa Kerja
mycursor.execute("SELECT masakerja FROM tb_emp")
masa=mycursor.fetchall()
#Gaji
mycursor.execute("SELECT gaji FROM tb_emp")
gaji=mycursor.fetchall()

fixU=list(zip(idK,nama,usia,masa,gaji,muda,paruhbaya,tua,baru,lama,rendah,
              sedang,tinggi))
df=pd.DataFrame(fixU,columns=['Id','Nama Karyawan','Usia','Masa Kerja','Gaji',
                              'Muda','paruhbaya','Tua','Baru','Lama',
                              'Rendah','Sedang','Tinggi'])
print(df)

# Operasi
judul = " Operasi Logika Fuzzy".center(75, "*")
print(f"""\r\n{judul}\r\n""")
i = 1
pilih = []
while i == True:
    judul = " Usia ".center(50, "=")
    print(f"""\r\n{judul}
    1. Muda
    2. paruhbaya
    3. Tua
    """)
    mUsia = int(input("Masukkan Pilihan Anda : "))

    judul = " Masa Kerja ".center(50, "=")
    print(f"""\r\n{judul}
    1. Baru
    2. Lama
    """)
    mMasa = int(input("Masukkan Pilihan Anda : "))

    judul = " Gaji ".center(50, "=")
    print(f"""\r\n{judul}
    1. Rendah
    2. Sedang
    3. Tinggi
    """)
    mGaji = int(input("Masukkan Pilihan Anda : "))

    judul = " Operasi ".center(50, "=")
    print(f"""\r\n{judul}
    1. OR - OR
    2. AND - AND
    """)
    mOp = int(input("Masukkan Pilihan Anda : "))

    pilih.append(mUsia)
    pilih.append(mMasa)
    pilih.append(mGaji)
    pilih.append(mOp)
    i += 1

    fix = []
    # Pilihan 1 OR - OR
    if pilih == [1, 1, 1, 1]:
        pil1 = max(max(muda, baru), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 1, 1, 1]:
        pil1 = max(max(paruhbaya, baru), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 1, 1, 1]:
        pil1 = max(max(tua, baru), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 2, 1, 1]:
        pil1 = max(max(muda, lama), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 2, 1, 1]:
        pil1 = max(max(paruhbaya, lama), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 2, 1, 1]:
        pil1 = max(max(tua, lama), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 1, 2, 1]:
        pil1 = max(max(muda, baru), sedang)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 1, 3, 1]:
        pil1 = max(max(muda, baru), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 1, 3, 1]:
        pil1 = max(max(paruhbaya, baru), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 1, 3, 1]:
        pil1 = max(max(tua, baru), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 2, 3, 1]:
        pil1 = max(max(tua, lama), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 2, 3, 1]:
        pil1 = max(max(paruhbaya, lama), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 2, 3, 1]:
        pil1 = max(max(muda, lama), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 2, 2, 1]:
        pil1 = max(max(muda, lama), sedang)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 2, 2, 1]:
        pil1 = max(max(paruhbaya, lama), sedang)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 2, 2, 1]:
        pil1 = max(max(tua, lama), sedang)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    # Pilihan 2 AND - AND
    if pilih == [1, 1, 1, 2]:
        pil1 = min(min(muda, baru), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 1, 1, 2]:
        pil1 = min(min(paruhbaya, baru), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 1, 1, 2]:
        pil1 = min(min(tua, baru), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 2, 1, 2]:
        pil1 = min(min(muda, lama), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 2, 1, 2]:
        pil1 = min(min(paruhbaya, lama), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 2, 1, 2]:
        pil1 = min(min(tua, lama), rendah)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 1, 2, 2]:
        pil1 = min(min(muda, baru), sedang)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 1, 3, 2]:
        pil1 = min(min(muda, baru), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 1, 3, 2]:
        pil1 = min(min(paruhbaya, baru), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 1, 3, 2]:
        pil1 = min(min(tua, baru), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 2, 3, 2]:
        pil1 = min(min(tua, lama), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 2, 3, 2]:
        pil1 = min(min(paruhbaya, lama), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 2, 3, 2]:
        pil1 = min(min(muda, lama), tinggi)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [1, 2, 2, 2]:
        pil1 = min(min(muda, lama), sedang)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [2, 2, 2, 2]:
        pil1 = min(min(paruhbaya, lama), sedang)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)

    elif pilih == [3, 2, 2, 2]:
        pil1 = min(min(tua, lama), sedang)
        for i in pil1:
            if i != 0:
                fix.append(i)
        print(fix)
    else:
        print("")

    # Hasil Akhir Proses Operasi
    # usia
    usia = []
    if pilih[0] == 1:
        usia.append(muda)
    elif pilih[0] == 2:
        usia.append(paruhbaya)
    elif pilih[0] == 3:
        usia.append(tua)
    else:
        usia.append('ERROR')

    masa = []
    if pilih[1] == 1:
        masa.append(baru)
    elif pilih[1] == 2:
        masa.append(lama)
    else:
        masa.append('ERROR')

    gaji = []
    if pilih[2] == 1:
        gaji.append(rendah)
    elif pilih[2] == 2:
        gaji.append(sedang)
    elif pilih[2] == 3:
        gaji.append(tinggi)
    else:
        gaji.append('ERROR')

    operasi = []
    if pilih[3] == 1:
        operasi.append('OR')
    elif pilih[3] == 2:
        operasi.append('AND')
    else:
        operasi.append('ERROR')

    fixU = list(zip(usia, masa, gaji, operasi))
    df = pd.DataFrame(fixU, columns=['Usia', 'Masa Kerja', 'Gaji', 'Operasi'])
    print(df)

#Hasil Akhir (Final)
print("Hasil Operasi Data Karyawan")
df=pd.DataFrame(fix,columns=['Hasil Operasi'])
print(df)