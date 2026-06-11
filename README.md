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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       777.62 |            46 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-dg-wohnung-im-10.bezirk-n%C3%A4he-r%C3%A4umannplatz%21-2054018928/)                                 | Jun 11, 12:54      |
|       745    |            60 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/sch%C3%B6ne-2-zimmer-wohnung---ruhig-&-zentral-935914777/)                                                            | Jun 11, 12:43      |
|       600    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/50m%C2%B2-wohnung-im-ruhigem-altbau-912329812/)                                                                          | Jun 11, 10:44      |
|       443.64 |            59 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ger%C3%A4umige-2-zimmer-wohnung-im-1.og-1082480503/)                                                                     | Jun 11, 07:03      |
|       674.4  |            48 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/matzingerstra%C3%9Fe:-sch%C3%B6ne-2-zimmerwohnung-in-u-bahnn%C3%A4he-1222775390/)                                          | Jun 10, 17:46      |
|       759.19 |            58 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/genie%C3%9Fen-sie-diesen-weitblick%21-teilm%C3%B6blierte-2-zimmer-wohnung---mit-gro%C3%9Fem-wintergarten-1497315679/)    | Jun 10, 17:35      |
|       726.1  |            41 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei:-unbefristeter-41m%C2%B2-altbau-mit-einbauk%C3%BCche-in-ruhelage---1150-wien-1958234651/) | Jun 10, 17:07      |
|       760    |            55 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/verandawohnung-f%C3%BCr-paare-zwischen-den-schl%C3%B6ssern-%28sch%C3%B6nbrunn---hetzendorf%29-1377679917/)                | Jun 10, 14:35      |
|       700    |            63 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindebauwohnung-in-gr%C3%BCnlage-3-personen-minimum%21-1525226988/)                                                | Jun 10, 13:42      |
