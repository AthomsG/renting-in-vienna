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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       685.05 |            46 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gem%C3%BCtliche-2-zimmer-wohnung-im-15.bezirk%21-1189773332/)                                            | Oct 15, 14:40      |
|       699    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleinod-in-hauptbahnhof-n%C3%A4he-1477628273/)                                                                           | Oct 15, 11:58      |
|       790.9  |            52 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ruhe-genie%C3%9Fen-in-simmering%21-zwei-zimmer-wohnung-hugogasse-12---top-9-1687978657/)                                 | Oct 15, 11:39      |
|       665.87 |            58 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/m%C3%B6blierte-zwei-zimmer-wohnung-im-10ten%21-1457875924/)                                                              | Oct 15, 11:07      |
|       563    |            57 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung-%28direktvergabe%29-in-toplage---1030-wien-n%C3%A4he-rochusmarkt-&-stadtpark-1078040721/) | Oct 14, 18:41      |
|       440    |            28 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/studentenwohnung-in-absoluter-bestlage-1517403719/)                                                                     | Oct 14, 18:28      |
|       686    |            63 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-wien-16.-bezirk-1060554669/)                                                                             | Oct 14, 17:52      |
|       582.37 |            97 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeinde-wohnung-1842325469/)                                                                                            | Oct 14, 17:09      |
|       563.9  |            62 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-n%C3%A4he-u1-oberlaa-vmd-bis-31.08.2025-1680925443/)                                                     | Oct 14, 16:56      |
|       690    |            47 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ger%C3%A4umige-2-zimmer-wohnung-in-sehr-guter-lage-in-%2A1140-wien%2A-1201230699/)                                         | Oct 14, 16:21      |
