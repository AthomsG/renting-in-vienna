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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       775.87 |            48 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-5:-gro%C3%9Fz%C3%BCgige-2-zi-wohnung-2080748687/)                                                                                   | Nov 05, 17:07      |
|       612.31 |            39 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/charmante-2-zi-wohnung-1051442264/)                                                                                                     | Nov 05, 17:07      |
|       717.65 |            45 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-6:-ger%C3%A4umige-2-zi-wohnung-1285600379/)                                                                                         | Nov 05, 17:07      |
|       741.72 |            53 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/top-2-zimmer-wohnung-mit-einbauck%C3%BCche-1534732137/)                                                                                  | Nov 05, 16:04      |
|       693.56 |            50 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/sch%C3%B6ne-2-zimmer-a-1540762033/)                                                                                                      | Nov 05, 16:01      |
|       617.4  |            52 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/charmante-2-zimmer-wohnung-2023740868/)                                                                                                  | Nov 05, 16:00      |
|       559.44 |            40 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/2-zimmer-wohnung-mit-kreativer-aufteilung-und-einbauk%C3%BCche-1354191906/)                                                              | Nov 05, 15:59      |
|       528    |            46 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/top-lage-im-zentrum-rathausn%C3%A4he-2-zimmer-528.---brutto-1163730980/)                                                             | Nov 05, 15:00      |
|       789.81 |            59 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gepflegte-altbauwohnung-n%C3%A4chst-urania-nur-3-gehminuten-vom-1.-wiener-bezirk-entfernt-1092343689/)                             | Nov 05, 14:06      |
|       410    |            64 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeindewohnung-direktvergabe-3-zimmer-ruhige-lage-1508584685/)                                                                         | Nov 05, 12:02      |
|       749    |            70 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/belghofergasse---sanierungsbed%C3%BCrftiger-2-zimmer-altbau-zu-vermieten-1298147745/)                                                  | Nov 05, 00:37      |
|       790.72 |            54 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erdw%C3%A4rmepumpe-%7C-balkon-%7C-erstbezug-ab-15.12.2025-1970327301/)                                                                | Nov 04, 20:40      |
|       664.66 |            46 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/u3-h%C3%BCtteldorfer-stra%C3%9Fe-ii-2-zimmer-mit-separater-k%C3%BCche-ii-n%C3%A4he-wien-penzing-bahnhof-und-s45-breitensee-1822914495/) | Nov 04, 17:55      |
|       740    |            49 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/charmante-wohnung-1588498472/)                                                                                                        | Nov 04, 17:02      |
|       768.63 |            40 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/cityapartment:-garagenplatz-im-haus-&-u6-spittelau-ums-eck---open-house-am-14.10.2025-um-14:00-1555017726/)                          | Nov 04, 16:53      |
