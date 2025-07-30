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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       482.07 |            37 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/komplett-sanierung-%2A%2A%2A-beim-kongressbad-und-s45-hernals-%2A%2A%2A-2-zimmer-wohnung-%2A%2A%2A-n%C3%A4he-hernalser-hauptstra%C3%9Fe-1961814576/)                             | Jul 30, 10:50      |
|       563.33 |            49 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zi-altbau---%C3%B6ffentliche-anbindung-s45-1896658046/)                                                                                                                        | Jul 30, 10:20      |
|       408    |            56 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-1524353480/)                                                                                               | Jul 30, 09:41      |
|       750    |            64 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%27%272-zimmer-wohnung-perfekt-f%C3%BCr-kleine-familien-und-studenten%27%27-1323667098/)                                                                                       | Jul 30, 07:11      |
|       517    |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/vormerkschein-30.06.2025---gemeindewohnung-top-lage---03.-bezirk---wiener-wohnen-/-wiener-wohnticket---billig---nur-4500%E2%82%AC-abl%C3%B6se---bezugsfertig-944922347/) | Jul 30, 00:56      |
|       594.63 |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-zweizimmer-wohnung-1446598904/)                                                                                                                          | Jul 29, 22:35      |
|       780    |            72 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/3-zi.-wohnung/-direktvergabe-vms-30.6.24-wienerwohnen-2134266926/)                                                                                                          | Jul 29, 22:18      |
|       790    |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direkt-bei-u%2Bs-bahn-%7C-raumwunder-%7C-fernblick-%7C-sparsam-1975754256/)                                                                                                    | Jul 29, 21:37      |
|       770    |            48 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/48m2-im-ruhigen-teil-simmerings-1632409426/)                                                                                                                                   | Jul 29, 19:23      |
|       445.72 |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-wiener-wohnen-direktvergabe-vormerkschein-30.06.2025-2-zimmer-1838038838/)                                                                              | Jul 29, 14:25      |
|       790    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nur-schriftliche-anfragen%3B-keine-anrufe-bitte%21-dg-maisonette-mit-14m%C2%B2-terrasse-in-der-erlachgasse-1531683117/)                                                        | Jul 29, 14:25      |
|       799    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-1746710282/)                                                                                                                 | Jul 29, 12:55      |
|       729.16 |            55 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/n%C3%A4he-allianz-stadion:-praktische-2-zimmer-altbau-wohnung-ca.-55qm-unbefristet-1052697857/)                                                                                  | Jul 29, 12:47      |
|       546.53 |            48 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-gemeindebau:-1020-2.-bezirk-bei-donau-2-zimmer-mit-balkon-779695420/)                                                                                         | Jul 29, 11:58      |
|       425    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-vmk-juni-2025-1025129771/)                                                                                                                                     | Jul 29, 10:00      |
|       449.36 |            30 |          3 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lager/atelier-zur-miete-in-1050-wien---ehemalige-wohnung-nahe-pilgramgasse-1798271816/)                                                                                       | Jul 29, 09:57      |
