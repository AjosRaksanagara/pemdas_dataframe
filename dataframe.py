import pandas as pd

data = pd.read_csv('data_sampah/data_sampah.csv', delimiter=',', encoding='utf-8')

# 1. Dengan menggunakan pustaka pandas di Python, buatlah sebuah DataFrame dari data jumlah produksi sampah berdasarkan Kabupaten/Kota di Jawa Barat. Pastikan kolom-kolomnya menyertakan nama Kabupaten/Kota, jumlah produksi sampah (dalam ton), dan tahun pencatatan
print(data.head())

# 2. Dari DataFrame yang telah dibuat, hitunglah total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun tertentu. Tampilkan hasilnya.
tahun = 2015 
total_sampah = 0

for index, row in data.iterrows():
    if row['tahun'] == tahun:
        total_sampah += row['jumlah_produksi_sampah']

print(f"Total produksi sampah di tahun {tahun}: {total_sampah} ton")

total_sampah_df = pd.DataFrame(
    [{'tahun': tahun, 'total_produksi_sampah': total_sampah}]
)
total_sampah_df.to_csv('total_sampah_tahun.csv', index=False, encoding='utf-8')
total_sampah_df.to_excel('total_sampah_tahun.xlsx', index=False, engine='openpyxl')

# 3. jumlah data pertahun
data_pertahun = {}
for index, row in data.iterrows():
    tahun = row['tahun']
    jumlah_sampah = row['jumlah_produksi_sampah']
    if tahun in data_pertahun:
        data_pertahun[tahun] += jumlah_sampah
    else:
        data_pertahun[tahun] = jumlah_sampah

data_pertahun_df = pd.DataFrame(list(data_pertahun.items()), columns=['tahun', 'jumlah_produksi_sampah'])
print(data_pertahun_df)

data_pertahun_df.to_csv('data_pertahun.csv', index=False, encoding='utf-8')
data_pertahun_df.to_excel('data_pertahun.xlsx', index=False, engine='openpyxl')


# 4. Jumlahkan data per Kota/Kabupaten per tahun
kota_pertahun = {}
for index, row in data.iterrows():
    kota = row['nama_kabupaten_kota']
    tahun = row['tahun']
    jumlah_sampah = row['jumlah_produksi_sampah']
    key = (kota, tahun)
    if key in kota_pertahun:
        kota_pertahun[key] += jumlah_sampah
    else:
        kota_pertahun[key] = jumlah_sampah

kota_pertahun_df = pd.DataFrame(
    [(key[0], key[1], jumlah) for key, jumlah in kota_pertahun.items()],
    columns=['nama_kabupaten_kota', 'tahun', 'jumlah_produksi_sampah'])
print(kota_pertahun_df)

kota_pertahun_df.to_csv('kota_pertahun.csv', index=False, encoding='utf-8')
kota_pertahun_df.to_excel('kota_pertahun.xlsx', index=False, engine='openpyxl')