# Projektna_naloga-UVP
Avtor: Žiga Mazej

Projektno nalogo sem delal na osnovi podatkov s spletne strani https://www.basketball-reference.com, s katere sem pobral bazo podatkov o vseh igralcih košarke, ki so igrali v ligi NBA od njene ustanovitve.
## Navodila za uporabo
Za urejanje podatkov v ustrezno obliko `csv` je koda napisana v datotekah `izlusci.py`, `preberi.py`, `shrani.py` in `glavny.py`. V `preberi.py` se prvih nekaj vrstic začne z `#`. To funkcijo sem uporabil le prvič, za pridobivanje vseh strani s podatki s paketom `requests`. V kolikor bi želel uporabnik na novo naložiti vse te `html` datoteke, ki so shranjene v mapi `podatki`, naj zbriše vse `#` in požene program.
Podatki so urejeni v datoteki `igralci.csv`, analiza pa je narejena z `Jupyter Notebook` v `Analiza.ipynb`. Tam so tudi natančneje razloženi podatki in potek analize ter cilj naloge.
Za prevod celotne analize so potrebni paketi: `pandas`, `matplotlib.pyplot`, `requests`, `re` in `csv`.