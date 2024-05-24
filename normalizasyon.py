import stanza
# Stanza pipeline'ı başlat
nlp = stanza.Pipeline('tr')

def normalize_et(metin):
    # Metni analiz et
    doc = nlp(metin)
    
    normalize_edilmis_kelimeler = []
    
    # Her cümle için
    for sentence in doc.sentences:
        # Her kelime için
        for word in sentence.words:
            # Kelimenin kökünü al ve listeye ekle
            root = word.lemma
            normalize_edilmis_kelimeler.append(root)
    
    return ' '.join(normalize_edilmis_kelimeler)

metin = "Bu tekniklerle çalışmayı seviyorum."
temizlenmis_metin = normalize_et(metin)
print(temizlenmis_metin)
