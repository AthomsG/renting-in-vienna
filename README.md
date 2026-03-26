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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       690    |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-2-zimmer-neubauwohnung-mit-balkon-&-lift-direkt-bei-mariahilfer-stra%C3%9Fe---provisionsfrei-&-sofort-frei%21-1262890218/) | Mar 26, 11:02      |
|       612    |            70 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-3-zimmer-genossenschaftswohnung-mit-weitergaberecht%21-n%C3%A4he-wienerberg-1692735191/)                                                 | Mar 26, 08:57      |
|       745.5  |            59 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/charmante-2-zimmer-wohnung-in-ruhiger-lage-des-17.-bezirks-1003645918/)                                                                            | Mar 26, 02:31      |
|       768.32 |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/s%C3%BCdlich-ausgerichtete-2---zimmer-wohnung-inkl.-neuer-einbauk%C3%BCche-mit-optimaler-infrastruktur-870563782/)                               | Mar 25, 18:56      |
|       710    |            75 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/geimeindewohnung-mit-wohnticket-ab-27.2.2026-oder-fr%C3%BCher-810044625/)                                                                  | Mar 25, 17:31      |
|       526.78 |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-helle-2-zimmer-gemeindewohnung-in-ruhiger-lage-mitten-im-sch%C3%B6nen-oberlaa-1765484769/)                                                  | Mar 25, 14:43      |
