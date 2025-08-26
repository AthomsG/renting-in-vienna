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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       547.23 |            50 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung%21-vormerkschein-bis-30.06.2025-direktvergabe-2066783541/)                             | Aug 26, 19:08      |
|       750    |            30 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%2Asmarte-2-zimmer-kleinwohnung%2A---neubau-in-sch%C3%B6nbrunn-n%C3%A4he-1317407432/)                    | Aug 26, 16:55      |
|       650    |            66 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/65m2-n%C3%A4he-mariahilferstra%C3%9Fe-%28vormerkschein-wiener-wohnen%29-u-bahn-u2-u3-&-u4-1746488452/) | Aug 26, 13:34      |
|       630.3  |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/moderne-2-zimmer-wohnung-mit-perfekter-infrastruktur-943814648/)                       | Aug 26, 12:49      |
|       770    |           nan |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernes-wohn--und-gesch%C3%A4ftshaus-1813514366/)                                                     | Aug 26, 09:56      |
|       778    |            51 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wundersch%C3%B6ne-2-zimmer-wohnung-zu-vermieten-2038635492/)                                             | Aug 26, 09:17      |
|       509    |            47 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-gemeindewohnung-vormerkschein-stichtag-31.5.2025-2046776653/)                         | Aug 26, 09:06      |
|       692.07 |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmerwohnung-in-der-gudrunstrasse-n%C3%A4he-u1-1915557035/)                                         | Aug 25, 20:35      |
|       580    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-965708792/)                                                                                     | Aug 25, 18:11      |
