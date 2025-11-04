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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       799.36 |            55 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/grossz%C3%BCgige-2-zimmer-wohnung-im-10.bezirk%21-1872106349/)                                                                     | Nov 04, 16:18      |
|       658.92 |            56 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/besonders-statt-gew%C3%B6hnlich-3-zimmer-wohnung-im-16.bezirk---ca.-56m%C2%B2-wfl---pantryk%C3%BCche---elektroheizung-1039563743/) | Nov 04, 15:22      |
|       736.5  |            57 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/unbefristete-wg-taugliche-3-zimmer-wohnung-im-15.bezirk%21-1686723983/)                                            | Nov 04, 14:57      |
|       776.62 |            42 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/ignazgasse---2-zimmer-wohnung-%7C-ca.-42-m%C2%B2-wohnfl%C3%A4che-%7C-einbauk%C3%BCche-%7C-ab-sofort-775235802/)                     | Nov 04, 14:57      |
|       747.92 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/besichtigung-am-06.11.2025-von-16:30-19:00-ohne-anmeldung---wohnung-in-1110-wien---felsgasse-4/33-1384771803/)                     | Nov 04, 11:20      |
|       699    |            36 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/himbergerstra%C3%9Fe-28-1559773134/)                                                                                               | Nov 04, 11:08      |
|       747.92 |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/besichtigung-am-06.11.2025-von-16:30-19:00---neu-sanierte-2-zimmer-wohnung-in-1110-wien---top26-1080236707/)                       | Nov 04, 11:05      |
|       770    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/nette-2-zimmerwohnung-mit-loggia-1169631802/)                                                                                      | Nov 04, 09:58      |
|       625    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien-van-der-n%C3%BCllgasse:-2-zimmer-altbauwohnung-ca.-52-m2-unbefristet-und-barrierefrei-mit-lift-zu-vermieten-1740321313/) | Nov 04, 00:47      |
|       494    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-in-oberlaa-1657635996/)                                                                              | Nov 03, 21:13      |
|       750    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-hoflage-attraktive-unbefristete-2-zimmerwohnung-in-stil-altbau-u-1-n%C3%A4he-2017816252/)                           | Nov 03, 16:23      |
