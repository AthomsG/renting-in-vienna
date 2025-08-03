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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       525.25 |            51 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemaidewohnung-zu-vergeben-51-qm-3.-bezirk-1615389161/)                                                                                      | Aug 03, 13:54      |
|       690    |            63 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-gemeinde-wohnung-1145550349/)                                                                                                                      | Aug 03, 13:44      |
|       770    |            61 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Ap%C3%A4rchentraum%2Asonniger-neubau-mit-bester-infrastruktur%21-1518950514/)                                                                             | Aug 03, 12:05      |
|       736.23 |            70 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wiener-wohnen-direktvergabe-vms-6/25-1131443212/)                                                                                                             | Aug 03, 10:29      |
|       515.67 |            46 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-gemeindewohnung-zu-vergeben-stichtag-30.06.2025-1682867657/)                                                                                         | Aug 03, 00:08      |
|       750    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-gr%C3%BCnlage-2-zimmer-beim-reumannplatz-1653457722/)                                                                                                | Aug 02, 18:04      |
|       700    |            43 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-gut-geschnittene-2-zimmerwohnung-in-ruhiger-lage-und-gr%C3%BCner-umgebung-tolle-anbindung-an-den-%C3%B6ffentlichen-verkehr-1992055258/) | Aug 02, 17:52      |
|       690    |            44 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ruhige-2-zi-altbau-3min-zu-u3-ottakring-823084971/)                                                                                                         | Aug 02, 16:02      |
