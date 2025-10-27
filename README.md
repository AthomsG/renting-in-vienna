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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       777.73 |            34 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/moderne-2-zimmer-wohnung-mit-balkon-in-ruhiger-lage-2135469424/)                                                                           | Oct 27, 10:56      |
|       796.01 |            35 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/tolle-2-zimmerwohnung-%2B-balkon%21-nachmietersuche%21-top-lage---sehr-nahe-dem-hauptbahnhof-&-belvedere%21-ubahn-n%C3%A4he%21-776160134/) | Oct 27, 09:49      |
|       648.53 |            44 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/besichtigung-28.10.2025-17:00-18:30-wohnung-in-1110-wien---felsgasse-4/8-2120378620/)                                                      | Oct 27, 09:27      |
|       450    |            41 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-wiener-wohnen-%28vms-07/2025%29-2063731150/)                                                                              | Oct 27, 09:22      |
|       520    |            68 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/weitergabe-gemeindewohnung-1160-wien-2013087141/)                                                                                          | Oct 27, 07:35      |
|       565    |            44 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neu-renovierte-wohnung-in-favoriten-1100-mit-guter-anbindung-1802125127/)                                                                  | Oct 26, 21:12      |
|       591.65 |            53 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-2119431999/)                                                                                                               | Oct 26, 19:01      |
|       480.9  |            44 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmerwohnung-nur-mit-vormerkschein%21-786636717/)                                                                                       | Oct 26, 15:42      |
