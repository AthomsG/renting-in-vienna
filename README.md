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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       557.12 |            43 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/erstbezug-nach-sanierung---2-zimmer-wohnung-in-zentraler-lage-1771938847/)                                             | Mar 03, 14:51      |
|       594.46 |            44 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nahe-sch%C3%B6nbrunn-%7C-2--zimmer-neubauwohnung-%7C-befristet-%7C-ab-sofort-1738149635/)                                                | Mar 03, 14:27      |
|       715.83 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-sehr-helle-dachgeschosswohnung-mit-sonniger-terrasse---2er-wg-tauglich---vis-a-vis-u3-station-enkplatz-gelegen%21-2080381507/) | Mar 03, 14:27      |
|       728    |            61 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gut-geschnittene-wohnung-in-guter-lage-932927905/)                                                                                     | Mar 03, 13:49      |
|       768.25 |            49 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/terrassentraum-f%C3%BCr-p%C3%A4rchen---wohnung-mit-perfektem-grundriss---n%C3%A4he-einkaufszentrum-huma-eleven-1648037480/)            | Mar 03, 13:18      |
|       760    |            79 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/3-zimmer-gemeinde-wohnung-im-1020-wien-wwt/-vk-906762386/)                                                                          | Mar 03, 11:49      |
|       780    |            45 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sehr-sch%C3%B6ne-2---zimmer-neubauwohnung-n%C3%A4he-...-1252313140/)                                                                   | Mar 03, 11:21      |
|       777.9  |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-perfektem-grundriss---n%C3%A4he-kaiserebersdorf-2107925973/)                                             | Mar 03, 11:20      |
|       789.3  |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-schloss-neugeb%C3%A4ude---wohnung-perfekt-f%C3%BCr-singles-oder-p%C3%A4rchen-mit-freifl%C3%A4che-989562853/)                 | Mar 03, 11:20      |
|       700    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmer-neubauwohnung-mit-balkon-im-10.-bezirk---himberger-stra%C3%9Fe-1106087063/)                                           | Mar 03, 11:12      |
|       741.74 |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ol%C3%A9-ol%C3%A9---oh-la-laa-%21-bezugsfertig-mai-2025%21-1101051871/)                                                                | Mar 03, 10:22      |
|       796.4  |            52 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/genossenschaftswohnung-mit-balkon-&-top-ausstattung-in-1030-wien-1711325663/)                                                    | Mar 03, 08:59      |
|       786.55 |            54 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gumpendorferstra%C3%9Fe%21-helles-moderne-2-zimmer-mietwohnung-n%C3%A4he-raimundtheater%21-1292456913/)                                | Mar 02, 17:54      |
|       432    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen-ticket-31.12.2024-1969505461/)                                                                             | Mar 02, 16:20      |
