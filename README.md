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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       698    |            32 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/kompakte-2-zimmer-wohnung-%7Cmoderner-neubau-in-simmering-%7C-perfekte-lage-nahe-u3%21-%7C-verf%C3%BCgbar-ab-juli-964032191/)                                                                                    | Jul 16, 10:07      |
|       408    |            56 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-1524353480/)                                                                                                                                 | Jul 16, 06:20      |
|       792.38 |            72 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/voll-m%C3%B6blierte-2-zimmer-wohnung-im-herzen-von-simmering.-1125718979/)                                                                                                                                       | Jul 16, 01:22      |
|       480    |            44 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%28reserviert%29-zentrale-2-zimmer-gemeindewohnung-1696479005/)                                                                                                                                                     | Jul 15, 20:54      |
|       510    |            43 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/studentenwohnung-%281-zimmer-1-durchgangszimmer%29-1108675907/)                                                                                                                                                  | Jul 15, 18:29      |
|       743.53 |            70 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/eigenmittel-:-33.409075%E2%82%AC---mietwohnung-mit-kaufoption-nach-10-jahren-in-wien-11---eigenmittel:-33.40975-%E2%82%AC--3-zimmer-mit-6940-m%C2%B2-wohnfl%C3%A4che-%2B-472-m%C2%B2-loggia-im-1.-og-657097039/) | Jul 15, 15:30      |
|       445.72 |            45 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-30.06.2025-2-zimmer-1838038838/)                                                                                                                                 | Jul 15, 14:25      |
|       684.62 |            65 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet:-ger%C3%A4umiger-2-zimmer-altbau-nahe-matzleinsdorfer-platz-2103742800/)                                                                                                                             | Jul 15, 13:48      |
|       506    |            43 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-gemeindewohnung-im-3.-bezirk-mit-vormerkschein-1067587977/)                                                                                                                               | Jul 15, 13:04      |
|       776.27 |            76 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-1160590317/)                                                                                                                                                                       | Jul 15, 10:33      |
|       450    |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-in-wien-10:-nachmieter-gesucht-2147444393/)                                                                                                                                                     | Jul 15, 10:27      |
|       449.36 |            30 |          3 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lager/atelier-zur-miete-in-1050-wien---ehemalige-wohnung-nahe-pilgramgasse-1798271816/)                                                                                                                         | Jul 15, 09:57      |
