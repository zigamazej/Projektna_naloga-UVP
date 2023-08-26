import re

def poisci_bloke(besedilo):
    bloki = []
    vzorec_bloka = re.compile(
        r'<tr class="player-row">'  r".*?" r"</div>\s+</td>\s+</tr>",
        flags=re.DOTALL,
    )
    
    for najdba in vzorec_bloka.finditer(besedilo):
        bloki.append(besedilo[najdba.start() : najdba.end()])
    
    return bloki

def izlusci_podatke(blok):
    nogometas = {}

    # izluscimo ime in id nogometaša
    vzorec_ime_in_id_nogometasa = re.compile(r'<a href="/player/(?P<id_nogometasa>\d+)/(?P<ime>.+)">', flags=re.DOTALL,)
    najdba = vzorec_ime_in_id_nogometasa.search(blok)
    nogometas["id_nogometasa"] = int(najdba["id_nogometasa"])
    nogometas["ime"] = najdba["ime"]

    # izluscimo klub in id kluba za katerega igra, na žalost se jih da dobiti le iz slike, zato zgleda tako grdo (podobno bo pri reprezentanci)
    vzorec_klub_in_id_kluba = re.compile(
        r'<img class="team-img lazy" data-lazy-error="/static/img/lazy-ph/club.png" data-lazy-placeholder="/static/img/lazy-ph/club.png"data-lazy-src="https://cdn.fifacm.com/content/media/imgs/fifa23/teams/52/l(?P<id_kluba>\d+).png?v=10" data-toggle="tooltip" title="(?P<klub>.+)" />', 
        flags=re.DOTALL,
        )
    najdba = vzorec_klub_in_id_kluba.search(blok)
    nogometas["id_kluba"] = int(najdba["id_kluba"])
    nogometas["klub"] = najdba["klub"]

    # izluscimo reprezentanco in id reprezentance
    vzorec_reprezentanca_in_id_reprezentance = re.compile(
        r'<img class="team-img lazy" data-lazy-error="/static/img/lazy-ph/club.png" data-lazy-placeholder="/static/img/lazy-ph/club.png" data-lazy-src="https://cdn.fifacm.com/content/media/imgs/fifa23/nations/(?P<id_reprezentance>\d+).png?v=10" data-toggle="tooltip" title="(?P<reprezentanca>.+)" />', 
        flags=re.DOTALL,
    )
    najdba = vzorec_reprezentanca_in_id_reprezentance.search(blok)
    nogometas["id_reprezentance"] = int(najdba["id_reprezentance"])
    nogometas["reprezentanca"] = najdba["reprezentanca"]

    # izluščimo pozicijo v enajsterici, ki jo ima
    vzorec_pozicija = re.compile(r'<div class="player-position-cln" > (?P<pozicija>.+) <span class="px-1">', flags=re.DOTALL,)
    najdba = vzorec_pozicija.search(blok)
    nogometas["pozicija"] = najdba["pozicija"]

    # izluščimo letnici prihoda v klub in konca trenutne pogodbe s tem klubom
    vzorec_trajanje = re.compile(r'<i class="fad fa-file-signature"></i> (?P<prihod_v_klub>\d+) - (?P<konec_pogodbe>\d+)</span>')
    najdba = vzorec_trajanje.search(blok)
    nogometas["prihod_v_klub"] = int(najdba["prihod_v_klub"])
    nogometas["konec_pogodbe"] = int(najdba["konec_pogodbe"])

    # izluscimo rating na igri fifa23
    vzorec_rating = re.compile(r'<div class="player-overall rating-search cm23 fifa-green-b "> (?P<rating>\d+) </div>')
    najdba = vzorec_rating.search(blok)
    nogometas["rating"] = int(najdba["rating"])

    # izluscimo potencialni rating
    vzorec_potencial = re.compile(r'<div class="player-potential rating-search cm23 fifa-green-b "> (?P<potencial>\d+) </div>')
    najdba = vzorec_potencial.search(blok)
    nogometas["potencial"] = int(najdba["potencial"])

    # izluscimo starost
    vzorec_starost = re.compile(r'<div class="player-age pt-3"> (?P<starost>\d+) </div>')
    najdba = vzorec_starost.search(blok)
    nogometas["starost"] = int(najdba["starost"])

    # izluscimo vrednost na trgu in tedensko plačo
    vzorec_vrednost_in_placa = re.compile(r'<div class="player-value-wage pt-2"> <div> €(?P<vrednost>.+)M</div> <div>€(?P<placa>.+)K</div>', flags=re.DOTALL,)
    najdba = vzorec_vrednost_in_placa.search(blok)
    nogometas["vrednost"] = int(najdba["vrednost"])
    nogometas["placa"] = int(najdba["placa"])

    # izluščimo višino
    vzorec_visina = re.compile(r'<div class="player-height"> (?P<visina>.+)cm | (?P<ameriska_visina>.+) </div>', flags=re.DOTALL,)
    najdba = vzorec_visina.search(blok)
    nogometas["visina"] = int(najdba["visina"])

    # izluščimo težo
    vzorec_teza = re.compile(r'<div class="player-weight pl-1"> (?P<modeli>.+) ((?P<teza>\d+)kg | (?P<ameriska_teza>\d+)lbs) </div>', flags=re.DOTALL,)
    najdba = vzorec_teza.search(blok)
    nogometas["teza"] = int(najdba["teza"])

    return nogometas

def izlusci_bloke(bloki):
    podatki_nogometasev = []
    for blok in bloki:
        podatki_nogometasev.append(izlusci_podatke(blok))
    return podatki_nogometasev
    

