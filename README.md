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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       461.2  |            45 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-/-gemeindebau-direktvergabe-843808031/)                                                                              | Jun 14, 21:39      |
|       512    |            48 |          2 | 04. Wieden    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/2-zimmer-gemeindewohnung-im-4.-bezirk/48m2-1757112704/)                                                                                  | Jun 14, 21:31      |
|       750    |            43 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-zentrale-2-zimmer-wohnung-%2843-m%C2%B2%29-nahe-thaliastra%C3%9Fe---teilm%C3%B6bliert-1329875959/)                              | Jun 14, 20:22      |
|       739    |            44 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei---25-zimmer-wohnung-in-ruhiger-lage---besichtigungstermin-montag-15.6.2026-um-20-uhr-1950843414/)                      | Jun 14, 19:34      |
|       677.61 |            39 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neilreichgasse-39-m2-neubau-2-zimmer-komplettk%C3%BCche-duschbad-parketten-1.-liftstock-1305544999/)                                  | Jun 14, 18:06      |
|       556    |            42 |          2 | 04. Wieden    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/g%C3%BCnstige-wohnung-in-wieden-1675453633/)                                                                                             | Jun 14, 17:53      |
|       512    |            44 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/1160-wien-seeb%C3%B6ckgasse:-extrem-ruhige-topsanierte-2-zimmer-altbautraumwohnung-ca.-44-m2-unbefristet-zu-vermieten%21-1254486934/) | Jun 13, 23:33      |
