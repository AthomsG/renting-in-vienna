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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       540    |            49 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohunung-im-5.-bezirk-1754240012/)                                                                                                                                                                                                        | Dec 17, 13:30      |
|       570    |            58 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gut-geschnittene-2-zimmer-wohnung-%28direktvergabe%29-928739665/)                                                                                                                                                                                  | Dec 17, 13:21      |
|       595    |            52 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sonniger-altbau-nahe-u6-dresdnerstra%C3%9Fe-1109947926/)                                                                                                                                                                                         | Dec 17, 11:59      |
|       795    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---gem%C3%BCtliche-2-zimmer-wohnung-mit-balkon---ihr-neues-zuhause-wartet%21-am-laaer-berg-1843229963/)                                                                                                                                  | Dec 17, 11:39      |
|       464.02 |            55 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ruhige-2-zimmer-gemeindewohnung-mit-loggia-1014829857/)                                                                                                                                                                                             | Dec 17, 11:09      |
|       730.01 |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-wohnung-n%C3%A4he-u4%21-1349280013/)                                                                                                                                                                                                        | Dec 17, 09:53      |
|       699.93 |            49 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sonniges-&-gartenseitiges-2-zimmer-apartment-%28-bj-1993-%29-1247645128/)                                                                                                                                                                            | Dec 17, 09:47      |
|       640.01 |            33 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/nette-2-zimmer--altbauwohnung-n%C3%A4he-w%C3%A4hringer-stra%C3%9Fe-1246524397/)                                                                                                                                                                   | Dec 17, 09:26      |
|       562.31 |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/atelier-:-%29---%3E.-ist-keine-mietwohnung-preiswert-&-aussergew%C3%B6hnlich---56231-eur-bruttomiete-993515347/)                                                                                                                                   | Dec 17, 09:18      |
|       748.44 |            64 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/erstbezug-nach-generalsanierung-1789071851/)                                                                                                                                                                                                     | Dec 17, 09:13      |
|       675.4  |            57 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/hofruhelage/-br%C3%BCnnerstra%C3%9Fe-helle-top-gepflegte-2-zimmer-altbauwohnung-1433733756/)                                                                                                                                                     | Dec 17, 09:13      |
|       721.25 |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-sanierung:-2-zimmer-wohnung-im-gr%C3%BCnen-1763482013/)                                                                                                                                                                              | Dec 17, 02:45      |
|       600    |            46 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%2A%2A%2Abitte-keine-neue-anfrage---habe-schon-%C3%BCber-100-schreiben-in-einem-tag-bekommen-%2A%2A%2Asuche-nachmieter-f%C3%BCr-eine-46m%C2%B2-altbauwohnung-in-der-n%C3%A4he-von-landstra%C3%9Fer-hauptstra%C3%9Fe-/-juchgasse-1911941489/) | Dec 16, 22:06      |
|       680    |            81 |          3 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/gemeinde-wohnung-vormerkschein-31.05.2024-1850603245/)                                                                                                                                                                                           | Dec 16, 21:33      |
|       795    |            41 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/neubau-2-zimmer-%2B-loggia-/-u3-simmering-%28privat-provisionsfrei%29-2119696154/)                                                                                                                                                                 | Dec 16, 21:03      |
|       795    |            80 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%28reserviert%29-80-m%C2%B2-gemeindewohnung-mit-balkon-3-wohnr%C3%A4ume---direktvergabe-1272762783/)                                                                                                                                              | Dec 16, 20:51      |
|       490    |            47 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-eckwohnung-1066730584/)                                                                                                                                                                                                                     | Dec 16, 18:34      |
|       692.32 |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1317724224/)                                                                                                                                                                 | Dec 16, 17:21      |
|       742.18 |            41 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                                                                                                                                 | Dec 16, 16:51      |
|       647.28 |            61 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sanierte-gemeindewohnung---top-lage-u3&u6-2-zimmer-1138890487/)                                                                                                                                                                    | Dec 16, 16:42      |
