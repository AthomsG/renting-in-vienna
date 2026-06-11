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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       500    |            45 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-gemeindewohnung-%21%21%21-nur-mit-g%C3%BCltigem-wohnticket%21%21%21-1247449248/)                                                             | Jun 11, 20:54      |
|       795    |            43 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/g%C3%BCnstige-wohnung-komplett-ausgestattet-825329339/)                                                                                                 | Jun 11, 18:45      |
|       720.9  |            68 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-altbau-3.-bezirk-2068076405/)                                                                                                  | Jun 11, 17:43      |
|       760    |            70 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/zwischenmiete-f%C3%BCr-7-monate-von-13.7.26-bis-22.02.27-1070-wien-der-preis-ist-inkl.-strom-heizung-und-internet-ideal-f%C3%BCr-studierende-924063048/) | Jun 11, 17:36      |
|       700    |            55 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/3-zimmer-wohnung-zu-vergeben-in-ottakring-1995855874/)                                                                                                | Jun 11, 17:21      |
|       479    |            43 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung-mit-balkon-wohnticket-mit-vmd-vor-30.04.2026-ben%C3%B6tigt-1746177589/)                                                | Jun 11, 15:20      |
|       777.62 |            46 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-dg-wohnung-im-10.bezirk-n%C3%A4he-r%C3%A4umannplatz%21-2054018928/)                                                              | Jun 11, 12:54      |
|       745    |            60 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/sch%C3%B6ne-2-zimmer-wohnung---ruhig-&-zentral-935914777/)                                                                                         | Jun 11, 12:43      |
|       600    |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/50m%C2%B2-wohnung-im-ruhigem-altbau-912329812/)                                                                                                       | Jun 11, 10:44      |
|       443.64 |            59 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ger%C3%A4umige-2-zimmer-wohnung-im-1.og-1082480503/)                                                                                                  | Jun 11, 07:03      |
