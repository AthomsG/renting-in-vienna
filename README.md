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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       798    |            40 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/2-zimmer-wohnung-in-ruhelage-n%C3%A4he-h%C3%B6chst%C3%A4dtplatz-%284.-stock%29-939066645/)                                                                                      | Jan 13, 18:20      |
|       550    |            45 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/unbefristete-renovierte-teilm%C3%B6blierte-altbau--mietwohnung-mit-freifl%C3%A4che-1359834640/)                                                                                     | Jan 13, 17:36      |
|       692.32 |            39 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1317724224/)                                                                                                | Jan 13, 17:21      |
|       742.18 |            41 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1764666987/)                                                                                                | Jan 13, 16:51      |
|       760    |            74 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-1110-wien-1779855004/)                                                                                                                                            | Jan 13, 16:21      |
|       795.19 |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnungen-nahe-u1-kagraner-platz---aufstrebendes-wohnviertel-1517264677/)                                                                                          | Jan 13, 16:16      |
|       795.19 |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/moderne-neubauwohnung-mit-gro%C3%9Fem-balkon-und-abstellraum-nahe-u1-kagraner-platz---im-neuen-wohnviertel-am-langen-felde-1911782186/)                                          | Jan 13, 15:35      |
|       743.33 |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-wohnung-inklusive-abstellraum%21-neubau-und-hochwertig---ab-01.03-1127569884/)                                                                                         | Jan 13, 14:58      |
|       798    |            37 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sehr-sch%C3%B6ne-2-zimmerwohnung---n%C3%A4he-donauinsel-&-handelskai-1066009313/)                                                                                               | Jan 13, 14:15      |
|       729.82 |            60 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/kuschlig-wohnen-im-zentrum-von-liesing-1880260887/)                                                                                                                                 | Jan 13, 13:34      |
|       768.98 |            35 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/p%C3%A4rchentraum-mit-hofseitigen-balkon-%7C-erlaaer-stra%C3%9Fe-20-%7C-1.24-1155211784/)                                                                                           | Jan 13, 12:32      |
|       739    |            41 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---u1-n%C3%A4he-kagran---ab-01.2.2025---gepflegte-neubau---singlewohnung-1477934269/)                                                                                   | Jan 13, 12:22      |
|       690    |            37 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---ab-01.02.2025---zweizimmer-singlewohnung-mit-perfektem-grundriss-und-gro%C3%9Fz%C3%BCgigem-balkon---neubau---provisionsfrei-1429821665/)                              | Jan 13, 12:22      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---lichtdurchflutet-und-modern:-2-zimmer-wohnung-mit-balkon--erstbezug-in-ruhelage-786080173/)                                                                      | Jan 13, 11:37      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---traumhafter-erstbezug-in-ruhelage-1311362301/)                                                                                                                   | Jan 13, 11:35      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---2-zimmer-aartment-mit-balkon-traumhafter-erstbezug-in-ruhelage-1043504437/)                                                                                      | Jan 13, 11:33      |
|       774    |            38 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-sch%C3%B6ner-wohnen-mit-stil-%2A-2-zimmer-wohnung-vollst%C3%A4ndig-m%C3%B6bliert---3.-bezirk-f%C3%BCr-universit%C3%A4ten/-business-%2A-all-in-1559533337/) | Jan 13, 11:29      |
|       696    |            41 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gem%C3%BCtliche-2-zimmer-wohnung-41m%C2%B2-1603863361/)                                                                                                           | Jan 13, 11:05      |
|       769    |            40 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/neubau-2-zimmer-wohnung-inkl-hochwertiger-k%C3%BCche-balkon-au%C3%9Fenfl%C3%A4che-und-kellerabteil-/sp64-5-50-1330949619/)                                                       | Jan 13, 11:00      |
|       790    |            49 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/erstbezug%21-moderne-2-zimmer-wohnung-mit-balkon-1230948998/)                                                                                                                   | Jan 13, 11:00      |
