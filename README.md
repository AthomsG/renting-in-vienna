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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       785    |            75 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-gemeinde-wohnung-75m2-im-11.-bezirk-%28-nur-mit-wohnticket-vor-dem-31.03.2025%29-908634689/)                                                                   | Oct 05, 19:48      |
|       750    |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neubauwohnung-zur-miete-in-wien-1100-1555926003/)                                                                                                                               | Oct 05, 18:23      |
|       680    |            60 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/n%C3%A4he-botanischer-garten---mohsgasse-%7C-zentral-gelegene-60m%C2%B2-altbauwohnung-mit-flair-%7C-2-zimmer-%7C-k%C3%BCche-%7C-gesamtmiete-%E2%82%AC-680----1483420042/) | Oct 05, 18:21      |
|       650    |            61 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-2086863769/)                                                                                                                                                    | Oct 05, 15:45      |
|       737.01 |            68 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-wohnung-vermieten-2082541844/)                                                                                                                                 | Oct 05, 14:37      |
|       510    |            50 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen/-2zimmer-n%C3%A4he-oberlaa-892056712/)                                                                                                              | Oct 05, 14:18      |
|       530    |            51 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-wiener-wohnen-ticket-vom-30.06.2025-oder-%C3%A4lter-notwendig-1346020686/)                                                                                      | Oct 05, 13:12      |
|       580    |            54 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-gemeindewohnung-54m%C2%B2-in-toplage-1020-zu-vergeben-1865720803/)                                                                                          | Oct 05, 11:58      |
|       680    |            58 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-58m2-/-2-zimmer-privat-wohnung-n%C3%A4he-u1-reumannplatz-ab-sofort-provisions-und-abl%C3%B6sefrei%21%21-1769897946/)                                           | Oct 05, 11:02      |
|       790    |            85 |       1234 | 01. Innere Stadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1010-innere-stadt/wohnung-wg-zimmer-2137975694/)                                                                                                                                               | Oct 05, 09:54      |
