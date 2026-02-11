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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       540    |            56 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-gemeindewohnung-mit-vormerkdatum-1.01.2026-1420406863/)                                                                 | Feb 11, 22:19      |
|       745    |            44 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/helle-ruhige-2-zimmer-altbauwohnung-%2844-m%C2%B2%29---toplage-neustiftgasse-48-1070-wien---m%C3%B6bliert-innenhoflage-2145004924/) | Feb 11, 21:45      |
|       576.81 |            44 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charmante-1-zimmer-wohnung-mit-wohnk%C3%BCche----sechshauserstra%C3%9Fe-1037071001/)                             | Feb 11, 21:41      |
|       780    |            29 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-1807064573/)                                                                                                              | Feb 11, 18:42      |
|       788.33 |            56 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/1040-sch%C3%B6ne-2-zimmer-wohnung-nahe-alois-drasche-park-2072964451/)                                                              | Feb 11, 18:26      |
|       505    |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-direktvergabe-gemeindewohnung-1030-1013241852/)                                                                   | Feb 11, 15:46      |
|       770    |            56 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/schicke-mietwohnung-in-privater-jugendstil-villa-mit-zwei-zimmern-568557971/)                                                     | Feb 11, 15:42      |
|       793.75 |            49 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/hochwertig-&-hell-///-verf%C3%BCgbar-ab-april-///-balkonwohnung-in-sch%C3%B6ner-lage-nahe-flughafen-wien-969541163/)             | Feb 11, 14:19      |
|       668.5  |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2--zimmer-wohnung-%7C-unbefristet-&-u-bahn-n%C3%A4he-1834819335/)                                              | Feb 11, 13:58      |
|       528    |            55 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-wohnung-auf-6-monate-befristet-in-untermiete-55m%C2%B2-1052819793/)                                                       | Feb 11, 09:30      |
