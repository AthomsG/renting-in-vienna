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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       698.3  |            47 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmerwohnung-2088954558/)                                                             | Nov 30, 12:25      |
|       798    |            59 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/f%C3%BCr-gr%C3%BCnliebhaber%21-2089992512/)                                                      | Nov 30, 09:19      |
|       650    |            51 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-in-1020-wien-zur-direktvergabe%3B-vormerkschein-vor-30.10.2025-1894184542/) | Nov 30, 09:11      |
|       700    |            64 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/helle-zweizimmer-altbau-wohnung-1329579191/)                                                  | Nov 29, 16:00      |
|       560    |            59 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/59-m%C2%B2-gemeindewohnung-nahe-wienerberg---vmk-31.10.2025-1331751878/)                       | Nov 29, 14:25      |
|       742.25 |            71 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/mautner-markhof-gasse---sanierter-2-zimmer-altbau-mit-extra-wohnk%C3%BCche-1579004510/)        | Nov 29, 13:14      |
