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
|       652.31 |            62 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kamarschgasse-/-helle-62-m%C2%B2-unbefristete-hauptmiete-/-4.-stock-ohne-lift-1450252873/)                                                                                      | May 12, 06:45      |
|       795    |            43 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/g%C3%BCnstige-wohnung-komplett-ausgestattet-1631886649/)                                                                                                                          | May 11, 19:37      |
|       720    |            63 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/n%C3%A4he-botanischer-garten---mohsgasse-%7C-zentral-gelegene-63m%C2%B2-altbauwohnung-mit-flair-%7C-2-zimmer-%7C-k%C3%BCche-%7C-gesamtmiete-%E2%82%AC-720----1922119787/) | May 11, 18:43      |
|       760    |            50 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nachmieter-f%C3%BCr-2-zimmerwohnung-im-10.-bezirk-gesucht-1816162836/)                                                                                                          | May 11, 14:45      |
|       749    |            45 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/generalsanierte-unbefristete-altbaumiete-bei-thaliastrasse-und-brunnen-markt-n%C3%A4he-%21-1828079116/)                                                                         | May 11, 14:08      |
|       780    |            25 |          3 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/heller-b%C3%BCroraum-im-6.-bezirk-zur-untermiete-1287685059/)                                                                                                                   | May 11, 13:16      |
|       511    |            64 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-3-zimmer-%2Adirektvergabe-vormerkschein-vor-31.03.2026-2025868556/)                                                                                             | May 11, 12:47      |
|       790    |            35 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisonsfrei:-bei-u1-keplerplatz-viktor-adler-markt-789956491/)                                                                                                                | May 11, 12:28      |
|       742.32 |            64 |          3 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/helle-3-zimmer-wohnung-unmittelbar-neben-der-u-bahnstation-alser-stra%C3%9Fe-1718253602/)                                                                                         | May 11, 12:05      |
|       589    |            95 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-mit-balkon-883269631/)                                                                                                                                         | May 11, 10:58      |
