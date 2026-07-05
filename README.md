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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                               | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       650    |            69 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-1050-wien---69-m%C2%B2-%7C-2-zimmer-%7C-vormerkschein-bis-30.06.26-erforderlich-1476809408/) | Jul 05, 18:04      |
|       652.31 |            62 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/karmarschgasse-/-helle-62-m%C2%B2-unbefristete-hauptmiete-/-4.-stock-ohne-lift-%28top-48-49%29-2123426868/)   | Jul 05, 15:16      |
|       799    |            38 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wundersch%C3%B6ne-2-zimmerwohnung-mit-balkon-in-u-bahn-n%C3%A4he-910074394/)                                  | Jul 05, 09:45      |
|       751.21 |            46 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-in-wien-meidling-zu-vermieten-1095660742/)                                                    | Jul 05, 09:36      |
