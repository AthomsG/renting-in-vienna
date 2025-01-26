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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       650    |            40 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/privat-vermietung-%28nichtraucher%29-740651970/)                                                                                            | Jan 26, 21:50      |
|       532.31 |            42 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/rarit%C3%A4t-unbefristete-sch%C3%B6n-renovierte-2-zimmer-wohnung-1119424970/)                                                                  | Jan 26, 21:40      |
|       790.65 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/n%C3%A4he-huma-eleven---wohnung-perfekt-f%C3%BCr-p%C3%A4rchen-geeignet-mit-balkon-1309031000/)                                               | Jan 26, 21:37      |
|       799.96 |            47 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1810981329/)                                              | Jan 26, 21:35      |
|       710    |            70 |          3 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/gemeinde-wohnung-in-21-.-bezirk-weitergeben-2044563217/)                                                                                   | Jan 26, 21:06      |
|       460    |            46 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeindewohnung-direktvergabe-vm-dez-2024-1254009226/)                                                                                         | Jan 26, 19:47      |
|       774    |            54 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/2-zimmer-single-wohnung-servitenviertel-altbau-1276025198/)                                                                                 | Jan 26, 19:18      |
|       495    |            50 |          2 | 13. Hietzing     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1130-hietzing/mietwohnung-gemeinde-wohnticket-31.12.2024-1368188222/)                                                                                       | Jan 26, 19:04      |
|       799.42 |            43 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/moderne-2-zimmer-wohnung-in-floridsdorf:-nachhaltigkeit-trifft-wohnkomfort---jetzt-anfragen-1794922627/)                                   | Jan 26, 18:55      |
|       699    |            63 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-/-direktvergabe-nur-mit-vormerkschein%21-vsnr:-30.11.2024-1672281334/)                                                       | Jan 26, 18:35      |
|       478    |            49 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/gemeindewohnung-zur-direktvergabe-1220583450/)                                                                                              | Jan 26, 17:26      |
|       525    |            50 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/f%C3%BCr-sportliche:-nette-1-zimmer-%2B-kabinett-wohnung-in-%2A1050-wien%2A-in-sehr-guter-lage-%284.-stock-ohne-aufzug%29-1909653919/)      | Jan 26, 17:21      |
|       490    |            44 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sch%C3%B6ne-gemeindewohnung-n%C3%A4he-elterleinplatz-1119455457/)                                                                              | Jan 26, 16:55      |
|       440.72 |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-1020-wien-vms:-31.10.2024-928811082/)                                                                                     | Jan 26, 15:57      |
|       523.08 |            51 |          2 | 23. Liesing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1230-liesing/gemeindewohnung-1230-/-u-bahn-n%C3%A4he-und-gr%C3%BCnlage-%28nur-mit-vormerkschein-f%C3%BCr-zwei-wohnr%C3%A4ume-bis-30.11.2024%29-1687561871/) | Jan 26, 12:42      |
|       780    |            41 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-sch%C3%B6ne-2-zimmer-wohnung-m%C3%B6bliert-mit-gemeinschaftsterrasse-1177823895/)                                           | Jan 26, 10:53      |
|       799.95 |            43 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                                              | Jan 26, 10:24      |
|       650    |            60 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/arbeiterwohnung/-mitbewohnerin-1791051217/)                                                                                                | Jan 25, 21:30      |
