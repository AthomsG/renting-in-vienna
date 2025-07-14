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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       669.03 |            55 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/perfekt-gelegene-2-zimmer-wohnung-//-unbefristet-oder-befristet-zu-vermieten-1807268970/)                                           | Jul 14, 21:34      |
|       706.21 |            49 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/dachterrassenhit-mit-sch%C3%B6nem-ausblick-1315855809/)                                                                           | Jul 14, 18:53      |
|       637    |            50 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/neu-sanierte-unbefristete-hauptmietwohnung-in-1070-wien-1120490082/)                                                                 | Jul 14, 16:27      |
|       540    |            53 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindebauwohnung-direktvergabe-1953876125/)                                                                                     | Jul 14, 15:15      |
|       699    |            60 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/u3-zippererstre%C3%9Fe/-wg-eignung%21-unbefristete-60-m2-altbaumiete-2-getrennte-zimmer-fliesenbad-gesamtmiete-699---2119024194/) | Jul 14, 14:00      |
|       629.98 |            43 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristete-hauptmietwohnung-in-1120-wien-1252368445/)                                                                            | Jul 14, 13:24      |
|       780.96 |            60 |          3 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-u3-enkplatz---ruhige-altbauwohnung---2-zimmer-%2B-wohnk%C3%BCche---unbefristet-2022015826/)                             | Jul 14, 12:35      |
|       799    |            42 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sch%C3%B6ne-2-zimmer-garten-wohnung-in-traumhafter-lage---nur-5min-zur-u3-entfernt-%28ab-01.10.2025%29-2012875495/)                 | Jul 14, 11:48      |
|       543.4  |            42 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierte-2-zimmerwohnung-n%C3%A4he-amalienbad-1429360799/)                                                                        | Jul 14, 09:12      |
|       670    |            65 |          3 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-vormerkschein-vor-05/2024-912697125/)                                                           | Jul 13, 23:08      |
