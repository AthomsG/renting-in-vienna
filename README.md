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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       578    |            55 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wundersch%C3%B6ne-2-zimmer-wohnung-mit-balkon-1030-wien-%28direktvergabe%29-1305513076/)      | Jan 13, 21:32      |
|       785    |            60 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sympathische-altbauwohnung-ideal-f%C3%BCr-single-oder-p%C3%A4rchen-2146719902/)                       | Jan 13, 17:54      |
|       748.79 |            60 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmerwohnung-in-1140-zu-vermieten-1540126970/)                                                     | Jan 13, 14:35      |
|       791.28 |            44 |          2 | 08. Josefstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/bitte-nur-schriftliche-anfragen%21-ruhig-gelegene-2-zimmer-wohnung-in-der-laudongasse-1723789799/) | Jan 13, 14:20      |
|       699.99 |            39 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/himbergerstra%C3%9Fe-28-1221994285/)                                                                | Jan 13, 14:06      |
|       550    |            43 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/charmante-2--zimmerwohnung-n%C3%A4he-hanusch-krankenhaus-1169806665/)                                 | Jan 13, 12:17      |
|       518.64 |            41 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/schmuckst%C3%BCck-am-brunnenmarkt-1708858382/)                                                      | Jan 13, 11:20      |
|       453    |            62 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe-1336262096/)                                                           | Jan 13, 11:18      |
|       760    |            47 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wohnung-im-28.-stockwerk-%21-894119376/)                                                      | Jan 13, 11:04      |
