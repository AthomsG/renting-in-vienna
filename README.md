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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       749.78 |            49 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/wundersch%C3%B6ne-kleine-25-zimmer-wohnung---turmburggasse---in-2-minuten-zur-u-bahn-pilgramgasse--bitte-nur-schriftlich-anfragen-termin-kommt-automatisch-931612325/) | May 04, 16:38      |
|       724    |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfreies-raumwunder-im-16.-bezirk---perfekt-f%C3%BCr-paare-oder-singles-1071014761/)                                                                           | May 04, 15:56      |
|       720    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtlich-zwei-zimmer-wohnung-mit-viel-sonne-und-gro%C3%9Fer-k%C3%BCche-1748055564/)                                                                              | May 04, 15:14      |
|       760    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/keine-neuen-anfragen-nachmieter-f%C3%BCr-2-zimmerwohnung-im-10.-bezirk-gesucht-1816162836/)                                                                            | May 04, 14:45      |
|       750    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-vermieten-1573125782/)                                                                                                                                         | May 04, 14:27      |
|       787.02 |            56 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-altbau-wohnung-nahe-u3-station-simmering-%23-fair-wohnen-1018784229/)                                                                                         | May 04, 11:06      |
|       799    |            65 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/stilaltbau/unbefristet/u3-n%C3%A4he:-65-m2-2-getrennte-zimmer-einbauk%C3%BCche-wannenbad-gesamtmiete-799---899135325/)                                                 | May 04, 10:56      |
|       625    |            48 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/wohnen-in-der-fussgeherzone-853016697/)                                                                                                                               | May 04, 08:53      |
|       610    |            47 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/mietwohnung-891608599/)                                                                                                                                | May 03, 17:29      |
