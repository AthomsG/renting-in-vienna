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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       696.67 |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/entz%C3%BCckende-gut-aufgeteilte-2-zimmer-wohnung-48-m2---sofortbezug%21-1274931458/)                                                 | Nov 05, 15:37      |
|       650    |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug-nach-kernsanierung---exquisite-&-klassische-wiener-altbau-wohnung-mit-2-zimmern---n%C3%A4he-hauptbahnhof%21-1934610304/)    | Nov 05, 15:26      |
|       528    |            46 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/top-lage-im-zentrum-rathausn%C3%A4he-2-zimmer-528.---brutto-1163730980/)                                                             | Nov 05, 15:00      |
|       789.81 |            59 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gepflegte-altbauwohnung-n%C3%A4chst-urania-nur-3-gehminuten-vom-1.-wiener-bezirk-entfernt-1092343689/)                             | Nov 05, 14:06      |
|       410    |            64 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeindewohnung-direktvergabe-3-zimmer-ruhige-lage-1508584685/)                                                                         | Nov 05, 12:02      |
|       749    |            70 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/belghofergasse---sanierungsbed%C3%BCrftiger-2-zimmer-altbau-zu-vermieten-1298147745/)                                                  | Nov 05, 00:37      |
|       790.72 |            54 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erdw%C3%A4rmepumpe-%7C-balkon-%7C-erstbezug-ab-15.12.2025-1970327301/)                                                                | Nov 04, 20:40      |
|       664.66 |            46 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/u3-h%C3%BCtteldorfer-stra%C3%9Fe-ii-2-zimmer-mit-separater-k%C3%BCche-ii-n%C3%A4he-wien-penzing-bahnhof-und-s45-breitensee-1822914495/) | Nov 04, 17:55      |
|       740    |            49 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/charmante-wohnung-1588498472/)                                                                                                        | Nov 04, 17:02      |
|       768.63 |            40 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/cityapartment:-garagenplatz-im-haus-&-u6-spittelau-ums-eck---open-house-am-14.10.2025-um-14:00-1555017726/)                          | Nov 04, 16:53      |
|       799.36 |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/grossz%C3%BCgige-2-zimmer-wohnung-im-10.bezirk%21-1872106349/)                                                                        | Nov 04, 16:18      |
