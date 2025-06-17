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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       695    |            37 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung-mit-gr%C3%BCnblick-beim-hauptbahnhof-1384787170/)                         | Jun 17, 21:35      |
|       550    |            36 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierte-einzimmer-single-wohnung-n%C3%A4he-wienerberg-1231502913/)                                    | Jun 17, 20:39      |
|       684.03 |            78 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/entdecken-sie-ihre-traumwohnung-in-1100-wien---3-zimmer-78-m%C2%B2-zum-wohlf%C3%BChlen%21-1715544148/) | Jun 17, 15:57      |
|       621.35 |            61 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-gemeindewohnung-in-1100-wien-2053081859/)                                                | Jun 17, 15:34      |
|       771.81 |            32 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-mit-wohlf%C3%BChlfaktor---topmoderne-mietwohnung-nahe-u6-&-s-bahn-2012956530/)                | Jun 17, 14:18      |
|       649.8  |            51 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-dachgeschoss-am-dornerplatz-1957868661/)                                                             | Jun 17, 13:49      |
|       506    |            43 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-im-3.-bezirk-mit-vormerkschein-1067587977/)                                      | Jun 17, 13:04      |
|       449.36 |            30 |          3 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lager/atelier-zur-miete-in-1050-wien---ehemalige-wohnung-nahe-pilgramgasse-1798271816/)               | Jun 17, 09:57      |
|       770    |            46 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/mietwohnung-von-privat--provisionsfrei-1133204176/)                                                   | Jun 17, 08:58      |
|       786.51 |            56 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/25-zimmer-dachgeschosswohnung-in-ruhelage-mit-blick-ins-gr%C3%BCne-1306609130/)                         | Jun 17, 03:23      |
|       620    |            39 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/generalsanierte-wohnung-ruhige-zentrale-lage-1840102690/)                                              | Jun 16, 20:59      |
