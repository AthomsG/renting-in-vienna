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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       560    |            42 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-helle-2-zimmer-wohnung-mit-blick-%C3%BCber-wien-1831503233/)                                         | Jul 05, 13:49      |
|       496    |            46 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeinde-wien-wohnung-per-direktvergabe-3.-bezirk-wien-1304839405/)                                           | Jul 05, 11:30      |
|       580    |            56 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-gemeindewohnung-direktvergabe-1352909406/)                                                                 | Jul 05, 11:15      |
|       560    |            56 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gepflegte-gemeindewohnung-im-11.-bezirk---n%C3%A4he-zentralfriedhof-%28tor-3-4%29-vm-31.05.25-%21%21-2126843330/)   | Jul 05, 09:35      |
|       782.19 |            78 |          3 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/seniorenwohnung%21-unbefristet.-erstbezug-nach-renovierung.-3.-liftstock.-bitte-schriftlich-anfragen%21-1646718529/) | Jul 05, 09:26      |
|       700    |            55 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/wohnung-gegen-abl%C3%B6se-an-nachmieterin/-nachmieter-2102391333/)                                                 | Jul 04, 19:52      |
|       773.3  |            58 |          3 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sanierte-helle-25-zimmer-wohnung-provisionsfrei%21-1239779441/)                                                     | Jul 04, 16:38      |
|       788.67 |            37 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/moderne-2-zimmer-wohnung-im-12.bezirk%21-1496366409/)                                                                | Jul 04, 14:57      |
|       660.98 |            50 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/wien-ottakring:-helle-ruhige-2-zimmer-mietwohnung-unbefristet-provisionsfrei-per-sofort-2135476983/)                | Jul 04, 14:26      |
|       579    |            47 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/unbefristete-helle-2-zimmer-wohnung-1857599171/)                                                                    | Jul 04, 14:07      |
