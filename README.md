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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       750    |            60 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/2-zimmer-wohnung-in-1050-wien---ideal-zum-renovieren-f%C3%BCr-750-eur%21-961452159/) | Feb 14, 16:35      |
|       785.75 |            84 |          3 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/vollausgestattete-3-zimmer-altbauwohnung-n%C3%A4he-meiselmarkt-2134274707/)             | Feb 14, 16:15      |
|       750    |           130 |          3 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/zimmer-in-gro%C3%9Fz%C3%BCgiger-3er-wg---miete-inkl.-aller-nebenkosten-1558595716/)  | Feb 14, 15:40      |
|       760    |            56 |          2 | 14. Penzing      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/2-zimmer-wohnung-mit-loggia-in-ruhiger-lage-von-penzing---provisionsfrei-1182249676/)   | Feb 14, 12:27      |
|       796    |            48 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung-2003254564/)                                             | Feb 14, 10:43      |
|       756.75 |            85 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-direktvergabe-792478660/)                                             | Feb 14, 10:04      |
|       693    |           nan |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/in-besonders-attraktiver-lage---mitten-in-hetzendorf-2118659587/)                      | Feb 14, 09:58      |
|       690    |            49 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/sonnige-49m2-wohnung/-atelier-in-1040-wien-1502856610/)                                  | Feb 14, 09:26      |
|       432    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/direktvergabe-wiener-wohnen-ticket-31.12.2024-1147334553/)                            | Feb 14, 07:38      |
|       473    |            46 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-2-zimmer-in-zentraler-lage-1287736518/)                               | Feb 13, 19:27      |
|       526    |            51 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/2-zimmer-gemeindewohnung-direkt-bei-u1-vorgantenstra%C3%9Fe-1534538170/)           | Feb 13, 18:59      |
