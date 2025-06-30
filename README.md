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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       458.79 |            47 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindebauwohnung-per-direktvergabe-1490919102/)                                                          | Jun 30, 23:51      |
|       694.61 |            60 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-nahe-u3-station-enkplatz-1316306778/)                                                      | Jun 30, 17:03      |
|       789    |            60 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ger%C3%A4umige-2-zimmerwohnung-in-gepflegtem-altbau%21-n%C3%A4he_schmelz%21-n%C3%A4he-u3-u6%21-2090857435/) | Jun 30, 15:57      |
|       765.87 |            47 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-nachmieter-gesucht-f%C3%BCr-wohnung-in-3er-bezirk---47m%C2%B2-948403138/)            | Jun 30, 13:37      |
|       670    |            65 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-vormerkschein-vor-05/2024-912697125/)                                     | Jun 29, 23:08      |
