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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                               | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       645    |            63 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-wohnung-weiter-geben-952130202/)                                                                                     | Feb 04, 12:46      |
|       761.23 |            34 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/sch%C3%B6ne-2-zimmer-wohnung-in-guter-lage---n%C3%A4chst-akh%21-773008746/)                                                  | Feb 04, 12:34      |
|       600    |            60 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung---direktvergabe.-3-zimmer-1179905399/)                                                                     | Feb 04, 09:00      |
|       659.08 |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/moderne-2-zimmer-wohnung-mit-balkon-in-1030-wien-1056058935/)                                                           | Feb 04, 02:45      |
|       728.92 |            46 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/moderne-2-zimmer-wohnung-mit-balkon-&-weitblick---1030-wien-910462666/)                                                 | Feb 04, 02:45      |
|       500    |            50 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung---direktvergabe%21-50-m%C2%B2-2-zimmer-gr%C3%BCnlage-im-16.-bezirk-vormerkschein-erforderlich-1081875644/)    | Feb 03, 23:33      |
|       510.44 |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/wiener-wohnen-wohnung-%28vormerkschein-2025%29-1558611323/)                                                   | Feb 03, 23:26      |
|       603.76 |            47 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-gem%C3%BCtlich-brunnenmarkt-1569233783/)                                                                             | Feb 03, 18:42      |
|       750    |            48 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/leopold-ernst-gasse---2-zimmer-neubau-mit-extra-einbauk%C3%BCche-876469462/)                                                    | Feb 03, 18:26      |
|       495    |            47 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-47-m%C2%B2-wohnung-im-herzen-von-wien-direkt-bei-der-u3-schweglerstra%C3%9Fe-1188687863/)               | Feb 03, 15:39      |
|       573.7  |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-am-wienerberg%21-vormerkschein-bis-31.12.2025-1159323993/)                                           | Feb 03, 14:11      |
|       704    |           nan |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernes-wohn--und-gesch%C3%A4ftshaus-1200382169/)                                                                            | Feb 03, 13:48      |
|       720    |            64 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zi.--altbauwohnung-1783546068/)                                                                                       | Feb 03, 13:00      |
|       604    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnen-ohne-aufwand:-komplett-eingerichtete-2-zimmer-wohnung-%21%21-keine-gemeind-/-genossenschaftswohnung%21%21-2102095229/) | Feb 03, 12:18      |
