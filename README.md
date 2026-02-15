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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                               | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       613.63 |            62 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe-mit-balkon-und-blick-auf-parkanlage-1837665499/)                                               | Feb 15, 23:22      |
|       780    |            72 |          4 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zu-vergeben-786701094/)                                                                                 | Feb 15, 20:49      |
|       572.22 |            29 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gem%C3%BCtliche-studenten/-singlewohnung-1049497895/)                                                                           | Feb 15, 19:29      |
|       557    |            55 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/wundersch%C3%B6ne-gemeindewohnung-55-m%C2%B2-im-2.-bezirk-%28direktvergabe%29-direkt-an-u1-1446005202/)                    | Feb 15, 19:29      |
|       570    |            59 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/privat-nette-mitbewohnerin-gesucht-%28koffer-packen-und-einziehen%21%29-874496374/)                                          | Feb 15, 18:40      |
|       585    |            57 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung---direktvergabe---vormerkschein-bis-31.01.2026-994524701/)                                              | Feb 15, 17:24      |
|       768.45 |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/geniale-2-zimmer-neubauwohnung---zwischen-matzleinsdorfer-platz-und-waldm%C3%BCllerpark-2050470020/)                          | Feb 15, 16:15      |
|       604    |            51 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnen-ohne-aufwand:-komplett-eingerichtete-2-zimmer-wohnung-%21%21-keine-gemeind-/-genossenschaftswohnung%21%21-2102095229/) | Feb 15, 15:44      |
|       700    |            53 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-quellenstra%C3%9Fe-991405980/)                                                                               | Feb 15, 13:54      |
|       540    |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-f%C3%BCr-singles-junge-paare-und-studenten-888236044/)                                                                | Feb 15, 13:09      |
|       430    |            39 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-1050-wien-1748160217/)                                                                                       | Feb 15, 07:02      |
|       535    |            53 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-am-augarten-%28vormerkschein-mit-3-zimmern-notwendig%29-2026297791/)                                       | Feb 15, 06:40      |
