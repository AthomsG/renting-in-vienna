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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       541    |            49 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-direktvergabe-2-zimmer-858349181/)                                                                                               | Mar 08, 11:01      |
|       652.1  |            66 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wg-eignung%21-25-zimmer-wohnung.-unbefristet.-bitte-schriftlich-anfragen%21-1870360726/)                                                             | Mar 08, 09:15      |
|       603    |            55 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/1090:-55m%C2%B2-altbau-befr.-603---%3B-hwb-1552-489782661/)                                                                                        | Mar 07, 17:22      |
|       778.8  |            59 |          3 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/nachmieter-gesucht%21-1060-wien%21-2099164894/)                                                                                                     | Mar 07, 16:57      |
|       799    |            38 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien---wohnen-am-erlachpark---6ter-liftstock---garagenplatz-inklusive-1331806037/)                                                             | Mar 07, 16:46      |
|       729.98 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-sch%C3%B6ne-2-zimmer-wohnung-mit-balkon%21-1194153677/)                                                                                        | Mar 07, 13:49      |
|       721.55 |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-helle-2-zimmer-wohnung-im-zentrum-von-favoriten-1623854276/)                                                                                   | Mar 07, 13:28      |
|       460    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-zu-vergeben-1100-wien-1124502640/)                                                                                                 | Mar 07, 13:22      |
|       650    |            38 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/moderne-wohnung-in-margareten-1425533192/)                                                                                                         | Mar 07, 12:42      |
|       796.05 |            48 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ne-48-m%C2%B2-wohnung-mit-2-zimmern-im-16.-bezirk---rosseggergasse-15-1974310578/)                                                   | Mar 07, 12:20      |
|       534.62 |            53 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sonnige-53m%C2%B2-gemeindewohnung-mit-balkon-prater--&-donaukanalblick---direktvergabe-vmd-vor-31.01.2025-ab-juli-verf%C3%BCgbar-1466171694/) | Mar 07, 10:55      |
|       720.88 |            78 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/721-eur-bruttomiete.-sehr-gut-eingeteilte-gepflegte-wohnung-977341521/)                                                             | Mar 07, 10:49      |
