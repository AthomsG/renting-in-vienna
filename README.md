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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       773.71 |            56 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/sonnige-2-zimmerwohnung-am-hernalser-g%C3%BCrtel-ecke-geblergasse-1597120221/)                                                                                                                   | Jan 27, 12:54      |
|       534.92 |            55 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeinde-wohnung-2143685011/)                                                                                                                                                               | Jan 27, 10:43      |
|       745    |            43 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/anfragestop%21-nachmieter%2Ain-gesucht%21-2-zimmer-wohnung-im-8.-bezirk-2128448750/)                                                                                                          | Jan 27, 10:17      |
|       658.41 |            61 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-mit-2-zimmer-wohnticketsnummer-:-42775/2024.-die-wohnung-ist-reserviert%21-1312659054/)                                                                                       | Jan 26, 21:23      |
|       660.01 |            66 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/direktvergabe---2-zimmer-gemeindewohnung-1090-%7C-u4-friedensbr%C3%BCcke-%7C-nur-mit-wiener-wohnticket-1188640014/)                                                                           | Jan 26, 18:26      |
|       500    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-gemeinde-wohnung-in-1120-wr.-wohn-ticket-sp%C3%A4testens-31.12.2025-1392923826/)                                                                                                       | Jan 26, 17:09      |
|       662    |            60 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/kalvarienberggasse/-n%C3%A4he-elterleinplatz-%2B%2B-ger%C3%A4umige-&-helle-60m%C2%B2-altbauwohnung-mit-flair-%2B%2B-2-zimmer-%2B%2B-k%C3%BCche-mit-fenster%2B%2B-gesamtmiete-662----1008182953/) | Jan 26, 16:45      |
