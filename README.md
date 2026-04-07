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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       695.62 |            48 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/unbefristet---ca.-50m%C2%B2-wfl---2-zimmer-1314601499/)                                                                                         | Apr 07, 13:07      |
|       619    |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ner-altbau-am-lerchenfelder-g%C3%BCrtel-1975058464/)                                                                          | Apr 07, 12:37      |
|       620    |            42 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/provisionsfrei-&-unbefristet%21-zentral-gelegene-wohnung-n%C3%A4he-mariahilferstrasse-1521881067/)                                           | Apr 07, 12:29      |
|       460    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-lage%21-2-zimmer-gemeindewohnung-n%C3%A4he-reumannplatz---direktvergabe-1645512142/)                                                     | Apr 07, 12:23      |
|       799    |            60 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-bester-lage-1802835344/)                                                                    | Apr 07, 12:02      |
|       750    |            40 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%21%21-n%C3%A4he-matzleinsdorfer-platz-%21%21-bezaubernde-modernisierte---sehr-ruhige---2-zimmer-altbauwohnung-zu-vermieten%21-1015607113/) | Apr 07, 10:38      |
|       798    |            67 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/unbefristete-hauptmietwohnung-in-1110-wien-988901906/)                                                                                       | Apr 07, 10:24      |
|       777.77 |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/st.-marx---in-15-minuten-am-opernring-1954405848/)                                                                                           | Apr 06, 16:38      |
|       799    |            38 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/charmante-zwei-zimmer-dg-wohnung-922578526/)                                                                                                | Apr 06, 12:45      |
|       795    |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-%2A-wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1944816924/)                                               | Apr 06, 11:31      |
|       699    |            46 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei--sch%C3%B6ne-2-zimmerwohnung-n%C3%A4he-sch%C3%B6nbrunn-1186798740/)                                           | Apr 06, 11:25      |
