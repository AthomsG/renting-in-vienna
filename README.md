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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       432.78 |            42 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/2-zimmer-gemeindewohnung-direktvergabe-%28nur-mit-wiener-wohnticket-bis-31.10.2025%29-1536772713/)                                                                                 | Feb 13, 21:15      |
|       648    |            65 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/nachmieter-f%C3%BCr-wiener-gemeindewohnung-gesucht-1385017605/)                                                                                                                 | Feb 13, 18:39      |
|       548    |            36 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-f%C3%BCr-den-mieter%21-singlewohnung%21-studenten-bevorzugt%21-laurenzgasse-zentrumslage-hofruhelage-%C3%A4ltere-36m%C2%B2-neubaumiete-erdgeschoss-1172235690/) | Feb 13, 16:07      |
|       762    |            57 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/provisionsfrei-f%C3%BCr-den-mieter%21-ganghofergasse-altbaumiete-57m%C2%B2-mit-balkon-3.-stock-mietvertrag-unbefristet-gartenben%C3%BCtzung%21-1068413378/)                     | Feb 13, 16:00      |
|       779    |            34 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.5.2026---laxenburgerstra%C3%9Fe-151---1100-wien---traumhafte-neubau---singlewohnung-im-9ten-stock-mit-fernblick-1428023853/)                                               | Feb 13, 12:37      |
|       700    |            44 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sanierte-2-zimmer-wohnung-1030-nahe-rochusmarkt-provisionsfrei-827011347/)                                                                                                | Feb 13, 10:49      |
|       604.83 |            58 |          3 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-%223-zimmer-gemeindewohnung---direktvergabe-%28vormerkschein-bis-30.11.2025%29-1170-wien-2030098717/)                                                            | Feb 13, 09:57      |
