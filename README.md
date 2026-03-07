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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       612.43 |            42 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/42m2-wohnung-in-akh-n%C3%A4he-f%C3%BCr-alleinstehende-nichtraucher-ohne-haustiere-946929588/)                                       | Mar 07, 09:59      |
|       735.88 |            74 |          3 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/bitte-schriftlich-anfragen%21-top-gelegenheit%21-2.-stock.-optimale-p%C3%A4rchen--oder-singlewohnung.-u6-n%C3%A4he.-993966400/)    | Mar 07, 08:54      |
|       733.75 |            52 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/lichtdurchflutete-wohnung-nahe-dem-wienfluss-u4-unter-st.-veit---pure-freude-wartet.-1058198326/)                                   | Mar 07, 08:47      |
|       726.48 |            58 |          3 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2%E2%80%91zimmer%E2%80%91wohnung-1110-wien-%28simmering%29-1894990255/)                                                           | Mar 07, 02:34      |
|       601    |            56 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnungsweitergabe---gemeindewohnung-%28mit-vormerksschein%29-942472305/)                                                         | Mar 06, 21:08      |
|       740.01 |            40 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-2-zimmerwohnung-mit-loggia-im-3.-og---wohnen-im-wildgarten-1431162609/)                                                | Mar 06, 18:00      |
|       649    |            45 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-2088023474/)                                                                | Mar 06, 17:15      |
|       639    |            45 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-ruhige-wohnung-beim-neuen-landgut-2060577915/)                                                    | Mar 06, 17:11      |
|       779    |            34 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.5.2026---laxenburgerstra%C3%9Fe-151---1100-wien---traumhafte-neubau---singlewohnung-im-9ten-stock-mit-fernblick-1428023853/) | Mar 06, 12:37      |
|       799.9  |            48 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktive-2-zimmer-wohnung-nahe-wielandpark-in-1100-wien-zu-mieten-1998135453/)                                                  | Mar 06, 12:19      |
