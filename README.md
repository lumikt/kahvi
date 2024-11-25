# kahvi
Ohjelmistotuotannon miniprojekti 2024 ryhmälle Kahvittelijat.

![GHA workflow badge](https://github.com/lumikt/kahvi/workflows/CI/badge.svg)

[Backlog](https://docs.google.com/spreadsheets/d/1QnEryqcotTWenMVUscbnGRMMuB6Qqb7guWqPP29eEs0/edit?gid=0#gid=0)

# sovelluksen käynnistysohjeet

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon.

Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
```
DATABASE_URL=postgresql:///uusidb
SECRET_KEY=salainen-avain
```
(salaisen avaimen voit luoda Pythonilla esim. alla olevalla tavalla, joka tulostaa 16 merkkisen salaisen avaimen):
```
$ python3
>>> import secrets
>>> secrets.token_hex(16)
```
Seuraavaksi asenna sovelluksen riippuvuudet ja siirry virtuaaliympäristöön komennoilla:
```
$ poetry install
$ poetry shell
```
Käynnistä sovellus komennolla 
```
$ python3 src/index.py
```

