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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       499    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-altbau-am-lerchenfelder-g%C3%BCrtel%21-852420906/)                                                               | Jan 17, 10:54      |
|       499    |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonniger-altbau-nahe-u1-keplerplatz-1300578245/)                                                                     | Jan 17, 10:54      |
|       758.61 |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/m%C3%B6blierte-2-zimmer-wohnung-im-15.bezirk%21-1083553328/)                                         | Jan 16, 17:25      |
|       717    |            65 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-2-zimmer-gemeindewohnung-1796436814/)                                                                  | Jan 16, 16:30      |
|       795    |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-%2A-wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1833355036/)                       | Jan 16, 15:18      |
|       787.74 |            63 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-entz%C3%BCckende-2-zimmerwohnung---n%C3%A4he-rennweg-795895808/)                              | Jan 16, 13:33      |
|       794.41 |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet:-2-zimmer-wohnung-in-oberlaa-mit-balkon-in-1100-wien-zu-mieten-1618815994/)                              | Jan 16, 12:46      |
|       604.83 |            58 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-%223-zimmer-gemeindewohnung---direktvergabe-%28vormerkschein-bis-30.11.2025%29-1170-wien-2030098717/) | Jan 16, 09:57      |
