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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei---pfalzgasse-29---traumhafter-erstbezug-in-ruhelage:-2-zimmer-wohnung-mit-balkon-1661410316/)                                       | Jan 15, 12:41      |
|       463.99 |            42 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeindewohnung-mit-vms-1-wohnraum-datum-31.12.24-1633489089/)                                                                                       | Jan 15, 12:30      |
|       554.57 |            39 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/n%C3%A4he-u3-station-ii-g%C3%BCnstige-singlewohnung-ii-zwischen-stadthalle-und-schmelz-ii-10min-in-die-wiener-innenstadt-1604204484/)  | Jan 15, 12:30      |
|       779.34 |            43 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/ideales-stadtapartment-in-zentraler-lage-2098209235/)                                                                                            | Jan 15, 12:30      |
|       777.21 |            48 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1030049299/)                                                                     | Jan 15, 12:22      |
|       639.12 |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charmante-&-modern-ausgestattete-2-zimmer-altbau-wohnung-mit-terrasse%21-1963680381/)                                                  | Jan 15, 12:19      |
|       789.57 |            51 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/wohnpark-liesing-%21-dirmhirngasse-76-&-78-1972153426/)                                                                                                  | Jan 15, 11:41      |
|       742.01 |            43 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil/-bg17-top-1-11-1587671001/)                                | Jan 15, 11:28      |
|       653    |            68 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%21%212-zimmer-gemeindewohnung-ab-m%C3%A4rz-verf%C3%BCgbar-ist%21-2140802943/)                                                                        | Jan 15, 10:28      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei-%7C-pfalzgasse-29---zwei-zimmer-und-ein-balkon---traumhafter-erstbezug-1201153703/)                                                  | Jan 15, 10:13      |
|       770    |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-sp%C3%A4ter-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                                                                    | Jan 15, 10:07      |
|       720    |            44 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genie%C3%9Fen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)                                                       | Jan 15, 10:07      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-954325505/)                                    | Jan 15, 07:56      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-968537777/)                                    | Jan 15, 07:54      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-2033089937/)                                   | Jan 15, 07:46      |
|       712.31 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/sehr-gut-gelegene-43m%C2%B2-wohnung---ihr-neues-zuhause-mit-allem-was-sie-brauchen%21-5-minuten-zu-fu%C3%9F-von-der-donauinsel-entfernt-1781341824/) | Jan 15, 02:09      |
|       650    |            63 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeinde-wohnung-3-zimmer-%21-1388261264/)                                                                                                              | Jan 14, 21:15      |
|       790    |            48 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/helle-2-zimmer-wohnung-in-liesing-zu-vermieten%21-999240734/)                                                                                            | Jan 14, 20:45      |
|       525.49 |            54 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-2-zimmer-1990952480/)                                                                                                                 | Jan 14, 19:34      |
|       787.92 |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m%C2%B2-zum-mietpreis-von-78792-eur%21-1580236359/)                                                     | Jan 14, 18:35      |
