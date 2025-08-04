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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       698.6  |            55 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-1053963436/)                 | Aug 04, 15:31      |
|       788.38 |            53 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohntraum-mit-balkon%21-1980986696/)                                                          | Aug 04, 13:56      |
|       790    |            40 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-balkon-1217205923/)                                                               | Aug 04, 13:55      |
|       781.81 |            54 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-altbau-mit-guter-anbindung-827249145/)                                                         | Aug 04, 12:27      |
|       689    |            45 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3-zimmerwohnung-2012154494/)                                                                             | Aug 04, 11:34      |
|       785    |            37 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-neubau-mit-loggia-k%C3%BCche-und-kellerabteil-in-top-lage-/pg44-og4-787213921/) | Aug 04, 11:28      |
|       726    |           nan |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/mitten-in-meidling---nahe-schlo%C3%9F-sch%C3%B6nbrunn-870816598/)                                       | Aug 04, 10:28      |
|       450    |            45 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/traumlage-im-2.-bezirk---gepflegte-gemeindewohnung-mit-g%C3%BCnstige-miete-1507585763/)             | Aug 04, 10:05      |
|       793.65 |            38 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/moderne-2-zimmerwohnung-i-100m-zur-u3-station-kendlerstra%C3%9Fe-1945735306/)                          | Aug 03, 19:54      |
