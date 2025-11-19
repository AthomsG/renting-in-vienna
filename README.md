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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       580    |            41 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sportlicher-singletraum-im-3.tten-stock-ohne-lift---langfristige-anmietung-erw%C3%BCnscht-1578877993/)      | Nov 19, 14:34      |
|       730    |            70 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-n%C3%A4he-u4-station-margareteng%C3%BCrtel-1500551329/)                                   | Nov 19, 13:36      |
|       750    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-zwei-zimmer-neubauwohnung-mit-einbauk%C3%BCche-abstellraum-2022624400/) | Nov 19, 11:58      |
|       524    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktveegabe-helle-gemeindebauwohnung-4.-stock-mit-aufzug-2121218026/)                                   | Nov 18, 21:34      |
|       540    |            78 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/3-zimmer-gemeindewohnung-im-15.-bezirk-am-meiselmarkt---direktvergabe-856859471/)         | Nov 18, 19:55      |
|       787.99 |            54 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-sofort-i-matzleinsdorferplatz-i-drei-zimmer-1740047769/)                                               | Nov 18, 18:57      |
|       567.59 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindebauwohnung-per-direktvergabe.-vormerkschein-bis-30.09.2025-1171001453/)                           | Nov 18, 18:24      |
|       790.72 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-%7C-balkon-%7C-erstbezug-ab-15.12.2025-1870362055/)                                              | Nov 18, 16:46      |
|       768.63 |            40 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/cityapartment:-garagenplatz-im-haus-&-u6-spittelau-ums-eck-1547574512/)                                  | Nov 18, 16:38      |
|       758.59 |            43 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/h%C3%BCbsche-hauptmietwohnung-auf-der-argentinierstra%C3%9Fe-/-sankt-elisabeth-platz-1343834412/)            | Nov 18, 14:57      |
