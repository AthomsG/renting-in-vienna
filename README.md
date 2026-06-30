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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       650    |            41 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/moderne-sch%C3%B6ne-sehr-ruhig-gelegene-2-zimmerwohnung-u-4-n%C3%A4he-1608481053/)                                                                                      | Jun 30, 18:51      |
|       550    |            72 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-wg-miete-pro-person.-max-3-personen-1808669107/)                                                                                                              | Jun 30, 17:17      |
|       736.3  |            54 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/supermiete-sch%C3%B6ne-2-zimmerwohnung-alle-nebenr%C3%A4ume-gute-%C3%B6ffentlicher-anbindung%21-2139697869/)                                                           | Jun 30, 16:43      |
|       746.52 |            46 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-ab-juli:-m%C3%B6bliertes-all-in-2-zimmer-apartment-im-2.-bezirk-nahe-wu-&-sfu-%7Cxl-bude-1177987177/)                                              | Jun 30, 16:25      |
|       695    |            44 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/25-zimmer-wohnung-in-ruhiger-lage---besichtigungstermin-mittwoch-1.7.2026-um-17.30h-1831939060/)                                                                       | Jun 30, 13:25      |
|       765    |            76 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-wohnung-nur-mit-vormerkschein-von-wiener-wohnen-1924915000/)                                                                                                  | Jun 30, 12:37      |
|       629    |            52 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sonniger-altbau-am-lerchenfelder-g%C3%BCrtel%21-1940453871/)                                                                                                           | Jun 30, 12:09      |
|       699    |            58 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2Azauberhafte-helligkeit%2A---brunnenmarkt-804169750/)                                                                                                                | Jun 30, 11:46      |
|       770.43 |            47 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung-mit-guter-verkehrsanbindung-in-gepflegtem-neubau-1038719322/)                                                                                   | Jun 30, 11:32      |
|       780    |            50 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-wohnung-mit-garten-neubau-%2850m%C2%B2-%2B-30m%C2%B2-garten%29---voll-m%C3%B6beliert---kein-genossenschaftsanteil%21-mit-abl%C3%B6se-%21-2067188168/) | Jun 29, 19:48      |
