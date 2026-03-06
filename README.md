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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       649    |            45 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-2088023474/)                                                                                       | Mar 06, 17:15      |
|       639    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-ruhige-wohnung-beim-neuen-landgut-2060577915/)                                                                           | Mar 06, 17:11      |
|       784.74 |            73 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-1030-wien-direktvergabe-mit-vormerkschein-bis-31.01.2026---3-zimmer-1106211512/)                                                   | Mar 06, 17:09      |
|       779    |            34 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.5.2026---laxenburgerstra%C3%9Fe-151---1100-wien---traumhafte-neubau---singlewohnung-im-9ten-stock-mit-fernblick-1428023853/)                        | Mar 06, 12:37      |
|       799.9  |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktive-2-zimmer-wohnung-nahe-wielandpark-in-1100-wien-zu-mieten-1998135453/)                                                                         | Mar 06, 12:19      |
|       760    |            78 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gro%C3%9Fz%C3%BCgige-hauptmietwohnung-in-1150-u4-n%C3%A4he-964404673/)                                                                   | Mar 06, 11:13      |
|       736    |            70 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/3-zimmer-wohnung-964637366/)                                                                                                                               | Mar 06, 11:01      |
|       650    |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/nachmieter-gesucht-ab-01.05.2026-1150-wien-1931469319/)                                                                                  | Mar 05, 20:54      |
|       790    |            37 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei-neubau-2022-privat-2-zimmer-wohnung-1120-wien-top-lage-1335852871/)                                                                        | Mar 05, 20:45      |
|       460    |            42 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/g%C3%BCnstige-2-zimmer-gemeindewohnung-in-wien-14-%7C-n%C3%A4he-h%C3%BCtteldorfer-stra%C3%9Fe-1880357887/)                                                 | Mar 05, 19:36      |
|       632.55 |            58 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ab-1.4.2026-bezugsfertig:-linzer-stra%C3%9Fe-111--ca.-58m%C2%B2-gro%C3%9Fe-2-zimmer-altbauwohnung-im-hochparterre-inkl.-heizung-%2B-warmwasser-809595628/) | Mar 05, 17:36      |
|       799    |            59 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/parkblick-%7C-2-zimmer-%7C-termine-siehe-text-1462331635/)                                                                                               | Mar 05, 17:27      |
