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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       790    |            50 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/bright-studio-apartment-furnished-/-helle-ein-zimmer-wohnung-m%C3%B6bliert-2047863584/)                                                                 | Feb 01, 14:04      |
|       470    |            47 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/moderne-2--zimmer-gemeindewohnung/-mit-vormerkschein-vsnr:-15.03.2018-1393069043/)                                                                 | Feb 01, 13:17      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1610205268/) | Feb 01, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1536756296/) | Feb 01, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1183927191/) | Feb 01, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-872917532/)  | Feb 01, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1928809618/) | Feb 01, 10:32      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1120135051/) | Feb 01, 10:31      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-2061795170/) | Feb 01, 10:31      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1375745267/) | Feb 01, 10:31      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1257301064/) | Feb 01, 10:31      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei-bei-anmietung-ab-01.02.2025%21---exklusiver-erstbezug-im-gr%C3%BCnen---n%C3%A4he-badeteich-hirschstetten-und-seestadt-1100819372/) | Feb 01, 10:31      |
|       723    |            74 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wiener-wohnen-direktvergabe-mit-vormerkschein-1117982830/)                                                                            | Feb 01, 10:03      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1305948891/)                                  | Feb 01, 08:02      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1390704747/)                                  | Feb 01, 07:54      |
|       792.62 |            73 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-altbaucharme-mit-optimaler-verkehrsanbindung-1785148889/)                                                                                    | Feb 01, 06:04      |
|       749    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/baujahr-2020-van-der-n%C3%BCll-gasse---hofseitige-2-zimmer-mit-957m2-gro%C3%9Fem-balkon-1308192383/)                                                  | Jan 31, 21:43      |
|       540    |            52 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeindewohnung:-moderne-2-zimmer-wohnung-direkt-bei-der-millennium-city---sofort-verf%C3%BCgbar%21-vm-31.01.25-921244371/)                         | Jan 31, 18:11      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-983920929/)                                   | Jan 31, 18:06      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1.-monat-mietfrei---pfalzgasse-29---traumhafter-erstbezug-in-ruhelage:-2-zimmer-wohnung-mit-balkon-1208077974/)                                      | Jan 31, 18:06      |
