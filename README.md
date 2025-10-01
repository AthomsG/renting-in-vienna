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
|       786.03 |            69 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-dachgescho%C3%9Fwohnung-mit-loggia---1120-wien-erlgasse-21-23-1622952647/)                                                                          | Oct 01, 14:22      |
|       600    |            73 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-gemeinde-wohnung-direktvergabe-mit-wohnticket-bis-30.06.2024-1979581422/)                                                                                | Oct 01, 12:04      |
|       596.54 |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-sehr-gut-angebunden%21-872401726/)                                                                                                               | Oct 01, 10:48      |
|       699    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-getrennt-begehbar-2044045114/)                                                                                                                     | Oct 01, 08:06      |
|       670    |            65 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-vormerkschein-31.08.2024-979629484/)                                                                                          | Oct 01, 07:29      |
|       779    |            76 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/1150-wien-fenzlgasse-topsanierte-2-zimmer-altbautraumwohnung-ca.-76-m2-n%C3%A4he-u-3-johnstra%C3%9Fe-unbefristet-zu-vermieten-1928872453/)        | Oct 01, 01:23      |
|       625    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien-van-der-n%C3%BCllgasse:-2-zimmer-altbauwohnung-ca.-80-m2-unbefristet-und-barrierefrei-mit-lift-zu-vermieten-1509288671/)                                | Oct 01, 01:19      |
|       631.71 |            61 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3-zimmer-gemeinde-wohnung-direkvergabe-1318736054/)                                                                                                         | Sep 30, 20:48      |
|       503.96 |            50 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%28reserviert%29-bitte-vorerst-keine-anfragen-mehr:-wiener-wohnen-wohnung-zur-%C3%BCbergabe-mit-abl%C3%B6se.-nur-mit-g%C3%BCltigem-vormerkschein%21-1589324305/) | Sep 30, 19:46      |
|       560    |            52 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/direktvergabe-gemeindewohnung-mit-2-zimmern-%7C-5240m2-2088143233/)                                                                                                 | Sep 30, 17:48      |
|       502    |            44 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-gem%C3%BCtliche-2-zimmer-gemeindewohnung---voll-m%C3%B6bliert-&-sofort-bezugsbereit-1614813223/)                                                   | Sep 30, 16:01      |
|       620    |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/nachmieter-ab-november-f%C3%BCr-sch%C3%B6ne-wohnung-am-yppenplatz-1897388588/)                                                                                    | Sep 30, 13:32      |
|       700    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-und-gem%C3%BCtliche-2-zimmer-wohnung-in-zentraler-lage-800443582/)                                                                          | Sep 30, 13:19      |
|       650    |            34 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-01.11.---1100-wien---ansprechende-neubau-singlewohnung-inkl.-k%C3%BCchenzeile-mit-balkon-1734456149/)                                                          | Sep 30, 12:37      |
