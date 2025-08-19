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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       520.37 |            52 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-per-direktvergabe---abl%C3%B6se---moderne-ausstattung-inkl.-neuer-k%C3%BCche-1296136406/) | Aug 19, 17:41      |
|       545.79 |            51 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-wiener-wohnen-vormerkscheindatum-31.03.2025-1320133045/)                                          | Aug 19, 17:23      |
|       648    |            43 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/ruhige-2-zimmer-altbauwohnung-%7C-n%C3%A4he-hauptbahnhof-%7C-unbefristet-%7C-ab-sofort-1437769274/)                | Aug 19, 16:36      |
|       760.01 |            57 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-nahe-wiener-hauptbahnhof-1673409105/)                                                          | Aug 19, 16:36      |
|       687.41 |            52 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%2Aideal-f%C3%BCr-stadtliebhaber%2A-1683672413/)                                                                   | Aug 19, 15:56      |
|       780    |            70 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-1020-wien-1345527839/)                                                                       | Aug 19, 14:32      |
|       649.84 |            51 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug%21-sanierte-mietwohnung-n%C3%A4he-quellenplatz%21-1404880178/)                                        | Aug 19, 14:08      |
|       530    |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-in-wien-10:-nachmieter-gesucht-1575320398/)                                                    | Aug 19, 14:01      |
|       546.53 |            48 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-gemeindebau:-1020-2.-bezirk-bei-donau-2-zimmer-mit-balkon-779695420/)                          | Aug 19, 11:58      |
|       630    |            79 |          3 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/3-zimmer-gemeindewohnung-direktvergabe-1540603589/)                                                              | Aug 19, 00:26      |
|       789    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/top-renoviert%21-1702930463/)                                                                                    | Aug 18, 21:50      |
|       474.21 |            47 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-n%C3%A4he-augarten-1893247661/)                                                              | Aug 18, 16:44      |
|       692.07 |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-u1-station-keplerplatz---2-zimmer-mit-separater-k%C3%BCche---beim-wiener-hauptbahnhof-2000104982/)    | Aug 18, 16:25      |
