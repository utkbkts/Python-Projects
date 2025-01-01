import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.sokmarket.com.tr/dondurma-c-31102")

# URL kontrolü
if url.status_code == 200:
    print("Siteden veri çekilebilir.")
else:
    print("Siteden veri çekilemedi.")

# BeautifulSoup ile HTML içeriğini parse etme
soup = BeautifulSoup(url.content, "html.parser")

# İlgili sınıf adını kullanarak veri çekme
data = soup.find_all("div", {"class": "PLPProductListing_PLPCardParent__GC2qb"})

# Verilerin kontrolü
say = 1
if data:
    user_input = input("Tüm verileri yazdırmak ister misiniz? (y/n): ")

    # Kullanıcı onayı
    if user_input.lower() == 'y':
        for i in data:
            print("*" * 48)  # Ayırıcı
            print("Sıra:", say)

            # Fiyat ve başlık alma
            fiyat_al = i.find("div", {"class": "CPriceBox-module_priceContainer__ZROpc"}).span.get_text(strip=True)
            baslik_al = i.find("div", {"class": "CProductCard-module_infoContainer__F8uxY"}).h2.get_text(strip=True)

            # Fiyat ve başlık yazdırma
            print("Fiyat:", fiyat_al)
            print("Başlık:", baslik_al)

            say += 1
    else:
        print("Program sonlandı.")
else:
    print("Veri bulunamadı.")
print("*" * 48)
