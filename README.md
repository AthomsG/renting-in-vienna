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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       462    |            47 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-zu-vermieten-2114036713/)                                                                                 | Mar 03, 19:00      |
|       560    |            39 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtliche-erdgescho%C3%9Fwohnung-sucht-langfristige/n-mieter/in--1977850985/)                                     | Mar 03, 18:13      |
|       795.01 |            38 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/diesterweggasse---2-zimmer-wohnung-mit-garage-zu-vermieten-1343640298/)                                                   | Mar 03, 18:06      |
|       763.42 |            39 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2---zimmer---wohnung-in-ausgezeichneter-lage-1167983564/)                                                     | Mar 03, 14:46      |
|       573.7  |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-2-zimmer-gemeindewohnung-am-wienerberg%21-vormerkschein-bis-31.12.2025-1159323993/)                    | Mar 03, 14:11      |
|       489    |            45 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe---2-zimmer-%28vormerkschein-/-wohnticket-erforderlich%29-1657265674/)                      | Mar 03, 14:07      |
|       649    |            45 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-1355374634/)                                                      | Mar 03, 14:06      |
|       799    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---charmante-2-zimmer-wohnung-mit-sonnigem-balkon---ihre-wohlf%C3%BChloase-am-laaer-berg-1406445669/)         | Mar 03, 13:32      |
|       729    |            43 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-einbauk%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-hs17-top-a-15-2058325697/) | Mar 03, 12:58      |
|       590    |            75 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wg---mitbewohnerin-gesucht-1279290233/)                                                                                 | Mar 03, 12:00      |
|       560    |            50 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-wiener-wohnen-838763643/)                                                                                 | Mar 03, 10:14      |
|       617.65 |            49 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/geniale-2-zimmerwohnung-im-obersten-stock-mit-lift-906423290/)                                                         | Mar 03, 09:20      |
