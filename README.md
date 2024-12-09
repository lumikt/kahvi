# kahvi
Ohjelmistotuotannon miniprojekti 2024 ryhmälle Kahvittelijat.

![GHA workflow badge](https://github.com/lumikt/kahvi/workflows/CI/badge.svg)  
[![codecov](https://codecov.io/gh/lumikt/kahvi/graph/badge.svg?token=19B6U61LPF)](https://codecov.io/gh/lumikt/kahvi)

[Backlog](https://docs.google.com/spreadsheets/d/1QnEryqcotTWenMVUscbnGRMMuB6Qqb7guWqPP29eEs0/edit?gid=0#gid=0)

# sovelluksen käynnistysohjeet

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon.

Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
```
DATABASE_URL=postgresql:///<psql-käyttäjänimi>
SECRET_KEY=<salainen-avain>
```
(salaisen avaimen voit luoda Pythonilla esim. alla olevalla tavalla, joka tulostaa 16 merkkisen salaisen avaimen):
```
$ python3
>>> import secrets
>>> secrets.token_hex(16)
```
Luo juurihakemistoon tiedosto pyproject.toml ja määritä sen sisältö seuraavanlaiseksi:
```
[tool.poetry]
name = "kahvi"
version = "0.1.0"
description = ""
authors = ["Karri Lumivirta <lumivirta.karri@hotmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10, <3.13"
flask = "^3.1.0"
python-dotenv = "^1.0.1"
psycopg2-binary = "^2.9.10"
flask-sqlalchemy = "^3.1.1"
robotframework-seleniumlibrary = "^6.6.1"
requests = "^2.32.3"
pytest = "^8.3.3"



[tool.poetry.group.dev.dependencies]
pytest = "^8.3.3"
coverage = "^7.6.7"
robotframework = "^7.1.1"
pytest-env = "^1.1.5"
pylint = "^3.3.1"

[tool.pytest.ini_options]
env = ["TEST_ENV=true"]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
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
Definiton of done:  
User story toimii hyväksymiskriteerien mukaisesti ja virheettömästi. Toimintoa on testattu ja se läpäisee testit.

This project is licensed under the terms of the MIT license.

