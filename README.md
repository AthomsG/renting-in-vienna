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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       755    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierte-25-zimmer-wohnung-nahe-sonnwendviertel-1083062890/)                                   | Dec 02, 12:58      |
|       761.41 |            47 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/helle-ruhige-1-1/2-zimmer-in-stilaltbau-2058481065/)                                        | Dec 02, 12:16      |
|       569.02 |            54 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnen-in-simmering%21-1756104670/)                                                            | Dec 02, 12:09      |
|       515    |            44 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sch%C3%B6ne-2-zimmer-wohnung-im-11.bezirk-1619185224/)                                         | Dec 02, 11:50      |
|       795    |            36 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neubau-in-massivholzbauweise-1732670607/)                                                       | Dec 02, 10:22      |
|       719    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-zwei-zimmer-neubauwohnung-1031321461/)                       | Dec 02, 10:18      |
|       697.52 |            45 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/termine-bitte-online-buchen-%28link-steht-im-text%29-1063132146/)                                | Dec 02, 09:27      |
|       798.42 |            37 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sch%C3%B6ne-wohnung-15-zimmer-wohnung-mit-balkon-in-1050-wien%21-1388551902/)                 | Dec 02, 09:21      |
|       461    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-%28vmd:-november-2025%29-2062417367/)                                 | Dec 01, 20:24      |
|       682.27 |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/m%C3%B6blierte-altbauwohnung-n%C3%A4he-meiselmarkt-u3-unbefristet-2135071827/) | Dec 01, 14:15      |
