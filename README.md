# Asiakirjapohjasovellus-tsoha-

Sovellus Herokussa: https://asiakirjapohjasovellus-tsoha.herokuapp.com/

Sovelluksen tarkoituksena on palvella organisaation työntekijöitä erilaisten asiakirjojen luomisessa. 
Yleensä tietyn organisaation asiakirjanlaadintatyössä toistuvat samanlaiset fraasit ja asiakirjat, joten valmiiden fraasien ja asiakirjapohjien olemassaolo nopeuttaa työntekoa huomattavasti. 
Sovellukseen työntekijä saa tallennettua organisaation asiakirjoihin vaadittavia faaseja (esim. sopimuspykäliä, päätöspykäliä yms.) ja luotua näiden perusteella asiakirjapohjia. 

Toiminnallisuus:

- Sovelluksessa on yksinkertaistettuna kaksi eri toiminnallisuutta: fraasien lisääminen sovellukseen ja asiakirjapohjien luominen näiden fraasien perusteella. 
- Asiakirjapohjia käyttäjä voi luoda ja tallentaa järjestelmään tallennettujen fraasien perustella.
- Asiakirjapohjia tallennettaessa käyttäjä antaa asiakirjalle asiakirjatyypin.

- Käyttäjä voi olla peruskäyttäjä tai ylläpitäjä.
- Peruskäyttäjä voi lisätä ja lukea fraaseja sekä tallentaa, lukea ja muokata asiakirjapohjia.
- Lopullisestta sovelluksessa ylläpitäjä voi lisätä, lukea ja poistaa fraaseja sekä tallentaa, lukea, muokata ja poistaa asiakirjapohjia (tämä on vielä toteuttamatta).

- Asiakirjapohjat käyttäjä muodostaa lukemalla fraaseja tietokannasta. Fraasit lisätään muokattavaan asiakirjapohjaan lisäysjärjestyksessä.

Tekninen toteutus:

- Tietokannassa on taulut: users, phrases, documents ja phrases_in_documents.
- Users-taulusta löytyvät käyttäjätunnukset, salasanat ja tuleva tieto ylläpitäjäoikeuksista.
- Phrases-taulusta löytyvät yksittäiset erilaiset fraasit (esim. "Kauppahinta maksetaan saajan pankkitilille välittömästi kauppakirjan allekirjoittamisen jälkeen." yms.).
- Documents-taulusta löytyvät tallennetut asiakirjapohjat.
- Phrases_in_documents-taulu on phrases- ja documents-taulujen join-taulu.

Sovelluksen tilanne 4.10.2020:

- Sovellus on vielä keskeneräinen. Sovelluksessa on tässä vaiheessa kirjautumismahdollisuus, fraasien lisääminen ja asiakirjapohjien lisääminen/muokkaaminen. 
- Käytettävyyttä ja koodia tulee vielä parantaa. 
- Ulkoasua ei ole vielä kehitetty juuri ollenkaan.
- Käyttäjiä on vain yhtä tyyppiä, jolla on kaikki oikeudet. Pääkäyttäjän oikeudet poisto-oikeuksineen on lisättävä ohjelmaan.
- Sovellukseen tulee mahdollisesti vielä lisäominaisuuksia, joita olen listannut alla.

Sovellukseen mahdollisesti lisättäviä toiminnallisuuksia:

- Fraaseja lisättäessä käyttäjä antaa fraasille fraasityypin.
- Käyttäjän valitsema fraasityyppi määrittelee kappaleen asiakirjapohjassa. 
  Esim. jos kiinteistön kauppakirjaan halutaan ensimmäiseksi kappaleeksi kauppahinta, valitsee käyttäjä fraasityypiksi kauppahinnan. 
  Kauppahinta viittaa tiettyihin fraaseihin ja käyttäjä valitsee haluamansa fraasin lisättäväksi muokattavaan asiakirjapohjaan. 
  Tällöin ohjelma lisää asiakirjapohjaan kappaleen 1. Kauppahinta ja alle fraasin 1.1, joka on haluttu fraasi.
- Asiakirjapohjalle annetaan asiakirjatyyppi, joka määrittää asiakirjapohjan otsikon asiakirjapohjan nimen asemesta.
- Tietokannassa on siis lisäksi taulut: phrase_types, document_types ja tarvittavat join-taulut.
- Phrase_types-taulusta löytyvät erilaiset fraasityypit (esim. Kauppahinta, Rasitukset, Muut ehdot yms.).
- Document_types-taulusta löytyvät erilaiset asisakirjatyypit (esim. Kiinteistön kauppakirja, Asunto-osakkeiden kauppakirja, Viranhaltijapäätös yms.).

Tietokannassa on 4.10.2020 taulut:

CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE phrases (id SERIAL PRIMARY KEY, phrase TEXT);
CREATE TABLE documents (id SERIAL PRIMARY KEY, docuname TEXT);
CREATE TABLE phrases_in_documents (phrase_id INTEGER REFERENCES phrases, document_id INTEGER REFERENCES documents, PRIMARY KEY (phrase_id, document_id));



