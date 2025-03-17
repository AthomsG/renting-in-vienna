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
|       554.57 |            39 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/n%C3%A4he-u3-station-ii-g%C3%BCnstige-singlewohnung-ii-zwischen-stadthalle-und-schmelz-ii-10min-in-die-wiener-innenstadt-2012645719/) | Mar 17, 09:59      |
|       508.43 |            46 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/360-tour-/-hofseitige-2-zimmer-altbauwohnung-in%C2%A0guter-zentraler-lage-des-14.-bezirks-890149154/)                                                   | Mar 17, 09:47      |
|       799    |            55 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wohnung-zu-vermieten-voll-m%C3%B6beliert-16.-bezirk-3-zimmer-1755000410/)                                                                             | Mar 17, 09:46      |
|       710.66 |            71 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hofseitige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen%2A%2A%2Aunbefristet%2A%2A%2A-1158573175/)                                                       | Mar 17, 09:27      |
|       789    |            66 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/achtung%21-provisionsfreie-mietwohnung-direkt-vom-eigent%C3%BCmer-1118735445/)                                                                        | Mar 17, 07:33      |
|       623.2  |            47 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/altbauwohnung-n%C3%A4he-u1-praterstern-heinestra%C3%9Fe-rueppgase-1421395830/)                                                                     | Mar 17, 03:25      |
|       680    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-im-12.-bezirk-zum-vermieten-1526874841/)                                                                                              | Mar 16, 21:22      |
|       432    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-direktvergabe-wiener-wohnen-ticket-31.12.2024-1969505461/)                                                                           | Mar 16, 16:20      |
|       795    |            54 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-2-zimmer-wohnung-mitten-im-karmeliterviertel-1647093026/)                                                                         | Mar 16, 09:44      |
