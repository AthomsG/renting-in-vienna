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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       772.59 |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-zwei-zimmer-neubauwohnung-mit-einbauk%C3%BCche-abstellraum-1031321461/)            | Nov 18, 10:18      |
|       699    |            51 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/termine-bitte-online-buchen-%28link-steht-im-text%29-790219523/)                                                     | Nov 18, 09:16      |
|       550.54 |            40 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kompakte-2-zimmer-wohnung%21-1415048072/)                                                                            | Nov 18, 07:05      |
|       777.31 |            74 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/hauptmietwohnung-n%C3%A4he-enkplatz-1606187221/)                                                                     | Nov 17, 21:35      |
|       498    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-2-zimmer-mit-vormerkschein-bis-30.09.2025-832615851/)                                                | Nov 17, 19:30      |
|       600    |            58 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-einer-2-zimmer-gemeindewohnung-mit-loggia-im-2.-bezirk-1037424519/)                                 | Nov 17, 18:28      |
|       565    |            53 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ger%C3%A4umige-2-zimmer-gemeindewohnung-%28wohnticket:-30.09.25%29-970470669/)                                         | Nov 17, 17:40      |
|       760    |            38 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfreie-mietwohnung-in-top-lage-38m2-807621734/)                                                            | Nov 17, 16:55      |
|       700    |            50 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/zwischenmiete-j%C3%A4n/-feb-2026-1338112940/)                                                                        | Nov 17, 16:51      |
|       799    |            40 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-und-geniessen-im-s%C3%BCdwesten-von-wien%21-perfekte-infrastruktur---n%C3%A4he-sch%C3%B6nbrunn%21-998178244/)  | Nov 17, 12:22      |
|       799    |            38 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-und-geniessen-im-s%C3%BCdwesten-von-wien%21-perfekte-infrastruktur---n%C3%A4he-sch%C3%B6nbrunn%21-2127905873/) | Nov 17, 11:59      |
|       799    |            46 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-und-geniessen-im-s%C3%BCdwesten-von-wien%21-perfekte-infrastruktur---n%C3%A4he-sch%C3%B6nbrunn%21-903224607/)  | Nov 17, 11:50      |
|       650    |            40 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/single-wohnung-im-5.-bezirk-1871386776/)                                                                            | Nov 17, 11:30      |
|       550    |            43 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/top-sanierte-wohnung-g%C3%BCnstig-zu-vermieten-890493681/)                                                            | Nov 17, 09:36      |
