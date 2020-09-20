# Asiakirjapohjasovellus-tsoha-

Sovellus Herokussa: https://asiakirjapohjasovellus-tsoha.herokuapp.com/

Sovelluksen tarkoituksena on palvella organisaation työntekijöitä erilaisten asiakirjojen luomisessa. 
Yleensä tietyn organisaation asiakirjanlaadintatyössä toistuvat samanlaiset fraasit ja asiakirjat, joten valmiiden fraasien ja asiakirjapohjien olemassaolo nopeuttaa työntekoa huomattavasti. 
Sovellukseen työntekijä saa tallennettua organisaation asiakirjoihin vaadittavia faaseja (esim. sopimuspykäliä, päätöspykäliä yms.) ja luotua näiden perusteella asiakirjapohjia. 
Fraasit on jaoteltu fraasityyppien (esim. kauppahinta) ja asiakirjapohjat asiakirjatyyppien (esim. kauppakirja) mukaan.

Lopullinen toiminnallisuus:

- Sovelluksessa on yksinkertaistettuna kaksi eri toiminnallisuutta: fraasien lisääminen sovellukseen ja asiakirjapohjien luominen näiden fraasien perusteella. 
- Fraaseja lisättäessä käyttäjä antaa fraasille fraasityypin.
- Asiakirjapohjia käyttäjä voi luoda ja tallentaa järjestelmään tallennettujen fraasien perustella.
- Asiakirjapohjia tallennettaessa käyttäjä antaa asiakirjalle asiakirjatyypin.

- Käyttäjä voi olla peruskäyttäjä tai ylläpitäjä.
- Ylläpitäjä voi lisätä, muokata, poistaa ja lukea fraaseja sekä tallentaa, muokata ja poistaa asiakirjapohjia.
- Peruskäyttäjä voi lisätä ja lukea fraaseja sekä tallentaa ja lukea asiakirjapohjia.

- Asiakirjapohjat käyttäjä muodostaa lukemalla fraaseja tietokannasta. Fraasit lisätään muokattavaan asiakirjapohjaan numeroituna lisäysjärjestyksessä tietyn kappaleen alle.
- Käyttäjän valitsema fraasityyppi määrittelee kappaleen. Esim. jos kiinteistön kauppakirjaan halutaan ensimmäiseksi kappaleeksi kauppahinta, valitsee käyttäjä fraasityypiksi kauppahinnan. Kauppahinta viittaa tiettyihin fraaseihin ja käyttäjä valitsee haluamansa fraasin lisättäväksi muokattavaan asiakirjapohjaan. Tällöin ohjelma lisää asiakirjapohjaan kappaleen 1. Kauppahinta ja alle fraasin 1.1, joka on haluttu fraasi.
- Käyttäjä voi tallentaa lopullisen asiakirjapohjan. Asiakirjapohjalle annetaan asiakirjatyyppi, joka määrittää asiakirjapohjan otsikon.


Lopullinen tekninen toteutus:

- Tietokannassa on taulut: phrases, phrase_types, documents, document_types, users ja tarvittavat join-taulut.
- Phrases-taulusta löytyvät yksittäiset erilaiset fraasit (esim. "Kauppahinta maksetaan saajan pankkitilille välittömästi kauppakirjan allekirjoittamisen jälkeen." yms.).
- Phrase_types-taulusta löytyvät erilaiset fraasityypit (esim. Kauppahinta, Rasitukset, Muut ehdot yms.).
- Documents-taulusta löytyvät tallennetut asiakirjapohjat.
- Document_types-taulusta löytyvät erilaiset asisakirjatyypit (esim. Kiinteistön kauppakirja, Asunto-osakkeiden kauppakirja, Viranhaltijapäätös yms.).
- Users-taulusta löytyvät käyttäjätunnukset, salasanat ja tieto ylläpitäjäoikeuksista.

Sovelluksen tilanne 20.9.2020:

Sovellus on vielä hyvin keskeneräinen. Sovelluksessa on tässä vaiheessa kirjautumismahdollisuus, suppea fraasien lisääminen ja suppea asiakirjapohjien lisääminen/muokkaaminen. Sovelluksessa ei ole vielä join-tauluja, joten yhden fraasin saa lisättyä vain yhteen asiakirjapohjaan. Käytettävyyttä, ulkoasua ja koodia tulee vielä kehittää. Asiakirjatyyppien ja fraasityyppien lisääminen ei vielä onnistu. Käyttäjiä on vain yhtä tyyppiä, jolla on kaikki oikeudet.

Tietokantaan tarvitaan 20.9.2020 taulut:

- users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
- phrases (id SERIAL PRIMARY KEY, phrase TEXT, document_id INTEGER REFERENCES documents);
- documents (id SERIAL PRIMARY KEY, docuname TEXT);

