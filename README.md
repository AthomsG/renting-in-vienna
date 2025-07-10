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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       690    |            45 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/1070//-unbefristet---charmante-2-zimmer---top-lage-schottenfeldgasse%21-827101172/)                                                          | Jul 10, 17:25      |
|       684.78 |            51 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/mietwohnung---1160-wien---51-m%C2%B2-1610970441/)                                                                                         | Jul 10, 17:11      |
|       510    |            47 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/gemeindewohnung-direktvergabe-mit-g%C3%BCltigen-wohnticket-und-abl%C3%B6se---wiener-wohnen-gemeindebau---9.-badgasse-10/1/9-1424315419/) | Jul 10, 11:09      |
|       790    |            49 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-m%C3%B6blierte-wohnung-1471798239/)                                                                                                 | Jul 10, 11:04      |
|       516.77 |            42 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-1802080933/)                                                                                                                | Jul 10, 09:34      |
|       790    |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Aall-inklusive-apartment-schlafzimmer%2B-wohnzimmer%2A-n%C3%A4he-hauptbahnhof-2083203679/)                                              | Jul 09, 19:52      |
|       788.38 |            53 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohntraum-mit-balkon%21-1094973186/)                                                                                             | Jul 09, 18:25      |
|       689.55 |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-48m%C2%B2-altbau-mit-2-zimmern-und-lift---1100-wien-1440235897/)                                            | Jul 09, 17:15      |
|       550    |            62 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-1255824861/)                                                                                                | Jul 09, 17:00      |
|       799    |            39 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-gepflegte-singlewohnung-mit-parkblick---sofortbezug-1810488975/)                                                                    | Jul 09, 16:07      |
