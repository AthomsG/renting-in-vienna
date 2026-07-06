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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       454    |            44 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeinde-direktvergabe-4475qm-mit-wohnticket-1283019923/)                                                                                                         | Jul 06, 21:02      |
|       720    |            40 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gepflegter-2-zimmer-neubau-bj-1970-mit-einbauk%C3%BCche-n%C3%A4he-ameisbr%C3%BCcke-u4-hiezing-keine-abl%C3%B6se.-1552474095/)                                       | Jul 06, 16:25      |
|       715    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sch%C3%B6ne-2-zimmer-wohnung-in-gr%C3%BCnderzeithaus-n%C3%A4he-schmelz-1486743041/)                                                               | Jul 06, 15:25      |
|       439    |            41 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/1140-wien:-dreyhausenstra%C3%9Fe:-sonnendurchflutete-2-zimmer-altbaukleinwohnung-ca.-41-m2-mit-herrlichem-parkblick-ohne-lift-langfristig-zu-vermieten-1785745238/) | Jul 06, 15:14      |
|       550    |            52 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-wohnung-in-der-koppstrasse-ab-sofort-verf%C3%BCgbar-1330921519/)                                                                                   | Jul 06, 13:01      |
|       799.08 |            63 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-mit-terrasse-zu-vermieten-1926561089/)                                                                                                           | Jul 06, 12:34      |
