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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       725.57 |            59 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/neu-renovierte-stilaltbauwohnung-%28-2-zimmer-%29-n%C3%A4he-elterleinplatz%21-1632961839/)                                                   | Dec 10, 17:55      |
|       791.33 |            55 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/s%C3%BCsse-ruhige-paar--oder-singlewohnung---clemens-hofbauer-platz-unbefristet-812366046/)                                                  | Dec 10, 17:28      |
|       765.92 |            43 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/supers%C3%BC%C3%9F-und-gr%C3%BCn-und-sonnig-1979679700/)                                                                                     | Dec 10, 17:28      |
|       650    |            62 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-ticket-3.-bezirk-3-zimmer-787879243/)                                                                    | Dec 10, 17:01      |
|       469.89 |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-und-preiswerte-zwei-zimmer-wohnung-1397901420/)                                                                                | Dec 10, 15:53      |
|       594    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-wg-tauglich-n%C3%A4he-westbahnhof-direkt-bei-u3-1615846005/)                                                      | Dec 10, 15:01      |
|       680.01 |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-2-zimmer-mietwohnung-.-komplett-neusaniert---ab-1.2.26-bezugsbereit-1143308813/)                                              | Dec 10, 11:33      |
|       790    |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zauberhafte-hoflage-in-city-n%C3%A4he%21-877100713/)                                                                                 | Dec 10, 09:40      |
|       790    |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/2-zimmer-wohnung-rennweg-n%C3%A4he-st.-marx-1793702492/)                                                                             | Dec 10, 08:39      |
|       533.06 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gepflegte-und-sehr-ruhige-2-zimmer-wohnung-55m%C2%B2-wohnung-in-1100-wien---ihr-neues-zuhause-f%C3%BCr-nur-miete-53306-eur%21-1170053246/) | Dec 09, 18:55      |
