pip install zeyrek
import zeyrek
import logging

# Uyarı mesajlarını kapatmak için logging seviyesini ayarla
logging.getLogger('zeyrek').setLevel(logging.ERROR)

# Zeyrek analizörü başlat
analyzer = zeyrek.MorphAnalyzer()

def normalize_et(metin):
    # Metni kelimelere böl ve her kelimeyi kök haline getir
    kelimeler = metin.split()
    normalize_edilmis_kelimeler = []

    for kelime in kelimeler:
        analysis = analyzer.analyze(kelime)
        if analysis:
            # En iyi analiz sonucunun kök kelimesini al
            root = analysis[0][0].lemma
            normalize_edilmis_kelimeler.append(root)
        else:
            normalize_edilmis_kelimeler.append(kelime)

    return ' '.join(normalize_edilmis_kelimeler)

metin = "Bu tekniklerle çalışmayı seviyorum."
temizlenmis_metin = normalize_et(metin)
print(temizlenmis_metin)
