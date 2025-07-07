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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       775.93 |            55 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gepflegte-altbauwohnung-n%C3%A4he-sch%C3%B6nbrunn%21-1189034843/)                                                                               | Jul 07, 11:23      |
|       693    |            53 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/mietwohnung-53m2-1701162054/)                                                                                                                  | Jul 07, 10:56      |
|       795    |            45 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/bitte-termine-online-buchen-%28link-im-text%29---anrufe-und-mails-werden-nicht-beantwortet-1701961857/)                                       | Jul 07, 09:28      |
|       609.2  |            55 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/helle-gemeinde-wohnung-55m2-im-5.-bezirk-1052783041/)                                                                                         | Jul 07, 07:38      |
|       590    |            58 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/m%C3%B6bilierte-3-zimmer-gemeinde-wohnung-%C3%BCber-direktvergabe-in-1100-wien---n%C3%A4he-altes-landgut-1689161114/)                          | Jul 07, 07:16      |
|       670    |            65 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-vormerkschein-vor-05/2024-912697125/)                                                                        | Jul 06, 23:08      |
|       525    |            60 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/m%C3%B6bilierte-3-zimmer-gemeindewohnung-%C3%BCber-direktvergabe-in-1100-wien---n%C3%A4he-raxstra%C3%9Fe-%28ruhige-seitengasse%29-2108985091/) | Jul 06, 15:25      |
|       770    |            61 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Ap%C3%A4rchentraum%2Asonniger-neubau-mit-bester-infrastruktur%21-1518950514/)                                                                | Jul 06, 12:05      |
|       778    |            66 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/renoviert-preiswert-und-zweier-wg-eignung-1278054567/)                                                                                         | Jul 06, 11:53      |
