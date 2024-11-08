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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799.14 |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/winteraktion---erster-monat-mietfrei%21-moderne-2-zimmerwohnung-mit-balkon%21-1780493551/)                                                                              | Nov 08, 13:36      |
|       769    |            44 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/ihr-neues-zuhause-in-brigittenau:-kompakte-2-zimmer-wohnung-mit-balkon-im-6.-stock-1647470239/)                                                                       | Nov 08, 13:28      |
|       570    |            57 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/privatvergabe-1090-wien-helle-2-zimmerwohnung-im-zweiten-stock-mit-guter-verkehrsanbindung-1573523939/)                                                                | Nov 08, 13:25      |
|       766.24 |            53 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/besichtigung-am-montag-um-16:30--2-zimmer-mit-loggia-im-2.-stock---1220-wien-seestadt---unbefristet-1231723804/)                                                       | Nov 08, 13:16      |
|       776.15 |            52 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/besichtigung-am-montag-um-16:00--2-zimmer-mit-balkon-im-4.-stock---1220-wien-seestadt---unbefristet-863107181/)                                                        | Nov 08, 13:16      |
|       749.01 |            60 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aentz%C3%BCckender-teilsanierter-neubau-in-hofruhelage%2A-1381779268/)                                                                                                 | Nov 08, 13:05      |
|       750    |            49 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-dachgeschosswohnung-%2A%2Awarmmiete%2A%2Aohne-provision%2A%2Abusstation-vor-der-haust%C3%BCre%2A%2A-2030561384/)                                             | Nov 08, 11:48      |
|       785    |            44 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/2-zimmer-neubauwohnung-inkl.-komplettk%C3%BCche-loggia-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/-k2-48-1231874088/)                                                     | Nov 08, 11:17      |
|       798.77 |            53 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-zweizimmerwohnung-mit-en-suite-bad-1400223763/)                                                                                                               | Nov 08, 11:17      |
|       799.9  |            47 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/ruhige-zweizimmerwohnung-mit-morgensonne-%2B%2B%2B-neubau-1844247074/)                                                                                                 | Nov 08, 11:17      |
|       740    |            54 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2---zimmer-m%C3%B6blierte-wohnung-mit-loggia-und-garage-beim-hansch-krankenhaus-1925589710/)                                                                              | Nov 08, 10:54      |
|       749    |            34 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/charmante-wohnungen-in-der-n%C3%A4he-der-seestadt%21-1461597180/)                                                                                                      | Nov 08, 10:47      |
|       790    |            51 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/traumhafte-zweizimmerwohnung-in-bestlage-2035966752/)                                                                                                                | Nov 08, 10:32      |
|       560    |            54 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/direktvergabe-gemeindewohnung-2-zimmer-%28generalsaniert%29-2080958038/)                                                                                              | Nov 08, 09:26      |
|       450    |            45 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-direktvergabe-vormerkschein-vor-30.9.2024-%28mit-begr%C3%BCndetem-wohnbedarf%29-1578879730/)                                                            | Nov 08, 08:43      |
|       497    |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-mit-wundersch%C3%B6ner-aussicht-1972336147/)                                                                                                            | Nov 08, 00:31      |
|       620    |            28 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/zweitwohnung-%7C-studentenwohnung-795194672/)                                                                                                                             | Nov 07, 20:21      |
|       679    |            38 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/urbanes-wohnen-in-deiner-neuen-2-zimmerwohnung-mit-balkon-im-wildgarten-1852290692/)                                                                                     | Nov 07, 19:42      |
|       730    |            55 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei-f%C3%BCr-den-mieter%21-hasnerstra%C3%9Fe-hofruhelage-altbauerstbezug-55m%C2%B2-neue-komplettk%C3%BCche-wg-eignung%21-studenten-bevorzugt%21-1039056920/) | Nov 07, 19:33      |
|       719    |            34 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---kirschbl%C3%BCtenpark---u1-n%C3%A4he-kagran---helle-hofseitige-ruhige-singlewohnung---provisionsfrei-1906948080/)                                          | Nov 07, 17:04      |
