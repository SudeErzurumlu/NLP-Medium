from nltk.corpus import stopwords
import nltk

# İlk kez NLTK stopwords kullanıyorsanız, aşağıdaki satırı çalıştırmalısınız
# nltk.download('stopwords')

stop_words = set(stopwords.words('turkish'))

def temizle_stopwords(metin):
    # Metni kelimelere böl ve stopwords olmayanları seç
    kelimeler = metin.split()
    temizlenmis_kelimeler = [kelime for kelime in kelimeler if kelime not in stop_words]
    return ' '.join(temizlenmis_kelimeler)

metin = "Bu makale, metin temizleme teknikleri hakkında bilgi verir."
temizlenmis_metin = temizle_stopwords(metin)
print(temizlenmis_metin)
