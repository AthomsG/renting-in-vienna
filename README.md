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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       500    |            46 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-2-zimmer-gemeindewohnung-im.-14.-bezirk-ticketnummer-bis-30.09.2025-2093066207/)                                                                           | Oct 24, 11:39      |
|       715.4  |            47 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug---n%C3%A4he-u4/u6-%2A%2A%2A-2-zimmer-mit-separater-k%C3%BCche-%2A%2A%2A-beim-bahnhof-matzleinsdorfer-platz-1061749725/)                                       | Oct 24, 11:37      |
|       780    |            84 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeinde-wohnung-1020wien/84m2/-780%E2%82%AC-1944868190/)                                                                                                           | Oct 24, 10:03      |
|       779    |            40 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/dringend-nachmieter-gesucht-ab-01.12.2025---2-zi.-wohntraum-in-top-lage---nur-5.-min.-zu-mah%C3%BC%21%21%21-2028779374/)                                               | Oct 24, 07:57      |
|       415.31 |            41 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/1150-m%C3%A4rzstra%C3%9Fe-2-zimmer-n%C3%A4he-u-bahn-2087932039/)                                                                                       | Oct 24, 03:32      |
|       795    |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sch%C3%B6ne-2-zimmer-neubau-wohnung-mit-balkon-909600938/)                                                                                                               | Oct 23, 21:33      |
|       558    |            50 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeinde-wohnung-mit-ticket-30-september-2025-1573880980/)                                                                                                             | Oct 23, 19:10      |
|       599    |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung---zentrale-lage-1470195319/)                                                                                                                          | Oct 23, 17:27      |
|       620    |            48 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-vogelsanggasse-hofruhelage-zentrumsnahe-48m%C2%B2-altbauhauptmiete-2.-stock-%28kein-lift%29-studenten-bevorzugt%21-2139177603/) | Oct 23, 17:24      |
