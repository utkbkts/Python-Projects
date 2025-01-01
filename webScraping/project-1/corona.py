import requests
from bs4 import BeautifulSoup

# URL'yi al
response = requests.get("https://covid19.saglik.gov.tr/")

# HTTP durum kodunu kontrol et
if response.status_code == 200:
    print("The page was successfully loaded.")
else:
    print(f"An error occurred. Status code: {response.status_code}")
    exit()

# HTML içeriği BeautifulSoup ile işle
soup = BeautifulSoup(response.content, "html.parser")

# Doğru class adını hedef alın
data = soup.find_all(class_="covid_haftalik_veriler_list")  # Doğru class adı burada olmalı.

say = 1
if data:
    user_input = input("Should we continue and print all data? (y/n): ")  # Kullanıcıdan onay al

    if user_input.lower() == "n":
        print("Program ended.")  # Kullanıcı 'n' girerse program sonlanır
    elif user_input.lower() == "y":
        for item in data:
            print(say, item.get_text(strip=True))  # Metni yazdır
            say += 1  # Sayaç artır
        print("All data printed.")  # Veriler tamamlandığında mesaj verilir
else:
    print("No data found with the specified class.")
