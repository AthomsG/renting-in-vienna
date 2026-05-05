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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       517.51 |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mietwohnung-in-favoriten%21-2059307551/)                                                                             | May 05, 15:07      |
|       787.14 |           nan |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nur-schriftliche-anfragen-bitte.-helle-2--zimmer-wohnung-in-der-guldengasse-1597390915/)                               | May 05, 14:54      |
|       740    |            32 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/erstbezug-%7C-exklusive-neubauwohnungen-im-altbaustil-%7C-beispiel-32-m%C2%B2-apartment-1203639120/)                | May 05, 12:58      |
|       799.99 |            47 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-helle-2-zimmer-wohnung-%7C-barrierefreier-neubau-%7C-bahnhof-penzing-%7C-garagenstellplatz-optional-787313077/) | May 05, 11:23      |
|       573.99 |            61 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/vielseitig-nutzbarer-hobbyraum-/-atelier-/-lagerfl%C3%A4che-im-16.-bezirk---6146-m%C2%B2-1947037006/)                | May 05, 10:41      |
|       590    |            56 |          3 | 01. Innere Stadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1010-innere-stadt/innenstadt~gemeindewohnung-nahe-k%C3%A4rntnerstra%C3%9Fe-860795385/)                                              | May 04, 20:44      |
|       776.66 |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%28reserviert%29-mietwohnung-1561912168/)                                                            | May 04, 20:43      |
|       724    |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfreies-raumwunder-im-16.-bezirk---perfekt-f%C3%BCr-paare-oder-singles-1071014761/)                         | May 04, 15:56      |
|       720    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtlich-zwei-zimmer-wohnung-mit-viel-sonne-und-gro%C3%9Fer-k%C3%BCche-1748055564/)                            | May 04, 15:14      |
|       750    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-vermieten-1573125782/)                                                                                       | May 04, 14:27      |
