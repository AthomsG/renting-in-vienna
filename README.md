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
|       604.83 |            58 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%223-zimmer-gemeindewohnung---direktvergabe-%28vormerkschein-bis-30.11.2025%29-1170-wien-864637199/)                                           | Nov 21, 14:59      |
|       799    |            47 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnquartier-wildgarten---2-zimmerwohnung-mit-terrasse-im-am-rosenh%C3%BCgel-1373552723/)                                                     | Nov 21, 14:35      |
|       750    |            60 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neusanierte-wohnung-mit-jahresbeginn-startbereit--wird-gerade-komplett-neu-saniert-2145420555/)                                              | Nov 21, 14:33      |
|       594.6  |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%222-zimmer---mietwohnung-in-1100-wien-unweit-hauptbahnhof%22-1830897492/)                                                                   | Nov 21, 13:53      |
|       798.42 |            37 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sch%C3%B6ne-wohnung-15-zimmer-wohnung-mit-balkon-in-1050-wien%21-1265204279/)                                                               | Nov 21, 13:28      |
|       447.96 |            35 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28bitte-derzeit-keine-weiteren-anfragen%21%29wohnung-im-herzen-von-ottakring-helle-2-zimmer-wohnung-in-ottakring---top-lage%21-2111010397/) | Nov 21, 13:10      |
|       551.1  |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-2-zimmer-wohnung---erstbezug---unbefristet---provisionsfrei-1929129143/)                                                              | Nov 21, 11:15      |
|       799    |            38 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ne-2-zimmerwohnung-mit-balkon-in-u-bahn-n%C3%A4he-1296639656/)                                                                | Nov 21, 10:57      |
|       690    |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmewohnung-in-ottakring-2084353656/)                                                                                           | Nov 21, 10:24      |
|       690    |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmewohnung-in-ottakring-2084353656/)                                                                                           | Nov 21, 10:24      |
|       799    |            38 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-sofort%21-kompakte-singlewohnung-mit-k%C3%BCchenzeile-und-balkon-im-dachgeschoss---1100-wien-erlachplatz-1014412587/)                     | Nov 21, 08:36      |
|       799    |            39 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-2-zimmer-neubauwohnung-mit-balkon-n%C3%A4he-mariahilferstra%C3%9Fe-1743489119/)                                        | Nov 20, 20:34      |
