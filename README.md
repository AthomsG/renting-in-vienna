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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|        790   |            33 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/stylisch-kompakt-zentral---dein-neuer-r%C3%BCckzugsort-1747976237/)                                                              | Aug 10, 10:24      |
|        500   |            46 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/vollm%C3%B6blierte-2-zimmer-gemeindewohnung-zu-vergeben-stichtag-30.06.2025-1682867657/)                                                           | Aug 10, 00:08      |
|        795   |            76 |          3 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-dierktvergebe-1678048219/)                                                                                                        | Aug 09, 20:15      |
|        487   |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-wien-10.-vormerkschein-1607613008/)                                                                                     | Aug 09, 18:59      |
|        580   |            60 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sonnendurchflutetes-2-zimmer-dachgeschossapartment-%28%22smart%22-gemeindewohnung%29---vormerkschein-stichtag-30.6.-1124652136/) | Aug 09, 15:14      |
|        477.1 |            44 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/anfragen-stopp-gemeindewohnung-mit-balkon-in-1030-wien-zu-vermieten-2033793661/)                                                           | Aug 09, 13:54      |
|        450   |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien-895795802/)                                                                                                                            | Aug 09, 12:57      |
|        670   |            64 |          3 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-818393195/)                                                                                                                       | Aug 09, 12:18      |
|        469   |            73 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-abzugeben-per-direktvergabe-1463176004/)                                                                                         | Aug 09, 10:04      |
|        699.6 |            58 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-2-zimmer-wohnung%21-openhouse-12.8.-16:40-17:00-uhr%21-keine-anrufe---anfragen-nur-per-mail%21-1833938909/)                                  | Aug 09, 09:19      |
