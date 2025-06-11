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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       454.19 |            45 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-nachmieter-gesucht-f%C3%BCr-sehr-sch%C3%B6ne&m%C3%B6blierte-2-zimmerwohnung-in-s80--und-u3-n%C3%A4he.-wiener-wohn-ticket-notwendig%21-1563699094/) | Jun 11, 08:26      |
|       590    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhig-gr%C3%BCn-&-perfekt-gelegen:-gemeindewohnung-in-1100-wien-zu-vergeben-981065082/)                                                                          | Jun 10, 19:35      |
|       690    |            83 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/4-zimmer-gemeindewohnung-%28mind.-vor-31.10.2019-vormerk-notwendig%29-1514934250/)                                                                               | Jun 10, 18:39      |
|       788.5  |            54 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-inkl.-gemeinschaftsinnenhof%21-1303259059/)                                                                                     | Jun 10, 13:35      |
|       772.33 |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/geschmackvolles-2-zimmer-apartment-mit-balkon-im-sonnwendviertel-1534706878/)                                                                                    | Jun 10, 11:48      |
|       544.69 |            50 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/gemeindewohnung-direktvergabe-vormerkschein-bis-28.02.2025-1685478774/)                                                                                       | Jun 10, 11:14      |
|       618.63 |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristeter-sofortbezug-in-der-fernkorngasse-1023292848/)                                                                                                      | Jun 10, 10:28      |
|       793    |            38 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-wohnung-in-1150-wien-2035393678/)                                                                                                       | Jun 10, 09:36      |
