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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       770    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmerwohnung---neuwertig-1902617440/)                                                                                                | Jul 02, 10:19      |
|       599.01 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonniger-altbau---n%C3%A4he-hauptbahnhof-846622583/)                                                                                      | Jul 02, 09:18      |
|       679    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/abl%C3%B6sefreie-neubauhauptmiete-mit-46-m%C2%B2-1748143719/)                                                                             | Jul 02, 08:22      |
|       750    |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/mietwohnung-in-gepflegtem-stilaltbau---bezugsfertig-&-hochwertig-ausgestattet---optional-vollm%C3%B6bliert%21-996023946/) | Jul 02, 07:23      |
|       799.95 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gut-geschnittene-2-zimmerwohnung-mit-balkon_t15_buchengasse-128-1086524763/)                                                              | Jul 02, 06:55      |
|       469    |            40 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/singlewohnung-in-erdberg-1652348617/)                                                                                               | Jul 01, 23:05      |
|       790    |            65 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-und-sanierte-dachgeschosswohnung-mit-einbauk%C3%BCche-939130851/)                                                                   | Jul 01, 21:14      |
|       750    |            57 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnige-wohnung-mit-gr%C3%BCnblick-1763965927/)                                                                                             | Jul 01, 16:21      |
|       770    |            54 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmerwohnung-in-sehr-guter-lage---provisionsfrei-182188908/)                                                                     | Jul 01, 13:52      |
|       506    |            43 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-gemeindewohnung-im-3.-bezirk-mit-vormerkschein-1067587977/)                                                        | Jul 01, 13:04      |
|       658    |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/u1-reumannplatz-ruhelage-1465529337/)                                                                                                     | Jul 01, 11:55      |
|       588.5  |           nan |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernes-wohn--und-gesch%C3%A4ftshaus-1113050000/)                                                                                        | Jul 01, 11:26      |
|       781.12 |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mi%28e%29tten-in-oberlaa:-erstklassige-2-zimmer-wohnung-mit-balkon-in-1100-wien-unbefristet-zu-mieten-2048175240/)                        | Jul 01, 10:56      |
|       743.12 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mi%28e%29tten-in-oberlaa:-unbefristete-2-zimmer-wohnung-mit-balkon-in-1100-wien-zu-mieten-1738186178/)                                    | Jul 01, 10:54      |
