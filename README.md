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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       650.75 |            61 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristeter-hauptmiethit-1152051009/)                                                                                                 | Nov 10, 10:39      |
|       752.08 |            55 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/unbefristete-2-zimmer-wohnung-im-17.bezirk%21-1555447898/)                                                                                | Nov 10, 10:23      |
|       799    |            53 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/u3-zippererstrasse/-wg-eignung:-unbefristete-53-m2-altbaumiete-2-getrennte-zimmer-einbauk%C3%BCche-gesamtmiete-eur-799---1011752530/)   | Nov 10, 09:52      |
|       555.17 |            50 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/1030-wien-direktvergabe-gemeindewohnung-%28wr.-wohnen%29.-vormerkschein-mit-vormerkdatum-30.09.2025-vorausgesetzt%21-1895049425/) | Nov 10, 09:49      |
|       749    |            82 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gro%C3%9Fz%C3%BCgige-3-zimmerwohnung-9-monate-befristete-07/2026-untermiete-/-wg-geeignet-1425732077/)                                    | Nov 09, 20:49      |
|       460    |            55 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-2-zimmer-gemeindewohnung-im-11.-bezirk-1678200892/)                                                                       | Nov 09, 18:15      |
|       480.9  |            44 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmerwohnung-nur-mit-vormerkschein%21-786636717/)                                                                                    | Nov 09, 15:42      |
|       650    |            62 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-wiener-wohnen-ticket-3.-bezirk-3-zimmer-1099808493/)                                                              | Nov 09, 15:35      |
|       434.17 |            44 |          2 | 01. Innere Stadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1010-innere-stadt/2-zimmer-gemeindebau-wohnung-in-top-lage-im-ersten-bezirk%21-972598629/)                                                             | Nov 09, 14:25      |
|       499    |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-2-zimmer-vergabe-mit-vormerkschein-2054891655/)                                                                         | Nov 09, 14:24      |
|       450    |            41 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-gemeinde-wohnung-direktvergabe-%28nur-mit-g%C3%BCltigem-wiener-wohn-ticket-%C3%A4lter-als-30.09.2025%29-1964119504/)            | Nov 09, 14:00      |
|       799    |            42 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wundersch%C3%B6ne-2-zimmer-neubauwohnung-in-bahnhofsn%C3%A4he-1905885113/)                                                                | Nov 09, 12:27      |
