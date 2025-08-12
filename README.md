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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       629.21 |            45 |          4 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristete-2-zimmer-wohnung-im-14.bezirk%21-1379207477/)                                                                               | Aug 12, 10:27      |
|       543.39 |            41 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/saniert-%2A%2A%2A-beim-kongressbad-und-s45-hernals-%2A%2A%2A-2-zimmer-wohnung-%2A%2A%2A-n%C3%A4he-hernalser-hauptstra%C3%9Fe-985124394/) | Aug 12, 07:34      |
|       650    |            60 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-%28zu-vergeben%29-1420086583/)                                                                           | Aug 11, 22:49      |
|       600    |            73 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-gemeinde-wohnung-direktvergabe-mit-wohnticket-bis-30.06.2024-1663419578/)                                                     | Aug 11, 21:50      |
|       710    |            61 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/top-sanierte-altbau-mietwohnung-nahe-belvedere-&-hauptbahnhof---2-zimmer-in-1030-wien-984024987/)                                | Aug 11, 20:50      |
|       749.56 |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sonnige-2-zimmer-wohnung%21-2097215139/)                                                                                                | Aug 11, 15:26      |
|       626.2  |            59 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wiener-wohnen-direktvergabe-/-datum-bis-31.07.2025-f%C3%BCr-2-personen-1259349256/)                                    | Aug 11, 10:30      |
