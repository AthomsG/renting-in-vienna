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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                   | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       720.89 |            46 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/die-zimmerei-%7C-ab-juni:-m%C3%B6bliertes-all-in-2-zimmer-apartment-im-2.-bezirk-nahe-wu-&-sfu-%7Cxl-bude-1177987177/)         | May 01, 16:25      |
|       543.2  |            55 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/direktvergabe-gemeindewohnung-1440180418/)                                                                                         | May 01, 14:55      |
|       790    |            42 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/tolle-2-zimmerwohnung-n%C3%A4he-u3-zippererstra%C3%9Fe---ideal-f%C3%BCr-singles-oder-p%C3%A4rchen---inkl.-k%C3%BCche-1079809746/) | May 01, 14:06      |
|       750    |            38 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/zweitwohnung-%7C-studentenwohnung-mit-lift-1216930310/)                                                                             | May 01, 09:42      |
|       780    |            55 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-wohnung-mit-k%C3%BC%2B-dusche/-wc-/-2-zimmer-eigener-eingang-1373191471/)                                                | May 01, 09:10      |
|       720    |            52 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gem%C3%BCtlich-zwei-zimmer-wohnung-mit-viel-sonne-und-gro%C3%9Fer-k%C3%BCche-1748055564/)                                         | Apr 30, 21:50      |
