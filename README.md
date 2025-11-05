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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            37 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gem%C3%BCtliche-2--zimmerwohnung-zwischen-u3-westbahnhof-und-u6-gumpendorfer-stra%C3%9Fe-1890158224/)                                 | Nov 05, 03:46      |
|       749    |            70 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/belghofergasse---sanierungsbed%C3%BCrftiger-2-zimmer-altbau-zu-vermieten-1298147745/)                                                  | Nov 05, 00:37      |
|       790.72 |            54 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erdw%C3%A4rmepumpe-%7C-balkon-%7C-erstbezug-ab-15.12.2025-1970327301/)                                                                | Nov 04, 20:40      |
|       760    |            57 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-nahe-wiener-hauptbahnhof-1762031063/)                                                                                | Nov 04, 18:21      |
|       664.66 |            46 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/u3-h%C3%BCtteldorfer-stra%C3%9Fe-ii-2-zimmer-mit-separater-k%C3%BCche-ii-n%C3%A4he-wien-penzing-bahnhof-und-s45-breitensee-1822914495/) | Nov 04, 17:55      |
|       740    |            49 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/charmante-wohnung-1588498472/)                                                                                                        | Nov 04, 17:02      |
|       768.63 |            40 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/cityapartment:-garagenplatz-im-haus-&-u6-spittelau-ums-eck---open-house-am-14.10.2025-um-14:00-1555017726/)                          | Nov 04, 16:53      |
|       799.36 |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/grossz%C3%BCgige-2-zimmer-wohnung-im-10.bezirk%21-1872106349/)                                                                        | Nov 04, 16:18      |
|       747.92 |            43 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/besichtigung-am-06.11.2025-von-16:30-19:00-ohne-anmeldung---wohnung-in-1110-wien---felsgasse-4/33-1384771803/)                        | Nov 04, 11:20      |
|       699    |            36 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/himbergerstra%C3%9Fe-28-1559773134/)                                                                                                  | Nov 04, 11:08      |
|       747.92 |            43 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/besichtigung-am-06.11.2025-von-16:30-19:00---neu-sanierte-2-zimmer-wohnung-in-1110-wien---top26-1080236707/)                          | Nov 04, 11:05      |
|       770    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nette-2-zimmerwohnung-mit-loggia-1169631802/)                                                                                         | Nov 04, 09:58      |
