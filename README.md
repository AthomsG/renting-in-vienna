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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       450    |            42 |          3 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/tolle-single-gemeindewohnung-in-wien-1248869842/)                                                                                                                                                            | May 20, 17:26      |
|       599    |            54 |          4 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/luxus-4-zimmer-wohnung-im-17.-bezirk-ab-15.-juli.-komplett-kernsaniert-&-vollm%C3%B6bliert-inklusive-tischlerk%C3%BCche-klima-samsung-tv-und-hochwertigen-m%C3%B6beln.-nur-599-%E2%82%AC-miete.-1714570921/) | May 20, 16:12      |
|       700    |            46 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-ruhige-altbauwohnung-ottakring-46qm-in-guter-lage-2133787169/)                                                                                                                                 | May 20, 12:21      |
|       790    |            48 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---charmante-2-zi-wohnung-mit-balkon---ihre-wohlf%C3%BChloase-am-laaer-berg-1966814260/)                                                                                                         | May 20, 09:47      |
|       617.69 |            51 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-altbauwohnung-mit-lift-in-guter-lage-des-14.-bezirks-2058704938/)                                                                                                                                   | May 20, 08:58      |
|       765.66 |            56 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1042611871/)                                                                                                                                                             | May 20, 02:32      |
