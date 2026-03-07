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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       490    |            47 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-mietwohnung-882752895/)                                                                                                 | Mar 07, 17:58      |
|       702.38 |            50 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/zentral-begehbare-2-zimmerwohnung-mit-aussenfl%C3%A4che-1387031425/)                                                             | Mar 07, 17:34      |
|       787.37 |            56 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/voll-ausgestattete-2-zimmer-altbauwohnung-mit-gro%C3%9Fen-abstellraum-im-6.-bezirk-1057410293/)                                | Mar 07, 17:04      |
|       500    |            45 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/gemeindewohnung-2-zimmer-direktvergabe-1696515070/)                                                                           | Mar 07, 16:50      |
|       750.01 |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-zwei-zimmer-neubauwohnung-2114677730/)                                                       | Mar 07, 14:24      |
|       735.88 |            74 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/bitte-schriftlich-anfragen%21-top-gelegenheit%21-2.-stock.-optimale-p%C3%A4rchen--oder-singlewohnung.-u6-n%C3%A4he.-993966400/) | Mar 07, 08:54      |
|       733.75 |            52 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/lichtdurchflutete-wohnung-nahe-dem-wienfluss-u4-unter-st.-veit---pure-freude-wartet.-1058198326/)                                | Mar 07, 08:47      |
|       726.48 |            58 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2%E2%80%91zimmer%E2%80%91wohnung-1110-wien-%28simmering%29-1894990255/)                                                        | Mar 07, 02:34      |
|       601    |            56 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnungsweitergabe---gemeindewohnung-%28mit-vormerksschein%29-942472305/)                                                      | Mar 06, 21:08      |
|       740.01 |            40 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-2-zimmerwohnung-mit-loggia-im-3.-og---wohnen-im-wildgarten-1431162609/)                                             | Mar 06, 18:00      |
