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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       480.9  |            44 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-gemeindewohnung-mit-vormerkschein-786636717/)             | Nov 23, 15:42      |
|       799    |            42 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wundersch%C3%B6ne-2-zimmer-neubauwohnung-in-bahnhofsn%C3%A4he-1905885113/)   | Nov 23, 12:27      |
|       700    |            62 |          2 | 06. Mariahilf | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/wohnung-6-bezirk-hauptmiete-1244088181/)                                   | Nov 23, 11:09      |
|       785    |            41 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/exklusive-2-zimmer-wohnung-in-neubau---ab-sofort-beziehbar%21-1134715618/) | Nov 23, 09:49      |
|       750    |            40 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wohnung-zur-untermiete-2008882434/)                                        | Nov 23, 00:34      |
|       720    |            41 |          2 | 04. Wieden    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/single-wohnung-in-toller-lage-1662178118/)                                    | Nov 22, 21:35      |
|       571.74 |            57 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe%21-911167932/)                               | Nov 22, 17:06      |
