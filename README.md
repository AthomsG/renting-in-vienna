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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       648.01 |            39 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sanierte-2-zimmer-wohnung-n%C3%A4he-u3-ottakrig-1405383656/)                                                                                      | Apr 14, 06:57      |
|       795    |            40 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1395567074/)                                                                                       | Apr 14, 02:22      |
|       720    |            52 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/hochwertige-zweizimmerwohnung-in-ottaktring-unbefristet-1732076186/)                                                                              | Apr 13, 23:27      |
|       475    |            43 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-2-zimmer-gemeindewohnung-in-top-zustand%21-direktvergabe-1083109868/)                                                      | Apr 13, 23:24      |
|       555    |            51 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-gemeinde-wohnung-/-gute-%C3%B6ffentliche-anbindungen-/-gute-parkm%C3%B6glichkeiten-/-sch%C3%B6n-zentral-mit-freier-sicht-1158291877/) | Apr 13, 22:13      |
|       420    |            41 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zur-vergabe-%28reserviert%29-1140494205/)                                                                                   | Apr 13, 22:07      |
|       499.92 |            46 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe:-zentrale-2-zimmer-gemeindewohnung-in-toplage-%28vormerkschein-vor-dem-30.11.2024%21%29-1191150306/)                             | Apr 13, 18:39      |
|       750.27 |            40 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter-gesucht-904078628/)                                                                                                                    | Apr 13, 16:00      |
|       784    |            79 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3-zimmer-gemeindewohnung-1119144123/)                                                                                                               | Apr 13, 13:15      |
|       450    |            40 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-wohnung-mit-herrlichem-gr%C3%BCnblick-1226018227/)                                                                                           | Apr 13, 12:40      |
|       630    |            41 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-wohnung-neubau-1259314394/)                                                                                                                | Apr 13, 10:23      |
