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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       685.31 |            38 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/nette-mieter%2Ainnen-welcome%21-perfekt-aufgeteilte-2-zimmer-wohnung-n%C3%A4he-postsportzentrum-1186406460/)            | Nov 11, 18:36      |
|       739.2  |            48 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-balkonhit%21-anfragen-nur-per-mail---keine-anrufe%21-1865177761/)                                            | Nov 11, 18:19      |
|       534    |            40 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/superg%C3%BCnstige-altbauwohnung%21-15-zimmer-%2840-m%C2%B2%29-im-erdgeschoss%21-hofseitige-ruhelage%21-1297534125/) | Nov 11, 17:28      |
|       760    |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-nahe-wiener-hauptbahnhof-1366747352/)                                                                | Nov 11, 16:22      |
|       425.83 |            48 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeindewohnung-1123464909/)                                                                          | Nov 11, 15:39      |
|       790    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wohnung-1960972011/)                                                                                  | Nov 11, 13:41      |
|       601.45 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-u1-ii-2-zimmer-ii-separate-k%C3%BCche-ii-beim-hauptbahnhof-wien-1946975243/)                                | Nov 11, 13:26      |
|       702.31 |            54 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6nes-zuhause-in-ruhelage-802069681/)                                                                          | Nov 11, 12:54      |
|       577    |            65 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-1905749197/)                                                                                          | Nov 11, 12:48      |
|       663.38 |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-freundliche-altbauwohnung-im-vierten-liftstock%21-427519915/)                                   | Nov 11, 11:49      |
|       780    |            53 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wundersch%C3%B6ne-2-zimmer-wohnung-in-absoluter-ruhelage-1952512620/)                                                   | Nov 11, 05:45      |
|       776.15 |            60 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/2-zimmerwohnung-n%C3%A4he-hauptbahnhof-mit-lft-1335941128/)                                                              | Nov 10, 21:32      |
