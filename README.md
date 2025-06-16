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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       610    |            55 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/gemeindewohnung-direktvergabe-2-zimmer-in-toplage-1907609198/)                                                                        | Jun 16, 14:25      |
|       770    |            51 |          2 | 07. Neubau     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/ruhige-51-m%C2%B2-altbaumiete-/-bandgasse-/-3.-stock-ohne-lift-/-durchgangszimmer-1856178330/)                                            | Jun 16, 14:17      |
|       723.49 |            43 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zimmer-wohnung-mit-balkon-n%C3%A4he-elterleinplatz-1519589897/)                                                                        | Jun 16, 12:56      |
|       760    |            62 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/liebevolle-wohnung-in-top-lage-am-quellenplatz-zu-vermieten-1990342714/)                                                               | Jun 16, 12:49      |
|       617    |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/1100-wien-leebgasse:-sonnige-liebevoll-sanierte-2-zimmer-altbautraumwohnung-ca.-55-m2-mit-lift-unbefristet-zu-vermieten%21-803465456/) | Jun 16, 01:03      |
|       690    |            43 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sch%C3%B6ne-zweizimmerwohnung-43m2-und-viel-nat%C3%BCrliches-licht-1174149363/)                                                         | Jun 15, 21:56      |
|       440    |            61 |          3 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/direktvergabe-%7C-wohnungsvergabe-3---zimmer-1109762545/)                                                                                 | Jun 15, 16:53      |
|       580    |            69 |          3 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe:-sch%C3%B6ne-gemeindewohnung-in-14-bezirk-wichtig-vormerkschein-1576559298/)                                               | Jun 15, 15:22      |
|       780.71 |            69 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-n%C3%A4he-u3-simmering-zu-mieten-in-1110-wien-1418374056/)                                                            | Jun 15, 13:27      |
