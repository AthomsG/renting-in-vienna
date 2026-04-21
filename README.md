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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       595    |            37 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/zweitbezug---top-2-zimmer-in-gepflegtem-stilaltbau-nahe-margaretenplatz-1600061403/)                                                   | Apr 21, 10:38      |
|       725    |            54 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ruhige-helle-&-perfekt-geschnittene-2-zimmer-wohnung-mit-loggia-in-top-zustand---voll-m%C3%B6bliert-sofort-bezugsfertig%21-1190541972/) | Apr 20, 19:40      |
|       760    |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-n%C3%A4he-u1-keplerplatz-1485414725/)                                                                                  | Apr 20, 19:06      |
|       620    |            45 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/sofort-bezugsfertige-ruhige-helle-2-zimmer-wohnung-45m2-von-privat-1786157741/)                                                      | Apr 20, 18:26      |
|       681.36 |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-50m%C2%B2-altbau-mit-2-zimmern---1100-wien-1175726842/)                                                   | Apr 20, 18:07      |
|       719    |            35 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.6.2026---laxenburger-stra%C3%9Fe-151---moderne-2-zimmer-singlewohnung-mit-westseitigem-balkon-im-7.-stock-1501777131/)             | Apr 20, 18:06      |
|       799.13 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-wohnung-mit-balkon-1777345926/)                                                                                        | Apr 20, 17:15      |
|       799    |            45 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-2---zimmer-wohnung-/-n%C3%A4he-bahnhof-wien-meidling-1010736709/)                                                            | Apr 20, 15:48      |
|       779    |            38 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.6.2026---single-dachgescho%C3%9Fwohnung-mit-atemberaubenden-fernblick-im-11.-stock---laxenburger-stra%C3%9Fe-151-1953174300/)      | Apr 20, 12:08      |
