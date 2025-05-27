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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       610.98 |            63 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/n%C3%A4he-u3-ottakring-:-voll-m%C3%B6blierte-mietwohnung%21-2032359177/)          | May 27, 17:45      |
|       618.63 |            50 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristeter-sofortbezug-in-der-fernkorngasse-907266005/)                        | May 27, 14:57      |
|       650    |            62 |          3 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe-gemeindewohnung---vormerkschein-f.-3-zimmer-1035361550/)             | May 27, 11:20      |
|       618    |            58 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/anfragestop%21%21-gemeindewhg-direktvergabe-vmd-%21%21-30.04.25-%21%21-1605941524/) | May 26, 23:09      |
|       750    |            35 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/schicke-singlewohnung-mit-weitblick-801346666/)                                     | May 26, 20:34      |
|       776.31 |            39 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/nach-generalsanierung-erstbezug-1984917871/)                                      | May 26, 20:22      |
|       540    |            50 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung---nachmieter-gesucht-936742454/)                                  | May 26, 17:51      |
