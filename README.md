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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       675.72 |            47 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-47m%C2%B2-altbau-mit-2-zimmern-und-lift---1100-wien-793213928/)                                      | Apr 20, 13:38      |
|       779    |            38 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.6.2026---single-dachgescho%C3%9Fwohnung-mit-atemberaubenden-fernblick-im-11.-stock---laxenburger-stra%C3%9Fe-151-1953174300/) | Apr 20, 12:08      |
|       699    |            64 |          3 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-ruhige-3-zimmer-altbaumiete-n%C3%A4he-u4-station-unter-sankt-veit-960549132/)                                                  | Apr 20, 11:08      |
