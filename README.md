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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       768.63 |            40 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/cityapartment:-garagenplatz-im-haus-&-u6-spittelau-ums-eck-1967661994/)                                                                                                     | Oct 13, 13:16      |
|       610.39 |            61 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung-im-10.-bezirk-1025153825/)                                                                                                                      | Oct 13, 13:06      |
|       488    |            53 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gem%C3%BCtliche-53m%C2%B2-singlemiete-im-trendviertel-n%C3%A4he-karmelitermarkt-%7C-2-zimmer-%7C-k%C3%BCche-bad-kombination-gesamtmiete-%E2%82%AC-488----%7C-1404194005/) | Oct 13, 12:43      |
|       565    |            53 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ger%C3%A4umige-2-zimmer-wohnung-%28wohnticket:-30.09.25%29-1452216840/)                                                                                                        | Oct 13, 12:03      |
|       550.54 |            40 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/kompakte-2-zimmer-wohnung%21-1053667849/)                                                                                                                                    | Oct 13, 11:51      |
|       499    |            39 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/1140-wien---sch%C3%B6ne-teilm%C3%B6blierte-2-zimmer-wohnung-befristung-5-jahre-1444026260/)                                                                                    | Oct 13, 11:08      |
|       427.65 |            41 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-im-erdgeschoss---direktvergabe-%28nur-mit-g%C3%BCltigem-wiener-wohn-ticket-vor-dem-30.09.2025%29-1991592446/)                                                | Oct 12, 19:59      |
|       785    |            75 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-gemeinde-wohnung-75m2-im-11.-bezirk-%28-nur-mit-wohnticket-vor-dem-31.03.2025%29-908634689/)                                                                | Oct 12, 19:48      |
|       650    |            61 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-2086863769/)                                                                                                                                                 | Oct 12, 15:45      |
|       737.01 |            68 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-wohnung-vermieten-2082541844/)                                                                                                                              | Oct 12, 14:37      |
