![Scraping Pipeline](https://github.com/AthomsG/renting-in-vienna/actions/workflows/run_pipeline.yml/badge.svg)


# Renting in Vienna

This repo fetches every **5 minutes** (Actually it's less than 30 minutes because github is a bit unreliable with the cron functionality) the latest apartments from [willhaben](https://www.willhaben.at/).
It then filters the listings according to my preferences and stores them in `check_these.csv` - You can change filter settings in the `filter_dataset.py` script.

The 20 latest listings according to my preferences are printed in this README for you conviniece! Press the link to see the listing post.
The table is sorted by publish times in ascending order, with the closest publish time to the current time listed first.

## Recent Listings

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                      |
|-------------:|--------------:|-----------:|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       790    |            54 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/charmante-2-zimmer-dachgeschosswohnung-mit-zwei-terrassen-2069008596/)                             |
|       790    |            42 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/erstklassige-2-zimmerwohnung-in-der-khekgasse-|-ruhige-lage-|-erstbezug-998568375/)                    |
|       799.1  |            52 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/##-ubahn-nähe---schön-&-charmant---2-zimmer-##-989242957/)                                             |
|       699    |            47 |          2 | 06. Mariahilf   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/1060-wien-hornbostelgasse-2-zimmer-küche-duschbad-ruhelage-1.-stock-ohne-lift-1575532071/)           |
|       739.45 |            38 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/fully-furnished.-hell-und-ruhig---eine-perfekte-kleine-wohnung-voll-möbliert-1001661999/)              |
|       743.97 |            52 |          2 | 13. Hietzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/2-zimmer-wohnung-im-grünen:-erstbezug-nach-sanierung-1968875370/)                                     |
|       733.77 |            42 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-döbling/gemütliche-singlewohnung-im-19.-bezirk-1191172900/)                                                    |
|       705.19 |            41 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-döbling/schöne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                     |
|       790    |            56 |          3 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/erstbezug-in-heller-sanierter-altbauwohnung-782617572/)                                              |
|       749    |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---helle-gepfegte-neubauwohnung-im-4ten-liftstock---sofortbezug-1857182406/) |
|       760    |            55 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zimmerwohnung*-privat-1366897509/)                                                                |
|       650    |            36 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/helle-2-zimmer-mietwohnung-mit-loggia-nähe-u1-kagraner-platz-2044095270/)                           |
|       478.7  |            45 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe-1900649810/)                                                            |
|       505    |            53 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-döbling/gemeindewohung-direktvergabe-mit-ablöse-1374904983/)                                                   |
|       530    |            50 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-direktvergabe-wohnticket:-31.8.2024!!-1285229637/)                                 |
|       789.9  |            39 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zi.-whg.-mit-terrasse-1490322788/)                                                           |
|       799    |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung-mit-balkon!-1693093114/)                                                   |
|       640    |            58 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeinde-wohnung-1120-wien-mit-vormekschein-bis-01.07.2024-842069402/)                                |
|       770    |            49 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-später-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                       |
|       720    |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genießen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)          |
