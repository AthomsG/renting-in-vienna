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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       460    |            44 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/gemeindewohnung-/-wohnticket-bis-28.02.26-883482331/)                                                                                                                             | Mar 19, 22:12      |
|       766    |            30 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter-gesucht%21-30m%C2%B2-wohnung-im-10.-bezirk---top-lage---ab-01.05.-1667822091/)                                                                                          | Mar 19, 21:01      |
|       780    |            72 |          4 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zu-vergeben-2007273524/)                                                                                                                                     | Mar 19, 15:27      |
|       492    |            60 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/direktvergabe-2-zimmer-gemeindewohnung-1160-wien-1480423959/)                                                                                                                      | Mar 19, 10:21      |
|       643.82 |            59 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-vormerkscheinnummer.-30.11.2025-2-zimmer-gemeindewohnung-%7C-59-m%C2%B2-%7C-balkon-%7C-frisch-renoviert-%7C-n%C3%A4he-u3-h%C3%BCtteldorfer-stra%C3%9Fe-1594803205/) | Mar 19, 10:02      |
|       669    |            60 |          3 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-altbau-beim-brunnenmarkt%21-1246458591/)                                                                                                                                         | Mar 19, 09:58      |
