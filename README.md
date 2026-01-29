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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       524    |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-helle-gemeindebauwohnung-4.-stock-mit-aufzug-1923638747/)                                                    | Jan 29, 08:56      |
|       520    |            39 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-erdgescho%C3%9Fwohnung-in-ruhiger-gasse-sucht-langfristige/n-mieter/in-1620381264/)                           | Jan 29, 02:07      |
|       749.58 |            48 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/westbahnstra%C3%9Fe---helle-2-zimmerwohnung-1207734046/)                                                                      | Jan 28, 18:25      |
|       504.75 |            46 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-%281-zimmer-plus-gro%C3%9Fe-wohnk%C3%BCche%29-zur-direktvergabe---perfekte-lage-im-5.-bezirk-1075971245/) | Jan 28, 16:22      |
|       680    |            58 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristeter-mietvertrag%21-4.-stock-ohne-lift%21-1337240631/)                                                             | Jan 28, 15:57      |
|       770    |            56 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/schicke-mietwohnung-in-privater-jugendstil-villa-mit-zwei-zimmern-568557971/)                                               | Jan 28, 15:42      |
