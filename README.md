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
|       799.91 |            66 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-mietwohnung-in-der-gudrunstra%C3%9Fe%21-1066023498/)                                                                                                                      | Jan 27, 15:35      |
|       759.32 |            44 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gepflegte-studentenwohnungen-mit-einbauk%C3%BCche-in-1210-zu-mieten-1311001680/)                                                                                                | Jan 27, 15:26      |
|       767.47 |            56 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/loftartige-2--zimmer-altbauwohnung-im-t%C3%B6pferlbad-%7C-unbefristet-%7C-ab-sofort-2103176781/)                                                                                   | Jan 27, 14:57      |
|       763.01 |            47 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/studentenwohnung-klein-und-fein---ab-april-25-1665184006/)                                                                                                                       | Jan 27, 14:19      |
|       798    |            37 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sehr-sch%C3%B6ne-2-zimmerwohnung---n%C3%A4he-donauinsel-&-handelskai-1066009313/)                                                                                               | Jan 27, 14:15      |
|       739    |            43 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/ab.-1.3.2025---1210-wien---weitblick---attraktive-nordseitige-neubauwohnung-mit-sch%C3%B6nem-balkon-1242545954/)                                                                | Jan 27, 13:53      |
|       479    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonniger-altbau-in-u1-n%C3%A4he-1050434959/)                                                                                                                                      | Jan 27, 13:28      |
|       759    |            58 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-&-unbefristet%21-zentral-gelegene-wohung-1797203257/)                                                                                              | Jan 27, 12:21      |
|       689    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-ruhige-wohnung-n%C3%A4he-hauptbahnhof-1592140586/)                                                                                                | Jan 27, 12:17      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei-in-der-pfalzgasse-29---2-zimmer-wohnung-mit-balkon---erstbezug-in-ruhelage-1609375860/)                                                                         | Jan 27, 11:51      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1705094653/)                                                              | Jan 27, 11:46      |
|       799    |            39 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---1-monat-mietfrei%21-2-zimmer-wohnung-mit-balkon-%7C-traumhafter-erstbezug-in-ruhelage-1283007542/)                                                               | Jan 27, 11:41      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/pfalzgasse-29---lichtdurchflutet-und-modern:-2-zimmer-wohnung-mit-balkon--erstbezug-in-ruhelage-786080173/)                                                                      | Jan 27, 11:37      |
|       799    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1-monat-mietfrei:-erstbezug-im-gr%C3%BCnen-nahe-der-u2---zwischen-badeteich-hirschstetten-und-seestadt-1043504437/)                                                              | Jan 27, 11:33      |
|       752.81 |            40 |          2 | 18. Währing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1180-w%C3%A4hring/nachmieter-f%C3%BCr-unbefristete-gut-aufgeteilte-2-zimmer-wohnung---200m-zu-u6-akh-844909976/)                                                                                 | Jan 27, 11:33      |
|       774    |            38 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-sch%C3%B6ner-wohnen-mit-stil-%2A-2-zimmer-wohnung-vollst%C3%A4ndig-m%C3%B6bliert---3.-bezirk-f%C3%BCr-universit%C3%A4ten/-business-%2A-all-in-1559533337/) | Jan 27, 11:29      |
|       763.15 |            56 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-in-der-br%C3%BCnner-strasse-912073341/)                                                                                                                | Jan 27, 11:00      |
|       695    |            33 |          2 | 23. Liesing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/ab-1.2.2025---u6-n%C3%A4he-erlaaer-stra%C3%9Fe---neuwertige-singlewohnung-in-ruhelage---sofortbezug-1461331672/)                                                                    | Jan 27, 10:52      |
|       729.3  |            46 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/provisionsfreie-traumwohnung:-2-zimmer-%7C-top-lage%7C-ausgezeichnete-anbindung-1587911057/)                                                                                    | Jan 27, 10:03      |
|       678.38 |            57 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sonnige-2-zimmerwohnung-mit-allen-nebenr%C3%A4umen--unbefristet-zu-mieten-1793337601/)                                                                                            | Jan 27, 10:01      |
