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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       710.41 |            54 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/nur-mailanfragen-%7C-erdgeschosswohnung-in-ruhiger-innenhoflage-mit-2-zimmern-&-terrasse-%7C-toplage-im-achten-quasi-%C3%BCber-die-stra%C3%9Fe-im-1.-bezirk-1978340894/)                   | Jun 02, 20:50      |
|       613    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-%28wienwohn-ticket-n%C3%B6tig%21%29-1426329914/)                                                                                                                           | Jun 02, 19:26      |
|       698    |            46 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-f%C3%BCr-den-mieter%21-reichsapfelgasse-mit-parkblick-n%C3%A4chst-u3/u4/u6-altbaumiete-46m%C2%B2-mietvertrag-unbefristet-studenten-bevorzugt%21-1706525855/) | Jun 02, 18:45      |
|       753.31 |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-zimmer-wohnung-mit-balkon-im-sonnwendviertel---unbefristet-zu-vermieten-1247536314/)                                                                                    | Jun 02, 15:59      |
|       795.29 |            32 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-2-zimmer-wohnung-1553179949/)                                                                                                                                                     | Jun 02, 14:21      |
|       799    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-&-unbefristet%21-neu-saniert%21-ruhige-wohnung-beim-neuen-landgut-1124468057/)                                                                                               | Jun 02, 13:13      |
|       709    |            52 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei-&-unbefristet%21-wohnung-in-bester-lage%21-1137354992/)                                                                                                                        | Jun 02, 13:03      |
|       719.01 |            38 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.7.---laxenburgerstrasse---helle-2-zimmer-singlewohnung-mit-s%C3%BCdseitigem-fernblick-im-7.-stock-1003818862/)                                                                         | Jun 02, 12:07      |
|       791.92 |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohung---wg-geeignet-1296359268/)                                                                                                                                                  | Jun 02, 11:14      |
|       770    |           nan |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktives-wohnen-mitten-im-sonnwendviertel-1622870157/)                                                                                                                                   | Jun 02, 09:25      |
|       799    |            67 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmerwohnung-superzustand-1149261490/)                                                                                                                                                   | Jun 02, 06:04      |
|       429.32 |            41 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/wiener-wohnen-direktvergabe-%7C-2-zimmer-wohnung-%7C-1140-wien-%7C-g%C3%BCnstige-miete-1788049819/)                                                                                           | Jun 01, 21:31      |
|       621.7  |            59 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe:-2-zimmer-gemeindebauwohnung-2035284735/)                                                                                                                                     | Jun 01, 21:28      |
