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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                                                               | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       790    |            51 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/frisch-renovierte-zweizimmerwohnung-in-bestlage-1712280321/)                                                                                                                                                               | Oct 14, 14:28      |
|       733.59 |            41 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/sonnige-2-zimmer-wohnung-in-top-lage%21-nahe-der-mariahilfer-stra%C3%9Fe%21-1005822985/)                                                                                                                                      | Oct 14, 13:56      |
|       598.92 |            45 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/preiswerte-und-gem%C3%BCtliche-2-zimmer-wohnung-2042750631/)                                                                                                                                                            | Oct 14, 11:18      |
|       766    |            65 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sozialbau-wohnung-geringergasse13-in-1110-wien-877641539/)                                                                                                                                                                    | Oct 14, 10:57      |
|       773.7  |            50 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-sonnige-renovierte-2-zimmerwohnung---goldschlagstra%C3%9Fe-1646467448/)                                                                                                                                                  | Oct 14, 10:55      |
|       798.62 |            44 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/1030-wien---absolut-neuwertig-%22panorama3%22-in-der-leopold-b%C3%B6hm-stra%C3%9Fe---2-zimmer-wohnung-mit-loggia-und-garagenplatz-1405391438/)                                                                          | Oct 13, 17:34      |
|       458.6  |            42 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristete-genossenschaftswohnungen-mit-kaufoption-und-top-ausstattung-im-erstbezug-in-gr%C3%BCnlage-n%C3%A4he-auhofcenter%21-direktbesichtigung-am-mittwoch-den-15.10.25-von-08:00-uhr-bis-10:00-uhr-vor-ort.-h-1177863098/) | Oct 13, 17:05      |
|       540.33 |            53 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%28reserviert%29-anfrage-stopp---direktvergabe-2-zimmer-gemeindewohnung-1090-wien---n%C3%A4he-franz-josefs-bahnhof-1153588300/)                                                                                              | Oct 13, 16:08      |
|       744    |            72 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%22direktvergabe-2-zimmer-%2B-wohnzimmer-1030-wien-n%C3%A4he-u3-kardinal-nagl-platz%22-797878979/)                                                                                                                      | Oct 13, 13:54      |
