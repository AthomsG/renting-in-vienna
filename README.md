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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                          | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       649    |            33 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-15.08.---1100-wien---ansprechende-neubau-singlewohnung-inkl.-k%C3%BCchenzeile-mit-balkon-1825026235/) | Jul 28, 12:37      |
|       799    |            65 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/abl%C3%B6sefreie-neu-adaptierte-traumhauptmiete-mit-65-m%C2%B2-1108607231/)              | Jul 28, 11:52      |
|       691    |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/saniert-mietwohnung-bei-u3-991082669/)                                                   | Jul 28, 09:41      |
|       727.25 |            73 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3-zimmer-gef%C3%B6rderte-wohnung-1030-905165188/)                                                  | Jul 28, 09:32      |
|       793.65 |            38 |          2 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/moderne-2-zimmerwohnung-i-100m-zur-u3-station-kendlerstra%C3%9Fe-1945735306/)                            | Jul 27, 19:54      |
|       665    |            58 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-3--zimmer-1829648175/)                                                                   | Jul 27, 13:30      |
|       746    |            37 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/perfekte-stadtwohnung:-vollm%C3%B6bliert-direkt-bei-u4/-u6-l%C3%A4ngenfeldgasse-1927991345/)              | Jul 27, 13:16      |
|       532.48 |            52 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe-2-zimmer-gemeindewohnung-1686100667/)                                                       | Jul 27, 12:28      |
|       770    |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%2Ap%C3%A4rchentraum%2Asonniger-neubau-mit-bester-infrastruktur%21-1518950514/)                          | Jul 27, 12:05      |
