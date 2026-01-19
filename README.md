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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       791.33 |            55 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/s%C3%BCsse-ruhige-2-zimmer--paar--oder-singlewohnung---clemens-hofbauer-platz-unbefristet-1460699539/)                              | Jan 19, 15:46      |
|       636.02 |            59 |          3 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/direktvergabe-gemeindewohnung-2-zi-vmd-31.12.2025-%283-zimmer%29-1065644585/)                                                    | Jan 19, 13:14      |
|       748.82 |            39 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/orea-%7C-moderne-2-zimmer-wohnung-mit-guter-%C3%B6ffentlicher-anbindung-%7C-smart-besichtigen-%C2%B7-online-anmieten-1533109232/) | Jan 19, 11:28      |
|       771.63 |            76 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-direktvergabe-gemeindewohnung-3-zimmer-1147501768/)                                                              | Jan 19, 11:09      |
|       726.9  |            54 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-im-neubau-1958639844/)                                                                                           | Jan 19, 09:36      |
|       789.99 |            39 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/ab-april:-gek%C3%BChlte-neubauwohnungen-mit-freifl%C3%A4che-1452069177/)                                                    | Jan 18, 21:32      |
|       638.25 |            44 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-%2844-m%C2%B2%29-in-1160-wien---ab-februar-verf%C3%BCgbar-1379391555/)                                           | Jan 18, 20:06      |
