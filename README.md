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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       700    |            36 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung---36-m%C2%B2---10.-bezirk-wien-1594294486/)                                                                                 | Mar 10, 11:56      |
|       789    |            45 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/top-ausgestattete-stylische-neubau-wohnung-1814489708/)                                                                                                    | Mar 10, 11:28      |
|       685.73 |            63 |          3 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-3-zimmer-altbauwohnung-in-der-heigerleinstra%C3%9Fe---achtung-gef%C3%B6rdert%21-1111503586/)                                                 | Mar 10, 10:53      |
|       799    |            42 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wundersch%C3%B6ne-2-zimmer-neubauwohnung-in-bahnhofsn%C3%A4he-1132521816/)                                                                                 | Mar 10, 09:58      |
|       690    |            42 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/apartment-zu-vermieten-1807428985/)                                                                                                                      | Mar 10, 09:06      |
|       605    |            28 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nahe-u1---modernes-wohnhaus-mitten-im-10.-974308535/)                                                                                                    | Mar 10, 08:47      |
|       433.42 |            52 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-2-zi-wohnung-beim-steinbauerpark-1989539279/)                                                                                                 | Mar 09, 14:29      |
|       799.92 |            39 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/smarte-2-zimmer-wohnung-nahe-reinprechtsdorfer-stra%C3%9Fe-in-1050-wien-zu-mieten-1213067568/)                                                          | Mar 09, 13:51      |
|       758.54 |            58 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ab-1.4.2026-bezugsfertig:-linzer-stra%C3%9Fe-111--ca.-58m%C2%B2-gro%C3%9Fe-2-zimmer-altbauwohnung-im-hochparterre-inkl.-heizung-%2B-warmwasser-883427708/) | Mar 09, 12:08      |
|       733.32 |            68 |          4 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sehr-sch%C3%B6ne-und-zentral-gelegene-4-zimmerwohnung-%28raumwunder%29-kommt-jetzt-zur-vermietung%21-852934101/)                                        | Mar 09, 11:51      |
