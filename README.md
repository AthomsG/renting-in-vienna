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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       558    |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/vollm%C3%B6blierte-2-zimmer-wohnung-in-zentraler-lage-des-10.-bezirks-1364324004/)                                         | Sep 23, 21:03      |
|       599.16 |            55 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-gemeindewohnung-im-3.-bezirk-1975786691/)                                                              | Sep 23, 19:48      |
|       500    |            63 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-zu-vergeben-1048587069/)                                                                                   | Sep 23, 19:33      |
|       798.05 |            47 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/charmantes-2-zimmer-apartment-in-1140-wien-1482595190/)                                                                      | Sep 23, 17:35      |
|       692.07 |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-u1-station-keplerplatz---2-zimmer-mit-separater-k%C3%BCche---beim-wiener-hauptbahnhof-1971956848/)               | Sep 23, 16:59      |
|       590    |            84 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeinde-wohnung-1020wien/84m2/-550%E2%82%AC-1204897235/)                                                               | Sep 23, 16:55      |
|       430    |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-gemeindewohnung-in-wien-%2811.-bezirk%29-zu-vermieten-1200932941/)                                                | Sep 23, 14:37      |
|       775.01 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-wohnung-mit-abstellraum-780728892/)                                                                       | Sep 23, 12:36      |
|       490    |            47 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-sch%C3%B6ne-zentrale-gemeindewohnung-1030-wien-landstra%C3%9Fe-vormerkschein-31.08.2025-895554242/) | Sep 23, 12:10      |
|       720    |            60 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ideal-f%C3%BCr-2er-wg-studenten-oder-berufst%C3%A4tige-singles-oder-paare%21-1480938845/)                                  | Sep 23, 10:30      |
|       585    |            55 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3-zimmer-gemeinde-wohnung-direktvergabe-876300522/)                                                                          | Sep 23, 07:41      |
|       794.98 |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stylische-2-zimmer-wohnung-renoviert-mit-hochwertiger-m%C3%B6blierung-1418337009/)                                         | Sep 23, 07:04      |
