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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       548    |            54 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/1160-wien-blumberggasse-topsanierte-2-zimmer-altbautraumwohnung-ca.-54-m2-unbefristet-zu-vermieten-1351778215/)                             | Feb 03, 01:43      |
|       670    |            61 |          3 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeindewohnung-%7C-3-zimmer-%7C-ca.-62-m%C2%B2-%7C-wohnticket-bis-30.11.2025%7C-franz%C3%B6sischer-balkon-%7C-teilm%C3%B6bliert-1183197662/) | Feb 02, 22:20      |
|       658.41 |            61 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-mit-2-zimmer-wohnticketsnummer-:-42775/2024.-die-wohnung-ist-reserviert%21-1312659054/)                                    | Feb 02, 21:23      |
|       770    |            64 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/stilvolle-2-zimmer-wohnung-mit-offener-wohnk%C3%BCche---zentral-&-hell-1916021794/)                                                        | Feb 02, 21:22      |
|       649    |            63 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/fenzlgasse---sanierungsbed%C3%BCrftiger-2-zimmer-altbau-mit-extra-k%C3%BCche-zu-vermieten-1981200035/)                                        | Feb 02, 18:25      |
|       620    |            56 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/wohnung-mieten-1077196170/)                                                                                                                   | Feb 02, 16:27      |
|       774.38 |            75 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/generalsanierung-2023---ger%C3%A4umige-mietwohnung%21-1532262194/)                                                                          | Feb 02, 14:53      |
