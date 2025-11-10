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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       776.15 |            60 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/2-zimmerwohnung-n%C3%A4he-hauptbahnhof-mit-lft-1335941128/)                                                                                | Nov 10, 21:32      |
|       720    |            37 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleine-2-zimmer-wohnung%3B-ruhig-und-saniert%3B-direkt-vom-eigent%C3%BCmer-1962179811/)                                                 | Nov 10, 17:24      |
|       703.25 |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnen-in-perfekter-lage/n%C3%A4he-reumannplatz-u1-804204471/)                                                                          | Nov 10, 17:07      |
|       630    |            74 |          4 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeindewohnung-4-zimmer.-vms-31.08.2019-794727114/)                                                                    | Nov 10, 16:30      |
|       632.5  |            53 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-sanierte-singlewohnung-im-haus-mit-lift-1731795990/)                                                                        | Nov 10, 12:24      |
|       749.5  |            49 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/neu%21-2-zimmer-altbauwohnung-im-nibelungenviertel-zu-vermieten%21-1150-wien%21-kein-lift%21-1835305571/)               | Nov 10, 11:57      |
|       759.99 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-vollsanierte-2-zimmer-wohnung-in-1100-wien---ideal-zum-wohlf%C3%BChlen%21-1554200138/)                                        | Nov 10, 10:56      |
|       799    |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/u3-zippererstrasse/-wg-eignung:-unbefristete-53-m2-altbaumiete-2-getrennte-zimmer-einbauk%C3%BCche-gesamtmiete-eur-799---1011752530/)   | Nov 10, 09:52      |
|       555.17 |            50 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/1030-wien-direktvergabe-gemeindewohnung-%28wr.-wohnen%29.-vormerkschein-mit-vormerkdatum-30.09.2025-vorausgesetzt%21-1895049425/) | Nov 10, 09:49      |
|       749    |            82 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gro%C3%9Fz%C3%BCgige-3-zimmerwohnung-9-monate-befristete-07/2026-untermiete-/-wg-geeignet-1425732077/)                                    | Nov 09, 20:49      |
