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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|          690 |            43 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%C3%B6ffis-vor-der-t%C3%BCr-&-alles-ums-eck-%7C-ruhige-innenhoflage-%7C-m%C3%B6bliert-1497510139/)        | Jun 16, 06:40      |
|          642 |            65 |          3 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-direktvergabe-in-1160-wien-nur-mit-wiener-wohnticket-919660047/)                        | Jun 15, 16:24      |
|          785 |            51 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/renovierte-neubauwohnung-bei-brg-11-und-u-3%21-1682238377/)                                             | Jun 15, 15:24      |
|          707 |            94 |          3 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-gemeindewohnung/-9411-m%C2%B27miete-707---/-abl%C3%B6se/-vormerkschein-vor-28.2.26-825003601/) | Jun 15, 09:50      |
