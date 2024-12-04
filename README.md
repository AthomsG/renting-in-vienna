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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       790    |            54 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/2-zimmerwohnung-im-altbau-n%C3%A4he-mariahilferstr.-1954436277/)                                                  | Dec 04, 10:22      |
|       503    |            49 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/6991-912140723/)                                                                                               | Dec 04, 10:09      |
|       720    |            44 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/mietwohnung-genie%C3%9Fen-kaufoption-nutzen:-wohnen-in-stammersdorfer-naturkulisse-761411356/)                  | Dec 04, 10:07      |
|       770    |            49 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/jetzt-mieten-sp%C3%A4ter-kaufen:-wohnen-in-stammersdorfer-naturidylle-761411382/)                               | Dec 04, 10:07      |
|       488    |            46 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/renovierte-gemeindewohnung-mit-2-zimmer-in-ruhiger-lage---ab-sofort-verf%C3%BCgbar%21-1118174412/)               | Dec 04, 10:01      |
|       798.99 |            40 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/traumwohnungen-in-top-lage-zu-vermieten%21-1055837955/)                                                         | Dec 04, 09:48      |
|       782    |            43 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/tolle-2-zimmer-wohnung-in-absoluter-ruhelage-mit-sch%C3%B6nem-balkon-1756981113/)                                   | Dec 04, 09:47      |
|       691.33 |            44 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/%28reserviert%29-neubauwohnung-zu-vermieten%21-1644760517/)                                                     | Dec 03, 23:11      |
|       630.68 |            61 |          3 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/3-zimmer-gemeindewohnung-mit-terasse-%7C-direktvergabe-mit-vormerkschein-778168897/)                            | Dec 03, 22:53      |
|       798    |            37 |          2 | 20. Brigittenau  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/sehr-sch%C3%B6ne-2-zimmerwohnung---n%C3%A4he-donauinsel-&-handelskai-1506947017/)                               | Dec 03, 21:36      |
|       617.28 |            59 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/direktvergabe-3-zimmer-gemeindewohnung-1656390258/)                                                               | Dec 03, 20:38      |
|       730    |            69 |          3 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/%2A%2A3-zimmer-gemeindewohnung-mit-blick-zum-naschmarkt%2A%2A-1916089637/)                                        | Dec 03, 20:32      |
|       568.55 |            56 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/2-zimmer-gef%C3%B6rderte-wohnung-mit-abstellraum-und-balkon-ab-31.01.25-zu-vergeben%21-869184078/)              | Dec 03, 18:58      |
|       787.92 |            41 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/modernes-wohnen-mit-balkon-in-1220-wien---4119m%C2%B2-zum-mietpreis-von-78792-eur%21-1580236359/)                | Dec 03, 18:35      |
|       795    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/baujahr-2020-van-der-n%C3%BCll-gasse---hofseitige-2-zimmer-mit-957m2-gro%C3%9Fem-balkon-1690441964/)              | Dec 03, 18:26      |
|       790    |            50 |          2 | 19. Döbling      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/%28reserviert%29-praktische-2-zimmer-wohnung-%2B-separate-k%C3%BCche---ab-1.1.2025-verf%C3%BCgbar-1506341196/) | Dec 03, 17:52      |
|       786.09 |            43 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/freundliche-helle-altbauwohnung-wg-geeignet---2-getrennte-schlafr%C3%A4ume-1298843722/)                           | Dec 03, 17:16      |
|       795    |            48 |          2 | 22. Donaustadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/%22breitenlee---moderne-gartenwohnung-2-zimmer%22-1932972531/)                                                   | Dec 03, 17:08      |
|       698    |            39 |          2 | 21. Floridsdorf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/wien---1210---ruhige-single-dachgescho%C3%9Fwohnung-mit-fernblick---neubau---ab-15.12.2024-2095133943/)         | Dec 03, 17:03      |
|       502.69 |            46 |          2 | 19. Döbling      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/gut-aufgeteilte-zwei-zimmer-gemeindewohnung-in-grinzing-2039666508/)                                           | Dec 03, 15:34      |
