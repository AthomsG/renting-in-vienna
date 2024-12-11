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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       575    |            56 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-gef%C3%B6rderte-wohnung-mit-abstellraum-und-balkon-ab-31.01.25-zu-vergeben%21-869184078/)                                                             | Dec 11, 12:15      |
|       729.52 |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/direkte-bautr%C3%A4gervergabe%21-supermarkt-im-haus-direkte-u-bahn-anbindung-inkl-k%C3%BCche%21-1907215437/)                                     | Dec 11, 11:49      |
|       729    |            44 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/ruhige-balkonwohnung-777984345/)                                                                                                                                  | Dec 11, 11:26      |
|       799    |            46 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1749667013/)                                                                                       | Dec 11, 11:19      |
|       558    |            55 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/top-gemeinde-wohnung-1695110631/)                                                                                                                             | Dec 11, 11:00      |
|       798.95 |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristete-neubauwohnung-in-gehweite-des-bahnhof-penzing---ruhige-seitengasse-der-linzer-stra%C3%9Fe%21-ab-m%C3%A4rz-2025.---wohntraum-2005229429/)              | Dec 11, 10:58      |
|       560    |            46 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sch%C3%B6ne-15-zimmerwohnung-nahe-u3-kardinal--nagl--platz%21-unbefristeter-mietvertrag%21-1938025074/)                                                    | Dec 11, 10:45      |
|       730.39 |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohntraum-mit-loggia-in-unmittelbarer-n%C3%A4he-zur-u2-station-hardeggasse%21-848409529/)                                                              | Dec 11, 10:09      |
|       688.77 |            40 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/charmante-2-zimmer-wohnung-nahe-u2-hardeggasse---ruhig-in-einer-seitengasse-gelegen-mit-einladender-loggia%21-1468304607/)                                      | Dec 11, 10:07      |
|       720    |            44 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genie%C3%9Fen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)                                                                 | Dec 11, 10:07      |
|       770    |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-sp%C3%A4ter-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                                                                              | Dec 11, 10:07      |
|       719.33 |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien-leopoldauer-stra%C3%9Fe-top-6-loggia-6m%C2%B2-2-zimmer-45m%C2%B2-fu%C3%9Fbodenheizung-wannenbad-einbauk%C3%BCche-1.-liftstock-erstbezug-1279190980/) | Dec 11, 09:16      |
|       779    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-sonnige-ruhige-und-sehr-gepflegte-wohnung---provisionsfrei-1373721648/)                                                                              | Dec 11, 07:55      |
|       609.71 |            62 |          3 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/3-zimmer-gemeindewohnung-1169314274/)                                                                                                                              | Dec 11, 07:36      |
|       799    |            37 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ne-2-zimmer-dachgeschosswohnung-mit-balkon-in-u-bahn-n%C3%A4he-1727405139/)                                                                       | Dec 11, 03:39      |
|       798    |            37 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sehr-sch%C3%B6ne-2-zimmerwohnung---n%C3%A4he-donauinsel-&-handelskai-1506947017/)                                                                              | Dec 10, 21:36      |
|       520    |            60 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/wohnung-zu-vermieten-1521748133/)                                                                                                                               | Dec 10, 20:42      |
|       764.19 |            78 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmerwohnung-unbefristet-zu-mieten-1602204884/)                                                                                                   | Dec 10, 19:33      |
|       755.9  |            47 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-mit-balkon-perfekt-ausgerichtet-f%C3%BCr-ruhe---nur-wenige-schritte-vom-bahnhof-floridsdorf-entfernt%21-1111885035/)                  | Dec 10, 17:39      |
|       482    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-43-m%C2%B2-2-zimmerwohnung-2008548347/)                                                                                                         | Dec 10, 17:36      |
