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
|       450    |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung-am-kardinal-nagl-platz---unbefristet-1043977975/)                                                                                                                                                                   | Oct 02, 15:38      |
|       785    |            45 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/top-lage%21-2-zimmer-privat-zu-mieten-3min-von-mariahilferstrasse-teilsaniert-764987824/)                                                                                                                                                          | Oct 02, 14:46      |
|       720    |            64 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/64m2---3-zimmer---wohnung---u3-n%C3%A4he-1301258112/)                                                                                                                                                                              | Oct 02, 12:45      |
|       580    |            54 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung-mit-loggia-1030-wien-rabenhof-1661423752/)                                                                                                                                                                          | Oct 02, 10:26      |
|       799    |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-u3-simmering---ruhelage---stellplatz-optional---zwischen-lorystra%C3%9Fe-und-simmeringer-hauptstra%C3%9Fe-1966859987/)                                                                                                                   | Oct 02, 07:21      |
|       799    |            46 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-single-wohnung-mit-vintage-flair-f%C3%BCr-individualisten-1090194387/)                                                                                                                                                            | Oct 02, 07:15      |
|       730    |            55 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sch%C3%B6ne-m%C3%B6blierte-wohnung-nahe-u3-simmering-1734964683/)                                                                                                                                                                                  | Oct 01, 21:56      |
|       515    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung/-wiener-wohnen-48m2-mit-balkon-1753913300/)                                                                                                                                                                                         | Oct 01, 20:53      |
|       552    |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nachmieter-gemeindewohnung-1761149382/)                                                                                                                                                                                                              | Oct 01, 20:37      |
|       700.39 |            50 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/helle-2-zimmerwohnung-in-1110-wien-mit-kleiner-loggia-und-perfekter-%C3%B6ffi-anbindung%21-2134528080/)                                                                                                                                            | Oct 01, 18:28      |
|       690    |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/privat-wg.-f%C3%A4hige-studentenhit-helle-sonnige-absolut-ruhige-neubauwohnung-mit-2-getr.-%28ca.-gleich-gross%29-begehbares-zimmern-in-guten-umgebung-infrastruktur-und-%C3%B6ffentliche-vehrkersm%C3%B6glichkeiten.-1464615776/) | Oct 01, 18:23      |
