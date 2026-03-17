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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       697.29 |            58 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/am-migazziplatz-%2A%2A%2A-n%C3%A4he-u4/u6-station-%2A%2A%2A-separate-k%C3%BCchenzeile-%2A%2A%2A-beim-theresienbad/park-1104364318/)   | Mar 17, 15:19      |
|       733.61 |            47 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet-gepflegte-47-m2-altbau-mit-27-m2-garten/terrasse-2-zimmer-kochnische-wannenbad-parketten-randhartingergasse-1477434652/) | Mar 17, 15:00      |
|       791.64 |            62 |          2 | 04. Wieden    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/sonnige-2-zimmer-mit-stil-beim-hauptbahnhof-824411845/)                                                                                 | Mar 17, 12:37      |
|       715    |            71 |          3 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wohnung-weitergabe-1131944132/)                                                                                                        | Mar 17, 12:27      |
|       790    |            47 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/top-lage-u4-unter-st.-veit-%7C-helle-2-zimmer-wohnung-%7C-47-m%C2%B2-%7C-frisch-saniert-1795471501/)                                   | Mar 17, 10:58      |
|       620    |            50 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/unbefristete-hauptmietwohnung-in-1110-wien-1764408248/)                                                                              | Mar 17, 09:05      |
|       507    |            50 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-1040850961/)                                                                                           | Mar 17, 01:49      |
|       495.22 |            50 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-mit-balkon-reserviert%21-1160172997/)                                                                                | Mar 16, 20:24      |
