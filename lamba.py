#digunakan untuk mengimpor modul math, yang menyediakan berbagai fungsi matematika 
# seperti trigonometri, logaritma, dan fungsi eksponensial, serta konstanta seperti pi.
import math 
luas_lingkaran = lambda r: math.pi * r*r

#jari jari untuk lingkaran = 7
jari_jari = 7 

# Memanggil fungsi luas_lingkaran dengan argumen jari_jari, 
# lalu hasil perhitungan (luas lingkaran) disimpan dalam variabel area.
area = luas_lingkaran(jari_jari) 


#perintah untuk mencetak teks dengan interpolasi variabel jari_jari dan area, 
# di mana nilai area dibulatkan hingga dua tempat desimal menggunakan format string f dan format spesifik {:.2f}
print (f"Luas Lingkaran dengan Jari Jari {jari_jari} adalah {area:.2f}")

