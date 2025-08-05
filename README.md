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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       643.77 |            47 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-gem%C3%BCtliche-wohnung-in-wien-ottakring---top-zustand-1929052702/)                                                                | Aug 05, 20:13      |
|       770    |            48 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/49m2-im-ruhigen-teil-simmerings-1632409426/)                                                                                                    | Aug 05, 19:23      |
|       702.78 |            44 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/keine-anrufe-bitte%21-nur-schriftliche-anfragen%21-nette-2-zimmer-wohnung-in-der-erlachgasse-1836209989/)                                       | Aug 05, 16:19      |
|       767.5  |            58 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/super-neubauwohnung-%28-2-zimmer-%29---direkt-bei-der-u1-altes-landgut%21-%21-1094706616/)                                                      | Aug 05, 15:27      |
|       748    |           nan |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktives-wohnen-mitten-im-sonnwendviertel-1097966689/)                                                                                       | Aug 05, 15:27      |
|       750.52 |            51 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ausschlie%C3%9Flich-schriftliche-anfragen-bitte-keine-anrufe%21-unbefristet.-aparte-2-zimmer-loggia--wohnung-in-der-karmarschgasse-1878392286/) | Aug 05, 14:19      |
|       790    |            65 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-repr%C3%A4sentative-2---zimmer-unbefristet-1599829638/)                                                                                     | Aug 05, 14:17      |
|       680    |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-43m%C2%B2-gro%C3%9Fe-2-zimmer-wohnung-in-1160-zu-vermieten-680-euro-%28inkl.-bk%29-1549283274/)                                           | Aug 05, 12:14      |
|       546.53 |            48 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-gemeindebau:-1020-2.-bezirk-bei-donau-2-zimmer-mit-balkon-779695420/)                                                          | Aug 05, 11:58      |
|       687.41 |            52 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%2Aideal-f%C3%BCr-stadtliebhaber%2A-1649797761/)                                                                                                   | Aug 05, 11:18      |
|       799.99 |            48 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/neubau-%7C-loggia-%7C-albrechtskreithgasse-2068444551/)                                                                                         | Aug 05, 03:33      |
|       750    |            52 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtlicher-neubau-mit-gartenterrasse-967625875/)                                                                                          | Aug 05, 03:33      |
|       699    |            31 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/15-zimmer-in-toller-lage%21%21-u3-schlachthausgasse-in-gehweite-1634179596/)                                                              | Aug 04, 21:54      |
