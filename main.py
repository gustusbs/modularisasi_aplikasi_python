"""
Aplikasi berita terkini
MODULARISASI DENGAN FUNCTION
"""
from beritaterkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('Aplikasi Berita Terkini')
    result = ekstraksi_data()
    tampilkan_data(result)