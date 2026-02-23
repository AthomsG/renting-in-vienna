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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       700    |            54 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sch%C3%B6ne-2-zimmerwohnung-1305425569/)                                                                                                              | Feb 23, 19:18      |
|       742.39 |            60 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/moderne-2-zimmer-wohnung-in-top-lage%21-880683302/)                                                                                   | Feb 23, 17:35      |
|       645    |            45 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohngl%C3%BCck-unbefristet-1954917683/)                                                                                                      | Feb 23, 17:27      |
|       730    |            70 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%21%21-1160-wien---n%C3%A4he-lugner-city-%21%21-sehr-sch%C3%B6ne-gepflegte-2-zimmer-altbauwohnung-mit-hofseitigem-balkon-zu-vermieten%21-1622002963/) | Feb 23, 15:30      |
|       625.17 |            35 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%2Akleinod-in-hofruhelage%2A-1824059805/)                                                                                                                | Feb 23, 14:32      |
|       669    |            60 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-altbau-beim-brunnenmarkt%21-1706155422/)                                                                                                            | Feb 23, 14:18      |
|       794.25 |            41 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/the-arrow---die-perfekte-balance-zwischen-urbanit%C3%A4t-und-natur-1591648919/)                                                                       | Feb 23, 12:06      |
|       795    |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-%2A-wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1944816924/)                                                        | Feb 23, 11:31      |
|       437    |            35 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-wohnung-mit-ausgezeichneter-verkehrsanbindung-2074412719/)                                                                      | Feb 23, 11:31      |
|       650    |            60 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/direktvergabe--helle-3-zimmer-gemeindewohnung-vm-bis-31.01.2026-876350000/)                                                                             | Feb 23, 11:10      |
|       750    |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wohnen-bei-der-mariahilfer-stra%C3%9Fe--balkon-ruhelage-provisionsfrei-1521716295/)                                                   | Feb 23, 10:30      |
|       612    |            70 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sozialbau-wohnung-958493330/)                                                                                                                         | Feb 23, 10:25      |
|       799.55 |            45 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ne-2-zimmer-wohnung-beim-brunnenmarkt-%7C-hell-&-freundlich-%7C-dan-markenk%C3%BCche-1559704875/)                                      | Feb 23, 08:55      |
|       560    |            52 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-direktvergabe-wiener-wohnen-2-zimmer-wohnung-in-1020-mit-traumhaftem-ausblick-962824273/)                                         | Feb 23, 01:04      |
|       625    |            64 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-wien-direktvergabe-mit-vormerkschein-bis-31.01.2026-1205602308/)                                                                | Feb 22, 20:41      |
