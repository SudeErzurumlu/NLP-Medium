def temizle_ozel_karakterler(metin):
    # Metindeki özel karakterleri çıkar
    return re.sub(r'[^\w\s]', '', metin)

metin = "Bu çok güzel bir ürün! @user #mutluluk"
temizlenmis_metin = temizle_ozel_karakterler(metin)
print(temizlenmis_metin)
