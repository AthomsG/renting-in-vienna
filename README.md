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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                      | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       665.07 |            48 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%2A%2A-garconniere-%2A%2A-f%C3%BCr-singles-im-fasanviertel-1273563877/)                                        | Jul 01, 10:16      |
|       449.36 |            30 |          3 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/lager/atelier-zur-miete-in-1050-wien---ehemalige-wohnung-nahe-pilgramgasse-1798271816/)                             | Jul 01, 09:57      |
|       713.04 |            51 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mi%28e%29tten-in-oberlaa:-gro%C3%9Fartige-2-zimmer-wohnung-mit-balkon-in-1100-wien-unbefristet-zu-mieten-809837974/) | Jul 01, 08:49      |
|       431    |            47 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/bitte-lesen:-gemeindewohnung-in-1170-wien-ab-1.11.25-verf%C3%BCgbar-2125951272/)                                       | Jul 01, 07:39      |
|       458.79 |            47 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindebauwohnung-per-direktvergabe-1490919102/)                                                                   | Jun 30, 23:51      |
|       789    |            60 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/ger%C3%A4umige-2-zimmerwohnung-in-gepflegtem-altbau%21-n%C3%A4he_schmelz%21-n%C3%A4he-u3-u6%21-2090857435/)          | Jun 30, 15:57      |
|       765.87 |            47 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/%28reserviert%29-nachmieter-gesucht-f%C3%BCr-wohnung-in-3er-bezirk---47m%C2%B2-948403138/)                     | Jun 30, 13:37      |
