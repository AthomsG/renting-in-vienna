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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       533.73 |            55 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gepflegte-altbauwohnung-mit-2-zentral-zimmern-%7C-hochparterre-1787529291/)                                             | Jun 09, 15:25      |
|       770    |            45 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung-otto-probst-str.-36-1100-wien-1571396725/)                                                       | Jun 09, 14:14      |
|       690    |            35 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/schicke-singlewohnung-mit-weitblick-1762459074/)                                                                          | Jun 09, 13:04      |
|       729.01 |            43 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-mit-dachschr%C3%A4ge-inkl.-k%C3%BCche-dachterrasse-und-kellerabteil-/hs28-top-2-261-2003606817/) | Jun 09, 12:29      |
|       729    |            68 |          3 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-2125652495/)                                                                                            | Jun 08, 18:32      |
|       750    |            45 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmerwohnung-im-12.-bezirk---kompakt-hell-und-zentral-gelegen-1431690822/)                                            | Jun 08, 15:24      |
