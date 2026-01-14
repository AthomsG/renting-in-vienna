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
|       754.36 |            62 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/miete-930--inkl.-heizung---2-zimmer-balkonwohnung-im-herzen-von-ottakring-ab-sofort---1655931210/)                | Jan 14, 09:47      |
|       754.36 |            62 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/miete-930--inkl.-heizung---2-zimmer-balkonwohnung-im-herzen-von-ottakring-ab-sofort---829397737/)                 | Jan 14, 09:47      |
|       797.22 |            48 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zauberhafte-hoflage-in-city-n%C3%A4he%21-877100713/)                                                      | Jan 14, 09:40      |
|       665.97 |            62 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnige-2-zimmer-gemeindewohnung-in-direktvergabe-vormerkschein-bis-31.10.2025-2048330628/)                     | Jan 14, 09:35      |
|       578    |            55 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-wundersch%C3%B6ne-2-zimmer-wohnung-mit-balkon-1030-wien-%28direktvergabe%29-1305513076/) | Jan 13, 21:32      |
|       785    |            60 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sympathische-altbauwohnung-ideal-f%C3%BCr-single-oder-p%C3%A4rchen-2146719902/)                                   | Jan 13, 17:54      |
|       748.79 |            60 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmerwohnung-in-1140-zu-vermieten-1540126970/)                                                                 | Jan 13, 14:35      |
|       791.28 |            44 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/bitte-nur-schriftliche-anfragen%21-ruhig-gelegene-2-zimmer-wohnung-in-der-laudongasse-1723789799/)             | Jan 13, 14:20      |
|       699.99 |            39 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/himbergerstra%C3%9Fe-28-1221994285/)                                                                            | Jan 13, 14:06      |
|       550    |            43 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/charmante-2--zimmerwohnung-n%C3%A4he-hanusch-krankenhaus-1169806665/)                                             | Jan 13, 12:17      |
