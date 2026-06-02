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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       753.31 |            46 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-mit-balkon-im-sonnwendviertel---unbefristet-zu-vermieten-1247536314/)            | Jun 02, 15:59      |
|       795.29 |            32 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-2-zimmer-wohnung-1553179949/)                                                                             | Jun 02, 14:21      |
|       799    |            60 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-neu-saniert%21-ruhige-wohnung-beim-neuen-landgut-1124468057/)                       | Jun 02, 13:13      |
|       709    |            52 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei-&-unbefristet%21-wohnung-in-bester-lage%21-1137354992/)                                                | Jun 02, 13:03      |
|       719.01 |            38 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.7.---laxenburgerstrasse---helle-2-zimmer-singlewohnung-mit-s%C3%BCdseitigem-fernblick-im-7.-stock-1003818862/) | Jun 02, 12:07      |
|       791.92 |            54 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohung---wg-geeignet-1296359268/)                                                                          | Jun 02, 11:14      |
|       770    |           nan |          3 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktives-wohnen-mitten-im-sonnwendviertel-1622870157/)                                                           | Jun 02, 09:25      |
|       799    |            67 |          3 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmerwohnung-superzustand-1149261490/)                                                                           | Jun 02, 06:04      |
|       429.32 |            41 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wiener-wohnen-direktvergabe-%7C-2-zimmer-wohnung-%7C-1140-wien-%7C-g%C3%BCnstige-miete-1788049819/)                   | Jun 01, 21:31      |
|       621.7  |            59 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe:-2-zimmer-gemeindebauwohnung-2035284735/)                                                             | Jun 01, 21:28      |
|       660    |           nan |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/in-besonders-attraktiver-lage---mitten-in-hetzendorf-1432814629/)                                                    | Jun 01, 16:44      |
|       550    |            20 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/attraktives-wohnen-in-wien-altmannsdorf---n%C3%A4he-u6%21-1925263450/)                                               | Jun 01, 16:40      |
|       720.5  |           nan |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/mitten-in-meidling---nahe-schlo%C3%9F-sch%C3%B6nbrunn-1746520431/)                                                   | Jun 01, 15:38      |
