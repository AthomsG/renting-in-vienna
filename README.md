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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       783.33 |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/b%C3%BCror%C3%A4umlichkeiten-%2A%2A-n%C3%A4he-u3/u4-%2A%2A-zur-befristeten-vermietung-1141195550/)                                               | Sep 25, 01:09      |
|       685    |            59 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%28reserviert%29-direktvergabe:-toplage-im-9.-bezirk-%28servitenviertel%29-nahe-donaukanal-%7C-2-zimmer-gemeindewohnung-59m%C2%B2-1230815188/) | Sep 24, 21:29      |
|       552    |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nachmieter-gemeindewohnung-1761149382/)                                                                                                           | Sep 24, 20:37      |
|       792.14 |            51 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-ruhige-2-zimmerwohnung-in-der-oelweingasse-1556402511/)                                                                   | Sep 24, 20:32      |
|       781.19 |            42 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/link-zur-terminbuchung-steht-im-text-1311788584/)                                                                                                 | Sep 24, 15:46      |
|       789.69 |            60 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/neusanierte-huptmietwohnung/-stumpergasse/-im-herzen-von-mariahilf-1138966254/)                                                                 | Sep 24, 14:08      |
|       720    |            43 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-2-zimmerwohnung-u-2-bald-vor-der-haust%C3%BCr-817333044/)                                                                       | Sep 24, 10:58      |
|       670    |            65 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-vormerkschein-31.08.2024-979629484/)                                                                        | Sep 24, 07:29      |
