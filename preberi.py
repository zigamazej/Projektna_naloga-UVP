#import requests
#
#for crka in "abcdefghijklmnopqrstuvwxyz":
#    url = f"https://www.basketball-reference.com/players/{crka}/"
#    odziv = requests.get(url)
#    if odziv.status_code == 200:
#        print(url)
#        with open(f"stran-{crka}.html", "w", encoding="UTF-8") as f:
#            f.write(odziv.text)
#    else:
#        print(odziv.status_code)
#
#seznam = "abcdefghijklmnopqrstuvwyz"

def preberi(seznam):
    besedila = []
    for crka in seznam:
        with open(f"podatki\stran-{crka}.html", encoding="UTF-8") as dat:
            besedilo = dat.read()
            besedila.append(besedilo)

    return besedila
