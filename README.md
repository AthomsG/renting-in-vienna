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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799    |            38 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-und-geniessen-im-s%C3%BCdwesten-von-wien%21-perfekte-infrastruktur---n%C3%A4he-sch%C3%B6nbrunn%21-2127905873/) | Nov 24, 11:59      |
|       799    |            46 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-und-geniessen-im-s%C3%BCdwesten-von-wien%21-perfekte-infrastruktur---n%C3%A4he-sch%C3%B6nbrunn%21-903224607/)  | Nov 24, 11:50      |
|       589.05 |            47 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-singlewohnung-im-wieden-1515048677/)                                                                | Nov 24, 11:28      |
|       753.62 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gepflegte-2-zimmer-wohnung-im-15.bezirk%21-1478431105/)                                              | Nov 24, 11:15      |
|       694.96 |            64 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhig-gelegene-2-zimmer-wohnung-beim-reumannplatz-1281950109/)                                                       | Nov 24, 11:15      |
|       774.75 |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/m%C3%B6blierte-2-zimmer-wohnung-im-15.bezirk%21-1646577131/)                                         | Nov 24, 10:29      |
|       736.5  |            57 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/unbefristete-wg-taugliche-3-zimmer-wohnung-im-15.bezirk%21-970930649/)                               | Nov 24, 10:29      |
|       708.44 |            45 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/1170-kalvarienberggasse-49/neu-sanierte-2-zimmerwohnung-ab-sofort-unbefristet-zu-vermieten-1932644050/)                | Nov 24, 10:21      |
|       654.98 |            51 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/singlewohnung-n%C3%A4he-wu-innenhoflage%21-1640575609/)                                                           | Nov 23, 19:15      |
|       780    |            50 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/1030-wien-1432761841/)                                                                                         | Nov 23, 17:31      |
|       480.9  |            44 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-gemeindewohnung-mit-vormerkschein-786636717/)                                                       | Nov 23, 15:42      |
