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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       550    |            51 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-gemeindewohnung-1100-wien-2094899393/)                                                                                                                                              | Jun 06, 20:04      |
|       796.48 |            46 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/1090-porzellangasse/u4-rossauer-l%C3%A4nde-sanierte-2-zimmerwohnung-%281-wohnschlafzimmer-mit-separater-k%C3%BCche%29-in-uni-n%C3%A4he-mit-kleiner-terrasse-unbefristet-zu-vergeben-1715637559/) | Jun 06, 18:46      |
|       730    |            55 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/nachmieter-f%C3%BCr-die-wohnung-1710989418/)                                                                                                                                                     | Jun 06, 15:21      |
|       770    |            47 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/hoflage---ruhige-2-zimmerwohnung---dornbacher-stra%C3%9Fe-1608226720/)                                                                                                                              | Jun 06, 14:55      |
|       799.08 |            63 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-mit-terrasse-zu-vermieten-1926561089/)                                                                                                                                           | Jun 06, 12:34      |
|       461.53 |            46 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-zu-vermieten-916563489/)                                                                                                                                                            | Jun 06, 11:59      |
|       478.96 |            43 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-863877626/)                                                                                                                                                                        | Jun 06, 11:14      |
|       655    |            44 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/single---p%C3%A4rchenwohnung-2-raum-2129900233/)                                                                                                                                                  | Jun 06, 10:27      |
|       588    |            56 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-in-wien---direktvergabe-1496241971/)                                                                                                                                               | Jun 05, 21:58      |
