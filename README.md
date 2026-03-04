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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       780    |            72 |          4 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zu-vergeben-786701094/)                                                            | Mar 04, 19:30      |
|       739.91 |            62 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gro%C3%9Fz%C3%BCgige-2-zimmer-wohnung-mit-balkon-in-1030-wien%21---ohne-k%C3%BCche%21-1790167449/) | Mar 04, 19:20      |
|       777.48 |            55 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/nette-zwei-zimmer-wohnung-981343712/)                                                                   | Mar 04, 16:39      |
|       774.13 |            56 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%7C-unbefristete-hauptmiete-verkehrsberuhigt-1161071281/)                                                | Mar 04, 14:39      |
|       594.92 |            58 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-gemeidewohnung-teilweise-m%C3%B6bliert-1100-wien-990034345/)                                    | Mar 04, 14:35      |
|       749    |            51 |          3 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionfrei%7Cmoderne-neubauwohnungen-mit-garten-balkon-oder-dachterrasse---1170-wien-1160729854/)       | Mar 04, 14:00      |
|       799.92 |            39 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/smarte-2-zimmer-wohnung-nahe-reinprechtsdorfer-stra%C3%9Fe-in-1050-wien-zu-mieten-1127836137/)          | Mar 04, 13:30      |
|       799.42 |            40 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/attraktive-15-zimmer-wohnung-nahe-reinprechtsdorfer-stra%C3%9Fe-in-1050-wien-zu-mieten-1518303665/)     | Mar 04, 13:28      |
|       466    |            47 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-wohnungs-weitergabe.-%28privat%29-904895341/)                                           | Mar 04, 13:11      |
|       713.96 |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/frisch-kernsanierte-traumwohnung-in-1100-wien---troststra%C3%9Fe-50-2012220144/)                         | Mar 04, 12:20      |
|       719    |            46 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-2-zimmer-mit-einbauk%C3%BCche-992411261/)                                                | Mar 04, 12:12      |
|       719    |            46 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-2-zimmer-mit-einbauk%C3%BCche-1455000206/)                                               | Mar 04, 12:11      |
|       429    |            41 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/unbefristete-2-zimmer-wohnung-im-3.-stock---n%C3%A4he-matzleinsdorfer-platz-1411447421/)                | Mar 04, 10:49      |
|       698.39 |            56 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/unbefristete-charmante-2-zimmer-wohnung-mit-lift-1936350499/)                                           | Mar 04, 10:46      |
|       770    |            70 |          4 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/direktvergabe-gemeindewohnung---4-zimmer-974582386/)                                                     | Mar 04, 10:17      |
|       765.66 |            56 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1042611871/)                                                           | Mar 04, 02:32      |
|       520    |            78 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-wohnung-wiener-wohnen-vormerkschein-vor-28.02.26-1492911126/)                                   | Mar 03, 23:23      |
