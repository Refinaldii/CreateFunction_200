# Masukan Nilai Suhu dan juga Satuannya
value = float(input("Masukan nilai Suhu: "))
# Meminta pengguna untuk memasukkan suhu sebagai input, 
# Mengubah input tersebut menjadi tipe data float (bilangan desimal), 
# lalu menyimpannya dalam variabel value untuk digunakan lebih lanjut.

unit = input("Masukan Jenis Suhunya ('C' untuk Celsius, 'F' untuk Fahrenheit): ")
# Meminta pengguna untuk memasukkan jenis satuan suhu (baik 'C' untuk Celsius atau 'F' untuk Fahrenheit) sebagai input,
# kemudian menyimpannya dalam variabel unit sebagai string untuk digunakan dalam kondisi atau perhitungan selanjutnya.


# Konversi suhu tergantung satuannya
if unit.upper() == 'C': #mengecek apakah nilai unit (dalam huruf kapital) adalah 'C'
    # Konversi Celsius ke Fahrenheit
    converted_value = (value * 9/5) + 32 #rumus untuk mengonversi suhu Celcius
    print(f"{value}°C is {converted_value}°F")
elif unit.upper() == 'F': #mengecek apakah nilai unit (dalam huruf kapital) adalah 'F'
    # Konversi Fahrenheit ke Celsius
    converted_value = (value - 32) * 5/9  #rumus untuk mengonversi suhu dari Fahrenheit
    print(f"{value}°F is {converted_value}°C")
else:
    #print hasil jika satuannya tidak valid selain C atau F 
    print("Satuanya tidak valid 'C' untuk Celcius atau 'F' Untuk Fahrenheit.")