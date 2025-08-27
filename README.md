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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                            | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       499.86 |            44 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sanierte-altbauwohnung---1-zimmer-%2B-kabinett-in-ruhiger-lage-in-der-storkgasse-880127597/)                                                                              | Aug 27, 21:37      |
|       750    |            36 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-top-zustand-in-cityn%C3%A4he-1770112205/)                                                                                                         | Aug 27, 19:34      |
|       680    |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/sch%C3%B6ne-m%C3%B6blierte-wohnung-nahe-u3-simmering-866827717/)                                                                                                           | Aug 27, 16:36      |
|       781.38 |            34 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/achtung.-hohe-mietzinsvorauszahlung%21---beschreibung-beachten---hochwertige-apartments-mit-balkon/terrasse-beim-liechtensteinpark---unbefristet---erstbezug-1106935443/) | Aug 27, 15:27      |
|       638.31 |            34 |          2 | 09. Alsergrund           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1090-alsergrund/achtung.-hohe-mietzinsvorauszahlung%21---beschreibung-beachten---hochwertige-apartments-mit-balkon/terrasse-beim-liechtensteinpark---unbefristet---erstbezug-1755188326/) | Aug 27, 15:27      |
|       404    |            65 |          3 | 16. Ottakring            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gemeinde-wohnung-65qm-in-1160-wien---ruhelage-2-stock-balkon---m%C3%B6bliert-mit-abl%C3%B6se-in-top-zustand-%21-1567061360/)                                               | Aug 27, 15:03      |
|       560    |            45 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-mit-balkon-in-gr%C3%BCnruhelage-45-m2-2039233073/)                                                                                                         | Aug 27, 11:52      |
