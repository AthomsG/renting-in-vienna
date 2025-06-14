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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                               | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       499.86 |            44 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sanierte-altbauwohnung---1-zimmer-%2B-kabinett-in-ruhiger-lage-in-der-storkgasse-804393591/) | Jun 14, 10:24      |
|       420    |            56 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe.-gut-angebundene-gemeinde-wohnung.-vormerkschein-ab-april-2025-974498791/)        | Jun 14, 10:12      |
|       799    |            40 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/moderne-2-zimmerwohnung-in-u-bahn-n%C3%A4he-kendlerstra%C3%9Fe-985083550/)                    | Jun 14, 09:54      |
|       753.36 |            59 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%22charmante-2-zimmer-mietwohnung-nahe-barankapark-hellerwiese%21%22-1489050934/)             | Jun 14, 07:11      |
|       608.3  |            56 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/studentenwohnung-2119365089/)                                                                   | Jun 14, 01:17      |
|       770    |            74 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-direkt-vergabe-2048871461/)                                                   | Jun 13, 18:24      |
|       776.27 |            76 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-1245979740/)                                                    | Jun 13, 18:16      |
|       534.4  |            50 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-gemeindewohnung-direktvergabe-vormerkschein-bis-31.05.2025-2015094273/)        | Jun 13, 13:58      |
|       577.63 |            60 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-von-wiener-wohnen---direktvergabe-1717816944/)                               | Jun 13, 13:40      |
|       770    |            70 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/preishit%21-3-zimmer-wohnung%21-923100485/)                                                    | Jun 13, 11:56      |
