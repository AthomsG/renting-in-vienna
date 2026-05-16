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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|          799 |            65 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/stilaltbau/unbefristet/u3-n%C3%A4he:-65-m2-2-getrennte-zimmer-einbauk%C3%BCche-wannenbad-gesamtmiete-799---997910101/)                                                  | May 16, 10:52      |
|          598 |            46 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-f%C3%BCr-den-mieter%21-huglgasse-n%C3%A4chst-u3-altbaumiete-46m%C2%B2-%C3%A4ltere-komplettk%C3%BCche-studenten-bevorzugt%21-1608295625/) | May 15, 21:42      |
|          799 |            29 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionfrei%7Cmoderne-neubauwohnungen-mit-balkon---1170-wien-1717414396/)                                                                                               | May 15, 20:58      |
|          740 |            53 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-1087438091/)                                                                                                      | May 15, 17:01      |
|          620 |            44 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-&-unbefristet%21-wohnung-bei-der-stadthalle%21-1380336761/)                                                                              | May 15, 16:58      |
|          799 |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-neu-saniert%21-ruhige-wohnung-beim-neuen-landgut-2025956945/)                                                                           | May 15, 16:54      |
|          799 |            60 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-bester-lage-1551999133/)                                                                                               | May 15, 16:53      |
|          650 |            33 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charmante-1.5-zimmer-wohnung-1028384064/)                                                                                                               | May 15, 16:46      |
