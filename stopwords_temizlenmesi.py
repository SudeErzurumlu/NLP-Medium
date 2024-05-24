import re
from nltk.corpus import stopwords
import nltk
# NLTK stopwords listesini indirme
nltk.download('stopwords')

# Türkçe stopwords listesi
stop_words = set(stopwords.words('turkish'))
def temizle_metin(metin):
    # Noktalama işaretlerini ve sayıları kaldır
    metin = re.sub(r'[^\w\s]', '', metin)
    metin = re.sub(r'\d+', '', metin)
    # Küçük harfe dönüştür
    metin = metin.lower()
    # Stopwords'leri temizle
    temizlenmis_kelimeler = [kelime for kelime in metin.split() if kelime not in stop_words]
    # Temizlenmiş metni birleştir
    temizlenmis_metin = ' '.join(temizlenmis_kelimeler)
    return temizlenmis_metin

# Örnek metin
metin = "Bu makale, metin temizleme teknikleri hakkında bilgi verir."

# Metni temizle
temizlenmis_metin = temizle_metin(metin)

# Temizlenmiş metni yazdır
print(temizlenmis_metin)
