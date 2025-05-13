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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       766    |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/10.-belgradplatz---provisionsfreie-2-zimmer-neubau-loggiamiete-mit-gr%C3%BCnblick-in-wienerberg-n%C3%A4he-869316861/) | May 13, 17:32      |
|       726    |            34 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/mitten-in-meidling---nahe-schlo%C3%9F-sch%C3%B6nbrunn-1938384679/)                                                     | May 13, 15:48      |
|       600    |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/ruhige-2-zimmer-wohnung-%7C-3.-stock-%7C-n%C3%A4he-praterstern-1829818422/)                                        | May 13, 14:33      |
|       700    |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zentral-lage-%7C-sch%C3%B6ne-2-zimmer-wohnung-1495425221/)                                                            | May 13, 13:29      |
|       783.42 |            53 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung--hochparterre--provisionsfrei-zu-vermieten-1211063936/)                                        | May 13, 11:50      |
|       750    |            48 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%22charmante-2-zimmerwohnung-n%C3%A4he-wilhelmsdorfer-park%22-869729092/)                                              | May 13, 07:12      |
|       750    |            60 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%22teilm%C3%B6blierte-2-zimmer-wohnung-in-ruhiger-lage-in-1140-wien%21%22-916846374/)                                   | May 13, 07:12      |
|       749    |            34 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/freundliche-neubauwohnung-mit-hochwertiger-ausstattung-in-top-lage-nahe-yppenplatz-2009358996/)                         | May 13, 06:25      |
|       503    |            61 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-gemeindewohnung-1110-enkplatz-2055926802/)                                                              | May 12, 20:44      |
|       596    |            35 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-zu-vermieten-1608199022/)                                                                                     | May 12, 18:16      |
|       408    |            56 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-1682915199/)                                      | May 12, 17:02      |
|       700    |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/wohnung-zu-vermieten-1020-wien-2115986483/)                                                                        | May 12, 16:46      |
|       409    |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zwei-zimmer-gemeindewohnung-mit-vormerkschein-vor-31.03.25-2033489083/)                                               | May 12, 16:03      |
