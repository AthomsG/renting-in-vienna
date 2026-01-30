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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       795    |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-%2A-wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1833355036/)                                            | Jan 30, 15:18      |
|       638.37 |            34 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/vollausgestattete-helle-2-zimmer-wohnung-direkt-vom-vermieter-1867862481/)                                                                | Jan 30, 15:07      |
|       700    |            40 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/studentenwohnung-in-neuwaldegg-40-m2-1298815956/)                                                                                           | Jan 30, 12:43      |
|       604.83 |            58 |          3 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-%223-zimmer-gemeindewohnung---direktvergabe-%28vormerkschein-bis-30.11.2025%29-1170-wien-2030098717/)                      | Jan 30, 09:57      |
|       470    |            43 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-per-direktvergabe-1517165752/)                                                                                           | Jan 30, 09:51      |
|       580    |            39 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtliche-wohnung-sucht-langfristige/n-mieter/in--2-stock-ohne-lift%21-1334444221/)                                                 | Jan 30, 09:13      |
|       737.06 |            71 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-bis-31.08.2024-%28bitte-f%C3%BCr-3-wohnr%C3%A4ume-und-g%C3%BCltige-wiener-wohn-ticket%29-2061243102/) | Jan 30, 08:26      |
|       480    |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/top-wohnung-f%C3%BCr-sozialbaumieter-&-co-957683553/)                                                                                     | Jan 30, 06:29      |
|       587    |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-2-zimmer-gemeindewohnung-882959164/)                                                                                        | Jan 30, 02:35      |
|       552.39 |            44 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-gemeindewohnung-n%C3%A4he-h%C3%BCtteldorf/-ober-st.-veit-%28nur-direktvergabe-mit-vormerkschein-bis-31.10.2025%29-1894016773/)     | Jan 29, 20:11      |
|       749    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-charmante-2-zimmer-wohnung---ideal-f%C3%BCr-urbane-lebensqualit%C3%A4t%21-784883303/)                   | Jan 29, 18:06      |
|       512.67 |            47 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/direktvergabe-sonnige-gemeindewohnung-im-4.-bezirk-859595159/)                                                                               | Jan 29, 15:46      |
