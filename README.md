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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            49 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/charmantes-2-zimmer-apartent-1472643256/)                                                       | Mar 24, 14:17      |
|       511.63 |            38 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleinod-in-hofruhelage%21-1320031607/)                                                          | Mar 24, 14:17      |
|       799    |            60 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-bester-lage-797699213/)                        | Mar 24, 13:48      |
|       590    |            47 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zimmer-%7C-altbau-unbefristet-%7C-jahngasse-1755327006/)                                     | Mar 24, 12:58      |
|       500    |            50 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeinde-direktvergabe-1308026934/)                                                            | Mar 24, 12:17      |
|       650    |            57 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-gemeindewohnung-direktvergabe-wohnticket-bis-31.03.2025-896088690/)                    | Mar 23, 21:46      |
|       749.75 |            46 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-ruhige-2-zimmer-wohnung-951834229/)                                                         | Mar 23, 19:57      |
|       715    |            50 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/helle-2-zimmer-wohnung-n%C3%A4he-urban-loritz-platz-2141793084/)                                   | Mar 23, 19:10      |
|       625.08 |            35 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/charmante-2-zimmer-wohnung-ca.35m%C2%B2-im-beliebten-1030-wien%21-1640707380/)            | Mar 23, 17:09      |
|       799.92 |            39 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/smarte-2-zimmer-wohnung-nahe-reinprechtsdorfer-stra%C3%9Fe-in-1050-wien-zu-mieten-1213067568/) | Mar 23, 13:51      |
