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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       699    |            62 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-1562919686/)                                                                                                                                        | May 22, 19:22      |
|       650    |            57 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeindewohnung-zur-direktvergabe-797350289/)                                                                                                                                                               | May 22, 17:18      |
|       799.94 |            44 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/modernes-wohngef%C3%BChl-mit-balkon-1061056852/)                                                                                                                                                          | May 22, 16:48      |
|       599    |            54 |          4 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/luxus-4-zimmer-wohnung-im-17.-bezirk-ab-15.-juli.-komplett-kernsaniert-&-vollm%C3%B6bliert-inklusive-tischlerk%C3%BCche-klima-samsung-tv-und-hochwertigen-m%C3%B6beln.-nur-599-%E2%82%AC-miete-1354814108/) | May 22, 16:34      |
|       787.6  |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/grossz%C3%BCgige-2-zimmer-wohnung-im-10.bezirk%21-1872106349/)                                                                                                                                            | May 22, 16:18      |
|       798    |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/topsaniert%21-k%C3%BCche-neu%21-ruhige-2-zimmer-wohnung%21-n%C3%A4he_u1-troststra%C3%9Fe%21-970788898/)                                                                                                   | May 22, 12:10      |
|       796.84 |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/neues-heim-direkt-auf-der-mariahilferstra%C3%9Fe-gelegen%21-1107432768/)                                                                                                                  | May 22, 10:28      |
|       794.2  |            73 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-helle-2-zimmer-altbauwohnung---n%C3%A4he-schloss-sch%C3%B6nbrunn-1340159827/)                                                                                                                    | May 22, 09:24      |
|       561    |           nan |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/attraktives-wohnen-mitten-im-sonnwendviertel-1521247803/)                                                                                                                                                 | May 22, 08:59      |
