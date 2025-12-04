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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                               | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       610    |            55 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2--zimmer-wohnung-zu-vermieten-777267007/)                                                     | Dec 04, 10:53      |
|       589    |            48 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/entz%C3%BCckender-altbau-am-lerchenfelder-g%C3%BCrtel%21-2132769919/)                         | Dec 04, 10:36      |
|       489    |            44 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-gemeindewohnung-1915511966/)                                                           | Dec 04, 09:33      |
|       494    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-gemeindewohnung---vormerkschein-bis-30.09.2025-ben%C3%B6tigt-1577136135/)      | Dec 04, 07:34      |
|       721.52 |            68 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeindebau-wohnung-im-gr%C3%BCnen---vormerkschein-vor-30.11.2024%21-1743175922/) | Dec 04, 06:45      |
|       770    |            45 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung%21-keine-anrufe---anfragen-nur-per-mail%21-857140441/)                 | Dec 04, 06:21      |
|       501.08 |            45 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/charmante-gemeinde-wohnung-nur-mit-%2Awohnticket%2A-867905440/)                              | Dec 04, 03:23      |
|       540    |            54 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung---vormerkschein-bis-30.09.2025-1528638569/)                          | Dec 03, 21:17      |
|       750    |            54 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmerwohnung-hoflage-n%C3%A4he-yppenplatz/-brunnenmarkt-1928697824/)                       | Dec 03, 20:21      |
|       750    |            55 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/herr-2036564056/)                                                                             | Dec 03, 20:06      |
|       627    |           nan |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/moderne-garconnieren-sowie-2-zimmer-apartments-in-zentraler-lage-in-altmannsdorf-1510995813/)  | Dec 03, 14:27      |
|       492    |            47 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-gemeindewohnung---vormerkschein-bis-vor-dem-30.11.2025-ben%C3%B6tigt-1863594071/)    | Dec 03, 13:49      |
|       680.01 |            52 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-2-zimmer-mietwohnung-.-komplett-neusaniert---ab-1.2.26-bezugsbereit-2058416114/) | Dec 03, 13:33      |
|       775    |            60 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sofortbezug---2er-wg-studenten-wohnung%21-1250127082/)                                        | Dec 03, 13:26      |
|       653    |            52 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-auf-der-thaliastra%C3%9Fe-1591829877/)                                       | Dec 03, 12:55      |
