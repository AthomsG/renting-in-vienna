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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       557.83 |            37 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/unbefristete-altbau-single-wohnung-beim-kongresspark-1316605813/)                                            | Jun 09, 17:25      |
|       750    |            33 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/charmante-2-zimmer-altbauwohnung-mit-einbauk%C3%BCche-in-1140-wien---3285m%C2%B2---750eur-miete-1487828651/) | Jun 09, 17:06      |
|       682    |            87 |          3 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung-1160-direktvergabe-1834363660/)                                                            | Jun 09, 16:50      |
|       795.29 |            32 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-2-zimmer-wohnung-1553179949/)                                                                    | Jun 09, 14:21      |
|       770    |            45 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-renovierung---unbefristet---u6-&-s-bahn-ums-eck---innenhof-ruhelage-1723941805/)             | Jun 09, 12:56      |
|       700    |            48 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wir-vermieten-unsere-2-zimmer-wohnung-zur-kurzzeitmiete-vom-15.06.-bis-31.07-1621845201/)                    | Jun 09, 12:10      |
|       525    |            65 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2.-zimmer-wohnung-wiener-wohnen-1148945371/)                                                                 | Jun 09, 09:52      |
|       680.02 |            51 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/anzeige-1696992555/)                                                                                         | Jun 09, 09:19      |
|       590    |            55 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ruhige-gemeindewohnung---wiener-wohnticket-mit-vormerkschein-vor-31.5.2026-n%C3%B6tig%21-2059494675/)      | Jun 08, 23:59      |
