def kucuk_harfe_donustur(metin):
    # Metindeki tüm harfleri küçük harfe dönüştür
    return metin.lower()

metin = "Bu Bir Test Mesajıdır."
temizlenmis_metin = kucuk_harfe_donustur(metin)
print(temizlenmis_metin)
