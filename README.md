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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|        644   |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet-u1-aufzug-1033302047/)                                                                                                           | Feb 18, 12:10      |
|        669.7 |            56 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-wohnung-%7C-sofort-beziehbar---1120-wien-1086937218/)                                                                          | Feb 18, 11:44      |
|        750   |            50 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gepflegte-2-zimmerwohnung-n%C3%A4he-ottakringer-brauerei-1569084260/)                                                                        | Feb 18, 10:51      |
|        750.3 |            38 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliches-m%C3%B6bliertes-apartment-in-innenstadtn%C3%A4he---kurzmiete-f%C3%BCr-maximal-6-monate%21-1230385154/)                     | Feb 18, 09:59      |
|        630   |            47 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/m%C3%B6blierte-2-zimmer-wohnung-in-zentraler-lage---miete-630-%E2%82%AC-abl%C3%B6se-4.000-%E2%82%AC-%2B-3.600-%E2%82%AC-kaution-1791761166/) | Feb 17, 21:21      |
|        573.7 |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-am-wienerberg%21-vormerkschein-bis-31.12.2025-1159323993/)                                                          | Feb 17, 14:11      |
