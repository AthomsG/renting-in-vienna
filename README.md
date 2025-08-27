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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       610.5  |            58 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nette-altbauwohnung-teilm%C3%B6bliert-908509807/)                                                                                                  | Aug 27, 14:08      |
|       560    |            45 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-mit-balkon-in-gr%C3%BCnruhelage-45-m2-2039233073/)                                                                                 | Aug 27, 11:52      |
|       547.23 |            50 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung%21-vormerkschein-bis-30.06.2025-direktvergabe-2066783541/)                                                                         | Aug 26, 19:08      |
|       750    |            30 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%2Asmarte-2-zimmer-kleinwohnung%2A---neubau-in-sch%C3%B6nbrunn-n%C3%A4he-1317407432/)                                                                | Aug 26, 16:55      |
|       670    |            66 |          2 | 06. Mariahilf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/%28keine-anfragen-werden-mehr-angenommen%29-65m2-n%C3%A4he-mariahilferstra%C3%9Fe-%28vormerkschein-wiener-wohnen%29-u-bahn-u2-u3-&-u4-1746488452/) | Aug 26, 13:34      |
