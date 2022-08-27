daftar_buku = ['Seven Habits','How to Influence People','Fist Things First', '4dx' ]
print('Tampilkan variabel daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda-beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits','How to Influence People','Fist Things First', '4dx']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika kelas adalah buku baru 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])