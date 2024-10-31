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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       715    |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmerwohnung-mit-perfekter-verkehrsanbindung-im-21.-bezirk-1807924268/)                                                                                                 | Oct 31, 18:57      |
|       483.01 |            46 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnug---vormerkschein-vor-31.10.24-975769396/)                                                                                                                | Oct 31, 18:43      |
|       765.37 |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/leo-131---hochwertiger-neubau-zu-fairen-preisen---gut-angebunden-%28u1-leopoldau-%2B-u6-floridsdorf%29---mit-vollm%C3%B6blierter-k%C3%BCche-&-freifl%C3%A4che-2048446564/) | Oct 31, 17:47      |
|       750    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/fernkorngasse-interessante-attraktive-teilm%C3%B6blierte-2-zimmer-wohnung-in-guter-lage-matzleinsdorferplatz-n%C3%A4he-2102019983/)                                          | Oct 31, 16:21      |
|       784.61 |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ol%C3%A9-ol%C3%A9---oh-la-laa-%21-1527551849/)                                                                                                                               | Oct 31, 16:17      |
|       787.26 |            40 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/neu-sanierte-moderne-2-zimmer-wohnung-in-zentraler-lage%21-867133540/)                                                                                                     | Oct 31, 15:36      |
|       610    |            60 |          3 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/direkt%C3%BCbergabe-mit-g%C3%BCltigem-wohn-ticket-%28wiener-wohnen-gemeindebau%29-953787569/)                                                                             | Oct 31, 15:32      |
|       599    |            57 |          3 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeinde-wohnung-1204539861/)                                                                                                                                              | Oct 31, 15:23      |
|       780    |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/top-gepflegte-helle-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-1654625958/)                                                                                               | Oct 31, 15:07      |
|       749.83 |            41 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina-%E2%97%8F-wohnanlage-am-leberberg:-top-a1-25-1416001906/)                                                                                                                | Oct 31, 14:42      |
|       773.07 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung-zur-miete%21-2037452819/)                                                                                                                       | Oct 31, 14:37      |
|       714    |            36 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wien---1150---klimatisierte-helle-singlewohnung-im-6ten-liftstock---n%C3%A4he-u6-station--gumpendorferstra%C3%9Fe-1762056592/)                               | Oct 31, 14:06      |
|       749    |            36 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/1210-wien---sensationelle-ruhige-neubau-gartenwohnung-inklusive-komplettk%C3%BCche-1513762631/)                                                                            | Oct 31, 14:06      |
|       770.78 |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug---ruhige-und-zentral-begehbare-2-zimmerwohnung-gleich-bei-der-u1-troststra%C3%9Fe%21-1226234220/)                                                                  | Oct 31, 13:26      |
|       725    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-erstbezug-mit-kleinem-balkon-1162558783/)                                                                                                                                | Oct 31, 12:58      |
|       798.77 |            53 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-zweizimmerwohnung-mit-en-suite-bad-2008849716/)                                                                                                                    | Oct 31, 12:22      |
|       624.87 |            37 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/erstbezug-nach-sanierung%21-gut-aufgeteilte-2-zimmer-wohnung-im-21.-bezirk%21-845263583/)                                                                                  | Oct 31, 12:22      |
|       795    |            42 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/dachterrassenwohnung-neubau-2-zimmer-inkl.-komplettk%C3%BCche-und-kellerabteil-/-k2-61-1165590027/)                                                                         | Oct 31, 11:57      |
|       513.88 |            51 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe-gemeindewohnung-920841236/)                                                                                                                                     | Oct 31, 11:52      |
|       750    |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernisierte-2-zimmer-wohnung-in-direkter-u-bahn-und-fh-campus-n%C3%A4he-1740397186/)                                                                                       | Oct 31, 11:16      |
