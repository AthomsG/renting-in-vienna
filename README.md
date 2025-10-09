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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       796.84 |            40 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei:-wundersch%C3%B6nerr-40m%C2%B2-neubau-mit-einbauk%C3%BCche-u.-balkon---1160-wien-1584220400/) | Oct 09, 13:48      |
|       760.39 |            36 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-sanierung:-sch%C3%B6ne-2-zimmer-wohnung-nahe-meidling-bahnhof-1121833885/)                     | Oct 09, 13:17      |
|       649    |            47 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/termine-bitte-online-buchen-%28link-steht-im-text%29-1066753279/)                                            | Oct 09, 13:15      |
|       640    |            60 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter-gesucht-1100-wien---2-zimmer-gemeindewohnung-1856699572/)                                         | Oct 09, 10:12      |
|       650    |            65 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-wohnung-in-ruhiger-lage-ab-sofort-verf%C3%BCgbar-977246228/)                                          | Oct 08, 22:34      |
|       650    |            44 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/private-zwei-zimmer-wohnung-%28geeignet-f%C3%BCr-zwei-personen%29-in-ruhiger-lage-1773622717/)               | Oct 08, 21:58      |
|       552    |            49 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nachmieter-gemeindewohnung-1761149382/)                                                                        | Oct 08, 20:37      |
|       633.58 |            43 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/anfragestopp---2-zimmer-wohnung-direkt-bei-der-u3-ottakring-1641059060/)                                     | Oct 08, 20:00      |
|       790    |            49 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/singleapartment-in-toplage-%7C-altbaucharme-inklusive-%7C-vollm%C3%B6bliert-1601360582/)                    | Oct 08, 18:26      |
|       750    |            52 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zimmer-wohnung-zu-vermieten-anfragestopp%21-1053916810/)                                                  | Oct 08, 18:26      |
|       780    |            44 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/11.hugogasse-unbefristete-provisionsfreie-unm%C3%B6blierte-2-zimmer-neubaumiete-in-u3-n%C3%A4he-1163235011/) | Oct 08, 13:41      |
