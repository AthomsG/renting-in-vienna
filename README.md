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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       627    |           nan |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/moderne-garconnieren-sowie-2-zimmer-apartments-in-zentraler-lage-in-altmannsdorf-1510995813/)                                 | Dec 03, 14:27      |
|       492    |            47 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-gemeindewohnung---vormerkschein-bis-vor-dem-30.11.2025-ben%C3%B6tigt-1863594071/)                                   | Dec 03, 13:49      |
|       680.01 |            52 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-2-zimmer-mietwohnung-.-komplett-neusaniert---ab-1.2.26-bezugsbereit-2058416114/)                                | Dec 03, 13:33      |
|       775    |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sofortbezug---2er-wg-studenten-wohnung%21-1250127082/)                                                                       | Dec 03, 13:26      |
|       653    |            52 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-auf-der-thaliastra%C3%9Fe-1591829877/)                                                                      | Dec 03, 12:55      |
|       699.7  |            68 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-2111200412/)                                                                                        | Dec 03, 10:30      |
|       776.49 |            57 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zentrale---g%C3%BCnstige---2-zi.-stadtwohnung---wg-m%C3%B6glich-2082311762/)                                           | Dec 03, 09:22      |
|       487.88 |            59 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/bastlerwohnung-gef%C3%B6rderte-2-zimmer-wohnung-1472382638/)                                                                 | Dec 03, 02:40      |
|       759.36 |            83 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gef%C3%B6rderte-3-zimmer-wohnung-mit-eigentumsoption-1695250042/)                                                            | Dec 03, 02:40      |
|       756.41 |            50 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gut-gelegene-50-m%C2%B2-wohnung-mit-lift-1245754730/)                                                                          | Dec 02, 22:41      |
|       487.59 |            45 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-zu-vergeben-in-1140-wien---%C3%BCber-wiener-wohnen-1542772402/)                                                | Dec 02, 17:36      |
|       768.63 |            40 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/cityapartment:-garagenplatz-im-haus-&-u6-spittelau-ums-eck-1547574512/)                                                     | Dec 02, 16:38      |
|       708    |            46 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-m%C3%B6blierte-2-zimmer-wohnung-an-der-wu-&-sfu-2.-bezirk-/-furnished-apartment-%7C-xl-bude-1177987177/) | Dec 02, 16:25      |
