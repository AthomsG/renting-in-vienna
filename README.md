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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District    | Link                                                                                                                                                                                                                                                    | 📅 Published Date   |
|-------------:|--------------:|-----------:|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       780    |            50 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/moderne-2-zimmer-wohnung-mit-garten-neubau-%2850m%C2%B2-%2B-30m%C2%B2-garten%29---voll-m%C3%B6beliert---kein-genossenschaftsanteil%21-abl%C3%B6se-%21-2067188168/) | Jun 29, 19:48      |
|       794.25 |            44 |          2 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/rainergasse:-zweizimmer-starterwohnung-nahe-hauptbahnhof-1464910359/)                                                                                                 | Jun 29, 19:38      |
|       795.18 |            44 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ihr-neues-zuhause-am-leberberg%21-2009649118/)                                                                                                                     | Jun 29, 17:38      |
|       798.5  |            43 |          2 | 11. Simmering  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/tolle-2-zimmerwohnung-mit-garten%21-1126838555/)                                                                                                                   | Jun 29, 17:38      |
|       715    |           nan |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/moderne-garconnieren-sowie-2-zimmer-apartments-in-zentraler-lage-in-altmannsdorf-1885271690/)                                                                       | Jun 29, 14:37      |
|       693    |           nan |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/moderne-garconnieren-sowie-2-zimmer-apartments-in-zentraler-lage-in-altmannsdorf-1366689443/)                                                                       | Jun 29, 14:00      |
|       595    |            58 |          3 | 04. Wieden     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/gemeindewohnung-zum-direkvegabe-1635060540/)                                                                                                                          | Jun 29, 13:58      |
|       690    |            47 |          2 | 05. Margareten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/zentrale-2-zimmer-wohnung-schlafzimmer-zum-innenhof-1982206260/)                                                                                                  | Jun 29, 09:03      |
|       529.82 |            39 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/sonnige-renovierte-2-zimmer-wohnung-in-zentraler-lage-2018241073/)                                                                                                  | Jun 29, 08:35      |
|       578.67 |            53 |          2 | 14. Penzing    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/ruhige-gemeindewohnung-im-14.-bezirk---vormerkschein/-wohnticket-bis-28.02.2026-%28direktvergabe%29-1188567254/)                                                     | Jun 29, 02:01      |
|       633    |            44 |          2 | 17. Hernals    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/yppenmarktn%C3%A4he-beim-akh-unbefristet%21%21-1644446435/)                                                                                                          | Jun 28, 22:34      |
|       770    |            42 |          2 | 12. Meidling   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/erstbezug-nach-renovierung---unbefristet---u6-&-s-bahn-ums-eck---innenhof-ruhelage-815356759/)                                                                      | Jun 28, 20:38      |
