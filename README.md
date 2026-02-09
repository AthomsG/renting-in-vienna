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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       658.41 |            61 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-mit-2-zimmer-wohnticketsnummer-:-42775/2024.-die-wohnung-ist-reserviert%21-1312659054/)                                                                                        | Feb 09, 21:23      |
|       698.75 |            54 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%21%21-n%C3%A4he-quellenstra%C3%9Fe-/-u-bahnn%C3%A4he-%21%21-abl%C3%B6sefreie-im-5.-stock-gelegene-%28kein-lift%29-2-zimmer-wohnung-zentral-begehbar---wg-geeignet-zu-vermieten%21-2004125578/) | Feb 09, 16:17      |
|       690    |            43 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gut-aufgeteilte-zwei-zimmer-wohnung-n%C3%A4he-hauptbahnhof-%21-950612053/)                                                                                                                      | Feb 09, 16:13      |
|       462    |            46 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-gemeindewohnung-46m2-balkon-1030-rennweg-1373845110/)                                                                                                                       | Feb 09, 16:02      |
|       475    |            44 |          2 | 03. Landstraße | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-gemeindewohnung---vormerkschein-bis-31.01.2026-oder-fr%C3%BCher-1920777696/)                                                                                                | Feb 09, 14:04      |
|       580    |            54 |          2 | 10. Favoriten  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-wiener-wohnen-2-zimmer-wohnung-abzugeben---einbauk%C3%BCche-schrank-&-bett-inklusive-1096763048/)                                                                              | Feb 09, 11:39      |
|       796.37 |            43 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/attraktive-2-zimmer-wohnung---u-bahn-fu%C3%9Fl%C3%A4ufig-erreichbar%21-971523457/)                                                                                                               | Feb 09, 10:35      |
