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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                         | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       774    |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/erstbezug-unbefristet-rotenhofgasse/-leibnizgasse-1130113136/)                                                          | Feb 19, 13:45      |
|       766.02 |            58 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/provisionsfrei:-parkseitiger-58m%C2%B2-altbau-mit-einbauk%C3%BCche---1170-wien-1007533300/)                               | Feb 19, 12:59      |
|       799    |            49 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---wohn%28t%29raum-zum-aufbl%C3%BChen---2-zimmerwohnung-mit-balkon-911304439/)                                | Feb 19, 12:30      |
|       716.1  |            52 |          2 | 09. Alsergrund   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/nachmieter-gesucht-%7C-helle-2-zimmer-wohnung-in-top-lage-%7C-1090-wien-1401037854/)                                   | Feb 19, 11:27      |
|       750    |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/vollm%C3%B6blierte-2-zimmer-wohnung-in-1020-wien-zur-untermiete-%28m%C3%A4rz-oktober-2026-oder-n.-v.%29-1946531552/) | Feb 19, 10:12      |
|       796.37 |            43 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/attraktive-2-zimmer-wohnung---u-bahn-fu%C3%9Fl%C3%A4ufig-erreichbar%21-1976733325/)                                      | Feb 19, 09:34      |
|       524    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-direktvergabe-helle-gemeindebauwohnung-4.-stock-mit-aufzug-1923638747/)                                | Feb 19, 08:56      |
|       505    |            50 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-mit-einer-wohnticket-f%C3%BCr-2-zimmer-vor-09.2025-1367336418/)                                      | Feb 19, 00:36      |
|       773.4  |            71 |          4 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/4-zimmer-gemeindewohnung-1541297502/)                                                                             | Feb 18, 21:35      |
|       561    |            46 |          2 | 08. Josefstadt   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/top-lage-im-zentrum-rathausn%C3%A4he-2-zimmer-561.---brutto-1510794785/)                                               | Feb 18, 17:30      |
|       510    |            77 |          3 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-2137037783/)                                                                                            | Feb 18, 15:56      |
|       770    |            56 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/schicke-mietwohnung-in-privater-jugendstil-villa-mit-zwei-zimmern-568557971/)                                            | Feb 18, 15:42      |
|       659    |            48 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-1369048410/)                                                    | Feb 18, 14:03      |
