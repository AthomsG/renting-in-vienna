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
|       748    |            45 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei-f%C3%BCr-den-mieter%21-felbigergasse-n%C3%A4chst-hanusch-krankenhaus-%C3%A4ltere-45m%C2%B2-neubaumiete-halbstock-1224906250/) | May 07, 19:03      |
|       750    |            52 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/helle-altbauwohnung-mit-moderner-k%C3%BCche-in-toplage-1040-wien-1421514615/)                                                                 | May 07, 16:45      |
|       617.69 |            51 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-altbauwohnung-mit-lift-in-guter-lage-des-14.-bezirks-1161608745/)                                                                   | May 07, 16:21      |
|       780    |            33 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/city-apartment-in-ruhiger-lage-mit-top-u-bahn-anschluss-1937114865/)                                                                         | May 07, 16:20      |
|       750    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sehr-sch%C3%B6ne-vor-einem-jahr-vollsaniert-2-zimmerwohnung-im-10.-bezirk%21%21-1323658315/)                                               | May 07, 16:13      |
|       689    |            48 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhiges-apartment-mit-2-zimmern-nahe-u3-h%C3%BCtteldorfer-stra%C3%9Fe/-schmelz---provisionsfrei-1193745974/)                                 | May 07, 15:56      |
|       712    |            61 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/sanierte-2-zimmer-wohnung---unbefristet%21-969034207/)                                                                     | May 07, 15:34      |
|       799.08 |            63 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-mit-terrasse-zu-vermieten-1926561089/)                                                                                    | May 07, 12:34      |
|       799.9  |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/himberger-stra%C3%9Fe-17/volkmargasse-4-1100-wien-992592569/)                                                                              | May 07, 11:48      |
|       782.87 |            66 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/brotfabrikn%C3%A4he-/-helle-66-m%C2%B2-altbaumiete-/-unbefristete-hauptmiete-853732891/)                                                   | May 07, 10:56      |
