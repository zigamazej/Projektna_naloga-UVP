import requests

st_strani = 50
for i in range(1, st_strani + 1):
    url = f"https://www.fifacm.com/players?page={i}&player_rating=75-99"
    odziv = requests.get(url)
    if odziv.status_code == 200:
        print(url)
        with open(f"stran-{stran}.html", "w") as f:
            f.write(odziv.text)
    else:
        print("Prišlo je do napake")


    