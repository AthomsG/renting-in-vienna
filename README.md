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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       798.99 |            40 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumwohnungen-in-top-lage-zu-vermieten%21-1055837955/)                                                                                                             | Oct 30, 09:48      |
|       635.87 |            48 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/super-sch%C3%B6ne-stilaltbauwohnung%21-1944362865/)                                                                                                                 | Oct 30, 09:36      |
|       560    |            54 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/direktvergabe-gemeindewohnung-2-zimmer-%28generalsaniert%29-2080958038/)                                                                                            | Oct 30, 08:01      |
|       676.17 |            45 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/n%C3%A4he-einsiedlerpark-hell-&-freundlich-neue-k%C3%BCche-schlafzimmer-in-den-innenhofunbefristet-1108902255/)                                                      | Oct 30, 04:47      |
|       561.11 |            41 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristete-altbauwohnung-mit-terrasse-in-der-wolfganggasse-1054729284/)                                                                                              | Oct 30, 03:20      |
|       781.45 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/praktisch-gelegene-2-zimmer-wohnung-1723277411/)                                                                                                                      | Oct 30, 00:38      |
|       723    |            74 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wiener-wohnen-direktvergabe-1456899497/)                                                                                                              | Oct 29, 22:19      |
|       788.34 |            49 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/traumhafte-neubauwohnung-in-direkter-u-bahn-n%C3%A4he-1708324488/)                                                                                                   | Oct 29, 21:32      |
|       516.02 |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtliche-2-zimmer-wohnung-2090680683/)                                                                                                                         | Oct 29, 21:31      |
|       430    |            45 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-/-wiener-wohnen-1140-wien--nur-mit-vormerkschein-1773891561/)                                                                                           | Oct 29, 20:59      |
|       685.01 |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kleinod--erstbezug-in-hauptbahnhof-n%C3%A4he-1577186673/)                                                                                                             | Oct 29, 20:33      |
|       695    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/zweizimmer-erstbezug-in-hauptbahnhof-n%C3%A4he-824306479/)                                                                                                            | Oct 29, 19:35      |
|       433.18 |            39 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/direktvergabe-gemeindewohnung--nur-mit-wiener-wohn-ticket-1205437738/)                                                                                               | Oct 29, 18:44      |
|       540    |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-mit-direktvergabe-2115627502/)                                                                                                                                | Oct 29, 18:07      |
|       570    |            55 |          3 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/helle-&-renovierte-3-zimmer-gemeinde-wohnung-weiterzugeben-1159566384/)                                                                                            | Oct 29, 14:26      |
|       765.37 |            45 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/tolle-2-zimmer-wohnung-mit-idealer-raumaufteilung-in-guter-und-infrastrukturell-ansprechender-lage%21-1791769254/)                                                  | Oct 29, 14:18      |
|       795    |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wundersch%C3%B6ne-2-zimmer-wohnung-mit-terrasse-1939918169/)                                                                                          | Oct 29, 13:51      |
|       798.88 |            41 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnwend-living%21-inklusive-k%C3%BCche%21-erstbezug%21-elektrische-raffstores%21-klima-vorb.%21-n%C3%A4he-u1.---wohntraum-774645004/)                                | Oct 29, 13:49      |
|       461    |            51 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/u-6-n%C3%A4he-topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-1957819797/)                                                              | Oct 29, 12:40      |
|       473.09 |            64 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3.-zimmer-gemeindewohnung-in-1100-wien-ohne-aufzug%21-/-vormerkschein-bis-30.09.2024-/-n%C3%A4chste-sammelbesichtigung-am-10.11.24-von-14-bis-17h-%21%21-1551815967/) | Oct 29, 12:33      |
