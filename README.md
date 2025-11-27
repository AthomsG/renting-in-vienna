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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       770    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung%21-keine-anrufe---anfragen-nur-per-mail%21-857140441/)                                                               | Nov 27, 06:21      |
|       750    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gut-aufgeteilte-und-helle-wohnung---tolle-anbindung-1589001343/)                                                                            | Nov 26, 20:46      |
|       701.94 |            45 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%2Ahofseitiger-neubau%2A-u3-neubaugasse-um%27s-eck%21-1181889605/)                                                                             | Nov 26, 16:49      |
|       649.9  |            43 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gem%C3%BCtliche-singlewohnung-im-fasanviertel-1168323240/)                                                                            | Nov 26, 16:49      |
|       580    |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ab-1.1.---n%C3%A4he-u3-johnstrasse-1150-wien---komplett-m%C3%B6blierte-zentral-begehbare-2-zimmeraltbauwohnung-1241295804/) | Nov 26, 16:36      |
|       798.42 |            37 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sch%C3%B6ne-wohnung-15-zimmer-wohnung-mit-balkon-in-1050-wien%21-2003718528/)                                                              | Nov 26, 16:28      |
|       745.14 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/my-lory---wohnen-in-der-grillgasse---provisionsfrei-1231912503/)                                                                            | Nov 26, 16:15      |
|       774.47 |            39 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmerwohnung-in-1110-wien-mit-balkon-946474680/)                                                                                         | Nov 26, 16:15      |
|       655    |            45 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/karmeliterviertel-provisionsfrei%21-953499614/)                                                                                          | Nov 26, 15:14      |
|       750    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-zwei-zimmer-neubauwohnung-mit-einbauk%C3%BCche-abstellraum-2022624400/)                                   | Nov 26, 11:58      |
|       730    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gem%C3%BCtliche-single--oder-p%C3%A4rchenwohnung-1144670427/)                                                                                | Nov 26, 11:27      |
|       480    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-ab-februar-2026-817394128/)                                                                                                 | Nov 26, 08:37      |
