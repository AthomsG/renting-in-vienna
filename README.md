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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       748    |            40 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/kleine-2-zimmer-dachwohnung-mit-terrasse%21-863096262/)                                                                        | Sep 05, 10:27      |
|       708.96 |            51 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zimmer-wohnung-1548483361/)                                                                                                  | Sep 05, 06:48      |
|       790    |            54 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/zwei-zimmer-wohnung-1696686991/)                                                                                            | Sep 04, 18:08      |
|       613    |            44 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/singlewohnung-hauptmiete-unbefristet-mit-k%C3%BCche-1407884512/)                                                                 | Sep 04, 17:31      |
|       790    |            41 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/berggasse--servitenviertel-%28privatvermietung%29-1365438111/)                                                                | Sep 04, 16:51      |
|       720    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-in-ruhelage-zu-vermieten-1625265733/)                                                                                   | Sep 04, 15:02      |
|       790    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/tichy-und-u1-ums-eck-963869023/)                                                                                               | Sep 04, 13:57      |
|       580    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeindewohnung-1975359121/)                                                                                   | Sep 04, 13:35      |
|       526    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-wiener-wohnen-ticket-vom-30.06.2025-oder-%C3%A4lter-notwendig-1836958922/)                                     | Sep 04, 12:51      |
|       622.85 |            47 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-2-zimmer-altbauwohnung---47-m%C2%B2---unbefristet---1120-wien-%28erlgasse%29-1100792184/)                             | Sep 04, 12:21      |
|       650    |            71 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/sch%C3%B6ne-2-zimmer-wohnung-mit-balkon-in-1160-wien---voll-m%C3%B6bliert-nur-f%C3%BCr-bestimmte-sozialbaumieter.-1590924052/) | Sep 04, 10:16      |
