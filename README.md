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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            48 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/leopold-ernst-gasse---2-zimmer-neubau-mit-extra-einbauk%C3%BCche-876469462/)                                           | Jan 20, 18:26      |
|       649    |            63 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/fenzlgasse---sanierungsbed%C3%BCrftiger-2-zimmer-altbau-mit-extra-k%C3%BCche-zu-vermieten-1354556248/)                 | Jan 20, 17:57      |
|       590    |            48 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-im-yppenviertel-1429826407/)                                                                        | Jan 20, 17:47      |
|       754    |            32 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hofruhelage%21-kleine-2-zimmer-neubauwohnung-mit-terrasse-n%C3%A4he-u1%21-1846306708/)                               | Jan 20, 15:27      |
|       797.22 |            48 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zauberhafte-hoflage-in-city-n%C3%A4he%21-2110358250/)                                                          | Jan 20, 11:47      |
|       798.09 |            45 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/neubau-i-2-zimmer-i-besichtigung-am-freitag-den-23.1.26-von-15:30-bis-16:30-uhr%21-2057594491/)                      | Jan 20, 11:36      |
|       597.85 |            47 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-2-zimmerwohnung-im-haus-mit-lift-957240851/)                                                        | Jan 20, 11:05      |
|       749    |            37 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-und-geniessen-im-s%C3%BCdwesten-von-wien%21-perfekte-infrastruktur---n%C3%A4he-sch%C3%B6nbrunn%21-1106908787/) | Jan 20, 11:03      |
|       749.1  |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung---n%C3%A4he-keplerplatz-1267524958/)                                                                | Jan 20, 10:17      |
|       658.41 |            61 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-mit-2-zimmer-wohnticketsnummer-:-42775/2024.-die-wohnung-ist-reserviert%21-1312659054/)             | Jan 19, 21:23      |
|       735    |            54 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/komplett-eingerichtete-wohnung-1142252715/)                                                                          | Jan 19, 20:24      |
|       421.7  |            40 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-2-zimmer-gemeindewohnung-2070508728/)                                                                    | Jan 19, 19:25      |
