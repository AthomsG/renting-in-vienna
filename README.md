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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       792.86 |            54 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Abestausstattung%2A---sonniger-neubau-beim-antonspark-1136092440/)                                                                         | Nov 22, 10:35      |
|       745.95 |            61 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gro%C3%9Fz%C3%BCgige-25-zimmer-altbauwohnung-genau-zwischen-u6-thaliastra%C3%9Fe-und-brunnenmarkt-%21%21-914286420/)                         | Nov 22, 08:40      |
|       606    |            52 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/gr%C3%BCn-ruhig-und-sch%C3%B6n-wohnen.-2-zi.-hauptmiete-kat-a-unbefristet-und-in-nur-15-min-ins-zentrum-und-zur-uni-1297568559/)               | Nov 21, 18:17      |
|       722    |            32 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-m%C3%B6blierte-2-zimmer-wohnung-mit-balkon-in-der-leopoldstadt-/-2nd-district-%7C-maxi-bude-1893604330/)                 | Nov 21, 16:28      |
|       799.36 |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/grossz%C3%BCgige-2-zimmer-wohnung-im-10.bezirk%21-1872106349/)                                                                               | Nov 21, 16:18      |
|       790    |            42 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/urban-living-meidling---m%C3%B6bliert-flexibel-modern---mit-langfristiger-flexibilit%C3%A4t-bis-zu-drei-jahren-1025747904/)                   | Nov 21, 15:28      |
|       604.83 |            58 |          3 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/%28reserviert%29-%223-zimmer-gemeindewohnung---direktvergabe-%28vormerkschein-bis-30.11.2025%29-1170-wien-864637199/)                          | Nov 21, 14:59      |
|       447.96 |            35 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/%28bitte-derzeit-keine-weiteren-anfragen%21%29wohnung-im-herzen-von-ottakring-helle-2-zimmer-wohnung-in-ottakring---top-lage%21-2111010397/) | Nov 21, 13:10      |
