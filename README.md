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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       720    |            44 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/zwei-zimmer-wohnung-2.-stock-top-lage-m%C3%B6bliert-n%C3%A4he-mariahilferstrasse-878516297/)                    | May 29, 22:05      |
|       768.41 |            46 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/smarte-stadtwohnung-in-der-josefstadt-1398259945/)                                                          | May 29, 19:18      |
|       616    |            60 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-gemeindewohnung-wien-1030-1329006302/)                                                   | May 29, 19:03      |
|       799.99 |            47 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-unbefristeter-47m%C2%B2-erstbezug-mit-2-zimmern-und-einbauk%C3%BCche---1140-wien-2098547683/)  | May 29, 14:09      |
|       486.08 |            46 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeindewohnung-2.-zi.-wiener-wohnticket-31.01.2026-1319241339/)                                 | May 29, 13:51      |
|       690    |            47 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/zentrale-2-zimmer-wohnung-schlafzimmer-zum-innenhof-1346292859/)                                            | May 29, 12:33      |
|       746.82 |            44 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/toplage%21-sehr-ruhige-2-zimmer-wohnung-%2A-prinz-eugen-strasse---vis-%C3%A0-vis-schloss-belvedere-1039612517/) | May 29, 10:07      |
|       728    |            48 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/helle-2-zimmer-wohnung---ideal-f%C3%BCr-student-oder-paare-1974964060/)                                   | May 29, 09:55      |
