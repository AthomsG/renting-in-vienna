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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       627    |            60 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-wohnung-stilaltbau-/-wien-penzing-1091188673/)                                                                              | Mar 18, 18:25      |
|       522.44 |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-40m%C2%B2-altbau-mit-einbauk%C3%BCche-und-2-zimmern---1100-wien-1539934267/)                         | Mar 18, 18:17      |
|       665.97 |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-%28keine-neuen-anfragen-bitte%29-1139465513/)                                                                      | Mar 18, 14:38      |
|       550    |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-hofruhelage-550.---brutto-2-zimmer-im-herzen-von-wien-1346824438/)                                           | Mar 18, 13:52      |
|       778    |            56 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-1235451150/)                                             | Mar 18, 13:23      |
|       405    |           131 |          4 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/blueground-id501-alsergrund-1929024461/)                                                                                          | Mar 18, 13:06      |
|       729    |            35 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/rusi-%7C-top-1-zimmerwohnung-mit-balkon-%7C-simmering-%7C-top-27-1168799313/)                                                      | Mar 18, 12:32      |
|       697.29 |            58 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/am-migazziplatz-%2A%2A%2A-n%C3%A4he-u4/u6-station-%2A%2A%2A-separate-k%C3%BCchenzeile-%2A%2A%2A-beim-theresienbad/park-1515624338/) | Mar 18, 10:41      |
|       799    |            50 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/erstbezug-nach-renovierung-%21%21%21--sehr-sch%C3%B6ne-helle-2-zimmerwohnung---10-minuten-zur-innenstadt-1157683582/)              | Mar 18, 08:36      |
|       490    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-zu-vergeben-1586617689/)                                                                                           | Mar 18, 08:27      |
|       765.66 |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1042611871/)                                                                                     | Mar 18, 02:32      |
