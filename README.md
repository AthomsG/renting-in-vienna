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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       782.87 |            66 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/brotfabrikn%C3%A4he-/-helle-66-m%C2%B2-altbaumiete-/-unbefristete-hauptmiete-853732891/)                                                                                     | May 07, 10:56      |
|       456.45 |            56 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/wohnung-zur-weitergabe-1466564576/)                                                                                                                                          | May 06, 19:43      |
|       796.84 |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/neues-heim-direkt-auf-der-mariahilferstra%C3%9Fe-gelegen%21-1630057430/)                                                                                     | May 06, 17:37      |
|       770    |           nan |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnen-mit-lebensqualit%C3%A4t-beim-schlo%C3%9F-sch%C3%B6nbrunn-1094754023/)                                                                                                  | May 06, 15:30      |
|       790    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmerwohnung-unbefristete-hauptmiete-n%C3%A4he-reumannplatz-1238161069/)                                                                                                  | May 06, 14:39      |
|       550    |            47 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/top-lage-im-zentrum-rathausn%C3%A4he-2-zimmer-550.---brutto-1718142712/)                                                                                                    | May 06, 13:20      |
|       570    |            56 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/helle-2-zimmer-wohnung-%7C-wiener-wohnen-mit-vormerkschein-%7C-56-m%C2%B2-%7C-1030-wien-%7C-n%C3%A4he-u3-&-prater-%7C-teilm%C3%B6bliert-%7C-%E2%82%AC-570-1131226445/) | May 06, 10:26      |
