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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       737.06 |            71 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-bis-31.08.2024-%28bitte-f%C3%BCr-3-wohnr%C3%A4ume-und-g%C3%BCltige-wiener-wohn-ticket%29-2061243102/) | Jan 30, 08:26      |
|       480    |            53 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-wohnung-f%C3%BCr-sozialbaumieter-&-co-957683553/)                                                                                     | Jan 30, 06:29      |
|       587    |            54 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-2-zimmer-gemeindewohnung-882959164/)                                                                                        | Jan 30, 02:35      |
|       552.39 |            44 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-gemeindewohnung-n%C3%A4he-h%C3%BCtteldorf/-ober-st.-veit-%28nur-direktvergabe-mit-vormerkschein-bis-31.10.2025%29-1894016773/)     | Jan 29, 20:11      |
|       749    |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-charmante-2-zimmer-wohnung---ideal-f%C3%BCr-urbane-lebensqualit%C3%A4t%21-784883303/)                   | Jan 29, 18:06      |
|       512.67 |            47 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/direktvergabe-sonnige-gemeindewohnung-im-4.-bezirk-859595159/)                                                                               | Jan 29, 15:46      |
|       471.4  |            47 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-gemeindewohnung-in-ottakring-%28direktvergabe%29-2076098211/)                                                                    | Jan 29, 13:27      |
|       680    |            47 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-altbauwohnung-nahe-yppenplatz-2116073730/)                                                                                         | Jan 29, 13:06      |
|       783.85 |            69 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/3-zimmer-wohntraum-in-sch%C3%B6nbrunn-n%C3%A4he-%22unbefristet%22-direkt-vom-eigent%C3%BCmer-1533740902/)                                   | Jan 29, 11:16      |
|       668.62 |            58 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/zwei-zimmer-wohnung---unbefristete-hauptmiete-774752111/)                                                                                 | Jan 29, 11:14      |
|       524    |            48 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-helle-gemeindebauwohnung-4.-stock-mit-aufzug-1923638747/)                                                                   | Jan 29, 08:56      |
