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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       610    |            60 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zimmerwohnung-bei-der-margarethenstra%C3%9Fe-2064765220/)                                                           | Jun 19, 07:21      |
|       795.29 |            32 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-2-zimmer-wohnung-2003847847/)                                                                                | Jun 19, 07:19      |
|       750    |            75 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/besichtigung-samstag-12:00---25-zentrale-zimmer-in-ruhelage-altbau-1256884835/)                                         | Jun 18, 19:32      |
|       720.01 |            57 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/inzersdorfer-stra%C3%9Fe---3-zimmer-altbau-mit-gemeinschaftsgarten-2135411867/)                                        | Jun 18, 18:37      |
|       599    |            54 |          4 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/4-zimmer-wohnung-im-17.-bezirk-maximal-3-personen---nur-f%C3%BCr-berufst%C3%A4tige-oder-studenten-599-miete-1619960916/) | Jun 18, 17:17      |
|       560    |            33 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gem%C3%BCtliche-wohnung-f%C3%BCr-singles-im-dritten-bezirk-2066699161/)                                          | Jun 18, 17:07      |
|       648.56 |            78 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gro%C3%9Fz%C3%BCgige-2-zimmer-altbauwohnung-mit-78-m%C2%B2---n%C3%A4he-u1-keplerplatz-1778570131/)                     | Jun 18, 14:05      |
|       775    |            33 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernes-single-apartment-mit-terrasse---erstbezug-1965841874/)                                                        | Jun 18, 13:48      |
|       730    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/jagdgasse:-gepflegte-helle-2-zimmerwohnung---gute-infrastruktur-und-verkehrsanbindung-1636511241/)                     | Jun 18, 12:09      |
|       776.54 |            53 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/generalsanierte-2-zimmer-wohnung-%28unbefristet%29-n%C3%A4he-u4-meidling-hauptstra%C3%9Fe-1343321989/) | Jun 18, 09:49      |
|       634.34 |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ideale-2-zimmer-neubauwohnung---zwischen-quellenstra%C3%9Fe-und-gudrunstra%C3%9Fe-1970495564/)                         | Jun 18, 08:28      |
