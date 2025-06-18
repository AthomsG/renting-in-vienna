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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       639.24 |            62 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristete-3-zimmer-wohnung-mit-balkon-in-hetzendorf-1177246828/)                                                       | Jun 18, 14:59      |
|       599    |            40 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/termine-bitte-online-buchen-1167023954/)                                                                              | Jun 18, 14:27      |
|       771.38 |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-2-zimmer-wohnung-in-ruhelage-mit-einbauk%C3%BCche-und-durchdachter-raumaufteilung---jetzt-anfragen-1980415430/) | Jun 18, 13:46      |
|       781.81 |            54 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-altbau-mit-guter-anbindung-1974132361/)                                                                          | Jun 18, 12:21      |
|       650    |            50 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2er-wg-altbau-%7C-jahngasse-%7C-unbefristet-1674543062/)                                                                | Jun 18, 10:28      |
|       750    |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristeter-altbau-wilhelmstra%C3%9Fe-1576835042/)                                                                      | Jun 18, 10:17      |
|       600    |            52 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/altbau-wohnung-2-zimmer-getrennt-begehbar-970034532/)                                                    | Jun 17, 22:06      |
|       684.03 |            78 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/entdecken-sie-ihre-traumwohnung-in-1100-wien---3-zimmer-78-m%C2%B2-zum-wohlf%C3%BChlen%21-1715544148/)                   | Jun 17, 15:57      |
|       621.35 |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-gemeindewohnung-in-1100-wien-2053081859/)                                                                  | Jun 17, 15:34      |
|       771.81 |            32 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-mit-wohlf%C3%BChlfaktor---topmoderne-mietwohnung-nahe-u6-&-s-bahn-2012956530/)                                  | Jun 17, 14:18      |
|       649.8  |            51 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/top-dachgeschoss-am-dornerplatz-1957868661/)                                                                               | Jun 17, 13:49      |
