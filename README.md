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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       650.29 |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter/-in-gesucht:-traumhafte-balkonwohnung-in-favoriten-1243775008/)                                                             | Jun 16, 19:14      |
|       799.99 |            45 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/schlosspark-sch%C3%B6nbrunn-%7C-u4-hietzing-%7C-s%C3%BCd-ausrichtung-1816131368/)                                                        | Jun 16, 18:15      |
|       499    |            38 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/altbau-charme-in-top-lage-direkt-an-der-u4---perfekt-f%C3%BCr-studierende%21-784673921/)                                              | Jun 16, 17:27      |
|       610    |            55 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%28reserviert%29-gemeindewohnung-direktvergabe-2-zimmer-in-toplage-1907609198/)                                                       | Jun 16, 14:25      |
|       723.49 |            43 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-wohnung-mit-balkon-n%C3%A4he-elterleinplatz-1519589897/)                                                                        | Jun 16, 12:56      |
|       760    |            62 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/liebevolle-wohnung-in-top-lage-am-quellenplatz-zu-vermieten-1990342714/)                                                               | Jun 16, 12:49      |
|       617    |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien-leebgasse:-sonnige-liebevoll-sanierte-2-zimmer-altbautraumwohnung-ca.-55-m2-mit-lift-unbefristet-zu-vermieten%21-803465456/) | Jun 16, 01:03      |
|       690    |            43 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-zweizimmerwohnung-43m2-und-viel-nat%C3%BCrliches-licht-1174149363/)                                                         | Jun 15, 21:56      |
