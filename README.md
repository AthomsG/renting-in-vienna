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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       550    |            62 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-1255824861/)                                                                          | Jul 23, 17:00      |
|       792.55 |            47 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/m%C3%B6blierte-gem%C3%BCtliche-2-zimmer-wohnung-im-15.bezirk%21-870079607/)                         | Jul 23, 16:55      |
|       519    |            48 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeinde-wohnung-vormerkschein-30.06.2025-1276953658/)                                                  | Jul 23, 16:44      |
|       457.68 |            43 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeindewohnung:-2-zimmer-%7C-43-m%C2%B2-%7C-1140-hugo-breitner-hof-%7C-wiener-wohn-ticket-1398510386/) | Jul 23, 16:26      |
|       719    |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-01.08.2025---gepflegte-neubau-singlewohnung-mit-balkon-1131123750/)                                              | Jul 23, 16:08      |
|       633.42 |            57 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-m%C3%B6blierte-gemeindewohnung-1110-wien-%28direktvergabe%29-922247438/)                           | Jul 23, 14:26      |
|       785.99 |            49 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ankommen-&-wohlf%C3%BChlen:-2-zimmer-in-zentraler-lage-in-1150-wien%21-1855773724/)                 | Jul 23, 12:17      |
|       630    |            42 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/charmante-2-zimmer-wohnung-in-ottakring-1601482759/)                                                                | Jul 23, 10:21      |
|       750    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-wohnung-i-top-anbindung-i-n%C3%A4he-sch%C3%B6nbrunn-2073893781/)                                      | Jul 23, 09:31      |
|       460.54 |            44 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe---gemeinde-wohnung-von-wiener-wohnen---1020-wien-1045035292/)                                      | Jul 22, 20:43      |
|       577.63 |            60 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-von-wiener-wohnen---direktvergabe-915984795/)                                                      | Jul 22, 19:42      |
|       790    |            68 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristet-1516865725/)                                                                                            | Jul 22, 19:35      |
|       770    |            48 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/48m2-im-ruhigen-teil-simmerings-1632409426/)                                                                        | Jul 22, 19:23      |
|       450    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen-ticket-notwendig-1504331306/)                                                           | Jul 22, 18:54      |
|       426    |            41 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-im-2.-bezirk-zu-vergeben---vms:-31.5.2025-1587969267/)                                           | Jul 22, 18:19      |
