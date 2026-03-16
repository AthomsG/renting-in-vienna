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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       448.05 |            48 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/nachmieter-gesucht---vollm%C3%B6blierte-altbauwohnung-%2848-m%C2%B2%29-in-sehr-guter-lage---ideal-f%C3%BCr-singles-oder-paare-1953949704/)                                             | Mar 16, 16:21      |
|       760    |            50 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/zentrale-&-helle-2-zimmer-wohnung-zu-vermieten-821307239/)                                                                                                                            | Mar 16, 15:36      |
|       439    |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-zu-vergeben-1742135266/)                                                                                                                                           | Mar 16, 14:22      |
|       799.92 |            39 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/smarte-2-zimmer-wohnung-nahe-reinprechtsdorfer-stra%C3%9Fe-in-1050-wien-zu-mieten-1213067568/)                                                                                     | Mar 16, 13:51      |
|       733.75 |            52 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/lichtdurchflutete-wohnung-nahe-dem-wienfluss-u4-unter-st.-veit---pure-freude-wartet.-1484152606/)                                                                                     | Mar 16, 09:25      |
|       649    |            60 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/studenten-zimmer-in-2er-wg%21-pauschalmiete-649eur-inkl.-strom-heizung-internet%21-ideale-verkehrsanbindung-n%C3%A4he-u4-stadtpark---ab-sofort-verf%C3%BCgbar%21-1815563294/) | Mar 16, 09:17      |
|       730    |            38 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-wohnung-in-ruhige-lage-in-oberlaa-1157841537/)                                                                                                                    | Mar 16, 08:51      |
|       505    |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-direktvergabe-gemeindewohnung-1030-1057196527/)                                                                                                                      | Mar 16, 05:29      |
|       750    |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wohnen-bei-der-mariahilfer-stra%C3%9Fe--balkon-ruhelage-provisionsfrei-1262890218/)                                                                                 | Mar 15, 22:40      |
