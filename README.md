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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799.9  |            47 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/ruhige-zweizimmerwohnung-mit-morgensonne-%2B%2B%2B-neubau-1752160874/)                                                                                                                                  | Nov 10, 21:33      |
|       585    |            34 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung-1984716232/)                                                                                                                                                                           | Nov 10, 21:19      |
|       739.07 |            39 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/nachmieter-f%C3%BCr-helle-2-zimmer-wohnung-mit-einbauk%C3%BCche-gesuchtt-1322435768/)                                                                                                                   | Nov 10, 20:46      |
|       760    |            47 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-mit-balkon-n%C3%A4he-marchfeldkanal-1217593785/)                                                                                                                                      | Nov 10, 17:25      |
|       663    |            62 |          3 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinede-wohnung-dirktvergabe-kaiserm%C3%BChlen-neben-u1-833386502/)                                                                                                                                   | Nov 10, 15:15      |
|       690    |            35 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/kleine-aber-feine-provisionsfreie-wohnung-mit-ausblick-auf-den-kirschbl%C3%BCtenpark-1129462037/)                                                                                                       | Nov 10, 15:15      |
|       551    |            84 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeinde-wohnung-direktvergabr-2093286640/)                                                                                                                                                           | Nov 10, 15:06      |
|       730    |            37 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-2-zimmer-wohnung---ideal-f%C3%BCr-singles-oder-paare-1390175627/)                                                                                                                                    | Nov 10, 15:04      |
|       796    |            47 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/sch%C3%B6ne-2-zimmer-wohnung-im-herzen-von-7.-bezirk-2049080290/)                                                                                                                                           | Nov 10, 14:30      |
|       698    |            46 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/zwischenmiete/-kurzzeitmiete-ab-dezember-bis-ende-mai:-g%C3%BCnstige-altbauwohnung-in-ruhiger-lage-direkt-an-der-mariahilfer-stra%C3%9Fe-vollm%C3%B6bliert-und-einzugsfertig-keine-provision-824706890/) | Nov 10, 13:26      |
|       783.3  |            76 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-76m%C2%B2-in-direktvergabe-mit-vormerkschein-und-abl%C3%B6se-zu-vergeben-1072261420/)                                                                                                    | Nov 10, 12:41      |
|       500    |            47 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung---direktvergabe-g%C3%BCltiger-vormerkschein-bis-31.07.2024-erforderlich%21%21-818489687/)                                                                                                 | Nov 10, 12:01      |
|       584.13 |            76 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-direktvergabe-1973821846/)                                                                                                                                                                      | Nov 10, 11:41      |
|       780    |            55 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/sonnige-2-zimmer-whg-wg--geeignet-keine-provision-1516099274/)                                                                                                                                         | Nov 10, 10:25      |
|       749.71 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                                                                                                          | Nov 10, 10:24      |
|       749    |            44 |          2 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/ruhige-balkonwohnung-1575130865/)                                                                                                                                                                         | Nov 10, 09:32      |
|       645    |            49 |          2 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/kleine-wohnung-in-1130-wien-1492229474/)                                                                                                                                                                  | Nov 10, 08:04      |
|       680    |            64 |          3 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/gemeinde-wohnung-direktvergabe-vormerkschein-31.10.2024-1866807470/)                                                                                                                                      | Nov 09, 22:37      |
