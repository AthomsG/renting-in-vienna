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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       737.36 |            70 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28direktvergabe%29-2-1/2-zimmer-gemeindewohnung-in-1110-wien-2014515130/)                   | Dec 18, 02:29      |
|       620    |            44 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmerwohnung-neuwertig-832315432/)                                                  | Dec 17, 15:26      |
|       495    |            48 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-gut-gelegene-sanierte-2-zimmer-wohnung-mit-parkblick-1578971979/)                      | Dec 17, 15:18      |
|       790    |            65 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/altbau-wohnung-mit-3-zimmern-2100330588/)                                                    | Dec 17, 14:12      |
|       565.38 |            44 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/loggiawohnung-3ter-liftstock-gr%C3%BCnruhelage-provisionsfrei-1515903868/)                   | Dec 17, 10:21      |
|       590    |            36 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/%28reserviert%29-kleine-wohnung-in-1060-wien---ruhige-lage-mit-weitblick-1979970070/)        | Dec 17, 10:10      |
|       790    |            48 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zauberhafte-hoflage-in-city-n%C3%A4he%21-877100713/)                                   | Dec 17, 09:40      |
|       731.5  |           nan |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/moderne-garconnieren-sowie-2-zimmer-apartments-in-zentraler-lage-in-altmannsdorf-2070877509/) | Dec 17, 08:56      |
