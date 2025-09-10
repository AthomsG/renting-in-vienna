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
|       750    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-hoflage-attraktive-unbefristete-2-zimmerwohnung-in-stil-altbau-u-1-n%C3%A4he-1319499206/)                                     | Sep 10, 16:58      |
|       779    |            31 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/erstbezug-in-bestlage-nahe-u3-s-bahn-und-hervorragender-infrastruktur-mit-hochwertiger-ausstattung%21---mitten-im-dritten-1983536972/) | Sep 10, 16:56      |
|       770.16 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ausschliesslich-schriftliche-anfragen%21-vor-1-jahr-renovierte-wohnung-in-der-erlachgasse-1134207109/)                                       | Sep 10, 16:50      |
|       430.36 |            65 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-preisg%C3%BCnstige-65m%C2%B2-wohnung-mit-2-zimmern-und-gang-wc---1140-wien-1147613536/)                                        | Sep 10, 16:17      |
|       539    |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-im-herzen-von-wien-wg-tauglich-direkt-bei-der-u3-2100654093/)                                                       | Sep 10, 15:43      |
|       716.06 |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-mit-loggia/-balkon-1258643602/)                                                                                             | Sep 10, 14:10      |
|       748    |            40 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/kleine-2-zimmer-dachwohnung-mit-terrasse%21-1491172414/)                                                                                     | Sep 10, 12:45      |
|       732    |            64 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnige-2-zimmer-wohnung-/-ab-sofort-/-penzing-/-ruhelage-1558181701/)                                                                         | Sep 10, 12:05      |
|       799    |            49 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmerwohnung-in-1150-wien-mit-lift-zu-vermieten-%7C-1.og-2014952068/)                                                     | Sep 10, 10:56      |
