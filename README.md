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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       559.64 |            40 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kompakte-2-zimmer-wohnung%21-1288151431/)                                                                                                                                                      | Dec 16, 14:25      |
|       755    |            60 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierte-25-zimmer-wohnung-nahe-sonnwendviertel-1083062890/)                                                                                                                                   | Dec 16, 12:58      |
|       689    |            59 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/entz%C3%BCckende-erdgescho%C3%9Fwohnung-n%C3%A4he-brunnenmarkt%21-1270150124/)                                                                                                                   | Dec 16, 12:36      |
|       682    |            52 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/helle-altbauwohnung-mit-kleiner-k%C3%BCche-bei-der-berggasse%21-direkt-besichtigung-am-mittwoch-den-17.12.2025-von-09:00-uhr-bis-10:00-uhr-vor-ort%21-hernalser-hauptstra%C3%9Fe-45-1255454948/) | Dec 16, 10:48      |
|       796.89 |            41 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-neubauwohnung-mit-gro%C3%9Fem-balkon---2.-og-1585649280/)                                                                                                                     | Dec 16, 08:13      |
|       697.52 |            45 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/termine-bitte-online-buchen-%28link-steht-im-text%29-945784158/)                                                                                                                                 | Dec 16, 08:05      |
|       590    |            54 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung---direktvergabe-%282-zimmer%29---1100-wien-1596996892/)                                                                                                                        | Dec 15, 20:23      |
|       616    |           nan |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernes-wohn--und-gesch%C3%A4ftshaus-1764196630/)                                                                                                                                             | Dec 15, 16:26      |
|       730    |            90 |          3 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-wohnung-1071204240/)                                                                                                                                                          | Dec 15, 15:59      |
|       700    |            52 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-1254252809/)                                                                                                       | Dec 15, 15:21      |
