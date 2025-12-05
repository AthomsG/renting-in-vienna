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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       749    |            48 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-charmante-2-zimmer-wohnung---ideal-f%C3%BCr-urbane-lebensqualit%C3%A4t%21-1645969411/) | Dec 04, 16:17      |
|       665.97 |            62 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnige-2-zimmer-gemeindewohnung-in-direktvergabe-vormerkschein-bis-31.10.2025-1724892065/)                              | Dec 04, 16:16      |
|       529.74 |            47 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-gemeinde-wohnung-in-1160-wien-977192409/)                                                                       | Dec 04, 16:05      |
|       595.83 |            55 |          2 | 06. Mariahilf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/zentrale-gemeindewohnung-in-1060-vormerkschein-bis-30.11.2025-842092453/)                                                | Dec 04, 14:53      |
|       797.98 |            71 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-1/2-zimmer-wohnung-/-unbefristet-1849187462/)                                                                          | Dec 04, 14:16      |
|       610    |            55 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2--zimmer-wohnung-zu-vermieten-777267007/)                                                                                | Dec 04, 10:53      |
|       489    |            44 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-gemeindewohnung-1915511966/)                                                                                      | Dec 04, 09:33      |
|       494    |            50 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-gemeindewohnung---vormerkschein-bis-30.09.2025-ben%C3%B6tigt-1577136135/)                                 | Dec 04, 07:34      |
|       721.52 |            68 |          3 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeindebau-wohnung-im-gr%C3%BCnen---vormerkschein-vor-30.11.2024%21-1743175922/)                            | Dec 04, 06:45      |
|       770    |            45 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung%21-keine-anrufe---anfragen-nur-per-mail%21-857140441/)                                            | Dec 04, 06:21      |
