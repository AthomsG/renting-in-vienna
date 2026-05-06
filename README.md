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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       770    |           nan |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-mit-lebensqualit%C3%A4t-beim-schlo%C3%9F-sch%C3%B6nbrunn-1094754023/)                                                                                                  | May 06, 15:30      |
|       790    |            56 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmerwohnung-unbefristete-hauptmiete-n%C3%A4he-reumannplatz-1238161069/)                                                                                                  | May 06, 14:39      |
|       550    |            47 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/top-lage-im-zentrum-rathausn%C3%A4he-2-zimmer-550.---brutto-1718142712/)                                                                                                    | May 06, 13:20      |
|       570    |            56 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/helle-2-zimmer-wohnung-%7C-wiener-wohnen-mit-vormerkschein-%7C-56-m%C2%B2-%7C-1030-wien-%7C-n%C3%A4he-u3-&-prater-%7C-teilm%C3%B6bliert-%7C-%E2%82%AC-570-1131226445/) | May 06, 10:26      |
|       734.32 |           nan |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wurlitzergasse---hell-und-freundlich---2-zimmer-altbauwohnung-mit-guter-%C3%B6ffentlicher-verkehrsanbindung-1211027440/)                                                     | May 06, 08:52      |
|       765.66 |            56 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1042611871/)                                                                                                                               | May 06, 02:32      |
|       680    |            43 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6n-m%C3%B6blierte-charmante-2-zimmer-wohnung-nachmieter-gesucht-1163859345/)                                                                                         | May 05, 20:04      |
|       768.2  |            73 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-wohnung-mit-tarasse-in-1110-wien---direktvergabe-g%C3%BCltiges-wohn-ticket-%28ausgestellt-vor-dem-30.04.2026-wiener-wohnung-2027687734/)                            | May 05, 17:30      |
|       543.45 |            48 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-anfrage-stop-direktvergabe-gemeindewohnung-2-zimmer---nur-mit-g%C3%BCltigen-wiener-wohn-ticket-1439752635/)                                                 | May 05, 16:23      |
|       787.14 |           nan |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nur-schriftliche-anfragen-bitte.-helle-2--zimmer-wohnung-in-der-guldengasse-1597390915/)                                                                                       | May 05, 14:54      |
