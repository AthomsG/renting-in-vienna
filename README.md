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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       649    |            30 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-1.8.---laxenburgerstrasse-151---klimatisierte-2-zimmer-singlewohnung-mit-s%C3%BCdseitigem-fernblick-im-6.-stock-1287028730/) | Jul 08, 12:38      |
|       740    |            53 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei%21-wohnung-in-ruhiger-lage-2070378558/)                                                                            | Jul 08, 12:36      |
|       790    |            55 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2zimmer---wohnung-zimmer-getrennt-begehbar-zu-mieten-nur-die-k%C3%BCche-ist-m%C3%B6bliert-1851774876/)                          | Jul 08, 12:29      |
|       799    |            37 |          2 | 09. Alsergrund | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/gem%C3%BCtliche-2-zimmerwohnung-f%C3%BCr-studierende-und-singles-mit-terrasse-im-servitenviertel-1881964396/)                  | Jul 08, 10:57      |
|       620    |            39 |          2 | 06. Mariahilf  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1060-mariahilf/unbefristete-hauptmietwohnung-in-1060-wien-1744653849/)                                                                         | Jul 08, 10:53      |
|       777.4  |            44 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/11.hugogasse-unbefristete-2-zimmer-neubaumiete-in-u3-n%C3%A4he-1449762314/)                                                     | Jul 08, 10:34      |
|       598.06 |            55 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/%28reserviert%29-helle-gemeindebau-wohnung-mit-balkon-im-5.-bezirk%21-1431206902/)                                             | Jul 08, 08:23      |
|       663.34 |            52 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/helle-neusanierte-2-zimmer-wohnung-unbefristet-1159197800/)                                                                       | Jul 08, 07:51      |
