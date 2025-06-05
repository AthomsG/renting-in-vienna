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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       648    |            48 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-vogelsanggasse-zentrumsnahe-48m%C2%B2-altbauhauptmiete-3.-stock-%28kein-lift%29-studenten-bevorzugt%21-1737958667/) | Jun 05, 15:19      |
|       771.04 |            45 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-2-zimmer-wohnung-in-ruhelage-mit-einbauk%C3%BCche-und-durchdachter-raumaufteilung%21-1439961724/)                                                 | Jun 05, 15:18      |
|       729    |            38 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-komplettk%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-hs17-a-10-1809601339/)                                      | Jun 05, 13:17      |
|       780    |            60 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/charmante-2-zimmer-altbauwohnung-in-toplage---61-m%C2%B2-in-1030-wien-kundmanngasse-7-1072760404/)                                                   | Jun 05, 11:24      |
|       713.63 |            41 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/liechtensteinstra%C3%9Fe-114:-2-zimmer-wohnung-mit-kfz-stellplatz-988402127/)                                                                             | Jun 05, 11:22      |
|       692.75 |            62 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-direktvergabe-62m2-nur-mit-wohnticket-1746107864/)                                                                                         | Jun 05, 11:18      |
|       783.72 |            55 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-erstbezug-in-wundersch%C3%B6nem-gr%C3%BCnderzeithaus%21%21%21-1059214867/)                                                                        | Jun 05, 10:19      |
|       693    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-renovierte-neubauwohnung-hofseitig-1775181648/)                                                                                                     | Jun 04, 17:56      |
|       598.39 |            41 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/saniert-%2A%2A%2A-beim-kongressbad-und-s45-hernals-%2A%2A%2A-2-zimmer-wohnung-zur-untermiete-%2A%2A%2A-n%C3%A4he-hernalser-hauptstra%C3%9Fe-1821861626/)     | Jun 04, 16:16      |
|       520.25 |            47 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-nahe-matzleinsdorfer-pl.-nur-mit-g%C3%BCltigem-wiener-wohn-ticket-1980287901/)                                                            | Jun 04, 15:44      |
|       795    |            54 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3.erdbergstrasse---provisionsfreie-charmante-2-zimmer-neubaumiete-direkt-beim-kardinal-naglplatz-2105617351/)                                        | Jun 04, 15:32      |
