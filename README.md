1. Ajanvarausjärjestelma - Python B&B

Topias Pöllänen 597348
Tieto- ja Palvelujohtaminen, Biz

2. Esittely

Kyseinen ohjelma on tehty Ohjelmoinnin peruskurssi Y2:lla henkilökohtaisena projektina. Ohjelma on varausjärjestelmä pienelle hotellille. Hotelliin voi lisätä asiakkaita ja asiakkaille voi tehdä huone- ja palveluvarauksia. Ohjelman kehittäminen on tapahtunut GitLab-ympäristössä ja repositoryyn on lisätty niin ohjelmakoodia kuin erilaisia projektisuunnitelmia ja dokumentteja.

3. Tiedosto- ja kansiorakenne

Repositoryssa on yksi kansio nimeltään docs. Tähän kansioon on tallennettu kaikki dokumentit ja ei-ohjelmaan liittyvät asiat. Ohjelman suorittamisen kannalta oleelliset tiedoston ovat kaikki master-haarassa ja nimetty luokkiensa mukaan tarkoitustaan kuvaavalla tavalla.

Kaikki tiedostot paitsi gui.py sisältävät täysin omaa koodiani. gui.py tiedostossa merkittävä osa koodista on saatu Qt-Designerin avulla ja tätä valmista koodia on sitten työstetty eteenpäin. 

4. Asennusohje

Ohjelma tarvitsee toimiakseen PyQt sekä datetime kirjastot. Datetime-kirjasto kuuluu valmiiksi osaan Pythonin versioista, mutta sen asentaminen onnistuu komentorivillä komennolla pip install DateTime.
https://pypi.org/project/DateTime/


5. Käyttöohje

Ohjelma käynnistetään suorittamalla main.py tiedosto esimerkiksi eclipsessä tai komentorivillä.

Ohjelma tarvitsee toimiakseen resources.csv tiedoston, jossa sijaitsee vakiomuotoiset tiedot hotellin luomiseen. Tämän lisäksi ohjelman sisällä luodut asiakkaat ja varaukset tallennetaan customers.csv tiedostoon. Tämän tiedoston avulla tiedot säilyvät ohjelmassa, vaikka se suljettaisiin välillä.







