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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       580    |            54 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeinde-wohnung-wiener-wohnen-2-zimmer-wohnung-abzugeben---einbauk%C3%BCche-schrank-&-bett-inklusive-1096763048/) | Feb 09, 11:39      |
|       799.33 |            57 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/gem%C3%BCtliche-2-zimmer-wohnung-in-1070-wien---ihr-neues-zuhause-auf-57m%C2%B2%21-1381910238/)                       | Feb 09, 11:27      |
|       796.37 |            43 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/attraktive-2-zimmer-wohnung---u-bahn-fu%C3%9Fl%C3%A4ufig-erreichbar%21-971523457/)                                  | Feb 09, 10:35      |
|       769    |            54 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/nachmieter-gesucht-f%C3%BCr-wohnung-im-7.-bezirk-1835919182/)                                                         | Feb 08, 20:20      |
|       588    |            72 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/gemeindewohnung-direktvergabe-818273868/)                                                          | Feb 08, 20:08      |
|       488    |            59 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%28reserviert%29-direktvergabe-wiener-gemeindewohnung-vmd-bis-31.12.2025-930452679/)                                | Feb 08, 17:44      |
|       635    |            50 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wohnung-im-3-bezirk-1773316653/)                                                                             | Feb 08, 15:34      |
