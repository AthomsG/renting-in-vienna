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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|          688 |            70 |          3 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-direktvergabe/1110-wien-3-zimmer-mit-balkon-ruhige-lage-1741447724/)                                                       | Jul 19, 21:12      |
|          450 |            70 |          3 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/mietwohnung-mit-eigene-zimmer-1210337368/)                                                                                                 | Jul 19, 18:07      |
|          740 |            35 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/neubau-in-ottakring%21-5min-zur-u3.-mit-einbauk%C3%BCche-und-westseitigem-balkon.-n%C3%A4chste-mietanpassung-erst-am-1.1.2027-1786293715/) | Jul 19, 15:02      |
|          525 |            60 |          3 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-3-zimmer---nur-%C3%BCber-direktvergabe-in-1100-wien---n%C3%A4he-raxstra%C3%9Fe-1903476582/)                                | Jul 19, 14:21      |
|          600 |            63 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/renovierte-altbauwohung-in-verkehrsg%C3%BCnstiger-lage-zu-vermieten-1476327995/)                                                            | Jul 19, 13:31      |
