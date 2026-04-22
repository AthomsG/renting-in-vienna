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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       690    |            54 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/befristete-hauptmietwohnung-in-1140-wien-2114073853/)                                                                                                                    | Apr 22, 08:24      |
|       799    |            67 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/unbefristete-hauptmietwohnung-in-1070-wien-1895067224/)                                                                                                                   | Apr 22, 08:22      |
|       726    |            58 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-mit-charakter-2028170334/)                                                                                                                                      | Apr 22, 08:21      |
|       765.66 |            56 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1042611871/)                                                                                                                         | Apr 22, 02:32      |
|       700    |            42 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/untermiete-befristst-1276804513/)                                                                                                                                     | Apr 21, 19:01      |
|       631.4  |            59 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe---gemeindewohnung-%28gro%C3%9Fer-balkon%29-1892352444/)                                                                                                   | Apr 21, 18:22      |
|       719.75 |            47 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/m183t8/-provisionsfreie-47m%C2%B2-absolut-ruhige-1a-teilm%C3%B6blierte-2-zi-wohnung-1.-og-o-lift-n%C3%A4he-u3/-u6/-westbahnhof-%28ikea%29-1292244494/) | Apr 21, 15:29      |
|       599    |            60 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1160-wien-mit-balkon-2-zimmer-2090048457/)                                                                                                             | Apr 21, 14:12      |
|       797    |            30 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/erstbezug-/-ruhige-innenhoflage-/-neben-parkanlage-st%C3%B6berpark-/-15-zimmer-wohnung-1052323363/)                                                                    | Apr 21, 12:52      |
|       777.02 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-2-zimmer-wohnung-in-hervorragender-lage-beim-quellenplatz%21-1145179385/)                                                                                    | Apr 21, 12:33      |
|       500    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/60m%C2%B2-1515312939/)                                                                                                                                                 | Apr 21, 12:11      |
