import time
from win10toast import ToastNotifier
import requests
from datetime import datetime
#funkcija za pretvaranje u sekunde radi usporedbe
def pretvori(vrijeme):
    ftr = [3600,60,1]
    return sum([a*b for a,b in zip(ftr, map(int,vrijeme.split(':')))])

#funkcija za slanje obavijesti za vrijeme namaza
def obavijesti(vrijeme1, vrijeme2):
    toaster = ToastNotifier()
    toaster.show_toast("NAMAZ REMINDER","Trenutno vrijeme je " + vrijeme1 + ", a vrijeme namaza je " + vrijeme2 )

#API URL
URL = "https://api.vaktija.ba/vaktija/v1/"
#UNOS REDNOG BROJA GRADA Visoko=97, Sarajevo=77
grad= str(input())
#SLANJE GET REQUESTA
podaci=requests.get(URL+grad)
#JSON FORMATIRANJE PREUZETIH PDOATAK
podaci = podaci.json()

while 1:
    now = datetime.now()
    pt = now.strftime("%H:%M:%S")
    for i in range(5):
        if abs(pretvori(pt)-pretvori(podaci['vakat'][i]+":00"))<600:
            obavijesti(pt, podaci['vakat'][i]+":00")
            break
    time.sleep(540)        
    