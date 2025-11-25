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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       681.81 |            49 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sonnige-2-zimmer-altbauwohnung-im-14.-bezirk-1506030422/)                                                              | Nov 25, 11:18      |
|       772.59 |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-zwei-zimmer-neubauwohnung-1031321461/)                                             | Nov 25, 10:18      |
|       775    |            61 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-1543462757/)                               | Nov 24, 18:21      |
|       799    |            47 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnquartier-wildgarten---2-zimmerwohnung-mit-terrasse-im-am-rosenh%C3%BCgel-1259276770/)                             | Nov 24, 14:19      |
|       505.48 |            46 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-gemeindewohnung-direktvergabe-vms:-bis-31.10.2025-872494085/)                                            | Nov 24, 12:35      |
|       799    |            40 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-und-geniessen-im-s%C3%BCdwesten-von-wien%21-perfekte-infrastruktur---n%C3%A4he-sch%C3%B6nbrunn%21-998178244/)  | Nov 24, 12:22      |
|       799    |            38 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-und-geniessen-im-s%C3%BCdwesten-von-wien%21-perfekte-infrastruktur---n%C3%A4he-sch%C3%B6nbrunn%21-2127905873/) | Nov 24, 11:59      |
|       799    |            46 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-und-geniessen-im-s%C3%BCdwesten-von-wien%21-perfekte-infrastruktur---n%C3%A4he-sch%C3%B6nbrunn%21-903224607/)  | Nov 24, 11:50      |
|       589.05 |            47 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-singlewohnung-im-wieden-1515048677/)                                                                | Nov 24, 11:28      |
