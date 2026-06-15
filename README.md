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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       772.26 |            58 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gut-aufgeteilte-zweieinhalb-zimmerwohnung-in-ruhiger-wohngegend%21-1270165041/)                        | Jun 15, 11:36      |
|       706    |            49 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/unbefristet%3B-zweizimmerwohnung-n%C3%A4chst-hauptbahnhof-1424404027/)                                                | Jun 15, 10:54      |
|       707    |            94 |          3 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/3-zimmer-gemeindewohnung/-9411-m%C2%B27miete-707---/-abl%C3%B6se/-vormerkschein-vor-28.2.26-825003601/)                | Jun 15, 09:50      |
|       783.59 |            36 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-2-zimmer-wohnung-%28ca.-36-m%C2%B2%29-in-meidling-zur-nachmiete---m%C3%B6bliert-&-top-lage-974021910/) | Jun 14, 23:31      |
|       461.2  |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-/-gemeindebau-direktvergabe-843808031/)                                                               | Jun 14, 21:39      |
|       750    |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-zentrale-2-zimmer-wohnung-%2843-m%C2%B2%29-nahe-thaliastra%C3%9Fe---teilm%C3%B6bliert-1329875959/)               | Jun 14, 20:22      |
|       755    |            44 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei---25-zimmer-wohnung-in-ruhiger-lage---besichtigungstermin-montag-15.6.2026-um-20-uhr-1950843414/)       | Jun 14, 19:34      |
|       556    |            42 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/g%C3%BCnstige-wohnung-in-wieden-1675453633/)                                                                              | Jun 14, 17:53      |
