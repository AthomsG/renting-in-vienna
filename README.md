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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                                     | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       580    |            54 |          2 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/54m%C2%B2-wiener-wohnen-gemeindewohnung-im-rabenhof-2114852356/)                                                                                              | Feb 17, 00:12      |
|       649    |            63 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/fenzlgasse---sanierungsbed%C3%BCrftiger-2-zimmer-altbau-mit-extra-k%C3%BCche-zu-vermieten-1185014840/)                                                                | Feb 16, 19:32      |
|       799    |            59 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/parkblick-%7C-2-zimmer-%7C-termine-siehe-text-1740111785/)                                                                                                          | Feb 16, 18:07      |
|       450    |            63 |          3 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/gemeindewohnung-in-wien-neubau-804253327/)                                                                                                                             | Feb 16, 17:11      |
|       799    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wundersch%C3%B6ne-2-z-mit-freiem-blick-in-richtung-westen---viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-1866684875/)                                          | Feb 16, 16:41      |
|       799    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-1384844240/)                                                                                                      | Feb 16, 16:40      |
|       560    |            39 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtliche-erdgescho%C3%9Fwohnung-sucht-langfristige/n-mieter/in--1421757942/)                                                                                 | Feb 16, 16:13      |
|       543.69 |            52 |          2 | 01. Innere Stadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1010-innere-stadt/%28reserviert%29-vermietet-%21-gemeindewohnung-direktvergabe-g%C3%BCltiges-wiener-wohn-ticket-bis-31.01.2026-f%C3%BCr-2-wohnr%C3%A4ume-voraussetzung-900270990/) | Feb 16, 15:17      |
|       748    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-hauptbahnhof%21-kleine-2-zimmer-neubauwohnung%21-1237211690/)                                                                                             | Feb 16, 15:16      |
|       750    |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/helle-2-zimmerwohnung-790148937/)                                                                                                                                   | Feb 16, 10:17      |
|       645    |            47 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nachmieterin-gesucht-f%C3%BCr-sch%C3%B6ne-helle-altbau-wohnung-922707575/)                                                                                            | Feb 16, 08:29      |
|       613.63 |            62 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-direktvergabe-mit-balkon-und-blick-auf-parkanlage-1837665499/)                                                                                     | Feb 15, 23:22      |
