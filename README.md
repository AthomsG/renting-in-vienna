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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       580    |            35 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sommerwohnung-f%C3%BCr-den-august-1209535151/)                                                                              | Jun 24, 16:17      |
|       649.8  |            51 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-dachgeschoss-am-dornerplatz-1957868661/)                                                                                  | Jun 24, 13:49      |
|       506    |            43 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-gemeindewohnung-im-3.-bezirk-mit-vormerkschein-1067587977/)                                          | Jun 24, 13:04      |
|       700    |            40 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sanierter-neubau-2-zimmer-mit-einbauk%C3%BCche-n%C3%A4he-ameisbr%C3%BCcke-hiezing-u4-keine-abl%C3%B6se-%21%21%21-1453069059/) | Jun 24, 10:20      |
|       745.33 |            48 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/balkonwohnung-in-n%C3%A4he-des-flughafens%21-1839962784/)                                                                   | Jun 24, 09:59      |
|       715    |            74 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-und-g%C3%BCnstige-3-zimmer-wohnung-795506569/)                                                                        | Jun 23, 22:39      |
|       560    |            56 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeinde-wohnung-vsdatum:-30.04.2025-1185384874/)                                                                           | Jun 23, 19:13      |
