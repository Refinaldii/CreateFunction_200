# Masukan Nilai Suhu dan juga Satuannya
value = float(input("Masukan nilai Suhu: "))
unit = input("Masukan Jenis Suhunya ('C' untuk Celsius, 'F' untuk Fahrenheit): ")

# Konversi suhu tergantung satuannya
if unit.upper() == 'C':
    # Konversi Celsius ke Fahrenheit
    converted_value = (value * 9/5) + 32
    print(f"{value}°C is {converted_value}°F")
elif unit.upper() == 'F':
    # Konversi Fahrenheit ke Celsius
    converted_value = (value - 32) * 5/9
    print(f"{value}°F is {converted_value}°C")
else:
    print("Satuanya tidak valid 'C' untuk Celsius atau 'F' Untuk Fahrenheit.")