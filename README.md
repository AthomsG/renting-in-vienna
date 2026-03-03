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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       763.42 |            39 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2---zimmer---wohnung-in-ausgezeichneter-lage-1167983564/)                                                       | Mar 03, 14:46      |
|       600    |            51 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/preishit%21-2-zimmer-wohnung%21-toplage%21-1926974095/)                                                                | Mar 03, 14:25      |
|       573.7  |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-2-zimmer-gemeindewohnung-am-wienerberg%21-vormerkschein-bis-31.12.2025-1159323993/)                      | Mar 03, 14:11      |
|       489    |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe---2-zimmer-%28vormerkschein-/-wohnticket-erforderlich%29-1657265674/)                        | Mar 03, 14:07      |
|       649    |            45 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-1355374634/)                                                        | Mar 03, 14:06      |
|       799    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---charmante-2-zimmer-wohnung-mit-sonnigem-balkon---ihre-wohlf%C3%BChloase-am-laaer-berg-1406445669/)           | Mar 03, 13:32      |
|       729    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-einbauk%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-hs17-top-a-15-2058325697/)   | Mar 03, 12:58      |
|       590    |            75 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mitbewohnerin-gesucht-1279290233/)                                                                                        | Mar 03, 12:00      |
|       675    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnige-singlewohnung-nahe-wienerberg-2057982324/)                                                                        | Mar 03, 10:54      |
|       560    |            50 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-wiener-wohnen-838763643/)                                                                                   | Mar 03, 10:14      |
|       617.65 |            49 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/geniale-2-zimmerwohnung-im-obersten-stock-mit-lift-906423290/)                                                           | Mar 03, 09:20      |
|       540    |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-sozialbau-%28nur-mit-berechtigung-f%C3%BCr-sozialbau%29-wohnung-in-1100-wien-802171179/)                         | Mar 02, 22:00      |
|       730    |            55 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/charmante-wohnung-zwischen-augarten-und-donaukanal-1112544464/)                                                        | Mar 02, 21:19      |
|       720.89 |            46 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-ab-mai:-m%C3%B6bliertes-all-in-2-zimmer-apartment-im-2.-bezirk-nahe-wu-&-sfu-%7C-xl-bude-1177987177/) | Mar 02, 16:25      |
|       700    |            36 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfreie-2-zimmer-mietwohnung-1150-wien-1589208759/)                                               | Mar 02, 16:00      |
