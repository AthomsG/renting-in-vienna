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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       640    |            43 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/43-m%C2%B2-wohnung-n%C3%A4he-volksoper-zu-vermieten-1121615942/)                                                                                                     | Jul 08, 20:26      |
|       650    |            32 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wohnung-zu-vermieten-im-16-bez-1212086852/)                                                                                                                           | Jul 08, 16:19      |
|       445.72 |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-30.06.2025-2-zimmer-1838038838/)                                                                                      | Jul 08, 14:25      |
|       506    |            43 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-gemeindewohnung-im-3.-bezirk-mit-vormerkschein-1067587977/)                                                                                    | Jul 08, 13:04      |
|       675.18 |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/bitte-den-text-f%C3%BCr-einen-besichtigungstermin-lesen-%28siehe-weiter-unten%29-1639179769/)                                                         | Jul 08, 12:19      |
|       550    |            35 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-fr%C3%B6hliche-altbauwohnung-ruhelage-1.-stock-sucht-eine/-n-liebe/-n-mieter/-in-oder-p%C3%A4rchen-f%C3%BCr-gem%C3%BCtliches-zusammensein.-899446181/) | Jul 08, 12:08      |
|       799    |            36 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gut-geschnittene-2-zimmer-wohnung-in-ruhiger-seitenstra%C3%9Fe-nahe-u4-hietzing-1795169194/)                                                                            | Jul 08, 08:46      |
