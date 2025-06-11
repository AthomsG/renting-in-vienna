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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       797.55 |            59 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/studentenwohnung:-sch%C3%B6ne-2-zimmer-wohnung-mit-separater-k%C3%BCche-1812581865/)                                                                               | Jun 11, 12:36      |
|       781.81 |            54 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-altbau-mit-guter-anbindung-1974132361/)                                                                                                                  | Jun 11, 12:21      |
|       625    |            67 |          3 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohnung-zu-vermieten--nachmieter-gesucht-1839362101/)                                                                                                            | Jun 11, 12:10      |
|       650    |            42 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/entz%C3%BCckende-wohnung-nahe-u1-und-doch-ruhig-1322108036/)                                                                                                     | Jun 11, 12:03      |
|       454.19 |            45 |          2 | 11. Simmering | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direktvergabe-nachmieter-gesucht-f%C3%BCr-sehr-sch%C3%B6ne&m%C3%B6blierte-2-zimmerwohnung-in-s80--und-u3-n%C3%A4he.-wiener-wohn-ticket-notwendig%21-1563699094/) | Jun 11, 08:26      |
|       590    |            56 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ruhig-gr%C3%BCn-&-perfekt-gelegen:-gemeindewohnung-in-1100-wien-zu-vergeben-981065082/)                                                                          | Jun 10, 19:35      |
|       690    |            83 |          3 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/4-zimmer-gemeindewohnung-%28mind.-vor-31.10.2019-vormerk-notwendig%29-1514934250/)                                                                               | Jun 10, 18:39      |
|       788.5  |            54 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gem%C3%BCtliche-2-zimmer-wohnung-inkl.-gemeinschaftsinnenhof%21-1303259059/)                                                                                     | Jun 10, 13:35      |
|       772.33 |            45 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/geschmackvolles-2-zimmer-apartment-mit-balkon-im-sonnwendviertel-1534706878/)                                                                                    | Jun 10, 11:48      |
