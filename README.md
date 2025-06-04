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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       693    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-renovierte-neubauwohnung-hofseitig-1775181648/)                                                                                                 | Jun 04, 17:56      |
|       598.39 |            41 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/saniert-%2A%2A%2A-beim-kongressbad-und-s45-hernals-%2A%2A%2A-2-zimmer-wohnung-zur-untermiete-%2A%2A%2A-n%C3%A4he-hernalser-hauptstra%C3%9Fe-1821861626/) | Jun 04, 16:16      |
|       520.25 |            47 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-nahe-matzleinsdorfer-pl.-nur-mit-g%C3%BCltigem-wiener-wohn-ticket-1980287901/)                                                        | Jun 04, 15:44      |
|       795    |            54 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3.erdbergstrasse---provisionsfreie-charmante-2-zimmer-neubaumiete-direkt-beim-kardinal-naglplatz-2105617351/)                                    | Jun 04, 15:32      |
|       781.81 |            54 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-altbau-mit-guter-anbindung-1974132361/)                                                                                                        | Jun 04, 12:21      |
|       622.22 |            39 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/openhouse-am-6.6.-von-13:00---13:20-uhr%21-keine-anrufe-anfragen-nur-per-mail%21-1158485666/)                                                         | Jun 04, 11:42      |
|       601.07 |            55 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/1040-sch%C3%B6ne-2-zimmer-wohnung-nahe-alois-drasche-park-1138123774/)                                                                                    | Jun 04, 10:28      |
|       745.39 |            60 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sonnige-ruhige-2-zimmer-wohnung-n%C3%A4he-s-bahn/-u6/-u4-1268194228/)                                                                                   | Jun 04, 10:06      |
|       760    |            40 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/wohnung-in-1060-wien-1675858195/)                                                                                                                      | Jun 03, 23:27      |
|       540    |            48 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-%21-dringend%21-gemeindewohnung%21-direktvergabe-nur-mit-g%C3%BCltigem-wiener-wohnticket-vms-30.04.25%21-1068837510/)                  | Jun 03, 22:11      |
