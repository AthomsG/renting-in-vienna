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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       608.23 |            53 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-helle-altbauwohnung-in-u1-n%C3%A4he-1911306621/)                                    | Jan 06, 08:55      |
|       721.52 |            68 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeindebau-wohnung-im-gr%C3%BCnen---vormerkschein-vor-30.11.2024%21-1188388686/)    | Jan 06, 07:08      |
|       754.36 |            62 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/miete-930--inkl.-heizung---2-zimmer-balkonwohnung-im-herzen-von-ottakring-ab-sofort---2031348699/) | Jan 06, 03:48      |
|       649.47 |            55 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/1040-ruhige-2-zimmer-wohnung-nahe-alois-drasche-park-1812174939/)                                   | Jan 06, 03:44      |
|       695    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-sch%C3%B6ne-2-zimmer-wohnung-783334429/)                                        | Jan 05, 15:11      |
|       658    |            37 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/m%C3%B6blierte-neubauwohnung-mit-balkon-1160-wien--abl%C3%B6se-3.700-1611649868/)                | Jan 05, 12:11      |
|       435    |            41 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/1050-wien-gassergasse-41/-stg.-4/-top-22-1125928790/)                                           | Jan 05, 11:55      |
