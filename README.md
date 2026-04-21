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
|       719.75 |            47 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/m183t8/-provisionsfreie-47m%C2%B2-absolut-ruhige-1a-teilm%C3%B6blierte-2-zi-wohnung-1.-og-o-lift-n%C3%A4he-u3/-u6/-westbahnhof-%28ikea%29-1292244494/) | Apr 21, 15:29      |
|       599    |            60 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1160-wien-mit-balkon-2-zimmer-2090048457/)                                                                                                             | Apr 21, 14:12      |
|       797    |            30 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/erstbezug-/-ruhige-innenhoflage-/-neben-parkanlage-st%C3%B6berpark-/-15-zimmer-wohnung-1052323363/)                                                                    | Apr 21, 12:52      |
|       777.02 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-2-zimmer-wohnung-in-hervorragender-lage-beim-quellenplatz%21-1145179385/)                                                                                    | Apr 21, 12:33      |
|       500    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/60m%C2%B2-1515312939/)                                                                                                                                                 | Apr 21, 12:11      |
|       760    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-n%C3%A4he-u1-keplerplatz-1485414725/)                                                                                                                 | Apr 20, 19:06      |
|       620    |            45 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/sofort-bezugsfertige-ruhige-helle-2-zimmer-wohnung-45m2-von-privat-1786157741/)                                                                                     | Apr 20, 18:26      |
|       719    |            35 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.6.2026---laxenburger-stra%C3%9Fe-151---moderne-2-zimmer-singlewohnung-mit-westseitigem-balkon-im-7.-stock-1501777131/)                                            | Apr 20, 18:06      |
|       799.13 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-wohnung-mit-balkon-1777345926/)                                                                                                                       | Apr 20, 17:15      |
|       799    |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-2---zimmer-wohnung-/-n%C3%A4he-bahnhof-wien-meidling-1010736709/)                                                                                           | Apr 20, 15:48      |
