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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       495    |            58 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-in-oberlaa---wohnbedarf-2-zimmer-wiener-wohnen-1264515524/)                              | Aug 22, 10:33      |
|       459    |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/topsanierte-2-zimmerwohnung-in-gepflegtem-altbau%21-n%C3%A4he_schmelz%21-n%C3%A4he-u3-u6%21-1402528712/) | Aug 22, 09:14      |
|       758.86 |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sch%C3%B6ne-2-zimmer-wohnung-nahe-meiselmarkt-zur-miete-1093992574/)                     | Aug 22, 09:06      |
|       597.25 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter-f%C3%BCr-privatwohnung-gesucht-%2854-qm-/-eur-59725%29-1801080821/)                           | Aug 21, 22:19      |
|       537.11 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%2Anur-mit-vormerkschein%2A-2-zimmer-gemeindewohnung-2079612733/)                                        | Aug 21, 20:50      |
|       495    |            48 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/8.-bezirk-top-lage-im-zentrum-rathausn%C3%A4he-2-zimmer-495.---brutto-1047164468/)                      | Aug 21, 19:15      |
|       644.48 |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/b%C3%BCro-atelier-mit-parkplatz-zu-vermieten-2025540490/)                                                | Aug 21, 17:47      |
|       750    |            30 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%2Asmarte-2-zimmer-kleinwohnung%2A---neubau-in-sch%C3%B6nbrunn-n%C3%A4he-1145205897/)                      | Aug 21, 15:35      |
|       720    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-in-ruhelage-zu-vermieten-1625265733/)                                                             | Aug 21, 15:02      |
|       653    |            51 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%21%21-anfragenstop%21%21-helle-wohnung-im-3.-bezirk-1999661513/)                                  | Aug 21, 09:20      |
|       770    |            48 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/49m2-im-ruhigen-teil-simmerings-1767924702/)                                                             | Aug 21, 09:09      |
