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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       729    |            31 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-mai:-top-aufgeteilte-mietwohnung-%7Cidyllische-lage-%7Cneubau-n%C3%A4he-u1-%7C-provisionsfrei%7C-2-zimmer-791107819/)   | Mar 27, 11:35      |
|       561.24 |            39 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/helle-und-g%C3%BCnstige-2-zimmer-wohnung-2038477604/)                                                                   | Mar 27, 11:00      |
|       561.72 |            47 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/16.n%C3%A4he-rankgasse-nur-f%C3%BCr-studenten%21%21-voll-m%C3%B6blierte-provisionsfreie-2-zimmer-altbaumiete-957873323/)   | Mar 27, 08:05      |
|       798.99 |            61 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/provisionsfrei:-sonniger-61m%C2%B2-altbau-mit-einbauk%C3%BCche-und-lift---1030-wien-1351813966/)                     | Mar 26, 18:36      |
|       742.58 |            63 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-in-1160-wien-2021392936/)                                                                 | Mar 26, 16:24      |
|       673.14 |            53 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/hell-renoviert-2-zi-mietwohnung-buchengasse-1602563780/)                                                                   | Mar 26, 15:27      |
|       420    |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindewohnung-direktvergabe-ruhelage-am-wienerberg-1351987124/)                                                           | Mar 26, 14:42      |
|       790    |            40 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ideale-helle-kleinwohnung-/-3-gehminuten-johnstrasse/-u3-1216812860/)                                      | Mar 26, 14:27      |
|       790    |            43 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%2Aanfragestopp%2A-2-zimmer-wohnung-in-top-lage---nachmieter-gesucht-%28thaliastra%C3%9Fe-68-/-wendgasse-2%29-1850943409/) | Mar 26, 12:19      |
