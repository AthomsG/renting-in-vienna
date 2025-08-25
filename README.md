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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       792.45 |            45 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/neu%21-perfekte-2-zimmerwohnung-im-servitenviertel-zu-vermieten%21-1561567872/)                                                                                                    | Aug 25, 16:17      |
|       580    |            69 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe:-sch%C3%B6ne-gemeindewohnung-in-14-bezirk-wichtig-vormerkschein-1349613914/)                                                                                            | Aug 25, 15:01      |
|       699    |            62 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6n-sanierte-2-zimmer-wohnung-mit-neuer-k%C3%BCche-in-%2A1100-wien%2A-1465592581/)                                                                                           | Aug 25, 14:40      |
|       725    |            74 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%2A%2Af%C3%BCr-sportliche---4.-stock-ohne-aufzug%2A%2A-liebevolle-2-zimmer-wohnung-in-ausgezeichneter-lage-direkt-auf-der-wiedner-hauptstra%C3%9Fe-in-%2A1050-wien%2A-1739823707/) | Aug 25, 14:39      |
|       660    |            57 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/besichtigung-heute-dem-25.08.2025-2-zimmer-gemeindewohnung-per-direktvergabe---1090-wien-1123053108/)                                                                              | Aug 25, 12:53      |
|       619.3  |            46 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/schicke-hofseitige-singlewohnung-im-2.-stock-1127704684/)                                                                                                                          | Aug 25, 10:56      |
|       625    |            52 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien-van-der-n%C3%BCllgasse:-2-zimmer-altbauwohnung-ca.-80-m2-unbefristet-und-barrierefrei-mit-lift-zu-vermieten-1371389116/)                                                  | Aug 25, 00:49      |
|       670    |            65 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-1187438720/)                                                                                                                                    | Aug 24, 21:03      |
|       600    |            37 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-charmante-2-zimmer-wohnung-in-ruhiger-lage-1872448587/)                                                                                                              | Aug 24, 20:31      |
|       793.65 |            38 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/moderne-2-zimmerwohnung-i-100m-zur-u3-station-kendlerstra%C3%9Fe-1945735306/)                                                                                                       | Aug 24, 19:54      |
|       795    |            42 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/sofort-beziehbar-1232092780/)                                                                                                                                                      | Aug 24, 16:15      |
|       659    |            58 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet____2__zimmer-1002754567/)                                                                                                                                               | Aug 24, 15:50      |
