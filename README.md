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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       752.4  |            41 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neuwertige-2-zimmer-wohnung-mit-balkon-in-1120-wien-siebertgasse-26---ihr-neues-zuhause%21-1145142857/)                       | Sep 19, 12:16      |
|       630    |            79 |          3 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-vormerkscheindatum-vor-31.8.2024---3-zimmer-gemeindewohnung-direktvergabe-1724054859/)                       | Sep 19, 07:08      |
|       511.25 |            64 |          2 | 06. Mariahilf    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/charmante-2-zimmer-wohnung-im-dachgeschoss-1178361556/)                                                                      | Sep 19, 06:47      |
|       648.52 |            68 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/penzing:-elegante-2-zimmerwohnung-mit-altbaucharakter-853003101/)                                                              | Sep 18, 19:35      |
|       722    |            32 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-m%C3%B6blierte-2-zimmer-wohnung-mit-balkon-in-der-leopoldstadt-/-2nd-district-%7C-maxi-bude-1893604330/) | Sep 18, 16:28      |
|       780    |            52 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/mietwohnung-1098878787/)                                                                                                     | Sep 18, 13:06      |
|       750    |            51 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/helle-und-gem%C3%BCtliche-3-zimmer-wohnung-in-zentraler-lage-1875691856/)                                                    | Sep 18, 11:31      |
