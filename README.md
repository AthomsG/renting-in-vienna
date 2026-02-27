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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       779    |            34 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.5.2026---laxenburgerstra%C3%9Fe-151---1100-wien---traumhafte-neubau---singlewohnung-im-9ten-stock-mit-fernblick-1428023853/) | Feb 27, 12:37      |
|       545.48 |            43 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/tolle-2---zimmer---altbauwohnung-%7C-unbefristet-%7C-ab-sofort-1310301017/)                                                        | Feb 27, 07:04      |
|       744.3  |            32 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-ab-mai:-m%C3%B6blierte-2-zimmer-wohnung-mit-balkon-zentral-in-der-leopoldstadt-%7C-maxi-bude-1893604330/)     | Feb 26, 16:28      |
|       550    |           100 |          4 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/wg-zimmer-zu-vermieten-in-top-lage-direkt-bei-der-u4-margareteng%C3%BCrtel-2009791768/)                                           | Feb 26, 13:51      |
|       794.25 |            41 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-neubauwohnung-mit-gro%C3%9Fem-balkon---2.-og-1198537752/)                                                        | Feb 26, 13:37      |
