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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       749.59 |            39 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage---1050-wien-2035304429/)                         | May 23, 16:19      |
|       781    |           nan |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mitten-im-10ten---zentral-und-ruhig-gelegen-1570323177/)                                         | May 23, 13:20      |
|       700    |            80 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wiener-wohnen-direktvergabe-%2831.05.2024%29-1581085253/)                                        | May 23, 12:02      |
|       732.39 |            52 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-vollsanierte-2-zimmer-wohnung-in-1100-wien---ideal-zum-wohlf%C3%BChlen%21-1607341800/) | May 23, 10:29      |
|       779    |            58 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-zentraler-lage-1470556842/)                   | May 23, 08:46      |
|       679    |            98 |          4 | 01. Innere Stadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1010-innere-stadt/zentraler-geht%27s-nicht:-wg-zimmer-im-1.-bezirk---stephansplatz-ums-eck-1484366376/)         | May 23, 08:34      |
|       716.97 |            45 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/moderne-2-zimmer-wohnung-im-17.%21-1315839104/)                                                    | May 22, 20:34      |
|       520    |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-auf-der-thaliastra%C3%9Fe-1831206262/)                                          | May 22, 15:33      |
|       799.99 |            38 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%2Atop-modern%2A---lichtdurchflutete-neubau-wohnung-mit-balkon-in-bester-lage-1019717868/)         | May 22, 15:16      |
