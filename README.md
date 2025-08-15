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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       690    |            74 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeinde-wohnung-1575544480/)                                                                           | Aug 15, 20:00      |
|       685    |            40 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ruhige-helle-generalsanierte-wohnung-privat-1447012730/)                                                    | Aug 15, 19:11      |
|       609    |            41 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neu-saniert/erstbezug%21-zentrale-wohnung-in-favoriten-1464551555/)                                        | Aug 15, 18:17      |
|       791.79 |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/neu%21-ideale-2-zimmerwohnung-mit-perfekter-verkehrsanbindung%21-1805768083/)                              | Aug 15, 16:54      |
|       726    |            51 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-mietwohnung-859830543/)                                                                              | Aug 15, 15:36      |
|       750    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/terrassentraum:-sonnige-2-zimmer-terrassenwohnung-nahe-hauptbahnhof-&-arsenal---provisonsfrei-1305746124/) | Aug 15, 15:05      |
|       650    |            28 |          2 | 01. Innere Stadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1010-innere-stadt/%22wg%22---zimmer-kabinett-in-toplage-hinter-stephansdom-ab-sofort-zu-vergeben-866208642/)              | Aug 15, 12:12      |
|       789.06 |            49 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei:-ruhiger-49m%C2%B2-neubau-mit-2-zimmern-und-einbauk%C3%BCche---1120-wien-1127315926/)        | Aug 15, 11:20      |
|       680    |            48 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/hochwertige-zweizimmerwohnung-in-ottaktring-unbefristet-1646060608/)                                       | Aug 15, 10:59      |
|       480    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wiener-wohnen---direktvergabe/-42qm/-2-zimmer-1818157650/)                                                  | Aug 15, 09:31      |
|       794.38 |            38 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/2-zi-neubau-%2B-balkon--k%C3%BCche---3.stock--zeitgem%C3%A4%C3%9F-ausstattung-834096900/)                  | Aug 15, 00:38      |
