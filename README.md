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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       730    |            55 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/privat-vermietung-wundersch%C3%B6n-erstbezug-ruhelage-1320705046/)                                                             | Sep 18, 06:52      |
|       574.81 |            49 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/anfragen-nur-schriftlich:-gepflegte-2-zimmer-altbauwohnung-in-guter-lage-%28unbefristet%29-1654586350/)      | Sep 18, 02:27      |
|       580    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/single-oder-p%C3%A4rchenwohnung-unbefristet-1826117148/)                                                                      | Sep 18, 02:08      |
|       552    |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nachmieter-gemeindewohnung-1761149382/)                                                                                        | Sep 17, 20:37      |
|       679.8  |            53 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/grangasse%21-2-zimmer-balkonhit%21-anfragen-nur-per-maill%21-openhouse-am-19.9.-13:00-13:20-uhr-1106905117/) | Sep 17, 20:26      |
|       773.55 |            82 |          4 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-einer-gemeindewohnung-wohnticket-bis-31.03.2019-4-zimmer-996520161/)                                        | Sep 17, 18:11      |
|       662.04 |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-45m%C2%B2-altbau-mit-2-zimmern-und-einbauk%C3%BCche---u1-n%C3%A4he%21-1680136189/)             | Sep 17, 17:45      |
|       799.99 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-k%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-hs17-top-a-11-856988592/)             | Sep 17, 15:15      |
|       780    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmerwohnung-im-sonnwendviertel-2102028419/)                                                                        | Sep 17, 13:17      |
|       792    |           nan |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnen-am-wienerberg---beste-lage-im-s%C3%BCden-von-wien-1474378946/)                                                        | Sep 17, 11:57      |
|       700    |            71 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug-n%C3%A4he-spinnerin-am-kreuz-1820583343/)                                                                          | Sep 17, 11:05      |
