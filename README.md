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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                               | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       784.28 |            48 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/h%C3%BCbsche-2-zimmer-wohnung---n%C3%A4he-elterleinplatz---4.-stock-mit-lift-2138428445/)                                       | Sep 02, 18:05      |
|       610.55 |            49 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/unbefristete-&-provisionsfreie-2-zimmer-wohnung-mit-lift-n%C3%A4he-u6-%22alser-strasse%22---1170-wien-zu-mieten%21-1412700686/) | Sep 02, 17:54      |
|       775    |            44 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/hofruhelage-2-zimmer-wohnung-mit-balkon%21-2089270214/)                                                       | Sep 02, 17:36      |
|       440    |            50 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-mit-vormerkschein-zu-vergeben---direktvergabe-ab-september-1271186979/)                                               | Sep 02, 16:38      |
|       523    |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-in-1030-wien-1296450408/)                                                                               | Sep 02, 14:24      |
|       448.4  |            34 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zimmer-wohnung-n%C3%A4he-meduni-wien-und-alserstra%C3%9Fe-1533646525/)                                                     | Sep 02, 09:22      |
|       540    |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindebauwohnung-direktvergabe-1262159336/)                                                                                 | Sep 02, 08:00      |
|       750    |            40 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/nachmieter-gesucht-1064175405/)                                                                                                | Sep 02, 07:13      |
|       780    |            41 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/2-zimmer-%7C-toplage-%7C-apollokino-n%C3%A4he-1497398593/)                                                                    | Sep 01, 21:29      |
|       550    |            70 |          3 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/3er-wg-hit-in-bestlage-%281070%29:-3-zimmer-gro%C3%9Fer-vorraum-balkon-zum-hof-super-anbindung-1398390468/)                      | Sep 01, 18:05      |
|       450    |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/reserviert-2-zimmer-gemeindewohnung-am-kardinal-nagl-platz---unbefristet-1489301078/)                                   | Sep 01, 16:59      |
