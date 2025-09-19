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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       729.81 |            48 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/2-zimmer-altbau-in-bester-lage-2103205780/)                                                               | Sep 19, 19:32      |
|       650    |            35 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/beautiful-one-bedroom-apartment-2038250790/)                                           | Sep 19, 18:40      |
|       720    |            80 |          4 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/3-zimmer-gemeindewohnung-im-12.-bezirk-zur-direktvergabe-1287142237/)                                   | Sep 19, 18:31      |
|       595    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sonniger-erstbezug---u6-um%60s-eck%21-1868694435/)                                                      | Sep 19, 15:06      |
|       670    |            62 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-1335818413/)                                                                          | Sep 19, 13:30      |
|       550    |            50 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-2-zimmer-gemeindewohnung-1581309000/)                                                      | Sep 19, 13:10      |
|       752.4  |            41 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neuwertige-2-zimmer-wohnung-mit-balkon-in-1120-wien-siebertgasse-26---ihr-neues-zuhause%21-1145142857/) | Sep 19, 12:16      |
|       630    |            79 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-vormerkscheindatum-vor-31.8.2024---3-zimmer-gemeindewohnung-direktvergabe-1724054859/) | Sep 19, 07:08      |
|       511.25 |            64 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/charmante-2-zimmer-wohnung-im-dachgeschoss-1178361556/)                                                | Sep 19, 06:47      |
