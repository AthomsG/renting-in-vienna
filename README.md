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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       727.07 |            40 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/u6-spittelau-ums-eck--cityapartment-beim-unizentrum-1257655034/)                                                | Sep 17, 16:34      |
|       750    |            51 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-n%C3%A4he-reumanplatz-in-ruhelage-bei-park-1372722583/)                                                 | Sep 17, 16:26      |
|       680    |            44 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-n%C3%A4he-reumanplatz-in-ruhelage-bei-park-1346630798/)                                                 | Sep 17, 16:18      |
|       799.99 |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-k%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-hs17-top-a-11-856988592/) | Sep 17, 15:15      |
|       780    |            47 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmerwohnung-im-sonnwendviertel-2102028419/)                                                            | Sep 17, 13:17      |
|       792    |           nan |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnen-am-wienerberg---beste-lage-im-s%C3%BCden-von-wien-1474378946/)                                            | Sep 17, 11:57      |
|       700    |            71 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug-n%C3%A4he-spinnerin-am-kreuz-1820583343/)                                                              | Sep 17, 11:05      |
|       528.19 |            50 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-1896774458/)                                                                               | Sep 16, 16:50      |
