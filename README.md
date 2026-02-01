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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       678.42 |            39 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-2-zimmer-wohnung-nahe-dem-viktor-adler-markt-1534306467/)                                                                                                   | Feb 01, 13:36      |
|       600    |            72 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-gut-gelegene-3-zimmer-wohnung.-hell-ruhig-gut-erhalten.-keine-maklerprovision.-direkt-vom-vermieter-1466848641/)                                              | Feb 01, 13:26      |
|       770    |            70 |          4 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/direktvergabe-wiener-wohnen---4-zimmer-1105411979/)                                                                                                                | Feb 01, 12:16      |
|       610    |            74 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3--zimmer-wohnung-im-11.-bezirk-1994335199/)                                                                                                                       | Feb 01, 11:49      |
|       450    |            46 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/direktvergabe-gemeindewohnung-2-zimmer-mit-balkon-1785910524/)                                                                                                    | Feb 01, 11:37      |
|       663.84 |            45 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/am-migazziplatz-%2A%2A%2A-n%C3%A4he-u4/u6-station-%2A%2A%2A-erdgeschoss-%2A%2A%2A-2-zimmer-mit-separater-k%C3%BCche-%2A%2A%2A-beim-theresienbad-/-park-1396345733/) | Feb 01, 09:34      |
|       515.62 |            50 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/vollm%C3%B6belierte-wohnung-in-top-lage-1070-wien-%28abl%C3%B6se-beachten%21%29-1346795004/)                                                                          | Jan 31, 20:46      |
|       720.89 |            46 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-ab-april:-m%C3%B6blierte-2-zimmer-wohnung-im-2.-bezirk-an-der-wu-und-sfu-%7C-xl-bude-1177987177/)                                              | Jan 31, 16:25      |
