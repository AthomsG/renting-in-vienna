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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       784.31 |            51 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-51m%C2%B2-altbau-%2B-8m%C2%B2-terrasse-mit-einbauk%C3%BCche-und-lift---1100-wien%21-2016217767/) | Jul 03, 17:35      |
|       786.03 |            69 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-dachgescho%C3%9Fwohnung-mit-loggia---1120-wien-erlgasse-21-23-1622952647/)                                       | Jul 03, 14:22      |
|       736.23 |            70 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wiener-wohnen-direktvergabe-vms-6/25-1281866554/)                                                                                | Jul 03, 11:46      |
|       790    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-m%C3%B6blierte-wohnung-1471798239/)                                                                                      | Jul 03, 11:04      |
|       780    |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/sch%C3%B6ne-ruhige-2-zimmer-wohnung-nahe-wu-und-praterpark-626188180/)                                                      | Jul 03, 10:43      |
|       710    |            40 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-15-zimmer-nahe-sch%C3%B6nbrunn-1783153900/)                                                                               | Jul 03, 09:09      |
|       615    |            60 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-direktvergabe-%28wohnticket-31.05.2025%29-mit-abl%C3%B6se-4.500%E2%82%AC-1657361863/)                                  | Jul 02, 23:45      |
|       408    |            56 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-1962386555/)                                               | Jul 02, 20:40      |
|       790    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Aall-inklusive-apartment-schlafzimmer%2B-wohnzimmer%2A-n%C3%A4he-hauptbahnhof-2083203679/)                                   | Jul 02, 19:52      |
|       750    |            52 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-altbauwohnung-zum-wohlf%C3%BChlen-2015553389/)                                                                           | Jul 02, 19:01      |
|       798.75 |            51 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei:-ruhiger-51m%C2%B2-neubau-mit-2-zimmern-und-einbauk%C3%BCche---1170-wien-1147640200/)                             | Jul 02, 18:35      |
