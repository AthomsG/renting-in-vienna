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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District     | Link                                                                                                                                                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       780    |            48 |          2 | 22. Donaustadt  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/neuwertige-2-zimmerwohnung/-klimatisiert/-gute-lage-im-22.-bezirk-1451008645/)                                                                                                                                                                                                                 | Oct 26, 20:39      |
|       767.29 |            54 |          2 | 14. Penzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-und-verkehrsg%C3%BCnstige-kleinwohnung-im-eg-voll-m%C3%B6bliert%21-1785480364/)                                                                                                                                                                                                            | Oct 26, 18:35      |
|       561.11 |            41 |          2 | 12. Meidling    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristete-altbauwohnung-mit-terrasse-in-der-wolfganggasse-1679438680/)                                                                                                                                                                                                                        | Oct 26, 16:24      |
|       540    |            52 |          2 | 21. Floridsdorf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-gemeinde-wohnung-zu-direkt-vergabe-mit-wohnticket-bzw.-vormerkschein-bis-30.09.2024-2048565740/)                                                                                                                                                                                     | Oct 26, 15:36      |
|       690    |            63 |          2 | 05. Margareten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/63m%C2%B2-gemeindewohnung-2-%283%29-zimmer-%2A%2A%2Apreis-je-nach-zubeh%C3%B6r%2A%2A%2A---zentrale-lage-%282min-zum-bhf-matzleinsdorferplatz%29---neue-k%C3%BCche-%28wird-fix-mitverkauft%29---m%C3%B6blierung-auf-wunsch-mitkaufen---neu-ausgemalt-und-renoviert---sehr-gepflegt-1347180757/) | Oct 26, 13:48      |
|       649    |            35 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/fernblick---9ter-liftstock---s%C3%BCdwestseitige-sonnige-balkonwohnung---ab-1.1.2025-2135858049/)                                                                                                                                                                                               | Oct 26, 10:56      |
|       793.74 |            31 |          2 | 10. Favoriten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/allegro-tosca-&-romulus---2-zimmer-dachgeschosswohnung-mit-balkon%21-1202718444/)                                                                                                                                                                                                               | Oct 26, 07:05      |
|       791.8  |            47 |          2 | 18. Währing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/unbefristet:-2-zimmer-altbauwohnung-in-der-herbeckstrasse-1001780185/)                                                                                                                                                                                                                       | Oct 26, 03:38      |
|       759.57 |            41 |          2 | 23. Liesing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/miet-kauf%21---singlehit%21-2-zimmer-neubauwohnung-in-beliebter-wohngegend-liesing%60s---nahe-perchtholdsdorfer-heide-1095208325/)                                                                                                                                                                | Oct 25, 20:32      |
