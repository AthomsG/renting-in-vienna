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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       695.96 |            34 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/smarte-2-zimmer-wohnung-in-bester-lage---1050-wien%21-1959888018/)                                                                | Aug 25, 11:49      |
|       799.17 |            40 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/entz%C3%BCckende-2-zimmer-wohnung-mit-perfektem-grundriss-999929890/)                                                              | Aug 25, 11:37      |
|       619.3  |            46 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/schicke-hofseitige-singlewohnung-im-2.-stock-1127704684/)                                                                         | Aug 25, 10:56      |
|       625    |            52 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien-van-der-n%C3%BCllgasse:-2-zimmer-altbauwohnung-ca.-80-m2-unbefristet-und-barrierefrei-mit-lift-zu-vermieten-1371389116/) | Aug 25, 00:49      |
|       670    |            65 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-1187438720/)                                                                                   | Aug 24, 21:03      |
|       600    |            37 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/charmante-2-zimmer-wohnung-in-ruhiger-lage-1872448587/)                                                                              | Aug 24, 20:31      |
|       793.65 |            38 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/moderne-2-zimmerwohnung-i-100m-zur-u3-station-kendlerstra%C3%9Fe-1945735306/)                                                      | Aug 24, 19:54      |
|       795    |            42 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/sofort-beziehbar-1232092780/)                                                                                                     | Aug 24, 16:15      |
|       659    |            58 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet____2__zimmer-1002754567/)                                                                                              | Aug 24, 15:50      |
|       529    |            51 |          3 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/hofseitiger-altbau-nahe-yppenmarkt-1149924243/)                                                                                      | Aug 24, 12:34      |
|       777.02 |            57 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/innenhoflage-&-wg-geeignet%21-wundersch%C3%B6ne-2-zimmer-whg.-mit-garten-n%C3%A4he-wienerberg-&-fh-2106468861/)                    | Aug 24, 12:28      |
|       500.73 |            49 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindebau-direktvergabe-1821004835/)                                                                                              | Aug 24, 12:11      |
|       795    |            37 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sch%C3%B6ne-2-zimmer-neubau-wohnung-mit-balkon-1746848067/)                                                                          | Aug 24, 11:15      |
