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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       680.01 |            52 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-2-zimmer-mietwohnung-.-komplett-neusaniert---ab-1.2.26-bezugsbereit-1143308813/)                                                                     | Dec 10, 11:33      |
|       565.38 |            44 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/loggiawohnung-3ter-liftstock-gr%C3%BCnruhelage-provisionsfrei-1249828696/)                                                                                        | Dec 10, 11:22      |
|       790    |            48 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zauberhafte-hoflage-in-city-n%C3%A4he%21-877100713/)                                                                                                        | Dec 10, 09:40      |
|       790    |            48 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-rennweg-n%C3%A4he-st.-marx-1793702492/)                                                                                                    | Dec 10, 08:39      |
|       533.06 |            54 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gepflegte-und-sehr-ruhige-2-zimmer-wohnung-55m%C2%B2-wohnung-in-1100-wien---ihr-neues-zuhause-f%C3%BCr-nur-miete-53306-eur%21-1170053246/)                        | Dec 09, 18:55      |
|       487.59 |            45 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-zu-vergeben-in-1140-wien---%C3%BCber-wiener-wohnen-1542772402/)                                                                                     | Dec 09, 17:36      |
|       556.77 |            55 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-ger%C3%A4umige-2-zimmer-gemeindewohnung-in-ruhiger-seitengassenlage-1559658195/)                                                                   | Dec 09, 13:14      |
|       643.82 |            59 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/vormerkscheinnummer.-30.11.2025-2-zimmer-gemeindewohnung-%7C-59-m%C2%B2-%7C-balkon-%7C-frisch-renoviert-%7C-n%C3%A4he-u3-h%C3%BCtteldorfer-stra%C3%9Fe-1568644594/) | Dec 09, 13:13      |
