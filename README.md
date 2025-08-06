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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       649    |            33 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-15.08.---1100-wien---ansprechende-neubau-singlewohnung-inkl.-k%C3%BCchenzeile-mit-balkon-1638962527/)                                                                     | Aug 06, 13:37      |
|       660    |            63 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gem%C3%BCtliche-2-zimmer-wohnung-nahe-auhofcenter-mit-gartenben%C3%BCtzung-ab-sofort-1850160120/)                                                                              | Aug 06, 12:26      |
|       714    |            56 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmantes-2-zimmer-apartment-in-wien-favoriten-1004056149/)                                                                                                                 | Aug 06, 12:07      |
|       408    |            56 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-886363684/)                                                                                              | Aug 06, 11:55      |
|       523.27 |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-miete:-2-zimmer-altbau-in-hoflage-1685389604/)                                                                                                                  | Aug 06, 10:55      |
|       758.6  |            66 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/studentenhit%21-ruhige-und-helle-2-zimmer-wohnung-965110865/)                                                                                                                | Aug 06, 09:48      |
|       672.63 |            69 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sch%C3%B6ne-2-zimmer-gemeindewohnung-in-1050-wien-/-ideal-als-2er-wg-%28wiener-wohnticket-vor-stichtag-30.06.2025-n%C3%B6tig%21%29-1725248488/)                             | Aug 06, 09:46      |
|       689    |            45 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3-zimmerwohnung-2012154494/)                                                                                                                                                   | Aug 06, 06:17      |
|       517    |            48 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung---vormerkschein-30.05.2025---top-lage---03.-bezirk---wiener-wohnen-/-wiener-wohnticket---billig---4250%E2%82%AC-abl%C3%B6se---bezugsfertig-944922347/) | Aug 06, 00:56      |
|       643.77 |            47 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-gem%C3%BCtliche-wohnung-in-wien-ottakring---top-zustand-1929052702/)                                                                                             | Aug 05, 20:13      |
|       770    |            48 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/49m2-im-ruhigen-teil-simmerings-1632409426/)                                                                                                                                 | Aug 05, 19:23      |
|       748    |           nan |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktives-wohnen-mitten-im-sonnwendviertel-1097966689/)                                                                                                                    | Aug 05, 15:27      |
|       767.5  |            58 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/super-neubauwohnung-%28-2-zimmer-%29---direkt-bei-der-u1-altes-landgut%21-%21-1094706616/)                                                                                   | Aug 05, 15:27      |
|       790    |            65 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-repr%C3%A4sentative-2---zimmer-unbefristet-1599829638/)                                                                                                                  | Aug 05, 14:17      |
|       680    |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-43m%C2%B2-gro%C3%9Fe-2-zimmer-wohnung-in-1160-zu-vermieten-680-euro-%28inkl.-bk%29-1549283274/)                                                                        | Aug 05, 12:14      |
|       546.53 |            48 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-gemeindebau:-1020-2.-bezirk-bei-donau-2-zimmer-mit-balkon-779695420/)                                                                                       | Aug 05, 11:58      |
