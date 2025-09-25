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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       677.34 |            57 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wundersch%C3%B6ne-2-zimmer-wohnung-mit-loggia-und-weitblick-im-helio-tower-nahe-u3-%22gasometer%22---unbefristet-mit-finanzierungsbeitrag-zu-vermieten-1912506741/) | Sep 25, 12:13      |
|       600.28 |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/besichtigung-am-30.09.2025-16:30-18:30---425m%C2%B2-wohnung-im-2.-bezirk-1643344524/)                                                                                  | Sep 25, 11:53      |
|       760    |            43 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%22sonnige-3-zimmer-mietwohnung-in-penzing%22-1386959134/)                                                                                                                  | Sep 25, 09:38      |
|       799    |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-u3-simmering---ruhelage---stellplatz-optional---zwischen-lorystra%C3%9Fe-und-simmeringer-hauptstra%C3%9Fe-1966859987/)                                          | Sep 25, 07:21      |
|       799    |            46 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gem%C3%BCtliche-single-wohnung-mit-vintage-flair-f%C3%BCr-individualisten-1090194387/)                                                                                   | Sep 25, 07:15      |
|       783.33 |            50 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/b%C3%BCror%C3%A4umlichkeiten-%2A%2A-n%C3%A4he-u3/u4-%2A%2A-zur-befristeten-vermietung-1141195550/)                                                                         | Sep 25, 01:09      |
|       685    |            59 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/%28reserviert%29-direktvergabe:-toplage-im-9.-bezirk-%28servitenviertel%29-nahe-donaukanal-%7C-2-zimmer-gemeindewohnung-59m%C2%B2-1230815188/)                           | Sep 24, 21:29      |
|       552    |            49 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nachmieter-gemeindewohnung-1761149382/)                                                                                                                                     | Sep 24, 20:37      |
|       781.19 |            42 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/link-zur-terminbuchung-steht-im-text-1311788584/)                                                                                                                           | Sep 24, 15:46      |
|       789.69 |            60 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/neusanierte-huptmietwohnung/-stumpergasse/-im-herzen-von-mariahilf-1138966254/)                                                                                           | Sep 24, 14:08      |
|       720    |            43 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/provisionsfrei-2-zimmerwohnung-u-2-bald-vor-der-haust%C3%BCr-817333044/)                                                                                                 | Sep 24, 10:58      |
