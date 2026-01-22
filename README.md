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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       497.76 |            44 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-1140-wien-1520414388/)                                                                     | Jan 22, 07:18      |
|       614    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-in-toplage-sucht-nachmieter/-in-1954878565/)                                            | Jan 21, 21:48      |
|       550    |           100 |          4 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/4-wg-zimmer-zu-vermieten-in-top-lage-direkt-bei-der-u4-margareteng%C3%BCrtel-1668848595/)                | Jan 21, 21:01      |
|       703    |            43 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-freundliche-2-zimmer-wohnung-1901751714/)                                                          | Jan 21, 19:46      |
|       750    |            45 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-2-zimmer-wohnung-in-zentraler-lage-mit-loggia-1377625052/)                              | Jan 21, 19:18      |
|       515    |            53 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wiener-wohnen-direktvergabe---sonnige-2-zimmer-wohnung-1100-wien---vormerkschein-31.12.2025-1227122289/) | Jan 21, 18:05      |
|       797.73 |            60 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-altbauwohnung-der-fernkorngasse-1438953571/)                                                | Jan 21, 17:56      |
|       424.95 |            40 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/direktvergabe---gemeinde-wohnung-nur-mit-g%C3%BCltigem-vormerkschein-1957774101/)                        | Jan 21, 15:55      |
|       770    |            56 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/schicke-mietwohnung-in-privater-jugendstil-villa-mit-zwei-zimmern-568557971/)                             | Jan 21, 15:42      |
|       780    |            47 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-2-zimmer-wohnung-in-oberlaa-%282-minuten-von-ubahn-station-u1-oberlaa%29-805535568/)        | Jan 21, 15:09      |
|       550    |            57 |          3 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/3-zimmer-wohnung-57m2-1415066868/)                                                                      | Jan 21, 13:45      |
|       542.39 |            35 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/exklusive-2-zimmer-wohnung-in-absoluter-bestlage-%28abl%C3%B6sesumme-beachten%21%29-797249892/)             | Jan 21, 11:31      |
