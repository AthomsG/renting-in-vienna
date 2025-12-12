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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       691.67 |            48 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/grossz%C3%BCgige-helle-2-zimmer-wohnung%21-1073682993/)                                                                                    | Dec 12, 17:35      |
|       736.5  |            57 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/unbefristete-wg-taugliche-3-zimmer-wohnung-im-15.bezirk%21-1457756308/)                                                  | Dec 12, 17:35      |
|       621.48 |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-2-zimmer-wohnung-im-herzen-von-favoriten%21-995038467/)                                                                     | Dec 12, 17:27      |
|       730    |            53 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/zweizimmer-wohnung-gegen%C3%BCber-der-volksoper-1646787119/)                                                                            | Dec 12, 17:09      |
|       484    |            43 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/gemeindewohnung-mit-loggia---direktvergabe---1050-wien-%28margareteng%C3%BCrtel%29-1293518816/)                                         | Dec 12, 15:35      |
|       795    |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-%2A-wundersch%C3%B6ne-2-zimmer-wohnung-in-top-lage-1833355036/)                                           | Dec 12, 15:18      |
|       739.13 |            74 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/h%C3%BCtteldorfer-stra%C3%9Fe-187:-unbefristet---2-zimmerwohnung-%28stra%C3%9Fenseitig%29---zentrale-lage---2.-stock-ohne-lift-955370844/) | Dec 12, 14:55      |
|       498.89 |            35 |          2 | 06. Mariahilf            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/sch%C3%B6ne-hauptmietwohnung-n%C3%A4he-u4-pilgramgasse/-m%C3%BCrzwardeingasse-1899768882/)                                               | Dec 12, 11:47      |
