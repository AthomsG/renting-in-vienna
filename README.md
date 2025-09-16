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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       770    |            53 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/traumhafte-2--zimmer-wohnung-%7C-mit-gemeinschaftsterrasse-1388395637/)                                         | Sep 16, 14:28      |
|       480.9  |            44 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmerwohnung-1018208647/)                                                                                   | Sep 16, 13:41      |
|       794    |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sanierte-2-zimmer-altbauwohnung-1524509102/)                                                             | Sep 16, 12:32      |
|       578.34 |            62 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-3-zimmerwohnung-787599159/)                                                                        | Sep 16, 10:51      |
|       659    |            67 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/preiswerte-dachgeschoss-whg2-min-zu-u1-ruhig-hell-fernblick-f%C3%BCr-sportliche6.-stock-ohne-lift-1973623808/) | Sep 16, 09:18      |
|       605.21 |            59 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe:-helle-2-zimmer-gemeindewohnung-mit-loggia-%2859-m%C2%B2%29-1555471238/)                          | Sep 16, 02:35      |
|       728    |            55 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/reserviert-wg-taugliche-2-zimmer-altbauwohnung-in-unmittelbarer-u-bahn-n%C3%A4he-1632069210/)  | Sep 15, 20:59      |
|       500    |            47 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/direktvergabe---2-zimmer-gemeindewohnung-n%C3%A4he-willhelminenberg-1565561363/)                               | Sep 15, 19:00      |
