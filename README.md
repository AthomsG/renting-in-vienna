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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            39 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-mit-loggia---zu-mieten-im-neubauprojekt-%22herz-&-heim%22-in-simmering-1110-wien-1727411451/)                                            | Jan 09, 09:22      |
|       733.26 |            59 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/charmante-2-zimmer-wohnung-in-ruhiger-lage-des-17.-bezirks-1258577686/)                                                                                     | Jan 09, 02:45      |
|       570    |            44 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-vogelsanggasse-zentrumsnahe-44m%C2%B2altbauhauptmiete-2.-stock-%28kein-lift%29-studenten-bevorzugt%21-1713948716/) | Jan 08, 20:42      |
|       750    |            65 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-helle-gemeindewohnung-im-gr%C3%BCnen-n%C3%A4he-erholungsgebiet-wienerberg-1100-wien-776910415/)                                             | Jan 08, 20:16      |
|       617.4  |            52 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/charmante-2-zimmer-wohnung-1009629127/)                                                                                                                      | Jan 08, 16:29      |
|       693.56 |            50 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/sch%C3%B6ne-2-zimmer-altbauwohnung-mit-einbauk%C3%BCche-1724273287/)                                                                                         | Jan 08, 16:27      |
|       796.89 |            41 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/the-arrow---willkommen-im-gr%C3%BCnen-teil-simmerings-784697756/)                                                                                         | Jan 08, 15:20      |
|       522    |            60 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-zur-weitervergabe-vm-30.11.2025-1494968646/)                                                                                                      | Jan 08, 15:19      |
|       607    |            54 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-gemeindewohnung-zu-vergeben-1532299597/)                                                                                                   | Jan 08, 14:47      |
|       696.2  |            44 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/nachmieterin-f%C3%BCr-meine-altbauwohnung-in-1080-wien-gesucht-1738923000/)                                                                              | Jan 08, 14:25      |
|       731.5  |           nan |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/moderne-garconnieren-sowie-2-zimmer-apartments-in-zentraler-lage-in-altmannsdorf-1303212139/)                                                              | Jan 08, 13:48      |
