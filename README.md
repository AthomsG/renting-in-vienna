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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       745    |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2Aprovisionsfrei%2A-sch%C3%B6ne-lichtdurchflutete-2-zimmer-wohnung-1569081927/)                                                                           | Nov 25, 16:51      |
|       742.17 |            41 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                                         | Nov 25, 16:51      |
|       738.87 |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnen-der-zukunft-mit-erdw%C3%A4rme-und-solaranlage.-2-zi.-mit-balkon-in-der-senefeldergasse-1809689732/)                                                 | Nov 25, 16:44      |
|       780.3  |            35 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/singlehit-in-1210-wien-zu-mieten-1946913358/)                                                                                                            | Nov 25, 16:35      |
|       799.73 |            46 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/privat/-provisionsfrei%21-nette-wohnung-allein-oder-als-p%C3%A4rchen---gemeinschaftsgarten-im-hof-963647047/)                                              | Nov 25, 16:25      |
|       799    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-nahe-dem-wien-hauptbahnhof---ab-sofort-beziehbar%21-1091639000/)                                                                          | Nov 25, 16:19      |
|       725    |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-zur-miete-1262465119/)                                                                                                                    | Nov 25, 15:32      |
|       520    |            44 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-15-zimmerwohnung-im-1160-908759233/)                                                                                                                   | Nov 25, 15:19      |
|       685    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---genochplatz---8ter-liftstock---neuwertige-helle-singlewohnung-in-modernen-wohnhaus-1072719993/)                                               | Nov 25, 14:04      |
|       720    |            71 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-1753526841/)                                                                                                                            | Nov 25, 13:41      |
|       656.49 |            57 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/altbau-2-zimmer-wohnung-1052822525/)                                                                                                                       | Nov 25, 13:35      |
|       790    |            48 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/h%C3%BCbsche-2-zimmer-wohnung-1437945331/)                                                                                                              | Nov 25, 13:16      |
|       618.64 |            52 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/nahe-augarten---ca.-51-m%C2%B2---1-1/2-zimmer---6-gehminuten-zur-u4-1829234261/)                                                                         | Nov 25, 13:07      |
|       797.76 |            46 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a4-39-1306355823/)                                                                                                     | Nov 25, 12:18      |
|       762.56 |            40 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---sonnige-wohnung-mit-loggia/balkon-:-top-a3-39-1499881145/)                                                                                           | Nov 25, 12:18      |
|       799.85 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---wohnanlage-am-leberberg-:-top-a3-41-776704156/)                                                                                                      | Nov 25, 12:18      |
|       789    |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnungen-nahe-u1-kagraner-platz---aufstrebendes-wohnviertel-991040077/)                                                                    | Nov 25, 11:58      |
|       790    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stilvolles-2-zimmer-apartment-mit-sonniger-terrasse---viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-1518345975/)                                       | Nov 25, 11:55      |
|       790    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-%7C-freiraum-genie%C3%9Fen:-2-zimmer-mit-terrasse-2043360015/)                                           | Nov 25, 11:55      |
|       799    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ca.-55-m2-%282-zimmer%29-erstbezug-nach-sanierung-atelier-im-souterrain-f%C3%BCr-firma-oder-privat---all-inclusive-miete-warm-1435909554/) | Nov 25, 11:03      |
