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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       761.5  |            56 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/wundersch%C3%B6ne-altbauwohnung-2-zimmer/-innenhoflage-unbefristet-1775632693/)                                        | Jun 02, 13:16      |
|       797.55 |            59 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/studentenwohnung:-sch%C3%B6ne-2-zimmer-wohnung-mit-separater-k%C3%BCche-1655137574/)                                      | Jun 02, 12:36      |
|       729.01 |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-mit-dachschr%C3%A4ge-inkl.-k%C3%BCche-dachterrasse-und-kellerabteil-/hs28-top-2-261-2003606817/) | Jun 02, 12:29      |
|       465.56 |            45 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/wohnvergabe-einer-2-zimmer-wohnung/-vormerkschein-bis-30.04.2025-1536679945/)                                        | Jun 02, 11:38      |
|       781.81 |            54 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-altbau-mit-guter-anbindung-2136377626/)                                                                         | Jun 02, 11:36      |
|       584    |            58 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe-gemeindewohnung---2-zimmer-58-m%C2%B2-zentral-2009746676/)                                                 | Jun 02, 11:11      |
|       790    |            62 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gr%C3%BCnblickwonung-1468236094/)                                                                                       | Jun 02, 10:43      |
|       795    |            40 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1395567074/)                                                             | Jun 02, 02:22      |
|       684.3  |            42 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-unbefristeter-42m%C2%B2-altbau-mit-einbauk%C3%BCche-und-2-zimmern---1140-wien-1502155482/)                | Jun 01, 17:24      |
|       579    |            54 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-direktvergabe-1811272324/)                                                                               | Jun 01, 16:41      |
