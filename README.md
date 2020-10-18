# Asiakirjapohjasovellus-tsoha-

Sovellus Herokussa: https://asiakirjapohjasovellus-tsoha.herokuapp.com/

Sovelluksen tarkoituksena on palvella organisaation työntekijöitä erilaisten asiakirjojen luomisessa. 
Yleensä tietyn organisaation asiakirjanlaadintatyössä toistuvat samanlaiset fraasit ja asiakirjat, joten valmiiden fraasien ja asiakirjapohjien olemassaolo nopeuttaa työntekoa huomattavasti. 
Sovellukseen työntekijä saa tallennettua organisaation asiakirjoihin vaadittavia faaseja (esim. sopimuspykäliä, päätöspykäliä yms.) ja luotua näiden perusteella asiakirjapohjia. 

Toiminnallisuus:

- Sovelluksessa on kaksi eri toiminnallisuutta: fraasien lisääminen sovellukseen ja asiakirjapohjien luominen ja muokkaaminen näiden fraasien perusteella.
- Käyttäjä voi lisätä ja lukea fraaseja sekä lukea, muokata ja tulostaa asiakirjapohjia.

Ohjeet käyttöön:

1. Käyttäjän on ensimmäiseksi rekisteröitävä käyttäjätunnus.
2. Käyttö aloitetaan luomalla tyhjä asiakirjapohja Luo tyhjä asiakirjapohja -sivulta.
3. Käyttäjä lisää haluamansa fraasit tietokantaan Luo fraasi -sivulta.
4. Asiakirjapohjien muokkaus -sivulta käyttäjä saa lisättyä tarvittavat fraasit haluttuun asiakirjapohjaan valitsemalla linkin: Lisää fraasi asiakirjapohjaan.
5. Asiakirjapohjien muokkaus -sivulta käyttäjä pääsee Näytä / tulosta asiakirjapohja -linkistä muokkaamaansa asiakirjapohjaan, josta asiakirjapohjaa pytyy tarkastelemaan ja sen pystyy tulostamaan.

Tekninen toteutus:

- Tietokannassa on taulut: users, phrases, documents ja phrases_in_documents.
- Users-taulusta löytyvät käyttäjätunnukset ja salasanat.
- Phrases-taulusta löytyvät yksittäiset erilaiset fraasit (esim. "Kauppahinta maksetaan saajan pankkitilille välittömästi kauppakirjan allekirjoittamisen jälkeen." yms.).
- Documents-taulusta löytyvät tallennetut asiakirjapohjat.
- Phrases_in_documents-taulu on phrases- ja documents-taulujen join-taulu.

Sovelluksen tilanne 18.10.2020:

- Sovellus jäi suppeaksi. Monia suunniteltuja toiminnallisuuksia jäi lisäämättä. Kehitystarpeet:

- Käyttäjiä on nyt vain yhtä tyyppiä, jolla on kaikki oikeudet. Pääkäyttäjän oikeudet poisto-oikeuksineen olisi hyvä lisätä ohjelmaan.
- Fraasien lisäys asiakirjoihin tapahtuu nyt fraasien luomisjärjestyksessä. Sovelluksen olisi parempi toimia niin, että fraasit tulisivat asiakirjapohjiin siinä järjestyksessä kuin ne lisäätään kyseiseen asiakirjapohjaan.
- Asiakirjapohja olisi hyvä saada tallennettua sovelluksesta esim. .doc-muodossa, jolloin sitä voisi helposti muokata tekstieditorilla.
- Fraaseja lisättäessä käyttäjä voisi antaa fraasille fraasityypin.
- Käyttäjän valitsema fraasityyppi määrittelisi kappaleen asiakirjapohjassa. 
  Esim. jos kiinteistön kauppakirjaan halutaan ensimmäiseksi kappaleeksi kauppahinta, valitsee käyttäjä fraasityypiksi kauppahinnan. 
  Kauppahinta viittaa tiettyihin fraaseihin ja käyttäjä valitsee haluamansa fraasin lisättäväksi muokattavaan asiakirjapohjaan. 
  Tällöin ohjelma lisää asiakirjapohjaan kappaleen 1. Kauppahinta ja alle fraasin 1.1, joka on haluttu fraasi.
- Asiakirjapohjalle voisi antaa asiakirjatyypin, joka määrittää asiakirjapohjan otsikon asiakirjapohjan nimen asemesta.
- Tietokantapyyntöjä koskeva koodi olisi ollut syytä laittaa erillisiin tiedostoihin kurssin ohjeiden mukaisesti.

Tietokannassa on 18.10.2020 taulut:

CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE phrases (id SERIAL PRIMARY KEY, phrase TEXT);
CREATE TABLE documents (id SERIAL PRIMARY KEY, docuname TEXT);
CREATE TABLE phrases_in_documents (phrase_id INTEGER REFERENCES phrases, document_id INTEGER REFERENCES documents, PRIMARY KEY (phrase_id, document_id));



