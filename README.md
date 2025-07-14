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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       553.08 |            39 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanirte-1-zimmer-wohnung-n%C3%A4he-reumannplatz%21-1480403548/)                                                                   | Jul 14, 14:01      |
|       699    |            60 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/u3-zippererstre%C3%9Fe/-wg-eignung%21-unbefristete-60-m2-altbaumiete-2-getrennte-zimmer-fliesenbad-gesamtmiete-699---2119024194/) | Jul 14, 14:00      |
|       629.98 |            43 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristete-hauptmietwohnung-in-1120-wien-1252368445/)                                                                            | Jul 14, 13:24      |
|       780.96 |            60 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-u3-enkplatz---ruhige-altbauwohnung---2-zimmer-%2B-wohnk%C3%BCche---unbefristet-2022015826/)                             | Jul 14, 12:35      |
|       799    |            42 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/sch%C3%B6ne-2-zimmer-garten-wohnung-in-traumhafter-lage---nur-5min-zur-u3-entfernt-%28ab-01.10.2025%29-2012875495/)                 | Jul 14, 11:48      |
|       703.31 |            61 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/61m%C2%B2-2-1/2-zimmer-wohnung-2126242374/)                                                                                       | Jul 14, 09:48      |
|       543.4  |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierte-2-zimmerwohnung-n%C3%A4he-amalienbad-1429360799/)                                                                        | Jul 14, 09:12      |
|       670    |            65 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-vormerkschein-vor-05/2024-912697125/)                                                           | Jul 13, 23:08      |
|       528    |            49 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-gemeindewohnung-per-direktvergabe---vormerkschein-bis-31.05.2025-1634562358/)                                         | Jul 13, 22:53      |
|       795.76 |            54 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-wohnung-in-1110-wien-mit-vollm%C3%B6blierung-&-sofortbezug---abl%C3%B6se-nur-4.000-%E2%82%AC-1730221899/)        | Jul 13, 20:47      |
|       503    |            47 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-gemeidewohnung-1422157022/)                                                                                                | Jul 13, 20:27      |
|       650    |            71 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-2-zimmer-wohnung-mit-balkon-in-1160-wien---voll-m%C3%B6bliert-f%C3%BCr-sozialbaumieter-1062416596/)                   | Jul 13, 16:55      |
|       517    |            48 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/vormerkschein-30.06.2025---gemeindewohnung-top-lage---03.-bezirk-944922347/)                                                | Jul 13, 13:13      |
