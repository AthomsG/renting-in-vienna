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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       784.98 |            71 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristet---wurlitzergasse-1717780566/)                                                                                                 | Sep 30, 09:20      |
|       625.73 |            37 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-helle-2-zimmer-wohnung-%7C-3.-stock-%7C-lift-1515004304/)                                                                | Sep 29, 15:33      |
|       648.05 |            39 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/n%C3%A4he-u4-/-u6---gartenwohnung-in-ruhelage---2-zimmer-mit-separater-k%C3%BCche---beim-gaudenzdorfer-g%C3%BCrtel-1950032848/)            | Sep 29, 14:26      |
|       745    |            64 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/philadelphia-br%C3%BCcke-meidlinger-hauptstra%C3%9Fe-911989813/)                                                                           | Sep 29, 13:02      |
|       569    |            47 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/erstbezug-am-lerchenfelder-g%C3%BCrtel-1913196816/)                                                                                       | Sep 29, 12:56      |
|       720    |            48 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-wohnung-in-ruhelage-zu-vermieten-1818750972/)                                                                             | Sep 29, 11:30      |
|       522.5  |            47 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-provisionsfreie-47m%C2%B2-=-2zi%2B-nr-n%C3%A4he-elterleinplatz-sehr-sch%C3%B6n-saniert-&-hell-3.-og-ohne-lift-1910368116/) | Sep 29, 10:56      |
