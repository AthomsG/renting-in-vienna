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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       746.47 |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/super-aufgeteilte-2-zimmerwohnung-beim-waldm%C3%BCller-park---n%C3%A4he-matzleinsdorferplatz-1826694763/) | Sep 05, 20:32      |
|       708    |            50 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/50-m%C2%B2-wohnung-n%C3%A4he-brunnenmarkt-/-u6-/-yppenplatz-1063743791/)                                  | Sep 05, 20:23      |
|       755    |            53 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%28reserviert%29-nachmieterin-wohnung-1050-2074673246/)                                                  | Sep 05, 17:24      |
|       520    |            50 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-1788913345/)                                                          | Sep 05, 13:52      |
|       771.51 |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gr%C3%BCnruhelage---super-geschnittene-2-zimmerwohnung-mit-kleinen-balkon-1891113989/)                    | Sep 05, 11:37      |
|       748    |            40 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/kleine-2-zimmer-dachwohnung-mit-terrasse%21-863096262/)                                                   | Sep 05, 10:27      |
|       708.96 |            51 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-1548483361/)                                                                             | Sep 05, 06:48      |
