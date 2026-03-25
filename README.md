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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       797.3  |            52 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/fu%C3%9Fg%C3%A4ngerzone-meidlinger-hauptstra%C3%9Fe---gepflegte-und-m%C3%B6blierte-2-zimmerwohnung-nahe-u6-philadelphiabr%C3%BCcke/bahnhof-meidling-1936352127/) | Mar 25, 18:00      |
|       710    |            75 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/geimeindewohnung-mit-wohnticket-ab-27.2.2026-oder-fr%C3%BCher-810044625/)                                                                                 | Mar 25, 17:31      |
|       526.78 |            51 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-helle-2-zimmer-gemeindewohnung-in-ruhiger-lage-mitten-im-sch%C3%B6nen-oberlaa-1765484769/)                                                                 | Mar 25, 14:43      |
|       799.74 |            41 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ihr-neues-zuhause-am-leberberg%21-1049061785/)                                                                                                                  | Mar 25, 10:31      |
|       757.75 |            47 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/ger%C3%A4umige-2-zimmer-wohnung-im-21.og-1126843733/)                                                                                                     | Mar 25, 02:50      |
|       765.66 |            56 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/p%C3%A4rchenhit-in-zentraler-lage-1042611871/)                                                                                                                  | Mar 25, 02:32      |
|       445    |            44 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-gemeinde-wohnung-vormerkschein-f%C3%BCr-2-zimmer-wird-ben%C3%B6tigt-1850141907/)                                                                         | Mar 24, 18:39      |
