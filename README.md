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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       778.17 |            73 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-3-zimmer-wohnung-mit-guter-anbindung%21-997943639/)                                                                                                            | Jan 13, 09:27      |
|       770    |            43 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-wohnung-mit-hochwertiger-k%C3%BCche-balkon-und-kellerabteil-%28i3-46%29-864784617/)                                                                       | Jan 13, 09:27      |
|       736.11 |            55 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/erstbezug---betreutes-wohnen-%28ab-dem-60.-lebensjahr%29-in-1220-wien-1682208939/)                                                                                         | Jan 13, 09:27      |
|       799    |            44 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-wohnung-mit-hochwertiger-k%C3%BCche-und-kellerabteil-%28i3-31%29-1430668443/)                                                                             | Jan 13, 09:27      |
|       779    |            43 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-2-zimmer-wohnung-inkl-hochwertiger-k%C3%BCche-mit-sonderausstattung-balkon-und-kellerabteil-/-i3-14-1996398254/)                                                   | Jan 13, 09:27      |
|       690.54 |            48 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/nette-zwei-zimmer-wohnung-mit-aussenbereich%21%21%21-1452583767/)                                                                                           | Jan 13, 09:21      |
|       790    |            46 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohntr%C3%A4ume-erleben:-mietwohnungen-mit-option-auf-zuk%C3%BCnftigen-kauf-739383800/)                                                                    | Jan 13, 08:56      |
|       730    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-in-favoriten-n%C3%A4he-u1-troststra%C3%9Fe-1073311402/)                                                                                                    | Jan 13, 08:00      |
|       697.84 |            34 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zimmer-wohnung-n%C3%A4he-bacherplatz-1071175978/)                                                                                                                        | Jan 13, 01:07      |
|       558.47 |            56 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-direktvergabe-883223660/)                                                                                                                                   | Jan 12, 23:16      |
|       750    |            57 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sonnige-2-zimmer-neubau-wohnung-1488758239/)                                                                                                                                | Jan 12, 19:42      |
|       545.19 |            53 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/%28bitte-derzeit-keine-anfragen-mehr%29-sch%C3%B6ne-2-zimmer-gemeindewohnung-in-zentraler-lage---mit-balkon-in-begr%C3%BCnten-innenhof-1944989193/)                         | Jan 12, 19:04      |
|       495    |            50 |          2 | 13. Hietzing             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/mietwohnung-gemeinde-wohnticket-31.12.2024-1368188222/)                                                                                                                      | Jan 12, 19:04      |
|       798.53 |            37 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristete-neubauwohnung-in-gehweite-des-bahnhof-penzing---ruhige-seitengasse-der-linzer-stra%C3%9Fe%21-ab-m%C3%A4rz-2025%21---jetzt-zuschlagen-2060975917/)                | Jan 12, 18:56      |
|       557.34 |            51 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/direktvergabe-ohne-ger%C3%A4te-wundersch%C3%B6ne-helle-gemeindewohnung-1-wohnraum-1-k%C3%BCchezeile-ohne-elektroger%C3%A4te-vmd-31.12.2024-oder-fr%C3%BCher-1906357566/) | Jan 12, 18:42      |
|       517    |            50 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/gemeindewohnung-2-zimmer-1060-vmd-10/2024-1226960909/)                                                                                                                      | Jan 12, 16:12      |
|       687.19 |            58 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/nachmieter-gesucht-1408471351/)                                                                                                                                               | Jan 12, 15:24      |
|       414.49 |            40 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/2-zimmer-wohnung-von-wiener-wohnen-mit-wohnticket-datum-bis-31.12.2024-1647175872/)                                                                                      | Jan 12, 14:25      |
|       499    |            39 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/kaiserstrasse-107-besichtigung-am-13.01.-von-11-11.30-uhr-1634200748/)                                                                                                         | Jan 12, 13:53      |
|       795    |            55 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-2-zimmer-wohnung-1607868609/)                                                                                                                                          | Jan 12, 12:08      |
