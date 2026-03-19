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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       780    |            72 |          4 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zu-vergeben-2007273524/)                                                                                                                                     | Mar 19, 15:27      |
|       492    |            60 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/direktvergabe-2-zimmer-gemeindewohnung-1160-wien-1480423959/)                                                                                                                      | Mar 19, 10:21      |
|       643.82 |            59 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-vormerkscheinnummer.-30.11.2025-2-zimmer-gemeindewohnung-%7C-59-m%C2%B2-%7C-balkon-%7C-frisch-renoviert-%7C-n%C3%A4he-u3-h%C3%BCtteldorfer-stra%C3%9Fe-1594803205/) | Mar 19, 10:02      |
|       669    |            60 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-altbau-beim-brunnenmarkt%21-1246458591/)                                                                                                                                         | Mar 19, 09:58      |
|       510.44 |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wiener-wohnen-wohnung-%28vormerkschein-vor-2026%29-1674937134/)                                                                                                    | Mar 19, 09:16      |
|       740.45 |            62 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%22altbau-stil-mietwohnung-nahe-sch%C3%B6nbrunn%27%27-1191996104/)                                                                                                                   | Mar 19, 08:37      |
|       774.95 |            50 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-anfragestopp--wohnung-im-3.-bezirk---nachmieter-gesucht-1422208806/)                                                                                        | Mar 19, 08:10      |
|       745.5  |            59 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/charmante-2-zimmer-wohnung-in-ruhiger-lage-des-17.-bezirks-1003645918/)                                                                                                              | Mar 19, 02:31      |
|       627    |            60 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-wohnung-stilaltbau-/-wien-penzing-1091188673/)                                                                                                                              | Mar 18, 18:25      |
