def temizle_sayilar(metin):
    # Metindeki tüm rakamları çıkar
    return re.sub(r'\d+', '', metin)

metin = "Toplamda 50 adet ürün var."
temizlenmis_metin = temizle_sayilar(metin)
print(temizlenmis_metin)
