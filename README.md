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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       617.65 |            49 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/geniale-2-zimmerwohnung-im-obersten-stock-mit-lift-906423290/)                                                           | Mar 03, 09:20      |
|       540    |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-sozialbau-%28nur-mit-berechtigung-f%C3%BCr-sozialbau%29-wohnung-in-1100-wien-802171179/)                         | Mar 02, 22:00      |
|       730    |            55 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/charmante-wohnung-zwischen-augarten-und-donaukanal-1112544464/)                                                        | Mar 02, 21:19      |
|       794.25 |            41 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-neubauwohnung-mit-gro%C3%9Fem-balkon---2.-og-1021396370/)                                                | Mar 02, 18:36      |
|       720.89 |            46 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-ab-mai:-m%C3%B6bliertes-all-in-2-zimmer-apartment-im-2.-bezirk-nahe-wu-&-sfu-%7C-xl-bude-1177987177/) | Mar 02, 16:25      |
|       700    |            36 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfreie-2-zimmer-mietwohnung-1150-wien-1589208759/)                                               | Mar 02, 16:00      |
|       616    |           nan |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/der-weitblick-von-den-dachterrassen-begeistert-1110138449/)                                                                | Mar 02, 15:51      |
|       625.17 |            35 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%2Akleinod-in-hofruhelage%2A-1824059805/)                                                                                    | Mar 02, 14:32      |
|       770    |           nan |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktives-wohnen-mitten-im-sonnwendviertel-1413322736/)                                                                 | Mar 02, 14:26      |
|       656.14 |            62 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/preiswerte-3---zimmer-wohnung-1724211282/)                                                                                | Mar 02, 14:15      |
|       799    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmerwohnung-im-viola-park-mit-balkon-1540017392/)                                                                     | Mar 02, 12:45      |
|       627.39 |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/mietwohnung-2-zimmer-felberstrasse-1781811272/)                                                           | Mar 02, 12:21      |
|       706.31 |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/57m%C2%B2-2-zimmer-wohnung-/-n%C3%A4he-hauptbahnhof-825536035/)                                                           | Mar 02, 11:24      |
|       750    |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wohnen-bei-der-mariahilfer-stra%C3%9Fe--balkon-ruhelage-provisionsfrei-1521716295/)                       | Mar 02, 10:30      |
|       769    |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/himbergerstra%C3%9Fe-28-1671001280/)                                                                                      | Mar 02, 10:17      |
