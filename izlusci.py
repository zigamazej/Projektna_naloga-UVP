import re

def poisci_bloke(besedilo):
    bloki = []
    vzorec_bloka = re.compile(
        r'<tr ><th scope="row" '  r".*?" r"</td></tr>",
        flags=re.DOTALL,
    )
    
    for najdba in vzorec_bloka.finditer(besedilo):
        bloki.append(besedilo[najdba.start() : najdba.end()])
    
    return bloki

def izlusci_podatke(blok):
    igralec = {}
    
    #izluscimo ime in oznako
    vzorec_ime_in_oznaka = re.compile(r'<a href="/players/(?P<oznaka>.+?).html">(?P<ime>.+?)</a>', flags=re.DOTALL,)
    najdba = vzorec_ime_in_oznaka.search(blok)
    igralec["ime"] = najdba["ime"]

    #izluscimo podatke o zacetku in koncu kariere
    vzorec_kariera = re.compile(
        r'<td class="right " data-stat="year_min" >(?P<zacetek_kariere>\d+)</td><td class="right " data-stat="year_max" >(?P<konec_kariere>\d+)</td>'
        )
    najdba = vzorec_kariera.search(blok)
    igralec["zacetek_kariere"] = int(najdba["zacetek_kariere"])
    igralec["konec_kariere/sedanjost"] = int(najdba["konec_kariere"])

    igralec["dolzina_kariere"] = igralec["konec_kariere/sedanjost"] - igralec["zacetek_kariere"] #tam kjer je 0, je igral manj kot eno leto, to so razne 10 dnevne pogodbe in podobno

    #izluscimo pozicijo na igriscu, ki je ponavadi igra
    vzorec_pozicija = re.compile(r'<td class="center " data-stat="pos" >(?P<pozicija>.+?)</td>', flags=re.DOTALL,)
    najdba = vzorec_pozicija.search(blok)
    igralec["pozicija"] = najdba["pozicija"][0]  #nekateri igralci lahko igrajo 2 poziciji, vzamemo le prvo, ki je preferirana

    #izluscimo visino
    vzorec_visina = re.compile(r'<td class="right " data-stat="height" csk="(?P<csk>.+?)" >(?P<feet>\d+)-(?P<inches>\d+)</td>')
    najdba = vzorec_visina.search(blok)
    igralec["visina"] = round(30.48 * int(najdba["feet"]) + 2.54 * int(najdba["inches"]))

    #izluscimo tezo
    vzorec_teza = re.compile(r'<td class="right " data-stat="weight" >(?P<teza>\d+)</td>')
    najdba = vzorec_teza.search(blok)
    if najdba:
        igralec["teza"] = round(0.454 * int(najdba["teza"]))
    else:
        igralec["teza"] = None

    #izluscimo leto rojstva
    vzorec_datum_rojstva = re.compile(r'<td class="left " data-stat="birth_date" csk="(?P<datum_rojstva>\d+)" >')
    najdba = vzorec_datum_rojstva.search(blok)
    if najdba:
        igralec["leto_rojstva"] = int(najdba["datum_rojstva"][0:4])
    else:    
        igralec["leto_rojstva"] = None

    #izluscimo ali je igralec v Hall of fame
    if "*" in blok:
        igralec["v_hall_of_fame"] = "da"
    else:
        igralec["v_hall_of_fame"] = "ne"

    #izluscimo ali je igralec se aktiven
    if "<strong>" in blok:
        igralec["trenutno_v_ligi"] = "da"
    else:
        igralec["trenutno_v_ligi"] = "ne"





    return igralec

def izlusci_bloke(bloki):
    podatki_igralcev = []
    for blok in bloki:
        podatki_igralcev.append(izlusci_podatke(blok))
    return podatki_igralcev
    
#with open("stran-a.html", encoding="UTF-8") as f:
#    html = f.read()
#    print(izlusci_bloke(poisci_bloke(html)))
