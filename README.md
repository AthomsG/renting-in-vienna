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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       562.96 |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-%2B-einbauk%C3%BCche-%2B-einbauschr%C3%A4nke-%7C-gemeindewohnung-direktvergabe-1004286374/)                      | Mar 05, 10:28      |
|       733.75 |            52 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/lichtdurchflutete-wohnung-nahe-dem-wienfluss-u4-unter-st.-veit---pure-freude-wartet.-2073340223/)                           | Mar 05, 09:19      |
|       798    |            57 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/provisionsfrei-f%C3%BCr-den-mieter%21-corneliusgasse-n%C3%A4chst-u4-zentrumsnahe-57m%C2%B2-altbauhauptmiete.-1953967262/) | Mar 05, 09:03      |
|       694.14 |            66 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/zentral-gelegene-2-zimmerwohnung-unbefristet%2A%2A%2A-1955864506/)                                                     | Mar 04, 21:47      |
|       630    |            60 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-wohnung-mit-vertrag-zu-%C3%BCbergeben-1855518694/)                                                 | Mar 04, 21:05      |
|       780    |            72 |          4 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zu-vergeben-786701094/)                                                                             | Mar 04, 19:30      |
|       777.48 |            55 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/nette-zwei-zimmer-wohnung-981343712/)                                                                                    | Mar 04, 16:39      |
|       594.92 |            58 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-gemeidewohnung-teilweise-m%C3%B6bliert-1100-wien-990034345/)                                                     | Mar 04, 14:35      |
|       749    |            51 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionfrei%7Cmoderne-neubauwohnungen-mit-garten-balkon-oder-dachterrasse---1170-wien-1160729854/)                        | Mar 04, 14:00      |
|       713.96 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/frisch-kernsanierte-traumwohnung-in-1100-wien---troststra%C3%9Fe-50-2012220144/)                                          | Mar 04, 12:20      |
|       719    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-2-zimmer-mit-einbauk%C3%BCche-992411261/)                                                                 | Mar 04, 12:12      |
|       719    |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-2-zimmer-mit-einbauk%C3%BCche-1455000206/)                                                                | Mar 04, 12:11      |
|       670    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-dachgeschosswohnung-mit-zwei-terrassen-direktvergabe-gemeindewohnung-1150-wien-1415379847/)      | Mar 04, 12:09      |
|       770    |            70 |          4 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/direktvergabe-gemeindewohnung---4-zimmer-974582386/)                                                                      | Mar 04, 10:17      |
