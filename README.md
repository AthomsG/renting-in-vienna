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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       531.11 |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-1613413500/)                                                                                                                                            | Jan 31, 07:50      |
|       432    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen-ticket-31.12.2024-1147334553/)                                                                                                      | Jan 31, 07:38      |
|       769    |            40 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/wien---1200-wien---ab-01.03.2025---attraktive-neubauwohnung-inkl.-loggia-und-komplettk%C3%BCche-in-u6-n%C3%A4he-1934025231/)                                  | Jan 31, 02:28      |
|       495.21 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeinde-wohnung--direktvegabe-1452506043/)                                                                                                     | Jan 30, 21:56      |
|       799.9  |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/balkonwohnung%21-koffer-packen-und-einziehen%21---garage-optional-891410264/)                                                                                   | Jan 30, 21:35      |
|       735.34 |            72 |          3 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/3--zimmer-gemeinde-wohnung%28ohne-finanzierungsbetrag%29-in-1210-wien-1475525722/)                                                                            | Jan 30, 19:43      |
|       799    |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wundersch%C3%B6ne-neu-sanierte-2-zimmer-wohnung-in-gr%C3%BCnruhelage-zu-vermieten-953196478/)                                                                   | Jan 30, 19:28      |
|       590    |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-42-m%C2%B2-wohnung-in-meidling---hofruhelage-teilm%C3%B6bliert-1960351810/)                                                                            | Jan 30, 19:02      |
|       552    |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-2-zimmer-bei-u1-troststra%C3%9Fe-1546576828/)                                                                                                   | Jan 30, 18:54      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1121290609/)                                            | Jan 30, 17:31      |
|       749.92 |            54 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/%2Akeine-k%C3%BCche-verbaut%2A-gro%C3%9Fz%C3%BCgige-2-zimmer-wohnung-nahe-millennium-tower-2011253068/)                                                       | Jan 30, 16:47      |
|       698    |            52 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/provisionsfrei-f%C3%BCr-den-mieter%21-oberm%C3%BCllnerstra%C3%9Fe-n%C3%A4chst-u1/u2-altbauhauptmiete-erstbezug%21-52m%C2%B2-studenten-bevorzugt-1678946971/) | Jan 30, 16:20      |
|       690    |            51 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%28reserviert%29-mietwohnung%C2%A0im%C2%A014.%C2%A0bezirk-1376770472/)                                                                                            | Jan 30, 15:50      |
|       645    |            41 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aprovisionsfrei%2A-gepflegte-2-zimmer-wohnung-ideal-f%C3%BCr-singles-oder-studenten-1412179388/)                                                               | Jan 30, 15:21      |
|       700    |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-am-columbuplatz-1398048797/)                                                                                                                   | Jan 30, 14:40      |
|       725    |            46 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumhafte-2-zimmerwohnung-mit-balkon%21-1481379808/)                                                                                                         | Jan 30, 13:59      |
|       585.92 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/heller-sofortbezug-in-der-fernkorngasse-1645303779/)                                                                                                            | Jan 30, 13:28      |
|       781.58 |            58 |          2 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/unbefristete-haupmiete-/-2-zimmer-altbauwohnung-/-hochpaterre-1980334360/)                                                                                   | Jan 30, 12:37      |
|       599    |            34 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ca.-34-m2-erstbezug-nach-sanierung-atelier-im-souterrain-f%C3%BCr-firma-oder-privat---all-inclusive-miete-warm-1578533243/)                                       | Jan 30, 12:01      |
|       768.97 |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/charmante-2-zimmer-wohnung-am-sechshauser-g%C3%BCrtel%21-1142683402/)                                                                           | Jan 30, 11:58      |
