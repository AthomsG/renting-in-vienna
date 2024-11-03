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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       764.57 |            50 |          3 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/p%C3%A4rchenhit-mit-fu%C3%9Fbodenheizung-und-deckenk%C3%BChlung---n%C3%A4he-schloss-neugeb%C3%A4ude-1155098675/)                    | Nov 03, 10:55      |
|       749.71 |            42 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                                     | Nov 03, 10:24      |
|       606    |            58 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-wohnung---direktvergabe-1968088608/)                                                                                      | Nov 03, 00:24      |
|       615    |            52 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinde-wohnung-direkt-vergabe-wien-1220-vormerkschein-ab-den-30.9.2024-2093421469/)                                              | Nov 02, 20:58      |
|       799    |            51 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-und-moderne-2-zimmer-wohnung-zwischen-keplerplatz-und-reumannplatz-1007128627/)                                               | Nov 02, 17:56      |
|       593.65 |            41 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/%28reserviert%29-15-zimmerwohnung-beim-augarten-1501033143/)                                                                      | Nov 02, 16:19      |
|       550    |            50 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnungsweitergabe-2-zimmer-wohnung----wohnticket-%28datum-egal%29-1307166663/)                                                     | Nov 02, 15:47      |
|       501    |            50 |          2 | 19. Döbling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gemeindebauwohnung-in-d%C3%B6bling---direktvergabe.-gr%C3%BCnruhelage-blick-in-weingarten-1940505380/)                           | Nov 02, 15:08      |
|       530    |            50 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-12.-bezirk-%28vmd-31.08.2024%29-1731146026/)                                                                         | Nov 02, 13:55      |
|       728.21 |            35 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wohnen-in-floridsdorf---2-zimmer-wohnung-mit-balkon-und-garagenplatz-n%C3%A4he-shopping-city-nord-&-klink-floridsdorf-844480360/) | Nov 02, 12:25      |
