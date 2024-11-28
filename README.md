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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       508    |            58 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sozialbau-genossenschaft-2-zimmer-1154953269/)                                                                                                                       | Nov 28, 08:18      |
|       733.77 |            42 |          2 | 19. Döbling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gem%C3%BCtliche-singlewohnung-im-19.-bezirk-1191172900/)                                                                                                          | Nov 28, 06:48      |
|       705.19 |            41 |          2 | 19. Döbling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/sch%C3%B6ne-2-zimmer-wohnung-im-19.-bezirk-1140179140/)                                                                                                           | Nov 28, 06:48      |
|       706.83 |            36 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zentral-gelegenes-apartment-in-wien---f%C3%BCr-singles-oder-paare-918995592/)                                                                                        | Nov 28, 03:31      |
|       540    |            43 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/matznerpark/helle-top-gepflegte-altbauwohnung-1005880698/)                                                                                                             | Nov 27, 21:35      |
|       770    |            48 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/kobelgasse-%7C-helle-2-zimmer-mit-gr%C3%BCnblick-%7C-u-bahn-n%C3%A4he-1934292621/)                                                                                   | Nov 27, 21:29      |
|       473.09 |            64 |          3 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug%21-/-vormerkschein-bis-31.03.2024-/-n%C3%A4chste-sammelbesichtigung-am-30.11.24-von-16-bis-18h-%21%21-891212848/) | Nov 27, 19:56      |
|       643.6  |            48 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/matzingerstra%C3%9Fe:-sch%C3%B6ne-2-zimmerwohnung-in-u-bahnn%C3%A4he-1000987570/)                                                                                      | Nov 27, 19:33      |
|       799    |            44 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-932458215/)                                                                                            | Nov 27, 18:07      |
|       799    |            44 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-970150195/)                                                                                            | Nov 27, 18:07      |
|       799    |            44 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1686856274/)                                                                                           | Nov 27, 18:07      |
|       775    |            44 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1157266369/)                                                                                           | Nov 27, 18:07      |
|       765    |            44 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1649059268/)                                                                                           | Nov 27, 18:07      |
|       799    |            44 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1228297509/)                                                                                           | Nov 27, 18:07      |
|       755    |            44 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1182797765/)                                                                                           | Nov 27, 18:07      |
|       690    |            37 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-1600458118/)                                                                                           | Nov 27, 17:56      |
|       569    |            43 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristeter-mietvertrag---2-zimmer-wohnung-maroltingergasse-61-1160-wien-834302675/)                                                                               | Nov 27, 17:35      |
|       753.5  |            37 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmerwohnung-mit-guter-anbindung-1124741977/)                                                                                                             | Nov 27, 17:16      |
|       685    |            65 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-im-14.-bezirk-zu-vergeben-1536047116/)                                                                                                                 | Nov 27, 16:58      |
|       798    |            85 |          3 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/3-zimmer-wohnhit-mit-parkblick-1994175849/)                                                                                                                          | Nov 27, 16:06      |
