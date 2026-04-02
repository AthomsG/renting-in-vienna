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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       456.45 |            56 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-zur-weitergabe-1616985990/)                                                                                                               | Apr 02, 19:52      |
|       685.32 |            46 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ner-altbau---erstbezug%21-884547862/)                                                                                                     | Apr 02, 19:32      |
|       740    |            70 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/provisionsfreie-mietwohnung-direkt-vom-eigent%C3%BCmer-1386548229/)                                                                               | Apr 02, 18:34      |
|       607.37 |            62 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/direktvergabe-2-zimmer-gemeindewohnung-1050-wien-2114689505/)                                                                                    | Apr 02, 17:45      |
|       550    |            51 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-direktvergabe-wohnticket-bis-31.3.2026-1207947540/)                                                                      | Apr 02, 14:49      |
|       635    |            57 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-2-zimmer-gemeindewohung-direktvergabe-%28vormerkschein-28.2.2026%29-1835001146/)                                           | Apr 02, 11:15      |
|       616.95 |            58 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sonnige-2-zimmer-wohnung-%7C-sanierter-altbau-%7C-im-16.-bezirk-1368855960/)                                                                      | Apr 02, 10:17      |
|       500.73 |            49 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-2-zimmer-gemeindewohnung---direktvergabe-wohnticket-/-vormerkschein-31.03.2026-1548878851/)                                        | Apr 02, 07:51      |
|       780    |            50 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-wohnung-mit-garten-neubau-%2850m%C2%B2-%2B-30m%C2%B2-garten%29---voll-m%C3%B6bliert---kein-genossenschaftsanteil%21-1276499617/) | Apr 02, 00:25      |
|       780    |            61 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3-zimmer-wohnung-vis-a-vis-sch%C3%B6nbrunn-1719434252/)                                                                                             | Apr 01, 20:58      |
|       465    |            43 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-2-zimmer-sch%C3%B6n-%28m%C3%B6bliert%29-881720082/)                                                                               | Apr 01, 18:07      |
