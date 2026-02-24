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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       659    |            48 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-1698701761/)                                                             | Feb 24, 10:28      |
|       749    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/s%C3%BCdlich-ausgerichtete-2---zimmer-wohnung-inkl.-neuer-einbauk%C3%BCche-mit-optimaler-infrastruktur-933175927/)               | Feb 24, 09:28      |
|       558.82 |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-1100-wien-57m%C2%B2-direktvergabe-mit-abl%C3%B6se-f%C3%BCr-vormerkschein-bis-31.01.2026-2-r%C3%A4ume-801237623/) | Feb 24, 09:26      |
|       790    |            41 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtlicher-neubau-%7C-albrechtskreithgasse-%7C-fu%C3%9Fbodenheizung-1911080385/)                                           | Feb 23, 21:39      |
|       700    |            54 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sch%C3%B6ne-2-zimmerwohnung-1305425569/)                                                                                         | Feb 23, 19:18      |
|       625.17 |            35 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%2Akleinod-in-hofruhelage%2A-1824059805/)                                                                                           | Feb 23, 14:32      |
|       669    |            60 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-altbau-beim-brunnenmarkt%21-1706155422/)                                                                                       | Feb 23, 14:18      |
|       795    |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-%2A-wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1944816924/)                                   | Feb 23, 11:31      |
|       437    |            35 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%28reserviert%29-helle-wohnung-mit-ausgezeichneter-verkehrsanbindung-2074412719/)                                | Feb 23, 11:31      |
|       650    |            60 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/direktvergabe--helle-3-zimmer-gemeindewohnung-vm-bis-31.01.2026-876350000/)                                                        | Feb 23, 11:10      |
|       750    |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wohnen-bei-der-mariahilfer-stra%C3%9Fe--balkon-ruhelage-provisionsfrei-1521716295/)                              | Feb 23, 10:30      |
|       612    |            70 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sozialbau-wohnung-958493330/)                                                                                                    | Feb 23, 10:25      |
