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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       604.83 |            58 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-%223-zimmer-gemeindewohnung---direktvergabe-%28vormerkschein-bis-30.11.2025%29-1170-wien-2030098717/)                                                                  | Jan 23, 09:57      |
|       470    |            43 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-per-direktvergabe-1517165752/)                                                                                                                                       | Jan 23, 09:51      |
|       739.13 |            52 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/neubauwohnung-mit-25-zimmer-nahe-matzleinsdorferplatz-1367857013/)                                                                                                                   | Jan 23, 04:04      |
|       787.22 |            53 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/perfekt-angebundene-%28u1%29-zentral-gelegene-altbauwohnung-in-1020-wien-%28ab-sofort-verf%C3%BCgbar%29-885930537/)                                                                | Jan 22, 16:37      |
|       516    |          4591 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeinde-wohnung-ticketnummer-30.11.2025-1632094532/)                                                                                                                                   | Jan 22, 15:24      |
|       690    |            60 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei-f%C3%BCr-den-mieter%21-hellgasse-n%C3%A4chst-u6-%C3%A4ltere-neubaumiete-60m%C2%B2-komplettk%C3%BCche-1.-stock-5-jahre-befristet%21-studenten-bevorzugt%21-2028435947/) | Jan 22, 13:24      |
|       799    |            36 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/odo25-%7C-2-zimmer-%7C-dachgeschoss-%7C-erstbezug-%7C-mietbeginn-ab-01.07.2026-1512653570/)                                                                                           | Jan 22, 11:47      |
|       680.66 |            38 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/nachmieter-gesucht-wohnung-in-top-lage-zu-vergeben-926776476/)                                                                                                                        | Jan 22, 11:20      |
