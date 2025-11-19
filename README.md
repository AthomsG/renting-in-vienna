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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            48 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/prater-1528584307/)                                                                                                                  | Nov 18, 22:10      |
|       524    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktveegabe-helle-gemeindebauwohnung-4.-stock-mit-aufzug-2121218026/)                                                                 | Nov 18, 21:34      |
|       540    |            78 |          4 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/4-zimmer-gemeindewohnung-im-15.-bezirk-am-meiselmarkt---direktvergabe-856859471/)                                       | Nov 18, 19:55      |
|       787.99 |            54 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-sofort-i-matzleinsdorferplatz-i-drei-zimmer-1740047769/)                                                                             | Nov 18, 18:57      |
|       567.59 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindebauwohnung-per-direktvergabe.-vormerkschein-bis-30.09.2025-1171001453/)                                                         | Nov 18, 18:24      |
|       790.72 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-%7C-balkon-%7C-erstbezug-ab-15.12.2025-1870362055/)                                                                            | Nov 18, 16:46      |
|       768.63 |            40 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/cityapartment:-garagenplatz-im-haus-&-u6-spittelau-ums-eck-1547574512/)                                                                | Nov 18, 16:38      |
|       758.59 |            43 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/h%C3%BCbsche-hauptmietwohnung-auf-der-argentinierstra%C3%9Fe-/-sankt-elisabeth-platz-1343834412/)                                          | Nov 18, 14:57      |
|       695    |            31 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.2.2026---laxenburger-stra%C3%9Fe-1100-wien---einzimmer-singlewohnung-mit-s%C3%BCdseitigem-balkon-und-k%C3%BCchenzeile-1344708074/) | Nov 18, 13:06      |
|       613    |            57 |          3 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sehr-sch%C3%B6ne-und-zentral-gelegene-3-zimmerwohnung-2039158658/)                                                                     | Nov 18, 11:36      |
|       658    |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-&-sanierte-45-m%C2%B2-wohnung-in-ruhelage-mit-perfekter-u4/-u6-anbindung-1202285347/)                                              | Nov 18, 11:29      |
|       772.59 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-zwei-zimmer-neubauwohnung-mit-einbauk%C3%BCche-abstellraum-1031321461/)                               | Nov 18, 10:18      |
