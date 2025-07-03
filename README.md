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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            49 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zi-wohnung---privat-ohne-provision-1400639826/)                                                                                                                | Jul 03, 02:35      |
|       615    |            60 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-direktvergabe-%28wohnticket-31.05.2025%29-mit-abl%C3%B6se-4.500%E2%82%AC-1657361863/)                                                                     | Jul 02, 23:45      |
|       408    |            56 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-1962386555/)                                                                                  | Jul 02, 20:40      |
|       790    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Aall-inklusive-apartment-schlafzimmer%2B-wohnzimmer%2A-n%C3%A4he-hauptbahnhof-2083203679/)                                                                      | Jul 02, 19:52      |
|       750    |            52 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-altbauwohnung-zum-wohlf%C3%BChlen-2015553389/)                                                                                                              | Jul 02, 19:01      |
|       798.75 |            51 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei:-ruhiger-51m%C2%B2-neubau-mit-2-zimmern-und-einbauk%C3%BCche---1170-wien-1147640200/)                                                                | Jul 02, 18:35      |
|       706.21 |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/dachterrassenhit-beim-hauptbahnhof-1458382214/)                                                                                                                   | Jul 02, 16:55      |
|       559    |            40 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/studentenwohnung-1549221320/)                                                                                                                                       | Jul 02, 16:36      |
|       750    |            36 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-top-zustand-in-cityn%C3%A4he-1488761917/)                                                                                                | Jul 02, 16:18      |
|       792.61 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sofortbezug-vollm%C3%B6blierte-spitzenneubauwohnung-n%C3%A4chst-u1---keplerplatz-1993574057/)                                                                     | Jul 02, 16:13      |
|       799    |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-gepflegte-singlewohnung-mit-parkblick---sofortbezug-1810488975/)                                                                                            | Jul 02, 16:07      |
|       795    |            54 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3.erdbergstrasse---provisionsfreie-charmante-2-zimmer-neubaumiete-direkt-beim-kardinal-naglplatz-2105617351/)                                               | Jul 02, 15:32      |
|       609    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wiener-wohnen-direktvergabe---top-gelegene-2-zimmer-wohnung-in-ruhiger-lage-%28abl%C3%B6se:-5.000%E2%82%AC---nur-mit-vormerkschein-bis-31.05.2025%29-1248968055/) | Jul 02, 14:03      |
|       771.38 |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-2-zimmer-wohnung-in-ruhelage-mit-einbauk%C3%BCche-und-durchdachter-raumaufteilung---jetzt-anfragen-1980415430/)                                          | Jul 02, 13:46      |
|       440    |            50 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-zu-vergeben---direktvergabe-ab-september-1779774064/)                                                                                                     | Jul 02, 12:45      |
|       770    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmerwohnung---neuwertig-1902617440/)                                                                                                                        | Jul 02, 10:19      |
|       599.01 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonniger-altbau---n%C3%A4he-hauptbahnhof-846622583/)                                                                                                              | Jul 02, 09:18      |
|       679    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/abl%C3%B6sefreie-neubauhauptmiete-mit-46-m%C2%B2-1748143719/)                                                                                                     | Jul 02, 08:22      |
|       750    |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/mietwohnung-in-gepflegtem-stilaltbau---bezugsfertig-&-hochwertig-ausgestattet---optional-vollm%C3%B6bliert%21-996023946/)                         | Jul 02, 07:23      |
