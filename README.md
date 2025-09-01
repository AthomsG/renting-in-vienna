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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       780    |            41 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/2-zimmer-%7C-toplage-%7C-apollokino-n%C3%A4he-1497398593/)                                                                                     | Sep 01, 21:29      |
|       550    |            70 |          3 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/3er-wg-hit-in-bestlage-%281070%29:-3-zimmer-gro%C3%9Fer-vorraum-balkon-zum-hof-super-anbindung-1398390468/)                                       | Sep 01, 18:05      |
|       450    |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-gemeindewohnung-am-kardinal-nagl-platz---unbefristet-1489301078/)                                                               | Sep 01, 16:59      |
|       767.47 |            56 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28anfragestopp%29-loftartige-2--zimmer-altbauwohnung-in-1120-1140615600/)                                                                      | Sep 01, 15:39      |
|       629.2  |            46 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-singlewohnung-n%C3%A4he-matzleinsdorferplatz-951298317/)                                                                      | Sep 01, 15:31      |
|       623.33 |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-mit-wiener-wohnticket%21-zentrale-ruhige-2-zimmer-wohnung-n%C3%A4he-u1-%28mit-balkon%29-1239753074/)                             | Sep 01, 15:17      |
|       786.03 |            69 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-dachgescho%C3%9Fwohnung-mit-loggia---1120-wien-erlgasse-21-23-1622952647/)                                                       | Sep 01, 14:22      |
|       490    |            78 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gro%C3%9Fz%C3%BCgige-wg-wohnung-f%C3%BCr-3-personen-geeignet---zentrale-lage-&-gute-anbindung-pro-person-ca.-monatlich-625---euro-1547786603/) | Sep 01, 14:04      |
|       620    |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/direktvergabe-gemeindewohnung-991009041/)                                                                                      | Sep 01, 13:45      |
|       732.39 |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-vollsanierte-2-zimmer-wohnung-in-1100-wien---ideal-zum-wohlf%C3%BChlen%21-1368477675/)                                               | Sep 01, 11:48      |
|       635    |            78 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wg-taugliche-mietwohnung---2-getrennte-schlafzimmer-%2B-gemeinschaftsbereich-1130799131/)                                                      | Sep 01, 11:33      |
|       748    |           nan |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktives-wohnen-mitten-im-sonnwendviertel-1482246041/)                                                                                      | Sep 01, 10:29      |
|       799.99 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-neubauwohnung-inkl-k%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-hs17-top-a-11-1408893401/)                              | Sep 01, 09:58      |
|       668.9  |            62 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-im-10.-bezirk-2-zimmer%2B-1-nebenzimmer%28nur-mit-wohnticket-f%C3%BCr-2-zimmer-bis-31.08.2025%29-1644978842/)                  | Aug 31, 22:12      |
|       670    |            65 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-1187438720/)                                                                                               | Aug 31, 21:03      |
