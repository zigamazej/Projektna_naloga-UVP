import csv

def shrani_igralce(ime_dat, podatki_igralcev):
    with open(ime_dat, "w", encoding="UTF-8", newline='') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                'ime',
                'zacetek_kariere',
                'konec_kariere/sedanjost',
                'dolzina_kariere',
                'pozicija',
                'visina',
                'teza',
                'leto_rojstva',
                'v_hall_of_fame',
                'trenutno_v_ligi',
            ]
        )
        for igralec in podatki_igralcev:
            pisatelj.writerow(
                [
                    igralec['ime'],
                    igralec['zacetek_kariere'],
                    igralec['konec_kariere/sedanjost'],
                    igralec['dolzina_kariere'],
                    igralec['pozicija'],
                    igralec['visina'],
                    igralec['teza'],
                    igralec['leto_rojstva'],
                    igralec['v_hall_of_fame'],
                    igralec['trenutno_v_ligi'],
                ]
            )