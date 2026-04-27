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
|       799.19 |            51 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/moderne-2-zimmer-eg-wohnung-in-1030-wien-mit-einbauk%C3%BCche-und-u-bahn-n%C3%A4he%21-2072604985/)             | Apr 27, 21:37      |
|       673.14 |            53 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-renovierte-3-zi-mietwohnung-buchengasse-2119869848/)                                                           | Apr 27, 21:34      |
|       744.3  |            32 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-m%C3%B6blierte-2-zimmer-wohnung-mit-balkon-zentral-in-der-leopoldstadt%7C-maxi-bude-1893604330/) | Apr 27, 16:28      |
|       520    |            57 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wienerwohnung-1116566840/)                                                                                           | Apr 27, 13:27      |
|       677.61 |            57 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/westbahnhofnah-neusanierte-hauptmietwohnung-in-der-zinckgasse-937550421/)                            | Apr 27, 12:04      |
|       514.64 |            44 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-und-preiswerte-2---zimmer-wohnung-948362092/)                                                            | Apr 27, 11:15      |
|       462.65 |            37 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/befristete-altbauwohnung-in-der-balderichgasse-1050558858/)                                                            | Apr 27, 09:48      |
|       790    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristet---ideal-geschnittene-2-zimmerwohnung-nahe-meidlinger-markt%21-kein-aufzug%21-1794653321/)                 | Apr 27, 07:43      |
