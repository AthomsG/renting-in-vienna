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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       630    |            79 |          3 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/3-zimmer-gemeindewohnung-direktvergabe-1540603589/)                                                           | Aug 19, 00:26      |
|       789    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/top-renoviert%21-1702930463/)                                                                                 | Aug 18, 21:50      |
|       669    |            51 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/provisionsfrei:-sonniger-51m%C2%B2-altbau-mit-einbauk%C3%BCche-am-augarten---1020-wien-2128999186/)       | Aug 18, 21:31      |
|       474.21 |            47 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-n%C3%A4he-augarten-1893247661/)                                                           | Aug 18, 16:44      |
|       692.07 |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-u1-station-keplerplatz---2-zimmer-mit-separater-k%C3%BCche---beim-wiener-hauptbahnhof-2000104982/) | Aug 18, 16:25      |
|       750    |            30 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%2Asmarte-2-zimmer-kleinwohnung%2A---neubau-in-sch%C3%B6nbrunn-n%C3%A4he-2064187743/)                          | Aug 18, 14:36      |
|       794.45 |            47 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%2Aab-01.11%2A-2-zimmer-wohntraum-mit-eigenem-garten%21-815028640/)                                          | Aug 18, 13:18      |
|       790    |            55 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchen-hit-1422780178/)                                                                                | Aug 18, 12:36      |
|       423    |            41 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/1050-wien-gassergasse-41/-stg.-4/-top-23-1287435093/)                                                       | Aug 18, 10:23      |
