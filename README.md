![Scraping Pipeline](https://github.com/AthomsG/renting-in-vienna/actions/workflows/run_pipeline.yml/badge.svg)


# Renting in Vienna

This repo fetches every **5 minutes** (Actually it's less than 30 minutes because github is a bit unreliable with the cron functionality) the latest apartments from [willhaben](https://www.willhaben.at/).
It then filters the listings according to my preferences and stores them in `check_these.csv` - You can change filter settings in the `filter_dataset.py` script.

```python
filtered_df = df[(df.State == 'Wien') & 
                 (df.Price < 800) &
                 (df.Price > 400) &
                 (df.Rooms > 1) &
                 (df['Property Type'] == 'Wohnung') &
                 (df['Published Date'] >= one_day_ago)]
```

The 20 latest listings according to my preferences are printed in this README for you conviniece! Press the link to see the listing post.
The table is sorted by publish times in ascending order, with the closest publish time to the current time listed first.

If you want to get notifications in real time for when new apartments pop up, you can join the telegram channel synced to this repo [here](https://t.me/+1HPAYOf5BSsyNTlk).

## Recent Active Listings

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       795.19 |            41 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnung-mit-gro%C3%9Fem-balkon-und-abstellraum-nahe-u1-kagraner-platz---im-neuen-wohnviertel-am-langen-felde-1911782186/)                                                                               | Jan 20, 15:35      |
|       759.32 |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1311001680/)                                                                                                                                     | Jan 20, 15:26      |
|       790    |            55 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/dachgeschoss-balkonwohung-hell-2-zimmer-ohne-lift-4.-stock-1274634123/)                                                                                                                                                | Jan 20, 15:23      |
|       725    |            40 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-895383341/)                                                                                                                                              | Jan 20, 15:12      |
|       680    |            56 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gepflegte-2-zimmer-wohnung-764283474/)                                                                                                                                                                                 | Jan 20, 14:22      |
|       798    |            37 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sehr-sch%C3%B6ne-2-zimmerwohnung---n%C3%A4he-donauinsel-&-handelskai-1066009313/)                                                                                                                                    | Jan 20, 14:15      |
|       479    |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonniger-altbau-in-u1-n%C3%A4he-1050434959/)                                                                                                                                                                           | Jan 20, 13:28      |
|       450    |           140 |          5 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ein-helles-zimmer-mit-direktem-terrassenzugang-in-7-zimmer-studenten-wohngemeinschaft-mit-5-schlafzimmern-22-m%C2%B2-terrasse-f%C3%BCr-studentinnen-wg-geeignet-%281-k%C3%BCche-2-badezimmer-und-2-wcs%29-1746791727/) | Jan 20, 12:58      |
|       640    |            60 |          3 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direkt-vergabe-gemeinde-wohnung-1100-wien-in-einem-guten-anlage-1386479260/)                                                                                                                                           | Jan 20, 12:26      |
|       690    |            37 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---moderne-neubau---singlewohnung---provisionsfrei---ab-1.02.2025-1429821665/)                                                                                                                                | Jan 20, 12:22      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei-in-der-pfalzgasse-29---2-zimmer-wohnung-mit-balkon---erstbezug-in-ruhelage-1609375860/)                                                                                                              | Jan 20, 11:51      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---traumhafter-erstbezug-in-ruhelage---1-monat-mietfrei%21-2-zimmer-apartment-mit-balkon-1705094653/)                                                                                                    | Jan 20, 11:46      |
|       799    |            39 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---1-monat-mietfrei%21-2-zimmer-wohnung-mit-balkon-%7C-traumhafter-erstbezug-in-ruhelage-1283007542/)                                                                                                    | Jan 20, 11:41      |
|       799    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---lichtdurchflutet-und-modern:-2-zimmer-wohnung-mit-balkon--erstbezug-in-ruhelage-786080173/)                                                                                                           | Jan 20, 11:37      |
|       799    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---2-zimmer-aartment-mit-balkon-traumhafter-erstbezug-in-ruhelage-1043504437/)                                                                                                                           | Jan 20, 11:33      |
|       774    |            38 |          2 | 03. Landstraße  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-sch%C3%B6ner-wohnen-mit-stil-%2A-2-zimmer-wohnung-vollst%C3%A4ndig-m%C3%B6bliert---3.-bezirk-f%C3%BCr-universit%C3%A4ten/-business-%2A-all-in-1559533337/)                                      | Jan 20, 11:29      |
|       762.3  |            55 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/geniale-2-zimmerwohnung-mit-lift-und-neuer-k%C3%BCche-%28ist-bis-zum-einzug-eingebaut%21%29-1532035290/)                                                                                                                 | Jan 20, 11:22      |
|       650    |            42 |          2 | 09. Alsergrund  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/charmante-15-zimmer-wohnung-in-top-lage---alserbachstra%C3%9Fe-33-top-25-1536373683/)                                                                                                                                 | Jan 20, 11:01      |
|       719    |            34 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---kirschbl%C3%BCtenpark---u1-n%C3%A4he-kagran---hofseitige-singlewohnung---provisionsfrei-1610628281/)                                                                                                      | Jan 20, 10:58      |
|       492.65 |            49 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/direktvergabe-2-zimmerwohnung-gemeinde-wohnung-vm:-31.12.2024-1586604573/)                                                                                                                                           | Jan 20, 10:35      |
