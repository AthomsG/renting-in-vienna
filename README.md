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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       445    |            44 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-gemeinde-wohnung-vormerkschein-f%C3%BCr-2-zimmer-wird-ben%C3%B6tigt-1850141907/)                            | Mar 24, 18:39      |
|       768.32 |            51 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/s%C3%BCdlich-ausgerichtete-2---zimmer-wohnung-inkl.-neuer-einbauk%C3%BCche-mit-optimaler-infrastruktur-853684235/) | Mar 24, 17:16      |
|       659    |            48 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-1429033026/)                                               | Mar 24, 16:13      |
|       750    |            49 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/charmantes-2-zimmer-apartent-1472643256/)                                                                          | Mar 24, 14:17      |
|       511.63 |            38 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleinod-in-hofruhelage%21-1320031607/)                                                                             | Mar 24, 14:17      |
|       799    |            60 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-bester-lage-797699213/)                                           | Mar 24, 13:48      |
|       500    |            50 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeinde-direktvergabe-1308026934/)                                                                               | Mar 24, 12:17      |
|       650    |            57 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-gemeindewohnung-direktvergabe-wohnticket-bis-31.03.2025-896088690/)                                       | Mar 23, 21:46      |
