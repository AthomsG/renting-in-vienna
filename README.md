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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       780    |            50 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-wohnung-mit-garten-neubau-%2850m%C2%B2-%2B-30m%C2%B2-garten%29---voll-m%C3%B6bliert---einziehen-&-wohlf%C3%BChlen%21-1276499617/) | Apr 02, 00:25      |
|       780    |            61 |          3 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3-zimmer-wohnung-vis-a-vis-sch%C3%B6nbrunn-1719434252/)                                                                                              | Apr 01, 20:58      |
|       465    |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-wohnung-881720082/)                                                                                                               | Apr 01, 18:07      |
|       795    |            59 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-wohnung-1656949656/)                                                                                                      | Apr 01, 16:58      |
|       720.89 |            46 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-ab-mai:-m%C3%B6bliertes-all-in-2-zimmer-apartment-im-2.-bezirk-nahe-wu-&-sfu-%7C-xl-bude-1177987177/)                          | Apr 01, 16:25      |
|       799    |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon---schleiergasse-1712643731/)                                                                                           | Apr 01, 12:17      |
|       450    |            50 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-2-zimmer-wohnung/-b%C3%BCro-im-14.-bezirk-1785250508/)                                                                                        | Apr 01, 11:31      |
