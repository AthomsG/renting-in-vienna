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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       793    |            56 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kompakte-mietwohnung-1147194543/)                                                                                                                                                                                                | Jul 17, 18:03      |
|       752.31 |            69 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/259-top-18---eigenmittel:-33.88030%E2%82%AC-3-zimmer-mietwohnung---6902-m%C2%B2-mit-kaufoption-nach-10-jahren-2040117542/)                                                                                                       | Jul 17, 16:22      |
|       755    |            61 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/helle-altbauwohnung-bei-der-berggasse%21-besichtigung-am-freitag-18.07.25-von-11:30-uhr-bis-12:00-uhr-vor-ort%21-hernalser-hptstr.-45/11-bitte-keine-anrufe%21%21-783631628/)                                                      | Jul 17, 14:47      |
|       680    |            56 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/11.lorystrasse---provisionsfreie-attraktive-2-zimmer-neubaumiete-nahe-der-u3-station-enkplatz-2139340009/)                                                                                                                       | Jul 17, 14:00      |
|       600    |            51 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-quellenplatz-2057567341/)                                                                                                                                                                                       | Jul 17, 13:18      |
|       490    |            47 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/studentenwohnung-895653533/)                                                                                                                                                                                                       | Jul 17, 12:17      |
|       450    |           140 |          5 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ein-helles-zimmer-mit-direktem-terrassenzugang-in-7-zimmer-studenten-wohngemeinschaft-mit-5-schlafzimmern-22-m%C2%B2-terrasse-f%C3%BCr-studentinnen-wg-geeignet-%281-k%C3%BCche-2-badezimmer-und-2-wcs%29-ab-sofort-1169882767/) | Jul 17, 11:38      |
|       715.01 |            53 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/unbefristete-2-zimmerwohnung-in-der-grasbergergasse-1567046850/)                                                                                                                                                           | Jul 17, 02:08      |
|       796    |            37 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/perfekte-stadtwohnung:-vollm%C3%B6bliert-direkt-bei-u4/-u6-l%C3%A4ngenfeldgasse-1927991345/)                                                                                                                                      | Jul 17, 00:15      |
|       640    |            62 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeinde-wohnung-ab-01.09.2025-beziehbar-1786055169/)                                                                                                                                                                      | Jul 16, 19:55      |
|       550    |            62 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-1255824861/)                                                                                                                                                                                       | Jul 16, 17:00      |
