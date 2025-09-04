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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       790    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/tichy-und-u1-ums-eck-963869023/)                                                                                                       | Sep 04, 13:57      |
|       580    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeindewohnung-1975359121/)                                                                                           | Sep 04, 13:35      |
|       767.7  |            60 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/sch%C3%B6ne-2-zimmer-altbauwohnung-in-1080-wien/-unbefristet-1197370105/)                                                             | Sep 04, 13:14      |
|       610.39 |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung-mit-balkon-in-favoriten-1180342387/)                                                                      | Sep 04, 13:09      |
|       526    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-wiener-wohnen-ticket-vom-30.06.2025-oder-%C3%A4lter-notwendig-1836958922/)                                             | Sep 04, 12:51      |
|       622.85 |            47 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-2-zimmer-altbauwohnung---47-m%C2%B2---unbefristet---1120-wien-%28erlgasse%29-1100792184/)                                     | Sep 04, 12:21      |
|       650    |            71 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-2-zimmer-wohnung-mit-balkon-in-1160-wien---voll-m%C3%B6bliert-nur-f%C3%BCr-bestimmte-sozialbaumieter.-1590924052/)         | Sep 04, 10:16      |
|       794.98 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stylische-2-zimmer-wohnung-renoviert-mit-hochwertiger-m%C3%B6blierung-1536551288/)                                                     | Sep 04, 07:04      |
|       590    |            46 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-vogelsanggasse-zentrumsnahe-46m%C2%B2-altbaumiete-1.-stock-studenten-bevorzugt%21-946167187/)   | Sep 04, 07:03      |
|       648    |            52 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/provisionsfrei-f%C3%BCr-den-mieter%21-laudongasse-zentrumsnahe-52m%C2%B2-altbaumiete-tiefparterre-studenten-bevorzugt%21-1424231066/) | Sep 04, 06:56      |
|       457.51 |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmer-wohnung-1922295801/)                                                                                                  | Sep 04, 06:48      |
|       783.57 |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-stilaltbauwohnung---hier-wohnen-sie-zentral-und-komfortabeln-%21-882078120/)                                                 | Sep 04, 03:52      |
|       560    |            55 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/3-zimmer-wohnung-mit-alles-drinen-1189217376/)                                                                                          | Sep 03, 21:48      |
|       680    |            38 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/1030-sch%C3%B6ne-zentrale-2-zimmer-singlewohnung-1294141984/)                                                                    | Sep 03, 17:31      |
|       740    |            55 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-2-zimmer-wohnung-n%C3%A4he-u4-station-unter-st.-veit-1542401214/)                                                                  | Sep 03, 13:12      |
