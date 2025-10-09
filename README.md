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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       795    |            37 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sch%C3%B6ne-2-zimmer-neubau-wohnung-mit-balkon-909600938/)                                                     | Oct 09, 21:33      |
|       650    |            40 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-n%C3%A4he-familienplatz-2124763420/)                                        | Oct 09, 17:13      |
|       500    |            48 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-gemeindewohnung-im-12.-bezirk-%28wohnticket%29-1564061280/)                                             | Oct 09, 15:27      |
|       796.84 |            40 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei:-wundersch%C3%B6nerr-40m%C2%B2-neubau-mit-einbauk%C3%BCche-u.-balkon---1160-wien-1584220400/) | Oct 09, 13:48      |
|       760.39 |            36 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-sanierung:-sch%C3%B6ne-2-zimmer-wohnung-nahe-meidling-bahnhof-1121833885/)                     | Oct 09, 13:17      |
|       649    |            47 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/termine-bitte-online-buchen-%28link-steht-im-text%29-1066753279/)                                            | Oct 09, 13:15      |
|       640    |            60 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter-gesucht-1100-wien---2-zimmer-gemeindewohnung-1856699572/)                                         | Oct 09, 10:12      |
|       650    |            65 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-wohnung-in-ruhiger-lage-ab-sofort-verf%C3%BCgbar-977246228/)                                          | Oct 08, 22:34      |
|       650    |            44 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/private-zwei-zimmer-wohnung-%28geeignet-f%C3%BCr-zwei-personen%29-in-ruhiger-lage-1773622717/)               | Oct 08, 21:58      |
