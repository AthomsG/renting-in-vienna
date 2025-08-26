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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       778    |            51 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wundersch%C3%B6ne-2-zimmer-wohnung-zu-vermieten-2038635492/)                                                                                                                          | Aug 26, 09:17      |
|       509    |            47 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-gemeindewohnung-vormerkschein-stichtag-31.5.2025-2046776653/)                                                                                                      | Aug 26, 09:06      |
|       692.07 |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmerwohnung-in-der-gudrunstrasse-n%C3%A4he-u1-1915557035/)                                                                                                                      | Aug 25, 20:35      |
|       580    |            48 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-965708792/)                                                                                                                                                                  | Aug 25, 18:11      |
|       580    |            69 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe:-sch%C3%B6ne-gemeindewohnung-in-14-bezirk-wichtig-vormerkschein-1349613914/)                                                                                            | Aug 25, 15:01      |
|       699    |            62 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6n-sanierte-2-zimmer-wohnung-mit-neuer-k%C3%BCche-in-%2A1100-wien%2A-1465592581/)                                                                                           | Aug 25, 14:40      |
|       725    |            74 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%2A%2Af%C3%BCr-sportliche---4.-stock-ohne-aufzug%2A%2A-liebevolle-2-zimmer-wohnung-in-ausgezeichneter-lage-direkt-auf-der-wiedner-hauptstra%C3%9Fe-in-%2A1050-wien%2A-1739823707/) | Aug 25, 14:39      |
|       660    |            57 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/besichtigung-heute-den-25.08.2025-2-zimmer-gemeindewohnung-per-direktvergabe---1090-wien-1123053108/)                                                                              | Aug 25, 12:53      |
|       619.3  |            46 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/schicke-hofseitige-singlewohnung-im-2.-stock-1127704684/)                                                                                                                          | Aug 25, 10:56      |
