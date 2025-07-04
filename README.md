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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       660.98 |            50 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wien-ottakring:-helle-ruhige-2-zimmer-mietwohnung-unbefristet-provisionsfrei-per-april-2135476983/)                                                                                         | Jul 04, 14:26      |
|       579    |            47 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristete-helle-2-zimmer-wohnung-1857599171/)                                                                                                                                            | Jul 04, 14:07      |
|       620    |            60 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gemeindewohnung-zur-direktvergabe-%28wiener-wohnen%29---alszeile-57-63-1170-wien-1524349112/)                                                                                                 | Jul 04, 08:41      |
|       544.69 |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-gemeindewohnung-direktvergabe-vormerkschein28.02.2025-1358765607/)                                                                                                      | Jul 04, 06:44      |
|       520.37 |            52 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-per-direktvergabe---abl%C3%B6se---moderne-ausstattung-inkl.-neuer-k%C3%BCche-785367603/)                                                                              | Jul 03, 20:16      |
|       778.71 |            42 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmerwohnung-mit-gartenblick-1347260771/)                                                                                                                                             | Jul 03, 19:46      |
|       798    |            60 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/provisionsfrei-f%C3%BCr-den-mieter%21-oberm%C3%BCllnerstra%C3%9Fe-n%C3%A4chst-u1/u2-zentrumn%C3%A4he-hofruhelage-60m%C2%B2-altbaumiete-wg-eignung%21-studenten-bevorzugt%21-1814397752/) | Jul 03, 19:10      |
|       784.31 |            51 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-51m%C2%B2-altbau-%2B-8m%C2%B2-terrasse-mit-einbauk%C3%BCche-und-lift---1100-wien%21-2016217767/)                                                              | Jul 03, 17:35      |
|       786.03 |            69 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/helle-2-zimmer-dachgescho%C3%9Fwohnung-mit-loggia---1120-wien-erlgasse-21-23-1622952647/)                                                                                                    | Jul 03, 14:22      |
