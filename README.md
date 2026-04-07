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
|       650    |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wohnung-in-ausgezeichneter-lage-1578959710/)                                                                                 | Apr 07, 17:44      |
|       740    |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gepflegte-2-zimmer-wohnung-nahe-hauptbahnhof-i-fischgr%C3%A4tenparkett-&-35-m-raumh%C3%B6he-2028078049/)                                     | Apr 07, 16:46      |
|       689    |            48 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhiges-apartment-mit-2-zimmern-nahe-u3-h%C3%BCtteldorfer-stra%C3%9Fe/-schmelz---provisionsfrei-1193745974/)                                   | Apr 07, 15:56      |
|       699.97 |            48 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/lichtdurchflutete-2-zimmerwohnung%21-achtung-5.-stock-ohne-lift%21-1844772271/)                                              | Apr 07, 15:40      |
|       689.62 |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/perfekte-2-zimmerwohnung-in-zentraler-lage-zu-vermieten.-1225848009/)                                                        | Apr 07, 15:29      |
|       562    |            57 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wiener-wohnen-wohnung-2-zimmer-562%E2%82%AC-miete-790503833/)                                                                                | Apr 07, 13:21      |
|       619    |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ner-altbau-am-lerchenfelder-g%C3%BCrtel-1975058464/)                                                                          | Apr 07, 12:37      |
|       620    |            42 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/provisionsfrei-&-unbefristet%21-zentral-gelegene-wohnung-n%C3%A4he-mariahilferstrasse-1521881067/)                                           | Apr 07, 12:29      |
|       460    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-lage%21-2-zimmer-gemeindewohnung-n%C3%A4he-reumannplatz---direktvergabe-1645512142/)                                                     | Apr 07, 12:23      |
|       799    |            60 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-bester-lage-1802835344/)                                                                    | Apr 07, 12:02      |
|       750    |            40 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%21%21-n%C3%A4he-matzleinsdorfer-platz-%21%21-bezaubernde-modernisierte---sehr-ruhige---2-zimmer-altbauwohnung-zu-vermieten%21-1015607113/) | Apr 07, 10:38      |
