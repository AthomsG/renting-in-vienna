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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       637.56 |            48 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/klassische-&-unbefristete-2-zimmer-altbauwohnung-1401758621/)                                                    | Nov 27, 16:45      |
|       504.43 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sch%C3%B6ne-gemeindewohnung-mit-loggia--direktvergabe---2-zimmer---1150-wien-1812526107/)         | Nov 27, 15:29      |
|       775    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-wg-oder-f%C3%BCr-ein-p%C3%A4rchen-%21%21-1659969157/)                                                           | Nov 27, 13:46      |
|       732    |            50 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/nachmieter%2Ain-gesucht---helle-2-zimmer-50m%C2%B2-neubauwohnung-in-der-simmeringer-hauptstra%C3%9Fe-1581998181/) | Nov 27, 13:00      |
|       774.95 |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/modernes-wohnen-in-simmering-1521674692/)                                                                         | Nov 27, 11:35      |
|       799.26 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnen-in-der-lorystra%C3%9Fe-1146686087/)                                                                        | Nov 27, 11:35      |
|       601.45 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-u1-ii-2-zimmer-ii-separate-k%C3%BCche-ii-beim-hauptbahnhof-wien-1673783352/)                            | Nov 27, 11:19      |
|       589    |            48 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/entz%C3%BCckender-altbau-am-lerchenfelder-g%C3%BCrtel%21-2132769919/)                                             | Nov 27, 10:36      |
|       710.2  |            56 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/n%C3%A4he-u6-und-kreuzgasse---erstbezug-nach-teilsanierung---in-der-schumanngasse-1666208353/)                      | Nov 27, 09:16      |
|       770    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung%21-keine-anrufe---anfragen-nur-per-mail%21-857140441/)                                     | Nov 27, 06:21      |
|       750    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gut-aufgeteilte-und-helle-wohnung---tolle-anbindung-1589001343/)                                                  | Nov 26, 20:46      |
|       701.94 |            45 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%2Ahofseitiger-neubau%2A-u3-neubaugasse-um%27s-eck%21-1181889605/)                                                   | Nov 26, 16:49      |
