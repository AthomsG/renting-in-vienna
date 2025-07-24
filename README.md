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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       793    |            56 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kompakte-mietwohnung-1147194543/)                                                                                                          | Jul 24, 18:03      |
|       722    |            45 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/45m2-vollm%C3%B6blierte-zweizimmer-wohnung-f%C3%BCr-2-%28wz-k%C3%BCche-vz-gard-bad-wc%29-wien-10-reumannplatz-sofort-beziehbar-582002678/) | Jul 24, 16:33      |
|       765    |            58 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/ruhige-2-zimmer-wohnung-im-herzen-des-3.-bezirks-2071176512/)                                                                        | Jul 24, 16:25      |
|       560    |            52 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%28reserviert%29-gemeindebauwohnung-am-bacherplatz---nur-mit-vormerkscheindatum-30.06.2025-%21%21-1219672089/)                            | Jul 24, 15:50      |
|       767.5  |            58 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/super-neubauwohnung-%28-2-zimmer-%29---direkt-bei-der-u1-altes-landgut%21-%21-897482324/)                                                  | Jul 24, 14:47      |
|       550    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung---50-m%C2%B2-inkl-balkon-und-kellerabteil-1065277817/)                                                            | Jul 24, 14:16      |
|       680    |            56 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/11.lorystrasse---provisionsfreie-attraktive-2-zimmer-neubaumiete-nahe-der-u3-station-enkplatz-2139340009/)                                 | Jul 24, 14:00      |
|       749.5  |            45 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-freundliche-single--oder-p%C3%A4rchenwohnung-1842362956/)                                                                            | Jul 24, 13:26      |
|       729.16 |            55 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/n%C3%A4he-allianz-stadion:-praktische-2-zimmer-altbau-wohnung-ca.-55qm-unbefristet-2130614150/)                                              | Jul 24, 09:27      |
|       795    |            33 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neubau-in-massivholzbauweise-2145216787/)                                                                                                   | Jul 24, 02:27      |
|       797.48 |            36 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmerwohnung-innenhoflage-mit-perfekter-infrastruktur-1549811136/)                                                              | Jul 24, 00:40      |
|       670    |            65 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-1372172298/)                                                                                             | Jul 23, 22:05      |
|       550    |            62 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-1255824861/)                                                                                                 | Jul 23, 17:00      |
|       519    |            48 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeinde-wohnung-vormerkschein-30.06.2025-1276953658/)                                                                         | Jul 23, 16:44      |
|       457.68 |            43 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeindewohnung:-2-zimmer-%7C-43-m%C2%B2-%7C-1140-hugo-breitner-hof-%7C-wiener-wohn-ticket-1398510386/)                        | Jul 23, 16:26      |
