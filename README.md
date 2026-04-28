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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       675.17 |            65 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/ruhige-wohnlage-%2B-gepflegter-altbau-%2B-nahe-wiedner-hauptstra%C3%9Fe%21-1438314540/)                             | Apr 28, 11:03      |
|       651.8  |            50 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristet-mit-untervermietungsrecht%21-individuell-gestaltbare-wohnung-mit-top-mietkonditionen-1383403702/)          | Apr 28, 11:03      |
|       767.11 |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mietwohnung-im-herzen-von-favoriten-incl.-garage%21-1349345028/)                                                     | Apr 28, 10:12      |
|       790    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/60-m2-2-zimmer-wohnung-hauptmiete.-1098030308/)                                                                      | Apr 28, 08:20      |
|       763.22 |            58 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gepflegte-ruhige-2-zimmer-wohnung-in-einer-sackgasse-2031592536/)                                                      | Apr 28, 04:11      |
|       673.14 |            53 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-sanierte-3-zimmer-buchengasse-2119869848/)                                                                     | Apr 27, 21:34      |
|       744.3  |            32 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-m%C3%B6blierte-2-zimmer-wohnung-mit-balkon-zentral-in-der-leopoldstadt%7C-maxi-bude-1893604330/) | Apr 27, 16:28      |
|       520    |            57 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wienerwohnung-1116566840/)                                                                                           | Apr 27, 13:27      |
|       677.61 |            57 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/westbahnhofnah-neusanierte-hauptmietwohnung-in-der-zinckgasse-937550421/)                            | Apr 27, 12:04      |
|       462.65 |            37 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/befristete-altbauwohnung-in-der-balderichgasse-1050558858/)                                                            | Apr 27, 09:48      |
