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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       684    |            58 |          2 | 08. Josefstadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/m%C3%B6blierte-2-zii-whng-im-1080-wien-08.-bezirk-josefstadt-924811115/)                                                        | Nov 14, 19:37      |
|       556.46 |            41 |          2 | 20. Brigittenau | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/unbefristete-terrassen-wohnung-in-der-ospelgasse-868547823/)                                                                   | Nov 14, 18:26      |
|       719    |            34 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---kirschbl%C3%BCtenpark---u1-n%C3%A4he-kagran---helle-hofseitige-ruhige-singlewohnung---provisionsfrei-1906948080/)   | Nov 14, 17:04      |
|       620    |            56 |          3 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-%7C-3-zimmer-nichtraucher-haushalt--keine-haustiere-sicherhetst%C3%BCr%7C-verhandelbar-805381675/) | Nov 14, 16:27      |
|       780    |            39 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/top-gepflegte-helle-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1654625958/)                                                   | Nov 14, 15:07      |
|       759    |            54 |          2 | 17. Hernals     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-2-zimmerwohnung-in-ruhiger-lage-787461412/)                                                                            | Nov 14, 14:57      |
|       749    |            36 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---sensationelle-ruhige-neubau-gartenwohnung-inklusive-komplettk%C3%BCche-1513762631/)                                | Nov 14, 14:06      |
|       749.62 |            61 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-altbauwohnung-1784266801/)                                                                                        | Nov 14, 13:17      |
|       799.05 |            65 |          2 | 18. Währing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/gersthof-/-helle-gepflegte-zwei-zimmerwohnung-2035811364/)                                                                    | Nov 14, 13:06      |
|       725    |            44 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-erstbezug-mit-kleinem-balkon-1162558783/)                                                                                    | Nov 14, 12:58      |
|       790    |            50 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sch%C3%B6ne-2-zimmer-wohnung-im-5.-bezirk-1482733504/)                                                                          | Nov 14, 12:57      |
|       746.09 |            44 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmerwohnung---nahe-der-alten-donau-1904170081/)                                                                    | Nov 14, 12:48      |
|       790    |            48 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohntraum-mit-balkon-im-viola-park-1011592335/)                                                                         | Nov 14, 11:58      |
|       790    |            47 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-im-viola-park-1566207186/)                                                                           | Nov 14, 11:51      |
|       750    |            57 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernisierte-2-zimmer-wohnung-in-direkter-u-bahn-und-fh-campus-n%C3%A4he-1740397186/)                                           | Nov 14, 11:16      |
|       799    |            44 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1325792396/)                                                       | Nov 14, 11:11      |
|       735    |            38 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1377855747/)                                                       | Nov 14, 11:11      |
|       765    |            44 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1633344682/)                                                       | Nov 14, 11:11      |
|       790    |            49 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/erstbezug%21-moderne-2-zimmer-wohnung-mit-balkon-1230948998/)                                                                  | Nov 14, 11:00      |
|       790    |            54 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/charmante-2-zimmer-dachgeschosswohnung-mit-zwei-terrassen-2069008596/)                                                         | Nov 14, 10:39      |
