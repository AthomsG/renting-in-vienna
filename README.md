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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            33 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/stylisch-kompakt-zentral---dein-neuer-r%C3%BCckzugsort-1786734461/)                                                   | Sep 01, 09:37      |
|       668.9  |            62 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-im-10.-bezirk-2-zimmer%2B-1-nebenzimmer%28nur-mit-wohnticket-f%C3%BCr-2-zimmer-bis-31.08.2025%29-1644978842/)         | Aug 31, 22:12      |
|       670    |            65 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-1187438720/)                                                                                      | Aug 31, 21:03      |
|       604.5  |           402 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-zwei-zimmer-wohnung-zweiter-stock-mit-lift-%2Averf%C3%BCgbar-ab-01.10.2025%2A-960058710/)                                 | Aug 31, 20:39      |
|       700.62 |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gr%C3%BCnruhelage---sehr-helle-stilaltbauwohnung-mit-terrasse%21-2013985656/)                                                         | Aug 31, 20:38      |
|       620    |            41 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/unbefristeter-mietvertrag%21-miete-inkl.-heizkosten%21-858264000/)                                                    | Aug 31, 20:04      |
|       764.74 |            63 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nur-an-sozialbau-mieter%21-wundersch%C3%B6ne-2-zimmer--genossenschaftswohnung-mit-balkon-&-moderner-k%C3%BCche-abzugeben-1586064481/) | Aug 31, 14:43      |
|       777.02 |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-innenhoflage-&-wg-geeignet%21-wundersch%C3%B6ne-2-zimmer-whg.-mit-garten-n%C3%A4he-wienerberg-&-fh-2106468861/)      | Aug 31, 12:28      |
|       740.6  |            60 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/helle-2-zimmer-altbauwohnung-n%C3%A4chst-margaretenplatz-und-naschmarkt-2018037946/)                                                 | Aug 31, 12:25      |
|       749.56 |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sonnige-2-zimmer-wohnung%21-2019575485/)                                                                                               | Aug 31, 11:35      |
|       795    |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sch%C3%B6ne-2-zimmer-neubau-wohnung-mit-balkon-1746848067/)                                                                             | Aug 31, 11:15      |
