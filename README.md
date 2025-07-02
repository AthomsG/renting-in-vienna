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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       609    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wiener-wohnen-direktvergabe---top-gelegene-2-zimmer-wohnung-in-ruhiger-lage-%28abl%C3%B6se:-5.000%E2%82%AC---nur-mit-vormerkschein-bis-31.05.2025%29-1248968055/) | Jul 02, 14:03      |
|       771.38 |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-2-zimmer-wohnung-in-ruhelage-mit-einbauk%C3%BCche-und-durchdachter-raumaufteilung---jetzt-anfragen-1980415430/)                                          | Jul 02, 13:46      |
|       440    |            50 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-zu-vergeben---direktvergabe-ab-september-1779774064/)                                                                                                     | Jul 02, 12:45      |
|       770    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmerwohnung---neuwertig-1902617440/)                                                                                                                        | Jul 02, 10:19      |
|       599.01 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonniger-altbau---n%C3%A4he-hauptbahnhof-846622583/)                                                                                                              | Jul 02, 09:18      |
|       679    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/abl%C3%B6sefreie-neubauhauptmiete-mit-46-m%C2%B2-1748143719/)                                                                                                     | Jul 02, 08:22      |
|       750    |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/mietwohnung-in-gepflegtem-stilaltbau---bezugsfertig-&-hochwertig-ausgestattet---optional-vollm%C3%B6bliert%21-996023946/)                         | Jul 02, 07:23      |
|       799.95 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gut-geschnittene-2-zimmerwohnung-mit-balkon_t15_buchengasse-128-1086524763/)                                                                                      | Jul 02, 06:55      |
|       790    |            65 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-und-sanierte-dachgeschosswohnung-mit-einbauk%C3%BCche-939130851/)                                                                                           | Jul 01, 21:14      |
|       750    |            57 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnige-wohnung-mit-gr%C3%BCnblick-1763965927/)                                                                                                                     | Jul 01, 16:21      |
|       506    |            43 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-gemeindewohnung-im-3.-bezirk-mit-vormerkschein-1067587977/)                                                                                | Jul 01, 13:04      |
