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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       619.01 |            58 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wg-geeignet---n%C3%A4he-elterleinplatz-1365044654/)                                                                        | Mar 18, 11:18      |
|       727.98 |            52 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-2-zimmer-wohnung---fair-wohnen-1532996118/)                                                                    | Mar 18, 11:10      |
|       789    |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%22panorama-city-living%22-inkl.-%22gemeinschafts-dachterrasse%22-u6-2108360611/)                                        | Mar 18, 10:57      |
|       569    |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/top-altbau-beim-brunnenmarkt-921292906/)                                                                                 | Mar 18, 10:57      |
|       730.47 |            54 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sehr-ruhige-2-zimmer-sonniger-gr%C3%BCnblick-unbefristet-vermietet-795914493/)                                             | Mar 18, 10:06      |
|       776    |            51 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/befristete-untermiete%21-m%C3%B6bliert-%21-ruhig%21-812569613/)                                                          | Mar 18, 09:57      |
|       720    |            46 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/m%C3%B6blierte-wohnung-825017951/)                                                                                      | Mar 18, 08:46      |
|       750    |            35 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/360%C2%B0-tour-//-neubau-balkonwohnung-am-wienerberg-783053018/)                                                          | Mar 18, 07:13      |
|       735.54 |            56 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gem%C3%BCtliche-2-zimmer-wohnung-n%C3%A4he-h%C3%BCtteldorfer-stra%C3%9Fe---ohne-lift-%7C-zellmann-immobilien-1234805574/)  | Mar 18, 07:04      |
|       680    |            31 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/zweitwohnung-%7C-studentenwohnung-mit-terrasse-1288142359/)                                                                | Mar 18, 04:59      |
|       787.05 |            65 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmerwohnung-3.-stock-kein-lift-26.03.25-15-17-h-1016718115/)                                                           | Mar 18, 02:24      |
|       690    |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gr%C3%BCnblick:-ruhige-%2B-freundliche-2-zimmerwohnung-n%C3%A4he-linie-49-und-u4-ober-st.-veit%21-2030586515/)             | Mar 17, 21:36      |
|       755    |            34 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/erstbezug%21-helle-2-zimmer-wohnung-mit-franz%C3%B6sischem-balkon-im-14.-bezirk-zu-vermieten%21-1661864379/)               | Mar 17, 20:51      |
|       799    |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1940698360/)                         | Mar 17, 20:38      |
|       799    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend---living%21-erstbezug---k%C3%BCche---klima---beschattung---u1-n%C3%A4he%21-1661379415/)                         | Mar 17, 20:38      |
|       440    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28keine-weiteren-anfragen-bis-28.3-%29-direktvergabe---2-zimmer-%2B-garten-1343906255/)                                 | Mar 17, 18:05      |
|       471.54 |            40 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sanierter-altbau-beim-brunnenmarkt-2045848374/)                                                                          | Mar 17, 17:26      |
|       799    |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/37m%C2%B2---2.stock---moderne-2-zimmer-wohnung-mit-heiz--und-k%C3%BChlkombi-1255935771/)                                   | Mar 17, 16:55      |
|       530    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe%2828.02.2025%29-2-zimmer-gemeindewohnung-in-favoriten---mit-abl%C3%B6se-1826919497/)                       | Mar 17, 16:33      |
|       718.52 |            42 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei:-unbefristeter-42m%C2%B2-altbau-mit-einbauk%C3%BCche-in-ruhelage---1150-wien-2115256489/) | Mar 17, 16:18      |
