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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                           | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       760    |            59 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/provisionsfrei-f%C3%BCr-den-mieter%21-huglgasse-n%C3%A4chst-u3-altbaumiete-59m%C2%B2-komplettk%C3%BCche-wg-eignung%21-studenten-bevorzugt%21-2142217077/) | Oct 17, 17:55      |
|       580    |            68 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeinde-wohnung-.-vormerkschein-bis-ende-2024-780354406/)                                                                                                                | Oct 17, 16:41      |
|       799    |            42 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/n%C3%A4he-waldm%C3%BCllerpark-%7C-helle-2-zimmer-wohnung---ideal-f%C3%BCr-singles%21-2061238125/)                                                                         | Oct 17, 16:16      |
|       750    |            57 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/anfrage-gestoppt---nachmieter-gesucht--1140-wien--sch%C3%B6ne-2-zimmer-wohnung-in-top-lage--unbefristet-2084334689/)                                                        | Oct 17, 14:54      |
|       720    |            64 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/helle-2-zi.--altbauwohnung-1360892750/)                                                                                                                                   | Oct 17, 14:14      |
|       545    |            60 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhige-2-zimmerwohnung-2047071001/)                                                                                                                                       | Oct 17, 13:55      |
|       688.36 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-sehr-helle-wohnung-in-einem-gepflegten-stilaltbauhaus-%28mit-lift%29---direkt-bei-der-u1-station-altes-landgut-gelegen%21-965641460/)                        | Oct 17, 13:17      |
|       418    |            40 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/im-moment-nehmen-wir-keine-neuen-anfragen-mehr-an-1484942177/)                                                                                                      | Oct 17, 12:28      |
