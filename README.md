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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       780    |            77 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/2--zimmerwohnung-nur-mit-wohnticket-1490228131/)                                                                                    | Oct 27, 19:24      |
|       530.37 |            50 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeindewohnung-direcktvergabe-vormerkschein-30.09.2024-1998155311/)                                                                 | Oct 27, 18:14      |
|       773.7  |            75 |          3 | 18. Währing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/sanierte-wohnung-f%C3%BCr-zwei-medizinstudentinnen-in-perfekter-lage-%28erstbezug%29-978750611/)                                   | Oct 27, 16:13      |
|       783.3  |            76 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-76m%C2%B2-in-direktvergabe-mit-vormerkschein-und-abl%C3%B6se-zu-vergeben-1072261420/)                                 | Oct 27, 12:41      |
|       760    |            88 |          3 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinde-wohnung-direkt-vergabe-1643824892/)                                                                                         | Oct 27, 12:40      |
|       715    |            56 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/luxuri%C3%B6ser-moderner-erstbezug-in-bestlage-%2B-perfekte-infrastruktur-%2B-ideale-anbindung-2044156702/)                          | Oct 27, 12:02      |
|       500    |            47 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung---direktvergabe-g%C3%BCltiger-vormerkschein-bis-31.07.2024-erforderlich%21%21-818489687/)                              | Oct 27, 12:01      |
|       764.57 |            50 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/p%C3%A4rchenhit-mit-fu%C3%9Fbodenheizung-und-deckenk%C3%BChlung---n%C3%A4he-schloss-neugeb%C3%A4ude-1155098675/)                      | Oct 27, 10:55      |
|       783    |            44 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-sonnige-ruhige-komplett-m%C3%B6blierte-und-sehr-gepflegte-zweizimmerwohnung.-provisionsfrei%21-1867715725/)               | Oct 27, 10:52      |
|       466.28 |            43 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeindewohnung-mit-vormerkschein-01.11.24-2045459672/)                                                                             | Oct 27, 10:35      |
|       749.71 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                                       | Oct 27, 10:24      |
|       730    |            37 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ruhige-wohnung-in-der-pohlgasse-n%C3%A4he-von-u4-u6-1846982743/)                                                                       | Oct 27, 10:06      |
|       610    |            53 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/altbauwohnung-in-denkmalgesch%C3%BCtztem-biedermeierhaus-926143772/)                                                               | Oct 27, 08:26      |
|       670    |            53 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/helle-2-zimmer-sanierte-stilatbauwohnung-unbefristet-1060334591/)                                                                        | Oct 27, 07:16      |
|       777    |            44 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/freundliche-und-moderne-2-zimmer-wohnung-mit-gro%C3%9Fem-hofseitigem-balkon-nahe-u3-simmering-/-ab-1.1.25-verf%C3%BCgbar.-825410227/) | Oct 27, 03:44      |
|       780    |            48 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/neuwertige-2-zimmerwohnung/-klimatisiert/-gute-lage-im-22.-bezirk-1451008645/)                                                       | Oct 26, 20:39      |
