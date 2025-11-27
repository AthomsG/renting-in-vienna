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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       774.95 |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/modernes-wohnen-in-simmering-1521674692/)                                                                                                   | Nov 27, 11:35      |
|       799    |            49 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnen-in-der-lorystra%C3%9Fe-786486867/)                                                                                                   | Nov 27, 11:35      |
|       799.26 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnen-in-der-lorystra%C3%9Fe-1146686087/)                                                                                                  | Nov 27, 11:35      |
|       797.62 |            38 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/modernes-wohnen-in-simmering-813967195/)                                                                                                    | Nov 27, 11:35      |
|       559.44 |            40 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/2-zimmer-wohnung-mit-kreativer-aufteilung-und-einbauk%C3%BCche-2090338943/)                                                                    | Nov 27, 11:34      |
|       601.45 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-u1-ii-2-zimmer-ii-separate-k%C3%BCche-ii-beim-hauptbahnhof-wien-1673783352/)                                                      | Nov 27, 11:19      |
|       589    |            48 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/entz%C3%BCckender-altbau-am-lerchenfelder-g%C3%BCrtel%21-2132769919/)                                                                       | Nov 27, 10:36      |
|       710.2  |            56 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/n%C3%A4he-u6-und-kreuzgasse---erstbezug-nach-teilsanierung---in-der-schumanngasse-1666208353/)                                                | Nov 27, 09:16      |
|       770    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung%21-keine-anrufe---anfragen-nur-per-mail%21-857140441/)                                                               | Nov 27, 06:21      |
|       750    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gut-aufgeteilte-und-helle-wohnung---tolle-anbindung-1589001343/)                                                                            | Nov 26, 20:46      |
|       701.94 |            45 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%2Ahofseitiger-neubau%2A-u3-neubaugasse-um%27s-eck%21-1181889605/)                                                                             | Nov 26, 16:49      |
|       649.9  |            43 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gem%C3%BCtliche-singlewohnung-im-fasanviertel-1168323240/)                                                                            | Nov 26, 16:49      |
|       580    |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ab-1.1.---n%C3%A4he-u3-johnstrasse-1150-wien---komplett-m%C3%B6blierte-zentral-begehbare-2-zimmeraltbauwohnung-1241295804/) | Nov 26, 16:36      |
|       745.14 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnen-in-der-grillgasse-1231912503/)                                                                                                       | Nov 26, 16:15      |
|       774.47 |            39 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/modernes-wohnen-in-simmering-946474680/)                                                                                                    | Nov 26, 16:15      |
|       655    |            45 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/karmeliterviertel-provisionsfrei%21-953499614/)                                                                                          | Nov 26, 15:14      |
|       724    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-zwei-zimmer-neubauwohnung-mit-einbauk%C3%BCche-abstellraum-2022624400/)                                   | Nov 26, 11:58      |
|       730    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gem%C3%BCtliche-single--oder-p%C3%A4rchenwohnung-1144670427/)                                                                                | Nov 26, 11:27      |
