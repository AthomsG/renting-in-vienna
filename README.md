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
|       595.83 |            55 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/%28reserviert%29-%28bitte-keine-anfragen-mehr%29-zentrale-gemeindewohnung-in-1060-vormerkschein-bis-30.11.2025-842092453/) | Dec 18, 14:53      |
|       699.34 |            48 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-gl%C3%BCck-in-hernals-%7C-unbefristet-wohlf%C3%BChlen-%7C-6-m%C2%B2-innenhof-terrasse-%7C-erdgeschoss-1633185559/)  | Dec 18, 13:43      |
|       795.3  |            43 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neubau-in-favoriten%21-2-zimmer-wohnung-auf-knapp-43m2-1080021267/)                                                        | Dec 18, 12:11      |
|       462    |            46 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-gemeindewohnung-46m2-balkon-1030-rennweg-1334106781/)                                                  | Dec 18, 11:51      |
|       622.43 |            38 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sonniger-neubau-beim-yppenplatz-1971325831/)                                                                                 | Dec 18, 10:37      |
|       799    |            41 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zi-wohnung-mit-balkon---nahe-u1-%28provisionsfrei%21%29-1545612855/)                                                     | Dec 18, 09:57      |
|       737.36 |            70 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28direktvergabe%29-2-1/2-zimmer-gemeindewohnung-in-1110-wien-2014515130/)                                                 | Dec 18, 02:29      |
|       495    |            48 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-gut-gelegene-sanierte-2-zimmer-wohnung-mit-parkblick-1578971979/)                                                    | Dec 17, 15:18      |
