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
|       767.14 |            91 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2A%2A-3-zimmer-%2A%2A-altbauwohnung-in-zentraler-lage-1773777006/)                         | Aug 08, 10:34      |
|       551.19 |            49 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-miete:-ger%C3%A4umiger-2-zimmer-altbau-1723898219/)                           | Aug 08, 10:26      |
|       561.43 |            49 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristet:-2-zimmer-altbau-nahe-matzleinsdorfer-platz-1930404390/)                       | Aug 08, 10:26      |
|       790    |            64 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-wohnung-mit-guter-verkehrsanbindung-1221127411/)                                     | Aug 08, 07:54      |
|       760.01 |            57 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-nahe-wiener-hauptbahnhof-1098035577/)                                     | Aug 07, 21:34      |
|       792    |           nan |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnen-am-wienerberg---beste-lage-im-s%C3%BCden-von-wien-1351958650/)                      | Aug 07, 17:07      |
|       480    |            42 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wiener-wohnen---direktvergabe/-42qm/-2-zimmer-1238706475/)                                  | Aug 07, 14:19      |
|       749.03 |            57 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung-beim-gellertplatz-im-10.bezirk%21-1061535800/)                      | Aug 07, 13:37      |
|       495.53 |            58 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe--2-zimmer-wohnung--nur-mit-wiener-wohn-ticket-f%C3%BCr-2-zimmer-1008715821/) | Aug 07, 12:32      |
|       617    |            53 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-gemeindewohnung-vmd-bis-31.7.2025-1440724038/)                                      | Aug 07, 11:24      |
|       653    |            51 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%21%21-anfragenstop%21%21-helle-wohnung-im-3.-bezirk-1999661513/)                    | Aug 07, 09:20      |
