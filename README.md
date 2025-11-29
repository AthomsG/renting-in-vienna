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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       560    |            59 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/59-m%C2%B2-gemeindewohnung-nahe-wienerberg---vmk-31.10.2025-1331751878/)                | Nov 29, 14:25      |
|       665.35 |            58 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/mautner-markhof-gasse---sanierter-2-zimmer-altbauwohnung-zu-vermieten-1655906548/)      | Nov 29, 13:24      |
|       742.25 |            71 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/mautner-markhof-gasse---sanierter-2-zimmer-altbau-mit-extra-wohnk%C3%BCche-1579004510/) | Nov 29, 13:14      |
|       792.86 |            54 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Abestausstattung%2A---sonniger-neubau-beim-antonspark-1136092440/)                    | Nov 29, 10:35      |
|       527    |            53 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-im-2.-bezirk-2-zimmer--direktvergabe-1640460069/)                    | Nov 29, 07:28      |
|       689.4  |            48 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/rennweg:-sanierte-2-zimmer-erdgescho%C3%9Fwohnung-1771312295/)                    | Nov 28, 20:38      |
|       633.09 |            49 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-altbauwohnung-in-ruhelage---menzelgasse-24-1160-wien-1694627972/)              | Nov 28, 17:21      |
