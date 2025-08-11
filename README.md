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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       643.01 |            44 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/erstbezug-nach-sanierung-top-lage-in-margareten-top-saniert%21-1718917399/)                                                                           | Aug 11, 20:39      |
|       768.43 |            33 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug---entz%C3%BCckende-2-zimmer-wohnung-mit-herrlicher-loggia-1685119282/)                                                                        | Aug 11, 20:34      |
|       749.56 |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sonnige-2-zimmer-wohnung%21-2097215139/)                                                                                                                | Aug 11, 15:26      |
|       551.19 |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-miete:-ger%C3%A4umiger-2-zimmer-altbau-1069097419/)                                                                                       | Aug 11, 12:39      |
|       626.2  |            59 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wiener-wohnen-direktvergabe-/-datum-bis-31.07.2025-f%C3%BCr-2-personen-1259349256/)                                                    | Aug 11, 10:30      |
|       719    |            70 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/1150-wien-pouhongasse:-extrem-ruhige-2-zimmer-albauwohnung-ca.-70-m2-im-hp-mit-eigenem-hofgarten-unbefristet-zu-vermieten-1821604346/) | Aug 10, 23:07      |
|       793.65 |            38 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/moderne-2-zimmerwohnung-i-100m-zur-u3-station-kendlerstra%C3%9Fe-1945735306/)                                                                          | Aug 10, 19:54      |
