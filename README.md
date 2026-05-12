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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       700    |            54 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/m%C3%B6blierte-wohnung-im-6.-bezirk-1033462989/)                                                                                                                                | May 12, 15:39      |
|       491    |            65 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-in-1030-wien-65-m%C2%B2-%2B-balkon-stichtag-wohnticket%3B-20.4.2026-1795526358/)                                                            | May 12, 15:08      |
|       699    |            42 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/for-students-only:-bright-2-room-apartment-1283093296/)                                                                                                                           | May 12, 13:34      |
|       799    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-neu-saniert%21-ruhige-wohnung-beim-neuen-landgut-1290062485/)                                                                                   | May 12, 12:28      |
|       620    |            44 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-&-unbefristet%21-wohnung-bei-der-stadthalle%21-1759471948/)                                                                                      | May 12, 12:20      |
|       799    |            60 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei-&-unbefristet%21-ruhige-wohnung-in-bester-lage-1233134629/)                                                                                                       | May 12, 12:08      |
|       651.8  |            50 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristet-mit-untervermietungsrecht%21-individuell-gestaltbare-wohnung-mit-top-mietkonditionen-1383403702/)                                                                     | May 12, 11:03      |
|       652.31 |            62 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/karmarschgasse-/-helle-62-m%C2%B2-unbefristete-hauptmiete-/-4.-stock-ohne-lift-%28top-48-49%29-1450252873/)                                                                     | May 12, 06:45      |
|       795    |            43 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/g%C3%BCnstige-wohnung-komplett-ausgestattet-1631886649/)                                                                                                                          | May 11, 19:37      |
|       720    |            63 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/n%C3%A4he-botanischer-garten---mohsgasse-%7C-zentral-gelegene-63m%C2%B2-altbauwohnung-mit-flair-%7C-2-zimmer-%7C-k%C3%BCche-%7C-gesamtmiete-%E2%82%AC-720----1922119787/) | May 11, 18:43      |
