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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       779.56 |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/unbefristete-2-zimmer-wohung-n%C3%A4he-westbahnhof%21-847584301/)                                       | Mar 04, 12:28      |
|       667.75 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/frisch-kernsanierte-traumwohnung-in-1100-wien---troststra%C3%9Fe-50-2012220144/)                                        | Mar 04, 12:20      |
|       719    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-2-zimmer-mit-einbauk%C3%BCche-992411261/)                                                               | Mar 04, 12:12      |
|       719    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-2-zimmer-mit-einbauk%C3%BCche-1455000206/)                                                              | Mar 04, 12:11      |
|       670    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-dachgeschosswohnung-mit-zwei-terrassen-direktvergabe-gemeindewohnung-1150-wien-1415379847/)    | Mar 04, 12:09      |
|       429    |            41 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/unbefristete-2-zimmer-wohnung-im-3.-stock---n%C3%A4he-matzleinsdorfer-platz-1411447421/)                               | Mar 04, 10:49      |
|       698.39 |            56 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/unbefristete-charmante-2-zimmer-wohnung-mit-lift-1936350499/)                                                          | Mar 04, 10:46      |
|       770    |            70 |          4 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/direktvergabe-gemeindewohnung---4-zimmer-974582386/)                                                                    | Mar 04, 10:17      |
|       675    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnige-singlewohnung-nahe-wienerberg-961368284/)                                                                       | Mar 04, 08:20      |
|       765.66 |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1042611871/)                                                                          | Mar 04, 02:32      |
|       520    |            78 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-wohnung-wiener-wohnen-vormerkschein-vor-28.02.26-1492911126/)                                                  | Mar 03, 23:23      |
|       462    |            47 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-zu-vermieten-2114036713/)                                                                                 | Mar 03, 19:00      |
|       794.99 |            38 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/diesterweggasse---2-zimmer-neubau-mit-garage-zu-vermieten-1343640298/)                                                    | Mar 03, 18:06      |
|       573.7  |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-2-zimmer-gemeindewohnung-am-wienerberg%21-vormerkschein-bis-31.12.2025-1159323993/)                    | Mar 03, 14:11      |
|       489    |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe---2-zimmer-%28vormerkschein-/-wohnticket-erforderlich%29-1657265674/)                      | Mar 03, 14:07      |
|       649    |            45 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-1355374634/)                                                      | Mar 03, 14:06      |
|       799    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---charmante-2-zimmer-wohnung-mit-sonnigem-balkon---ihre-wohlf%C3%BChloase-am-laaer-berg-1406445669/)         | Mar 03, 13:32      |
|       729    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-einbauk%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-hs17-top-a-15-2058325697/) | Mar 03, 12:58      |
|       590    |            75 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wg---mitbewohnerin-gesucht-1279290233/)                                                                                 | Mar 03, 12:00      |
