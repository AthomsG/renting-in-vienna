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
|       577.63 |            60 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-von-wiener-wohnen---direktvergabe-1717816944/)                                            | Jun 13, 13:40      |
|       770    |            70 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/preishit%21-3-zimmer-wohnung%21-923100485/)                                                                 | Jun 13, 11:56      |
|       618.63 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristeter-sofortbezug-in-der-fernkorngasse-1724781354/)                                                | Jun 13, 07:04      |
|       739.15 |            53 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/perfekte-stadtwohnung-n%C3%A4he-pilgramgasse-u4%21-br%C3%A4uhausgasse-17-19/1/13-1260268768/)             | Jun 13, 07:00      |
|       544.69 |            50 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-direktvergabe-vormerkschein28.02.2025-1358765607/)                                      | Jun 13, 06:44      |
|       710    |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/zentrale-altbauwohnung-mit-top-anbindung---zinckgasse-4-1150-wien-1620074606/)             | Jun 12, 19:58      |
|       777.57 |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-helle-gartenlage:-2-zimmer-wohnung-mit-gemeinschaftsgarten-nahe-des-liesingbachs-892704027/)        | Jun 12, 15:36      |
|       771.04 |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-2-zimmer-wohnung-in-ruhelage-mit-einbauk%C3%BCche-und-durchdachter-raumaufteilung%21-1439961724/) | Jun 12, 15:18      |
|       495    |            44 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeindewohnung-in-hernals-1074608622/)                                                                      | Jun 12, 12:18      |
