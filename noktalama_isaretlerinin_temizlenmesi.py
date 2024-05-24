import string

def temizle_noktalama(metin):
    # Noktalama işaretlerini metinden çıkar
    return metin.translate(str.maketrans('', '', string.punctuation))

metin = "Merhaba! Nasılsınız?"
temizlenmis_metin = temizle_noktalama(metin)
print(temizlenmis_metin)
