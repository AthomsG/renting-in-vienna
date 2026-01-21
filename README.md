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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            36 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/odo25---helles-wohnen-mit-blick-ins-gr%C3%BCne-&-nachhaltigen-lebenskonzepten-1258751751/)           | Jan 21, 11:47      |
|       644.04 |            37 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/tolle-stadtwohnung-924969067/)                                                                          | Jan 21, 11:19      |
|       508    |            48 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-im-prater-1728551727/)                                                            | Jan 20, 21:55      |
|       750    |            48 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/leopold-ernst-gasse---2-zimmer-neubau-mit-extra-einbauk%C3%BCche-876469462/)                           | Jan 20, 18:26      |
|       649    |            63 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/fenzlgasse---sanierungsbed%C3%BCrftiger-2-zimmer-altbau-mit-extra-k%C3%BCche-zu-vermieten-1354556248/) | Jan 20, 17:57      |
|       590    |            48 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-im-yppenviertel-1429826407/)                                                        | Jan 20, 17:47      |
|       754    |            32 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hofruhelage%21-kleine-2-zimmer-neubauwohnung-mit-terrasse-n%C3%A4he-u1%21-1846306708/)               | Jan 20, 15:27      |
|       797.22 |            48 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zauberhafte-hoflage-in-city-n%C3%A4he%21-2110358250/)                                          | Jan 20, 11:47      |
|       798.09 |            45 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/neubau-i-2-zimmer-i-besichtigung-am-freitag-den-23.1.26-von-15:30-bis-16:30-uhr%21-2057594491/)      | Jan 20, 11:36      |
