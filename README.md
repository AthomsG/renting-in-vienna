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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       500    |            42 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-gemeinde-wohnung-in-1120-wr.-wohn-ticket-sp%C3%A4testens-31.12.2025-1392923826/)                                                                                                       | Jan 26, 17:09      |
|       662    |            60 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/kalvarienberggasse/-n%C3%A4he-elterleinplatz-%2B%2B-ger%C3%A4umige-&-helle-60m%C2%B2-altbauwohnung-mit-flair-%2B%2B-2-zimmer-%2B%2B-k%C3%BCche-mit-fenster%2B%2B-gesamtmiete-662----1008182953/) | Jan 26, 16:45      |
|       609.07 |            41 |          2 | 04. Wieden    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/sch%C3%B6ne-2-zimmer-wohnung-in-optimaler-lage-nahe-der-tu-2118910900/)                                                                                                                           | Jan 26, 10:31      |
|       753.41 |            44 |          2 | 07. Neubau    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/ruhige-sch%C3%B6ne-wohnung-in-bester-lage-im-7.-bezirk-mit-gr%C3%BCnblick-komplett-m%C3%B6bliert-1279363855/)                                                                                     | Jan 25, 20:24      |
|       751.36 |            33 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/m%C3%B6blierte-zweizimmerwohnung-%28reserviert%29-829281441/)                                                                                                                                    | Jan 25, 18:03      |
