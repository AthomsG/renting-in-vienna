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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       600    |            60 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-vormerkschein-august-2025-2111099678/)                                                                            | Oct 07, 18:57      |
|       638    |            51 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/topaltbau-hauptmiete-unbefristet-f%C3%BCr-p%C3%A4rchen-oder-single-geeignet-2106017518/)                                               | Oct 07, 18:17      |
|       739.57 |            34 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/wohnung-in-ruhelage-mitten-im-8.-f%C3%BCr-singls-1343385042/)                                                                          | Oct 07, 17:33      |
|       500.73 |            49 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindebau-direktvergabe-848868991/)                                                                                                    | Oct 07, 17:05      |
|       796    |            36 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter%2Ain-f%C3%BCr-teilm%C3%B6blierte-wohnung-mit-balkon-pool-und-sauna-im-sonnwendviertel-1983444977/)                           | Oct 07, 16:27      |
|       750    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-hoflage-attraktive-unbefristete-2-zimmerwohnung-in-stil-altbau-u-1-n%C3%A4he-987551283/)                                 | Oct 07, 15:58      |
|       770    |            53 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/traumhafte-2--zimmer-wohnung-%7C-unbefristet-%7C-mit-gemeinschaftsterrasse-2066549860/)                                                  | Oct 07, 15:17      |
|       719    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zimmer-wohnung-nahe-reumannplatz-zu-vermieten---provisionsfrei-1197112402/)                                                     | Oct 07, 10:38      |
|       699    |            46 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei--sch%C3%B6ne-2-zimmerwohnung-n%C3%A4he-sch%C3%B6nbrunn-1020264997/)                                      | Oct 07, 09:53      |
|       705.32 |            42 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/erstbezug-nach-sanierung-%28wird-gerade-saniert%29--miete-inkl.-heizkosten-und-warmwasser/-unbefristeter-mietvertrag-1962813371/) | Oct 07, 09:13      |
