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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       726    |           nan |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/in-besonders-attraktiver-lage---mitten-in-hetzendorf-922612754/)                                                                   | Jun 01, 16:44      |
|       660    |           nan |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/in-besonders-attraktiver-lage---mitten-in-hetzendorf-1432814629/)                                                                  | Jun 01, 16:44      |
|       550    |            20 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/attraktives-wohnen-in-wien-altmannsdorf---n%C3%A4he-u6%21-1925263450/)                                                             | Jun 01, 16:40      |
|       720.5  |           nan |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/mitten-in-meidling---nahe-schlo%C3%9F-sch%C3%B6nbrunn-1746520431/)                                                                 | Jun 01, 15:38      |
|       665.1  |            58 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet-zu-vermieten:-moderne-wohnung-%28soeben-saniert%29-mit-balkon-in-den-ruhigen-innenhof-in-zentraler-lage.-1343268788/) | Jun 01, 15:03      |
|       763.22 |            58 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gepflegte-ruhige-2-zimmer-wohnung-in-einer-sackgasse-872948615/)                                                                    | Jun 01, 14:09      |
|       570    |            49 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-gemeindewohnung-wohnticket-vor-dem-31.03.2026-780765775/)                                                     | Jun 01, 12:54      |
|       630    |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstsemestrige%21-whg-1100-wien-6-mo.-faire-selbstkosten-2048163870/)                                                             | Jun 01, 10:57      |
|       625    |            64 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-wien-direktvergabe-mit-vormerkschein-bis-31.01.2026-1563472132/)                                            | Jun 01, 09:19      |
|       517.25 |            51 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-helle-2-zimmer-gemeindewohnung-zur-direktvergabe-1796042197/)                                                      | Jun 01, 08:55      |
|       773.72 |            34 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/smarte-2-zimmer-wohnung-in-bester-lage---1050-wien%21-2040611311/)                                                               | Jun 01, 08:19      |
|       460    |            51 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sozialbau-genossenschaft-1805710689/)                                                                                             | Jun 01, 00:19      |
|       572    |            55 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-gemeindewohnung-im-11-bezirk-mit-ticket-nr-bis-30.04.2026-1749910300/)                                                   | May 31, 18:59      |
