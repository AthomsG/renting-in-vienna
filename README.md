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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       700    |            63 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-in-gr%C3%BCnlage-und-trotzdem-zentral-1525226988/)                                      | Jun 10, 13:42      |
|       714.79 |            72 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/altbauwohnung-in-der-m%C3%A4rzstrasse-1523526229/)                                         | Jun 10, 11:41      |
|       610.58 |            58 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-gemeindewohnung-im-11.-bezirk-/5880m2---vormerkung-31.05.2026-1991556882/)                        | Jun 10, 10:01      |
|       765.66 |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1042611871/)                                                             | Jun 10, 02:32      |
|       557.83 |            37 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/unbefristete-altbau-single-wohnung-beim-kongresspark-1316605813/)                                            | Jun 09, 17:25      |
|       750    |            33 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/charmante-2-zimmer-altbauwohnung-mit-einbauk%C3%BCche-in-1140-wien---3285m%C2%B2---750eur-miete-1487828651/) | Jun 09, 17:06      |
|       682    |            87 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1160-direktvergabe-1834363660/)                                                            | Jun 09, 16:50      |
|       795.29 |            32 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-2-zimmer-wohnung-1553179949/)                                                                    | Jun 09, 14:21      |
|       700    |            48 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wir-vermieten-unsere-2-zimmer-wohnung-zur-kurzzeitmiete-vom-15.06.-bis-31.07-1621845201/)                    | Jun 09, 12:10      |
