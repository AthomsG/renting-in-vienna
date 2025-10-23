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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|          650 |            53 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sonnige-25-zimmer---n%C3%A4he-lorenz-bayer-park-1844784075/)                                                                | Oct 23, 15:46      |
|          405 |            42 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kosteng%C3%BCnstige-mietwohnung-899043662/)                                                                               | Oct 23, 11:35      |
|          700 |            41 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neu-renovierte-2-zimmer-wohnung-mit-perfekter-%C3%B6ffentlicher-anbindung-ideal-f%C3%BCr-studenten-1429313660/)           | Oct 23, 10:48      |
|          636 |            44 |          2 | 07. Neubau    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/nachmieter-gesucht-f%C3%BCr-helle-ruhige-wohnung-%2844-mq%29--n%C3%A4he-lugner-city-kontakt-bitte-per-whats-upp-2055428666/) | Oct 23, 10:04      |
|          750 |            48 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/vollm%C3%B6blierte-wohnung-mitte-november---mitte-april-1130935152/)                                                        | Oct 22, 18:40      |
