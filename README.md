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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       594.1  |            43 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/neu-sanierte-unbefristete-hauptmietwohnung-in-1110-wien-1502310962/)                                                                         | Sep 09, 15:26      |
|       779    |            34 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/mitten-im-dritten---erstbezug-nahe-u3-s-bahn-und-hervorragender-infrastruktur-mit-hochwertiger-ausstattung%21-1361524069/)             | Sep 09, 14:57      |
|       729    |            31 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/erstbezug-in-bestlage-nahe-u3-s-bahn-und-hervorragender-infrastruktur-mit-hochwertiger-ausstattung%21---mitten-im-dritten-2119700406/) | Sep 09, 14:57      |
|       717    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-u1-keplerplatz---erstbezug---2-zimmer-mit-wohnk%C3%BCche---n%C3%A4he-wiener-hauptbahnhof-1738458192/)                              | Sep 09, 10:49      |
|       499    |            46 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-2-zimmer-wohnung-linzer-stra%C3%9Fe-provisionsfrei-2063709268/)                                                               | Sep 08, 18:27      |
|       570.62 |            33 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-2-zimmer-wohnung-im-herzen-von-ottakring-mit-option-auf-pkw-stellplatz-2050854912/)                                                    | Sep 08, 14:30      |
