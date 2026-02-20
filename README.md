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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       795    |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/herzgasse---2-zimmer-neubau-mit-2-loggien-und-garage-1927940269/)                                                                 | Feb 20, 18:55      |
|       789.9  |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauhit-mit-terrasse-und-garagenstellplatz-1538432248/)                                                                | Feb 20, 16:20      |
|       795    |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-%2A-wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1833355036/)                                    | Feb 20, 15:18      |
|       576.81 |            44 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charmante-1-zimmer-wohnung-mit-wohnk%C3%BCche----sechshauserstra%C3%9Fe-1056602696/)                              | Feb 20, 12:57      |
|       779    |            34 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.5.2026---laxenburgerstra%C3%9Fe-151---1100-wien---traumhafte-neubau---singlewohnung-im-9ten-stock-mit-fernblick-1428023853/) | Feb 20, 12:37      |
|       750.3  |            38 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliches-m%C3%B6bliertes-apartment-in-innenstadtn%C3%A4he---miete-f%C3%BCr-maximal-6-monate%21-983556905/)               | Feb 20, 12:18      |
|       730    |            57 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-gepflegte-neubauwohnung-1557947533/)                                                                                            | Feb 20, 10:49      |
|       545    |            60 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-zur-direktvergabe..%21-mit-balkon-kein-aufzug..%21-951633321/)                                                     | Feb 19, 19:10      |
