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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       528    |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-zentrumsnah-neu-renoviert-528.---1990404233/)                                                                    | Jul 01, 16:06      |
|       609    |            86 |          3 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-in-1120-wien-nachmieter-gesucht-ab-01.08.-1436816177/)                                                             | Jul 01, 13:25      |
|       680.02 |            51 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/anzeige-1331069435/)                                                                                                        | Jul 01, 10:49      |
|       690    |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/11.braunhubergasse-provisionsfreie-unbefristete-2-zimmer-dachgeschossmiete-in-u3-n%C3%A4he-1562398321/)                   | Jul 01, 10:34      |
|       736.3  |            54 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/supermiete-sch%C3%B6ne-2-zimmerwohnung-alle-nebenr%C3%A4ume-gute-%C3%B6ffentlicher-anbindung%21-2139697869/)              | Jun 30, 16:43      |
|       746.52 |            46 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-ab-juli:-m%C3%B6bliertes-all-in-2-zimmer-apartment-im-2.-bezirk-nahe-wu-&-sfu-%7Cxl-bude-1177987177/) | Jun 30, 16:25      |
