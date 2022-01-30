def ekstraksi_data():
    """
    Aplikasi Berita Terkini
    Pertama: Sebaran 11.588 Kasus COVID-19 RI 29 Januari: DKI Tertinggi 5.765, Jabar 2.525
    detikHealth | 2 jam yang lalu
    Kedua: Update Corona RI 29 Januari Tambah 11.588 Kasus Baru, Sembuh 2.590
    detikHealth | 2 jam yang lalu
    Ketiga: Data Lengkap COVID-19 RI 29 Januari: DKI-Jabar-Banten Tertinggi
    detikNews | 2 jam yang lalu
    Keempat: Omicron Melonjak, Menag Keluarkan Panduan Perayaan Imlek
    detikNews | 2 jam yang lalu
    Kelima: Bongkar Dugaan Jebakan Karantina, Ini Ancaman Sandiaga ke Oknum Coreng RI!
    detikNews | 2 jam yang lalu
    :return:
    """
    result = dict()
    result['pertama'] = {'berita': 'Sebaran 11.588 Kasus COVID-19 RI 29 Januari: DKI Tertinggi 5.765, Jabar 2.525',
                         'sumber': 'detikHealth', 'update': '2 jam yang lalu'}
    result['kedua'] = {'berita': 'Update Corona RI 29 Januari Tambah 11.588 Kasus Baru, Sembuh 2.590',
                       'sumber': 'detikHealth', 'update': '2 jam yang lalu'}
    result['ketiga'] = {'berita': 'Data Lengkap COVID-19 RI 29 Januari: DKI-Jabar-Banten Tertinggi',
                        'sumber': 'detikHealth', 'update': '2 jam yang lalu'}
    result['keempat'] = {'berita': 'Omicron Melonjak, Menag Keluarkan Panduan Perayaan Imlek',
                         'sumber': 'detikHealth', 'update': '2 jam yang lalu'}
    result['kelima'] = {'berita': 'Bongkar Dugaan Jebakan Karantina, Ini Ancaman Sandiaga ke Oknum Coreng RI!',
                        'sumber': 'detikHealth', 'update': '2 jam yang lalu'}

    return result


def tampilkan_data(result):
    print('\nBerita terpopuler tanggal 29 Januari')
    print(f"\npertama: {result['pertama']['berita']}, {result['pertama']['sumber']}, {result['pertama']['update']}")
    print(f"kedua: {result['kedua']['berita']}, {result['kedua']['sumber']}, {result['kedua']['update']}")
    print(f"ketiga: {result['ketiga']['berita']}, {result['ketiga']['sumber']}, {result['ketiga']['update']}")
    print(f"keempat: {result['keempat']['berita']}, {result['keempat']['sumber']}, {result['keempat']['update']}")
    print(f"kelima: {result['kelima']['berita']}, {result['kelima']['sumber']}, {result['kelima']['update']}")

#if __name__ == '__main__':
#print('Aplikasi package berita terkini')
#forpackage