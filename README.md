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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       797.22 |            48 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zauberhafte-hoflage-in-city-n%C3%A4he%21-877100713/)                                                      | Jan 14, 09:40      |
|       675.26 |            49 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-2-zimmer-altbauwohnung-im-16.-bezirk-1094033331/)                                                   | Jan 14, 09:35      |
|       665.97 |            62 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnige-2-zimmer-gemeindewohnung-in-direktvergabe-vormerkschein-bis-31.10.2025-2048330628/)                     | Jan 14, 09:35      |
|       595.85 |            36 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/sch%C3%B6ne-2-zimmer-studentenhit-mit-terrasse%21-833437330/)                                                      | Jan 14, 09:16      |
|       578    |            55 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-wundersch%C3%B6ne-2-zimmer-wohnung-mit-balkon-1030-wien-%28direktvergabe%29-1305513076/) | Jan 13, 21:32      |
|       785    |            60 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sympathische-altbauwohnung-ideal-f%C3%BCr-single-oder-p%C3%A4rchen-2146719902/)                                   | Jan 13, 17:54      |
|       748.79 |            60 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmerwohnung-in-1140-zu-vermieten-1540126970/)                                                                 | Jan 13, 14:35      |
|       699.99 |            39 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/himbergerstra%C3%9Fe-28-1221994285/)                                                                            | Jan 13, 14:06      |
|       550    |            43 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/charmante-2--zimmerwohnung-n%C3%A4he-hanusch-krankenhaus-1169806665/)                                             | Jan 13, 12:17      |
|       518.64 |            41 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/schmuckst%C3%BCck-am-brunnenmarkt-1708858382/)                                                                  | Jan 13, 11:20      |
|       453    |            62 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe-1336262096/)                                                                       | Jan 13, 11:18      |
|       760    |            47 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wohnung-im-28.-stockwerk-%21-894119376/)                                                                  | Jan 13, 11:04      |
