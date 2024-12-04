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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       580    |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-2-zimmer-wohnung-mit-guter-aufteilung-und-top-preis-n%C3%A4he-u3-johnstra%C3%9Fe-1600130133/)                                                                                                                                                                             | Dec 04, 21:37      |
|       473.09 |            64 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug%21-/-vormerkschein-bis-31.03.2024-/-n%C3%A4chste-sammelbesichtigung-am-08.12.24-von-16-bis-18h-%21%21-891212848/)                                                                                                                            | Dec 04, 19:56      |
|       631.15 |            52 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sch%C3%B6ne-wohnung-ideal-als-studenten-wg-1122111701/)                                                                                                                                                                                                                                       | Dec 04, 19:36      |
|       778.6  |            58 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/unbefristet-charmante-altbaumiete-1356367697/)                                                                                                                                                                                                                                               | Dec 04, 18:58      |
|       548.78 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/super-preis---2-zimmerwohnung-mitten-in-favoriten%21-1670347542/)                                                                                                                                                                                                                               | Dec 04, 16:26      |
|       769.36 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/ideale-2-zimmer-dachgeschosswohnung-mit-gr%C3%BCnblick-in-stammersdorfer-heurigengegend-880459439/)                                                                                                                                                                                           | Dec 04, 16:17      |
|       782.61 |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/bitte-nur-schriftliche-anfragen-keine-anrufe.-unbefristete-h%C3%BCbsche-2-zimmer-wohnung-in-der-pernerstorfergasse-1174470888/)                                                                                                                                                                 | Dec 04, 16:11      |
|       750    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/brunnenmarkt:-stylische-2-zimmer-wohnung-mit-gutem-grundriss-in-hofruhelage-1860136196/)                                                                                                                                                                                                        | Dec 04, 15:29      |
|       610    |            60 |          3 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/direkt%C3%BCbergabe-mit-g%C3%BCltigem-wohn-ticket-%28wiener-wohnen-gemeindebau%29-1623032986/)                                                                                                                                                                                               | Dec 04, 14:48      |
|       475.08 |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/g%C3%BCnstige-und-helle-wohnung%21-1254984765/)                                                                                                                                                                                                                                                 | Dec 04, 13:41      |
|       690    |            63 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/63m%C2%B2-gemeindewohnung-2-%283%29-zimmer-%2A%2A%2Apreis-je-nach-zubeh%C3%B6r%2A%2A%2A---zentrale-lage-%282min-zum-bhf-matzleinsdorferplatz%29---neue-k%C3%BCche-%28wird-fix-mitverkauft%29---m%C3%B6blierung-auf-wunsch-mitkaufen---neu-ausgemalt-und-renoviert---sehr-gepflegt-1243982129/) | Dec 04, 13:06      |
|       790    |            53 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/privat---2-zimmer-whg-%2853m2%29-nahe-u3-h%C3%BCtteldorfer-stra%C3%9Fe-1499099300/)                                                                                                                                                                                                               | Dec 04, 12:39      |
|       720    |            50 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/13-altbauwohnung-sucht-nachmieter-direkt-am-wolfrathplatz-1637869854/)                                                                                                                                                                                                                           | Dec 04, 12:38      |
|       777.21 |            48 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1030049299/)                                                                                                                                                                                                              | Dec 04, 12:22      |
|       689    |            38 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1936334166/)                                                                                                                                                                                                                      | Dec 04, 12:18      |
|       502    |            46 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe---top-lage:-voll-m%C3%B6blierte-2-zimmer--gemeindewohnung-im-1020-wien---vms-vor-01.09.24-1043703898/)                                                                                                                                                                         | Dec 04, 12:13      |
|       737    |           nan |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mitten-im-10ten---zentral-und-ruhig-gelegen-920788606/)                                                                                                                                                                                                                                         | Dec 04, 11:47      |
|       797    |            77 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinde-wohnung-im-22.-bezirk-zu-vergeben-1591194473/)                                                                                                                                                                                                                                        | Dec 04, 11:43      |
|       548.79 |            34 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/entz%C3%BCckende-kleine-wohnung-perfekt-f%C3%BCr-singels%21-unbefristet%21-mitten-im-16.-bezirk%21-973968527/)                                                                                                                                                                                  | Dec 04, 11:13      |
|       798.95 |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristete-neubauwohnung-in-gehweite-des-bahnhof-penzing---ruhige-seitengasse-der-linzer-stra%C3%9Fe%21-ab-m%C3%A4rz-2025.---wohntraum-2005229429/)                                                                                                                                             | Dec 04, 10:58      |
