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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       670.96 |            39 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/toplage/zentrum%21-unbefristete-extravagante-altbau-kleinwohnung-ca.-40-m2-2-zimmer%21-sofortbezug%21-1541874302/)     | Jun 03, 11:21      |
|       788.5  |            54 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-inkl.-gemeinschaftsinnenhof%21-2088895557/)                                            | Jun 03, 10:36      |
|       449.36 |            30 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lager/atelier-zur-miete-in-1050-wien---ehemalige-wohnung-nahe-pilgramgasse-1798271816/)                                | Jun 03, 09:57      |
|       695.17 |            59 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristeter-sofortbezug-in-der-fernkorngasse-1569563572/)                                                             | Jun 03, 08:46      |
|       795    |            46 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/perfekt-aufgeteilte-2-zimmer-wohnung-in-bahnhofsn%C3%A4he-1469641861/)                                                   | Jun 03, 03:20      |
|       750    |            35 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/schicke-singlewohnung-mit-weitblick-801346666/)                                                                           | Jun 02, 20:34      |
|       660    |            57 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zimmer-gemeindewohnung-per-direktvergabe---1090-wien-1405612803/)                                                    | Jun 02, 16:19      |
|       729.01 |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-mit-dachschr%C3%A4ge-inkl.-k%C3%BCche-dachterrasse-und-kellerabteil-/hs28-top-2-261-2003606817/) | Jun 02, 12:29      |
|       465.56 |            45 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/wohnvergabe-einer-2-zimmer-wohnung/-vormerkschein-bis-30.04.2025-1536679945/)                                        | Jun 02, 11:38      |
|       584    |            58 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe-gemeindewohnung---2-zimmer-58-m%C2%B2-zentral-2009746676/)                                                 | Jun 02, 11:11      |
|       790    |            62 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gr%C3%BCnblickwonung-1468236094/)                                                                                       | Jun 02, 10:43      |
