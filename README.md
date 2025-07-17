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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       600    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-quellenplatz-2057567341/)                                                                                                                                                                                       | Jul 17, 13:18      |
|       798.99 |            44 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/rusi-%7C-2-zimmerwohnung-in-ruhelage-%7C-erdw%C3%A4rmepumpe%7C-top-34-1268347468/)                                                                                                                                               | Jul 17, 12:34      |
|       490    |            47 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/studentenwohnung-895653533/)                                                                                                                                                                                                       | Jul 17, 12:17      |
|       450    |           140 |          5 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ein-helles-zimmer-mit-direktem-terrassenzugang-in-7-zimmer-studenten-wohngemeinschaft-mit-5-schlafzimmern-22-m%C2%B2-terrasse-f%C3%BCr-studentinnen-wg-geeignet-%281-k%C3%BCche-2-badezimmer-und-2-wcs%29-ab-sofort-1169882767/) | Jul 17, 11:38      |
|       715.01 |            53 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/unbefristete-2-zimmerwohnung-in-der-grasbergergasse-1567046850/)                                                                                                                                                           | Jul 17, 02:08      |
|       796    |            37 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/perfekte-stadtwohnung:-vollm%C3%B6bliert-direkt-bei-u4/-u6-l%C3%A4ngenfeldgasse-1927991345/)                                                                                                                                      | Jul 17, 00:15      |
|       640    |            62 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeinde-wohnung-ab-01.09.2025-beziehbar-1786055169/)                                                                                                                                                                      | Jul 16, 19:55      |
|       550    |            62 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-1255824861/)                                                                                                                                                                                       | Jul 16, 17:00      |
|       750    |            36 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-top-zustand-in-cityn%C3%A4he-1488761917/)                                                                                                                                                               | Jul 16, 16:18      |
|       719    |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-01.08.2025---gepflegte-neubau-singlewohnung-mit-balkon-1131123750/)                                                                                                                                                           | Jul 16, 16:08      |
|       798.92 |            52 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/langzeitnachmieter-gesucht-f%C3%BCr-2-zimmer-wohnung-in-1030-wien-%28n%C3%A4he-s-bahn-st.-marx%29-1826552353/)                                                                                                             | Jul 16, 15:44      |
|       749.05 |            45 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gepflegte-2-zimmer-wohnung-am-musilplatz-in-1160-wien-zu-mieten-2018251056/)                                                                                                                                                     | Jul 16, 15:28      |
|       633.42 |            57 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-m%C3%B6blierte-gemeindewohnung-1110-wien-%28direktvergabe%29-922247438/)                                                                                                                                        | Jul 16, 14:26      |
|       784.43 |            52 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gro%C3%9Fz%C3%BCgige-2-zimmer-wohnung-in-u-bahn-nahe-in-ottakring-zu-vermieten%21-1213902687/)                                                                                                                                   | Jul 16, 13:54      |
|       768    |            46 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/nachmiete-ab-august-f%C3%BCr-wg-taugliche-wohnung-mit-garten-1044614688/)                                                                                                                                                          | Jul 16, 12:13      |
