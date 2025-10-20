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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                               | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       732.5  |            30 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-sanierung:-sch%C3%B6ne-2-zimmer-wohnung-mit-top-anbindung-1241916316/)                                          | Oct 20, 10:52      |
|       630    |            79 |          3 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/diirektvergabe-nur-noch-im-oktober-2025-vormerkscheindatum-vor-31.8.2024---3-zimmer-gemeindewohnung-direktvergabe-1016241640/) | Oct 20, 09:14      |
|       696    |            70 |          3 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-gemeindewohnung-nur-mit-vms-bis-31.3.2025%21%21-1930884145/)                                                         | Oct 19, 20:42      |
|       650    |            43 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-43m%C2%B2-zu-vermieten-keine-makler-erw%C3%BCnscht-1086173593/)                                                        | Oct 19, 17:16      |
|       737.01 |            68 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-wohnung-vermieten-2082541844/)                                                                               | Oct 19, 14:37      |
|       750    |            49 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-zu-vermieten-1236850083/)                                                                                             | Oct 19, 12:50      |
