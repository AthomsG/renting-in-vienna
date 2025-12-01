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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       770.67 |            70 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-altbauwohnung-n%C3%A4he-u3-simmering-in-1110-wien-zu-mieten-1927122421/)                                                                   | Dec 01, 11:20      |
|       545.6  |            46 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-singlewohnung-beim-einsiedlerplatz-931155645/)                                                                                     | Dec 01, 11:10      |
|       695    |            43 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/singlehit/n%C3%A4he-u3-ottakring%21-unbefristete-43-m2-stilaltbaumiete-wohnzimmer-mini-kabinett-einbauk%C3%BCche-gesamtmiete-eur-695---1045192397/) | Dec 01, 10:54      |
|       797.73 |            60 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-altbauwohnung-der-fernkorngasse-1714684085/)                                                                                                  | Dec 01, 09:58      |
|       790    |            76 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-wiener-gemeindewohnung---1020-wien-engerthstra%C3%9Fe-%28u2-krieau%29-1120461218/)                                                 | Dec 01, 09:46      |
|       440    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe---voll-m%C3%B6blierte-helle-2-zimmer-gemeindewohnung-im-10.-bezirk-918667643/)                                                        | Dec 01, 09:23      |
|       751    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter-gesucht-1904278145/)                                                                                                                     | Nov 30, 23:06      |
|       760    |            72 |          4 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-%28nur-mit-wiener-wohn-ticket%21%29-vmd:-vor-30.10.2020-1876423831/)                                                                 | Nov 30, 19:43      |
|       676.01 |            48 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/ruhige-sch%C3%B6ne-altbauwohnung-mit-gutem-grundriss-in-1090-wien-liechtensteinstra%C3%9Fe-1770067155/)                                            | Nov 30, 18:55      |
|       750    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-%7C-provisionsfrei-1913235795/)                                                                                                     | Nov 30, 14:58      |
|       760    |            39 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei-attraktive-ruhig-gelegene-kleine-2-zimmerwohnung-u-4-n%C3%A4he-1176067739/)                                                           | Nov 30, 14:52      |
