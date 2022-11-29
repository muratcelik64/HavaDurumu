#İl Hava durumunu göster...
#Hava durumu API'sini sorgular ve belirli bir şehir için hava durumu verilerini döndürür.
import pandas as pd
import requests
import json
df = pd.read_csv("Orderdata/SehirlerBolgeler.csv")
#df[df.columns[0:2]]  #df[['id', 'sehirad']].head() #df.loc[0,:] #columns #isnull() #dtypes #shape #display(df)
pd.set_option('display.max_rows', None) # df.shape[0]+1)
df.set_index("id", inplace=True)
print(df[df.columns[0:2]])
try:
    plakakod = int(input("İl Plaka Kodu:"))
    sehirad = df["sehirad"].values[plakakod-1]
except ValueError as hata:
    print("Lütfen, sayısal bir değer giriniz... ",hata)

#df.loc[plakakod:plakakod, ['sehirad']]
API_key = "" #https://opensource.com/
             #adresinden alacağınız API KEY yazınız.
watermap_url = "https://api.openweathermap.org/data/2.5/weather?q=" + sehirad + ",tr&APPID=" + API_key
#print(plakakod," -> ", weathermap_url)
response = requests.get(watermap_url)
jsonResponse = json.loads(response.text)
print(response.text)
print("Koordinat: Boylam: " + str(jsonResponse["coord"]["lon"]) +"; "+ "Enlem: " + str(jsonResponse["coord"]["lat"]))
print("Sıcaklık: " + str(round(jsonResponse["main"]["temp"] - 273, 3)) + " °C")
print("Basınç: " + str(jsonResponse["main"]["pressure"]) + " atm")
print("Nem Oranı: " + str(jsonResponse["main"]["humidity"]) + "%")

df.loc[plakakod,:]
