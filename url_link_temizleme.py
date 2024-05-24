import re

def temizle_url(metin):
    # http ile başlayan URL'leri bul ve çıkar
    return re.sub(r'http\S+', '', metin)

metin = "Bu makaleyi okumanız için link: https://ornek.com"
temizlenmis_metin = temizle_url(metin)
print(temizlenmis_metin)
