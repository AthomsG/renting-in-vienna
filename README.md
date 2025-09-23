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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       490    |            47 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sch%C3%B6ne-zentrale-gemeindewohnung-1030-wien-landstra%C3%9Fe-vormerkschein-31.08.2025-895554242/) | Sep 23, 12:10      |
|       720    |            60 |          3 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ideal-f%C3%BCr-2er-wg-studenten-oder-berufst%C3%A4tige-singles-oder-paare%21-1480938845/)                 | Sep 23, 10:30      |
|       585    |            55 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3-zimmer-gemeinde-wohnung-direktvergabe-876300522/)                                                         | Sep 23, 07:41      |
|       794.98 |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stylische-2-zimmer-wohnung-renoviert-mit-hochwertiger-m%C3%B6blierung-1418337009/)                        | Sep 23, 07:04      |
|       797.73 |            60 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-altbauwohnung-der-fernkorngasse-780587760/)                                                         | Sep 22, 18:25      |
|       754    |            32 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hofruhelage%21-kleine-2-zimmer-neubauwohnung-mit-terrasse-n%C3%A4he-u1%21-1756424757/)                    | Sep 22, 16:25      |
|       569    |            47 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/erstbezug-am-lerchenfelder-g%C3%BCrtel-1913196816/)                                                       | Sep 22, 12:56      |
|       720    |            48 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-wohnung-in-ruhelage-zu-vermieten-1818750972/)                                             | Sep 22, 11:30      |
