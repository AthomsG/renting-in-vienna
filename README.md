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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       779    |            34 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.5.2026---laxenburgerstra%C3%9Fe-151---1100-wien---traumhafte-neubau---singlewohnung-im-9ten-stock-mit-fernblick-1428023853/)    | Mar 13, 12:37      |
|       607    |            45 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/wundersch%C3%B6nes-city-appartment---voll-m%C3%B6bliert-und-ausgestattet-1429360995/)                                                   | Mar 13, 12:28      |
|       799.9  |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktive-2-zimmer-wohnung-nahe-wielandpark-in-1100-wien-zu-mieten-1998135453/)                                                     | Mar 13, 12:19      |
|       690    |            62 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-wohnung-im-3.-obergeschoss-in-1150-wien-1816572032/)                                                        | Mar 13, 10:49      |
|       606    |            59 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/direktvergabe---wiener-wohnen-1346760329/)                                                                                          | Mar 13, 10:31      |
|       719    |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/unbefristete-2-zimmer-wohnung-f%C3%BCr-selbst-sanierer-%21keine-lohnzettel-als-nachweis-erforderlich%21-1175261986/) | Mar 13, 09:13      |
|       561.72 |            47 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/16.n%C3%A4he-rankgasse-nur-f%C3%BCr-studenten%21%21-voll-m%C3%B6blierte-provisionsfreie-2-zimmer-altbaumiete-957873323/)             | Mar 13, 08:05      |
|       798.99 |            61 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/provisionsfrei:-sonniger-61m%C2%B2-altbau-mit-einbauk%C3%BCche-und-lift---1030-wien-1746398397/)                               | Mar 12, 18:35      |
