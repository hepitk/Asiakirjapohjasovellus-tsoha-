# Asiakirjapohjasovellus-tsoha-

Sovelluksen tarkoituksena on palvella organisaation työntekijöitä erilaisten asiakirjojen luomisessa. Yleensä tietyn organisaation asiakirjanlaadintatyössä toistuvat samanlaiset fraasit ja asiakirjat, joten valmiiden fraasien ja asiakirjapohjien olemassaolo nopeuttaa työntekoa huomattavasti. Sovellukseen työntekijä saa tallennettua organisaation asiakirjoihin vaadittavia faaseja (esim. sopimuspykäliä, päätöspykäliä yms.) ja luotua näiden perusteella asiakirjapohjia. Fraasit on jaoteltu fraasityyppien (esim. kauppahinta) ja asiakirjapohjat asiakirjatyyppien (esim. kauppakirja) mukaan.

Toiminallisuus:

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


Tekninen toteutus:

- Tietokannassa on taulut: fraasit, fraasityypit, asiakirjapohjat, asiakirjatyypit ja käyttäjät.
- Fraasit-taulusta löytyvät yksittäiset erilaiset fraasit (esim. "Kauppahinta maksetaan saajan pankkitilille välittömästi kauppakirjan allekirjoittamisen jälkeen." yms.). Fraasit-taulusta löytyy myös viite fraasityypit-tauluun.
- Fraasityypit-taulusta löytyvät erilaiset fraasityypit (esim. Kauppahinta, Rasitukset, Muut ehdot yms.).
- Asiakirjapohjat-taulusta löytyvät tallennetut asiakirjapohjat. Taulusta on viite asiakirjatyyppi-tauluun.
- Asiakirjatyyppi-taulusta löytyvät erilaiset asisakirjatyypit (esim. Kiinteistön kauppakirja, Asunto-osakkeiden kauppakirja, Viranhaltijapäätös yms.).
- Käyttäjät-taulusta löytyvät käyttäjätunnukset, salasanat ja tieto ylläpitäjäoikeuksista.
