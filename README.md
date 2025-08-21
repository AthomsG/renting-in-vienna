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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       653    |            51 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%21%21-anfragenstop%21%21-helle-wohnung-im-3.-bezirk-1999661513/)                    | Aug 21, 09:20      |
|       770    |            48 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/49m2-im-ruhigen-teil-simmerings-1767924702/)                                               | Aug 21, 09:09      |
|       791.08 |            58 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3-zimmer-mietwohnung-993563951/)                                                             | Aug 21, 06:47      |
|       783.57 |            61 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-stilaltbauwohnung---hier-wohnen-sie-zentral-und-komfortabeln-%21-882078120/)     | Aug 21, 03:52      |
|       692.07 |            60 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmerwohnung-in-der-gudrunstrasse-n%C3%A4he-u1-1203841803/)                             | Aug 21, 03:52      |
|       767.5  |            58 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/super-neubauwohnung-%28-2-zimmer-%29---direkt-bei-der-u1-altes-landgut%21-%21-1110426140/) | Aug 21, 03:52      |
|       764.28 |            58 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-stilaltbauwohnung---hier-wohnen-sie-zentral-und-komfortabeln-%21-1038302807/)    | Aug 21, 03:52      |
|       797.48 |            36 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmerwohnung-innenhoflage-mit-perfekter-infrastruktur-1549811136/)              | Aug 21, 00:40      |
|       750    |            55 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/charmante-2-zimmer-wohnung-in-der-innenstadt---nachmieter-gesucht-2098708736/)             | Aug 20, 22:53      |
|       600    |            56 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/zwischenmiete-wien-zentrum-06.--20.09.-1400677942/)                                           | Aug 20, 22:27      |
|       670    |            65 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-1372172298/)                                             | Aug 20, 22:05      |
|       750    |            64 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/35-zimmer-wohnung-/-mietwohnung-quellenstra%C3%9Fe-provisionsfrei-813260777/)              | Aug 20, 18:34      |
|       700    |            43 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/single-p%C3%A4rchen-wohnung-mit-traumhaften-ausblick-2063596189/)                            | Aug 20, 10:29      |
