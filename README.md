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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       650    |            40 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%28reserviert%29-moderne-2-zimmer-wohnung-in-bestlage-1871791473/)                                                                                               | Oct 16, 15:10      |
|       429    |            46 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-gemeindewohnung-%28direktvergabe%29---toplage-im-2.-bezirk-nahe-donauinsel-%7C-perfekt-f%C3%BCr-studierende-oder-junge-berufst%C3%A4tige-1627457408/) | Oct 16, 10:02      |
|       480    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wiener-wohnen---direktvergabe/-42qm/-2-zimmer-986168180/)                                                                                                          | Oct 16, 09:41      |
|       770.33 |            60 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug%21-sanierte-mietwohnung-n%C3%A4he-quellenplatz%21-1340355347/)                                                                                          | Oct 16, 08:09      |
|       505    |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-1071222420/)                                                                                                                                   | Oct 15, 22:36      |
|       460    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-direktvergabe-1614062493/)                                                                                                               | Oct 15, 20:39      |
|       799    |            58 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28reserviert%29-1160-stillfriedplatz-1/10---unbefristet-zu-vermieten-2063355608/)                                                                                | Oct 15, 19:53      |
|       417    |            39 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/nur-mit-%21%21%21%21%21%21-vormerkschein-%21%21%21%21%21%21-bis-30.06.25.-gemeinde--wohnung-1351170544/)                                                    | Oct 15, 18:05      |
