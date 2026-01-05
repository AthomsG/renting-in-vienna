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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            60 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/single--oder-p%C3%A4rchenwohnung-sucht-langfristige/n-mieter/in-1153149688/)                                                                      | Jan 05, 14:13      |
|       770.07 |            52 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/helle-moderne-und-top-ausgestattete-2-zimmerwohnung-unbefristet-zu-vermieten-2070161799/)                                                           | Jan 05, 14:00      |
|       473    |            41 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/zimmer-k%C3%BCche-kabinett---altbau-wohnung-in-top-zustand-direkt-bei-u3-und-ekazent-1487644214/)                                                 | Jan 05, 13:55      |
|       658    |            37 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/m%C3%B6blierte-neubauwohnung-mit-balkon-1160-wien--abl%C3%B6se-3.700-1611649868/)                                                                 | Jan 05, 12:11      |
|       435    |            41 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/1050-wien-gassergasse-41/-stg.-4/-top-22-1125928790/)                                                                                            | Jan 05, 11:55      |
|       797    |            41 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-freundliche-2-zimmer-wohnung-gute-anbindung-viel-stauraum-1312711165/)                                                                      | Jan 04, 19:09      |
|       543.4  |            52 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe---wiener-wohnen-%7C-52-m%C2%B2-%7C-2-zimmer-%7C-balkon-%7C-viel-sonne-&-gr%C3%BCn-%7C-wiener-wohnticket-bis-31.10.2025-1003571743/) | Jan 04, 15:40      |
