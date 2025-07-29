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
|       745    |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/stilvolle-neubauwohnung-mit-top-ausstattung---sofort-verf%C3%BCgbar%21-1883697092/)                      | Jul 29, 03:35      |
|       655    |            34 |          2 | 08. Josefstadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1080-josefstadt/34m2-befristete-altbaumiete-1749329306/)                                                                | Jul 28, 19:41      |
|       785.99 |            49 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/ankommen-&-wohlf%C3%BChlen:-2-zimmer-in-zentraler-lage-in-1150-wien%21-861865813/)       | Jul 28, 18:45      |
|       540    |            56 |          2 | 04. Wieden               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1040-wieden/direktvergabe-4.-bezirk-vms.31.05.2025-1775788919/)                                                         | Jul 28, 18:09      |
|       704    |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/quellenstra%C3%9Fe---2-zimmer-altbau-mit-extra-einbauk%C3%BCche-im-2.-stock-1962769571/)                 | Jul 28, 16:55      |
|       730.81 |            49 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/charmante-2-zimmer-wohnung-in-unmittelbarer-u-bahn-n%C3%A4he%21-970120821/)                               | Jul 28, 14:53      |
|       788.38 |            53 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohntraum-mit-balkon%21-1980986696/)                                                            | Jul 28, 13:56      |
|       649    |            33 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ab-15.08.---1100-wien---ansprechende-neubau-singlewohnung-inkl.-k%C3%BCchenzeile-mit-balkon-1825026235/) | Jul 28, 12:37      |
|       799    |            65 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/abl%C3%B6sefreie-neu-adaptierte-traumhauptmiete-mit-65-m%C2%B2-1108607231/)              | Jul 28, 11:52      |
|       727.25 |            73 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/3-zimmer-gef%C3%B6rderte-wohnung-1030-905165188/)                                                  | Jul 28, 09:32      |
