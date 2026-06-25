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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       777.62 |            46 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-dg-wohnung-im-10.bezirk-n%C3%A4he-r%C3%A4umannplatz%21-2054018928/)                        | Jun 25, 12:54      |
|       599    |            40 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/provisionsfrei%21-ruhige-wohnung-in-zentraler-lage-1066421123/)                                                    | Jun 25, 11:51      |
|       599    |            44 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei%21-ruhige-wohnung-beim-neuen-landgut-877619219/)                                                 | Jun 25, 11:51      |
|       799    |            60 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei%21-ruhige-wohnung-in-bester-lage-1394892739/)                                                     | Jun 25, 11:51      |
|       780    |            42 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/liechtensteinstrasse-unbefristete-42-m2-altbau-2-zimmer-k%C3%BCche-parketten-duschbad-hofruhelage-1685516651/) | Jun 25, 10:04      |
|       736.3  |            54 |          2 | 16. Ottakring  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/supermiete-sch%C3%B6ne-2-zimmerwohnung-alle-nebenr%C3%A4ume-gute-%C3%B6ffentlicher-anbindung%21-1752575258/)    | Jun 24, 21:40      |
|       643    |            56 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2__zimmer___ruhig__unbefristet-1882988663/)                                                                     | Jun 24, 17:25      |
|       768.7  |            80 |          3 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%28reserviert%29-gemeinde-wohnung-1050-wien-1795344110/)                                                       | Jun 24, 15:15      |
