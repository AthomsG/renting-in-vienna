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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                                                                                       | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       631    |            86 |          3 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/3-zimmer-gemeindebauwohnung-86-qm-inkl.-13-qm-loggia-812755777/)                                                                                   | Aug 01, 15:36      |
|       750    |            42 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/terrassentraum:-sonnige-2-zimmer-terrassenwohnung-nahe-hauptbahnhof-&-arsenal---provisonsfrei-1305746124/)                                            | Aug 01, 15:05      |
|       792.67 |            41 |          2 | 17. Hernals      | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/ruhige-2-zimmerwohnung-auf-der-hernalser-hauptstra%C3%9Fe-1302404842/)                                                                                  | Aug 01, 14:07      |
|       493.77 |            45 |          2 | 04. Wieden       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/%5Bnur-mit-g%C3%BCltigem-wohnticket%5D-2-zimmer-wohnung-1040-direktvergabe---wiener-wohnen-%28ticket-bis-31.05.2025%29---nachmieter-gesucht-1158011138/) | Aug 01, 13:22      |
|       624.64 |            40 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/neuwertig---fernblick---2-zimmer-wohnung---n%C3%A4he-u6-meidling---gr%C3%BCnblick---unbefristet-1085810893/)                                           | Aug 01, 11:50      |
|       789.06 |            49 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/provisionsfrei:-ruhiger-49m%C2%B2-neubau-mit-2-zimmern-und-einbauk%C3%BCche---1120-wien-1127315926/)                                                   | Aug 01, 11:20      |
