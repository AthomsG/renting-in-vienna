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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       780    |            71 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hofseitige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen%2A%2A%2Aunbefristet%2A%2A%2A-1781169223/)                                                                 | Feb 07, 11:58      |
|       460    |            45 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wohnung-weitergabe-%28nur-mit-vormerkschein-von-wiener-wohnen%29-1894237741/)                                                                             | Feb 07, 09:29      |
|       752.6  |            67 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/provisionsfrei%21-helle-mietwohnung-n%C3%A4he-grillgasse-1605227571/)                                                                                           | Feb 07, 09:26      |
|       420    |            40 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-direkt-vergabe-1295931208/)                                                                                                                            | Feb 07, 08:46      |
|       432    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen-ticket-31.12.2024-1147334553/)                                                                                                      | Feb 07, 07:38      |
|       765.95 |            47 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/hofseitige-2-zimmer-stielalbauwohnung---n%C3%A4he-u1-vorgartenstra%C3%9Fe-778319933/)                                                                        | Feb 06, 19:32      |
|       548    |            36 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/provisionsfrei-f%C3%BCr-den-mieter%21-tandelmarktgasse-n%C3%A4chst-u1/u2-altbauhauptmiete-36m%C2%B2-hofruhelage-3.-stock-studenten-bevorzugt%21-1194444437/) | Feb 06, 19:29      |
|       479    |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmerwohnung-bei-u-bahn-keplerplatz-1269054020/)                                                                                                             | Feb 06, 17:44      |
|       799.88 |            57 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-unbefristeter-57m%C2%B2-altbau-mit-einbauk%C3%BCche---1140-wien-1432133190/)                                                                      | Feb 06, 17:17      |
|       739    |            50 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/%28reserviert%29-befristete-untermiete%21-m%C3%B6bliert-%21-ruhig%21-1948306609/)                                                                               | Feb 06, 16:12      |
|       532.49 |            69 |          3 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-altbauwohnung-in-der-singrienergasse-meidling-stilvoll-wohnen-mit-charakter-1044229690/)                                                               | Feb 06, 15:48      |
