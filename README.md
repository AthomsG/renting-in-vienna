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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       581.99 |            43 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmerwohnung-967458711/)                                                                                                                          | Oct 20, 16:46      |
|       758.5  |            57 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/unbefristete-wg-taugliche-3-zimmer-wohnung-im-15.bezirk%21-1921752380/)                                                             | Oct 20, 16:27      |
|       520    |            50 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sonnige-gemeindewohnung-3.-bezirk-%28rabenhof%29-1197414041/)                                                                                 | Oct 20, 16:02      |
|       688.36 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-sehr-helle-wohnung-in-einem-gepflegten-stilaltbauhaus-%28mit-lift%29---direkt-bei-der-u1-station-altes-landgut-gelegen%21-2053037329/) | Oct 20, 15:17      |
|       650    |            61 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-781037298/)                                                                                                                         | Oct 20, 15:00      |
|       720    |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei:-gro%C3%9Fz%C3%BCgige-mietwohnung-in-guter-lage-nahe-mariahilfer-stra%C3%9Fe/sechshauser-stra%C3%9Fe-2092861450/)    | Oct 20, 13:20      |
|       630    |            79 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/diirektvergabe-nur-noch-im-oktober-2025-vormerkscheindatum-vor-31.8.2024---3-zimmer-gemeindewohnung-direktvergabe-1016241640/)                       | Oct 20, 09:14      |
|       696    |            70 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-gemeindewohnung-nur-mit-vms-bis-31.3.2025%21%21-1930884145/)                                                                               | Oct 19, 20:42      |
|       650    |            43 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-43m%C2%B2-zu-vermieten-keine-makler-erw%C3%BCnscht-1086173593/)                                                                              | Oct 19, 17:16      |
