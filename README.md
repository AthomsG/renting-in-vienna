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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       549.37 |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-im-10.-bezirk-813015206/)                                                                                                            | Jul 09, 18:41      |
|       783.95 |            69 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gef%C3%B6rderte-mietwohnung-mit-kaufoption---3-zimmer-in-wien-1110-kaiser-ebersdorfer-stra%C3%9Fe-257-259-eigenmittel-34.58815%E2%82%AC-1572107676/) | Jul 09, 16:19      |
|       761.75 |            45 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/naschmarktn%C3%A4he-ruhig-45m%C2%B2-86159-eur.-inkl.-heizung-u.-ww-unbefristet-1105367693/)                                                         | Jul 09, 14:17      |
|       653.83 |            62 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-wohnung-in-1140-wien-1507220371/)                                                                                                             | Jul 09, 13:57      |
|       609.03 |            50 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gef%C3%B6rderte-mietwohnung-mit-kaufoption---eigenmittel:-26.95293%E2%82%AC---2-zimmer-4953-m%C2%B2-mit-1332-m%C2%B2-dachterrasse-1427147943/)       | Jul 09, 13:49      |
|       777.62 |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-dg-wohnung-im-10.bezirk-n%C3%A4he-r%C3%A4umannplatz%21-2054018928/)                                                             | Jul 09, 12:54      |
|       790    |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/stadthalle-n%C3%A4he-%21-helle-neubauwohnung-in-hofseitiger-ruhelage-876715003/)                                                     | Jul 09, 12:07      |
|       775.15 |            52 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ger%C3%A4umige-2-zimmer-wohnun-2111841652/)                                                                                                          | Jul 09, 07:02      |
|       695.23 |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1557143531/)                                                                                                       | Jul 09, 07:02      |
|       757.75 |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/ger%C3%A4umige-3-zimmer-wohnung-im-21.og-1530191638/)                                                                                          | Jul 09, 07:02      |
|       570    |            49 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28anfragenstopp%29-direktvergabe-gemeindewohnung-wohnticket-vor-dem-31.03.2026-1346522250/)                                                   | Jul 09, 01:03      |
|       750    |            31 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wohnung-mit-terrasse-1410962064/)                                                                                                                      | Jul 08, 21:56      |
|       607    |            57 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-gemeinde-wohnung-direktvergabe-1833060173/)                                                                                         | Jul 08, 21:21      |
