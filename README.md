# Miniprojekti

![GHA workflow badge](https://github.com/akuraunio/miniprojekti/actions/workflows/ci.yaml/badge.svg)
![codecov](https://codecov.io/gh/akuraunio/miniprojekti/graph/badge.svg?token=URKILIPGIB)](https://codecov.io/gh/akuraunio/miniprojekti)

Ohjelmistuotanto syksy 2025

## Definition of Done
- Acceptance kriteerit täyttyy
- Toiminolle on testit, jotka menevät läpi
- Joku on hyväksynyt pull requestin
- Kaikki tarvittava toiminnan dokumentaatio on kirjoitettu

## Branchit
 - Branchit nimetään taskin mukaan, siten että tulee selväkisi mihin user storyyn branchi liittyy
 - Kun definition of done kriteerity täyttyy muuten kuin branchin osalta, se mergetään main branchiin

## Vaatimusmäärittely
 - Book -tyyppinen viite, joka sisältää: title, author, year, ISBN, publisher
## Backlog
 - https://docs.google.com/spreadsheets/d/1kqmGFZCdFphiSFvcZc1TDuBp6KPJ7YDvSF_VAUqDIxU/edit?usp=sharing

## Kielikysymykset
 - Commitit ja branchit suomeksi
 - Koodi englanniksi
 - Koodikommentit suomeksi

## Asennusohjeet
 - Sovellus tarvitsee PostgreSQL-tietokannan
 - Luo sovelluksen juureen .env tiedosto tyyliin:
   DATABASE_URL=postgresql://xxx
   TEST_ENV=true
   SECRET_KEY=satunnainen_merkkijono
 - Ennen sovelluksen käynnistämistä ensimmäistä kertaa suorita komento          "python src/db_helper.py"
 - Sovellus käynnistetään Poetry-virtuaaliympäristössä antamalla komento        "python src/index.py"
