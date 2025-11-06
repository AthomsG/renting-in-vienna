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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       730    |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-vermieten-1693099395/)                                                                                     | Nov 06, 16:08      |
|       554.28 |            58 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeindewohnung---direktvergabe---wohnticket-f%C3%BCr-2-zimmer---vor-31.10.2025-1638564529/)                                | Nov 06, 14:34      |
|       485    |            44 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-f%C3%BCr-wiener-wohnen-2-zimmer-wohnung-1180719112/)                                                            | Nov 06, 13:05      |
|       741.72 |            53 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/top-2-zimmer-wohnung-mit-einbauck%C3%BCche-1381812063/)                                                                        | Nov 06, 11:15      |
|       590.28 |            49 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/charmante-2-zimmer-altbauwohnung-1954506923/)                                                                                  | Nov 06, 11:15      |
|       710    |            65 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-geimeindewohnung-10.-bezirk-otto-probst-stra%C3%9Fe.-vormerkschein-bis-zum-31.10.2025-n%C3%B6tig-1684726354/) | Nov 06, 10:57      |
|       752.02 |            54 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/text-f%C3%BCr-einen-besichtigungstermin-lesen-%28siehe-weiter-unten%29-957270523/)                          | Nov 06, 10:17      |
|       799    |            38 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-sofort%21-kompakte-singlewohnung-mit-k%C3%BCchenzeile-und-balkon-im-dachgeschoss---1100-wien-erlachplatz-1014412587/)    | Nov 06, 08:36      |
|       480    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-1191593378/)                                                                                                | Nov 05, 18:28      |
