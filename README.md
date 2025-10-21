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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                 | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       680    |            74 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/1020-wien-novaragasse-top-10-drei-zimmer-74m%C2%B2-k%C3%BCche-bad.-wc-garderobe-hofruhelage-2.-stock-ohne-lift-miete:-eur-680---1898491794/) | Oct 21, 16:56      |
|       660    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/private-2-zimmer-wohnung-zur-vermieten-952640152/)                                                                                              | Oct 21, 16:24      |
|       604.53 |            53 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/%21-nur-mit-vormerkschein%21-helle-ruhige-gemeindewohnung-direktvergabe-in-top-lage-2097055254/)                                | Oct 21, 15:35      |
|       530    |            59 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-vormerkschein-30.09.2025-2087789689/)                                                                                           | Oct 21, 13:57      |
|       461    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-%28vmd:-oktober-2025%29-1726656485/)                                                                                   | Oct 20, 19:29      |
|       795    |            59 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei:-sonniger-59m%C2%B2-altbau-mit-2-zimmern-und-lift---1160-wien-1301427543/)                                                       | Oct 20, 17:36      |
|       796.71 |            52 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/open-house-am-22.10.---keine-anrufe---anfragen-nur-per-mail-1077685579/)                                                                        | Oct 20, 16:49      |
|       520    |            50 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sonnige-gemeindewohnung-3.-bezirk-%28rabenhof%29-1197414041/)                                                                             | Oct 20, 16:02      |
