import izlusci
import preberi
import shrani

seznam = "abcdefghijklmnopqrstuvwyz"

besedila = preberi.preberi(seznam)
podatki_igralcev = []
for besedilo in besedila:
    bloki = izlusci.poisci_bloke(besedilo)
    podatki_igralcev += izlusci.izlusci_bloke(bloki)

shrani.shrani_igralce("igralci.csv", podatki_igralcev)
