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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       755    |            44 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/25-zimmer-wohnung-in-ruhiger-lage---besichtigungstermin-samstag-11.04.2026-um-15.00-1543570819/)                | Apr 08, 21:38      |
|       680    |            59 |          3 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-16.-bezirk-/-wohnticket-bis-31.03.2026-1295634505/)                                             | Apr 08, 20:58      |
|       550    |            54 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/geimeindewohnung-wohnticket-ab-1.3.2026-843488317/)                                                               | Apr 08, 20:50      |
|       726.09 |            36 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/neubauprojekt-hernals---bezugsfertig-mai-2026--hochwertige-mietwohnungen-%2Ainkl.-einbauk%C3%BCche%2A-914757157/) | Apr 08, 17:57      |
|       661.95 |            60 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/mietwohnung-n%C3%A4he-u3---simmeringer-hauptstrasse-1307686625/)                                                | Apr 08, 15:37      |
|       620    |            56 |          3 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeinde-wohnung-1023196875/)                                                                                   | Apr 08, 14:44      |
|       734.69 |            44 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung-in-1100-wien-1727491242/)                                                                | Apr 08, 14:38      |
|       730.25 |            60 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/nachmieter-gesucht:-ruhige-2-zimmer-wohnung-in-u3-n%C3%A4he-1482261904/)                                  | Apr 08, 13:27      |
|       765.66 |            56 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1042611871/)                                                                  | Apr 08, 02:32      |
