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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       780    |            44 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/11.hugogasse-unbefristete-provisionsfreie-unm%C3%B6blierte-2-zimmer-neubaumiete-in-u3-n%C3%A4he-1163235011/)                           | Oct 08, 13:41      |
|       656.94 |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/kleinmietwohnung-in-rennweg---n%C3%A4he-1509346484/)                                                                             | Oct 08, 12:38      |
|       630    |            44 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/schweglerstra%C3%9Fe:-2-zimmer-erstbezug-n%C3%A4he-schmelz-1125502530/)                                                | Oct 08, 10:59      |
|       670    |            65 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-direktvergabe-vormerkschein-31.08.2024-979629484/)                                                               | Oct 08, 07:29      |
|       750    |            51 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/m%C3%B6blierte-2-zimmer-direkt-u1-1607179733/)                                                                                         | Oct 08, 03:45      |
|       795    |            52 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/bright-2-room-flat-next-to-u1-1697852775/)                                                                                             | Oct 08, 03:45      |
|       588.25 |            53 |          3 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/direktvergabe-gemeindebau-%28nur-mit-wiener-wohnticket%21%29:-helle-2/3-zimmer-wohnung-mit-top-anbindung-im-14.%C2%A0bezirk-1388878384/) | Oct 07, 22:49      |
|       600    |            60 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-vormerkschein-vor-september-2025-2111099678/)                                                                    | Oct 07, 18:57      |
|       739.57 |            34 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/wohnung-in-ruhelage-mitten-im-8.-f%C3%BCr-singls-1343385042/)                                                                         | Oct 07, 17:33      |
|       500.73 |            49 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/gemeindebau-direktvergabe-848868991/)                                                                                                   | Oct 07, 17:05      |
|       796    |            36 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-nachmieter%2Ain-f%C3%BCr-teilm%C3%B6blierte-wohnung-mit-balkon-pool-und-sauna-im-sonnwendviertel-1983444977/)         | Oct 07, 16:27      |
|       750    |            43 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei-hoflage-attraktive-unbefristete-2-zimmerwohnung-in-stil-altbau-u-1-n%C3%A4he-987551283/)                                | Oct 07, 15:58      |
|       770    |            53 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/traumhafte-2--zimmer-wohnung-%7C-unbefristet-%7C-mit-gemeinschaftsterrasse-2066549860/)                                                 | Oct 07, 15:17      |
