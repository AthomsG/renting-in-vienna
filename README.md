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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       714.01 |            38 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/neu%21-ideale-2-zimmerwohnung-im-herzen-des-9.-bezirks%21-1919777122/)                                                                               | Aug 01, 13:46      |
|       493.77 |            45 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/%5Bnur-mit-g%C3%BCltigem-wohnticket%5D-2-zimmer-wohnung-1040-direktvergabe---wiener-wohnen-%28ticket-bis-31.05.2025%29---nachmieter-gesucht-1158011138/) | Aug 01, 13:22      |
|       792.55 |            47 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/m%C3%B6blierte-gem%C3%BCtliche-2-zimmer-wohnung-im-15.bezirk%21-1989169647/)                                                          | Aug 01, 12:25      |
|       624.64 |            40 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neuwertig---fernblick---2-zimmer-wohnung---n%C3%A4he-u6-meidling---gr%C3%BCnblick---unbefristet-1085810893/)                                           | Aug 01, 11:50      |
|       789.06 |            49 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei:-ruhiger-49m%C2%B2-neubau-mit-2-zimmern-und-einbauk%C3%BCche---1120-wien-1127315926/)                                                   | Aug 01, 11:20      |
|       793    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kompakte-mietwohnung-1147194543/)                                                                                                                     | Jul 31, 18:03      |
|       598    |            32 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-leitgebgasse-zentrumslage-%C3%A4ltere-32m%C2%B2-neubaumiete-4.-liftstock-studenten-bevorzugt%21-2120295291/)   | Jul 31, 14:31      |
