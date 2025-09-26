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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       692.07 |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmerwohnung-in-der-gudrunstrasse-n%C3%A4he-u1-860856904/)                                                                    | Sep 25, 20:38      |
|       590    |            57 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe---2-zimmer-wohnung-mit-balkon-%285768-m%C2%B2%29-1604038231/)                                                      | Sep 25, 18:36      |
|       708.14 |            55 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristete-ruhelage-am-migazziplatz-918292870/)                                                                                 | Sep 25, 16:26      |
|       700    |            38 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfreie-mietwohnung-in-top-lage-38m2-1850995236/)                                                                       | Sep 25, 14:56      |
|       784.97 |            71 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gro%C3%9Fz%C3%BCgige-altbauwohnung-mit-guter-anbindung--unbefristet%21-992961644/)                                               | Sep 25, 13:15      |
|       600.28 |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/besichtigung-am-30.09.2025-16:30-18:30---425m%C2%B2-wohnung-im-2.-bezirk-1643344524/)                                         | Sep 25, 11:53      |
|       799    |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-u3-simmering---ruhelage---stellplatz-optional---zwischen-lorystra%C3%9Fe-und-simmeringer-hauptstra%C3%9Fe-1966859987/) | Sep 25, 07:21      |
|       799    |            46 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-single-wohnung-mit-vintage-flair-f%C3%BCr-individualisten-1090194387/)                                          | Sep 25, 07:15      |
