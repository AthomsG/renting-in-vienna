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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       798.99 |            40 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumwohnungen-in-top-lage-zu-vermieten%21-1055837955/)                                                            | Nov 27, 09:48      |
|       782    |            43 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/tolle-2-zimmer-wohnung-in-absoluter-ruhelage-mit-sch%C3%B6nem-balkon-1756981113/)                                      | Nov 27, 09:47      |
|       599.44 |            55 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/erstbezug---betreutes-wohnen-%28ab-dem-60.-lebensjahr%29-in-1220-wien-1314226870/)                                  | Nov 27, 09:39      |
|       799    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1671560474/) | Nov 27, 08:26      |
|       799.33 |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-954325505/)  | Nov 27, 07:56      |
|       799.33 |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-968537777/)  | Nov 27, 07:54      |
|       799    |            38 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-2033089937/) | Nov 27, 07:46      |
|       691.33 |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%28reserviert%29-neubauwohnung-zu-vermieten%21-1644760517/)                                                        | Nov 26, 23:11      |
|       754    |            74 |          3 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-74m%C2%B2-2036269498/)                                                                             | Nov 26, 21:58      |
|       790    |            57 |          2 | 16. Ottakring   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-sch%C3%B6ne-wohnung-privat-zu-vermieten-1561778290/)                                                | Nov 26, 20:27      |
|       604    |            65 |          3 | 06. Mariahilf   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gemeindewohnung-direktvergabe-vormerkschein-bis-30.9.2024-2105592210/)                                               | Nov 26, 20:14      |
|       764.19 |            78 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmerwohnung-unbefristet-zu-mieten-1602204884/)                                                       | Nov 26, 19:33      |
|       740    |            75 |          2 | 11. Simmering   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/hauptmiethit-n%C3%A4he-enkplatz-1578235463/)                                                                         | Nov 26, 18:58      |
|       786.09 |            43 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/freundliche-helle-altbauwohnung-wg-geeignet---2-getrennte-schlafr%C3%A4ume-1298843722/)                              | Nov 26, 17:16      |
|       580.5  |            56 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-1210-wien---vormerkschein-nur-bis-31.10.24-953308908/)                                             | Nov 26, 16:21      |
|       790    |            41 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/top-2-zimmer-s%C3%BCd-balkonwohnung-in-ruhiger-gr%C3%BCnlage-1479201196/)                                              | Nov 26, 15:56      |
|       780    |            73 |          3 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/diektvergabe-nur-mit-vormerkschein-31.5.2024-renovierte-3-zimmer-wohnung-1548508489/)                              | Nov 26, 15:07      |
|       706.59 |            60 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-daschgescho%C3%9Fwohnung-in-ruhiger-lage-bei-sch%C3%B6nbrunn-858378955/)                                      | Nov 26, 14:47      |
|       799.01 |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-dachgeschoss-wohnung-in-top-lage---10.bezirk.---wohntraum-1706949546/)                                      | Nov 26, 13:49      |
|       750    |            46 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/helle-freundliche-2-zimmer-wohnung-nahe-der-donauinsel-1234991560/)                                                | Nov 26, 13:17      |
