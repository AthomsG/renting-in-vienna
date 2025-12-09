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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       487.59 |            45 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-zu-vergeben-in-1140-wien---%C3%BCber-wiener-wohnen-1542772402/)                                                                                     | Dec 09, 17:36      |
|       755    |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/kompakte-2-zimmerwohnung-im-3.-stock-1794251948/)                                                                                                 | Dec 09, 17:27      |
|       756.87 |            65 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-altbauwohnung-im-3.-liftstock-mit-wohlf%C3%BChlcharakter-n%C3%A4he-sch%C3%B6nbrunn-827462469/)                                                           | Dec 09, 17:25      |
|       556.77 |            55 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-ger%C3%A4umige-2-zimmer-gemeindewohnung-in-ruhiger-seitengassenlage-1559658195/)                                                                   | Dec 09, 13:14      |
|       643.82 |            59 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/vormerkscheinnummer.-30.11.2025-2-zimmer-gemeindewohnung-%7C-59-m%C2%B2-%7C-balkon-%7C-frisch-renoviert-%7C-n%C3%A4he-u3-h%C3%BCtteldorfer-stra%C3%9Fe-1568644594/) | Dec 09, 13:13      |
|       755    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierte-25-zimmer-wohnung-nahe-sonnwendviertel-1083062890/)                                                                                                      | Dec 09, 12:58      |
|       689    |            59 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/entz%C3%BCckende-erdgescho%C3%9Fwohnung-n%C3%A4he-brunnenmarkt%21-1270150124/)                                                                                      | Dec 09, 12:36      |
|       725.57 |            59 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/neu-renovierte-stilaltbauwohnung-%28-2-zimmer-%29-n%C3%A4he-elterleinplatz%21-1078357110/)                                                                          | Dec 09, 12:27      |
|       635    |            52 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/weihnachten-in-der-neuen-wohnung-1468351670/)                                                                                                                  | Dec 09, 11:43      |
|       547.25 |            42 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/h%C3%BCbsche-singlewohnung-n%C3%A4he-prater-2086974685/)                                                                                                       | Dec 09, 09:25      |
|       562.24 |            57 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/rarit%C3%A4t-gemeindewohnung-%28direktvergabe%29-am-praterstern---vormerkschein-vor-30.09.2025-1859780265/)                                                    | Dec 08, 19:08      |
