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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       561.43 |            49 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet:-2-zimmer-altbau-nahe-matzleinsdorfer-platz-1505204892/)                                     | Aug 07, 12:26      |
|       617    |            53 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-gemeindewohnung-vmd-bis-31.7.2025-1440724038/)                                                    | Aug 07, 11:24      |
|       653    |            51 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%21%21-anfragenstop%21%21-helle-wohnung-im-3.-bezirk-1999661513/)                                  | Aug 07, 09:20      |
|       533.29 |            33 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/ruhige-2-zimmer-wohnung-%2A-prinz-eugen-strasse---schloss-belvedere-1998310919/)                            | Aug 07, 08:47      |
|       497.38 |            69 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ger%C3%A4umige-2-zimmer--wohnung-1838488071/)                                                            | Aug 07, 06:54      |
|       797.48 |            36 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmerwohnung-innenhoflage-mit-perfekter-infrastruktur-1549811136/)                            | Aug 07, 00:40      |
|       670    |            65 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-1372172298/)                                                           | Aug 06, 22:05      |
|       608.3  |            56 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/studentenwohnung-1383282094/)                                                                              | Aug 06, 19:38      |
|       680    |            45 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/student:-innen-zur-untermiete-gesucht-%28nur-1-person%29-1862522028/)                                   | Aug 06, 18:04      |
|       649    |            74 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnhit-wg-tauglich-provisionsfrei-gute-lage-1409967891/)                                       | Aug 06, 14:37      |
|       649    |            33 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-15.08.---1100-wien---ansprechende-neubau-singlewohnung-inkl.-k%C3%BCchenzeile-mit-balkon-1638962527/) | Aug 06, 13:37      |
|       660    |            63 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gem%C3%BCtliche-2-zimmer-wohnung-nahe-auhofcenter-mit-gartenben%C3%BCtzung-ab-sofort-1850160120/)          | Aug 06, 12:26      |
|       714    |            56 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmantes-2-zimmer-apartment-in-wien-favoriten-1004056149/)                                             | Aug 06, 12:07      |
|       408    |            56 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-886363684/)                          | Aug 06, 11:55      |
