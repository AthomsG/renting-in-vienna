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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       763.16 |            63 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wg-tauglich%21-63-m2-zwei-zimmer-wohnung%21-883122315/)                                                                                      | Sep 10, 15:36      |
|       716.06 |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-mit-loggia/-balkon-1258643602/)                                                                                             | Sep 10, 14:10      |
|       748    |            40 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/kleine-2-zimmer-dachwohnung-mit-terrasse%21-1491172414/)                                                                                     | Sep 10, 12:45      |
|       602.99 |            51 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/singlehit%21-wohnen-am-karmelitermarkt%21-914280885/)                                                                                     | Sep 10, 12:39      |
|       732    |            64 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnige-2-zimmer-wohnung-/-ab-sofort-/-penzing-/-ruhelage-1558181701/)                                                                         | Sep 10, 12:05      |
|       799    |            49 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmerwohnung-in-1150-wien-mit-lift-zu-vermieten-%7C-1.og-2014952068/)                                                     | Sep 10, 10:56      |
|       769    |            31 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/mitten-im-dritten---erstbezug-nahe-u3-s-bahn-und-hervorragender-infrastruktur-mit-hochwertiger-ausstattung%21-1466179046/)             | Sep 09, 17:56      |
|       779    |            34 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/mitten-im-dritten---erstbezug-nahe-u3-s-bahn-und-hervorragender-infrastruktur-mit-hochwertiger-ausstattung%21-1361524069/)             | Sep 09, 14:57      |
|       729    |            31 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/erstbezug-in-bestlage-nahe-u3-s-bahn-und-hervorragender-infrastruktur-mit-hochwertiger-ausstattung%21---mitten-im-dritten-2119700406/) | Sep 09, 14:57      |
