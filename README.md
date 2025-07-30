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
|       670    |            65 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/direktvergabe-wiener-wohnen-1372172298/)                                                                                                                             | Jul 30, 22:05      |
|       770.5  |            56 |          3 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/provisionsfrei:-unbefristeter-56m%C2%B2-erstbezug-mit-3-zimmern-im-topsanierten-altbau---1100-wien-1086341909/)                                                            | Jul 30, 20:38      |
|       783.57 |            61 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-stilaltbauwohnung---hier-wohnen-sie-zentral-und-komfortabeln-%21-1049286993/)                                                                                    | Jul 30, 17:26      |
|       764.28 |            58 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-stilaltbauwohnung---hier-wohnen-sie-zentral-und-komfortabeln-%21-1818676289/)                                                                                    | Jul 30, 17:26      |
|       750    |            36 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-top-zustand-in-cityn%C3%A4he-1488761917/)                                                                                                         | Jul 30, 16:18      |
|       633.42 |            57 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/%28reserviert%29-m%C3%B6blierte-gemeindewohnung-1110-wien-%28direktvergabe%29-922247438/)                                                                                  | Jul 30, 14:26      |
|       563.33 |            49 |          2 | 17. Hernals              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/2-zi-altbau---%C3%B6ffentliche-anbindung-s45-1896658046/)                                                                                                                    | Jul 30, 10:20      |
|       408    |            56 |          3 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/wiener-wohnen-direktvergabe-vormerkschein-29.04.2024-3-zimmer-1524353480/)                                                                                           | Jul 30, 09:41      |
|       750    |            64 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%27%272-zimmer-wohnung-perfekt-f%C3%BCr-kleine-familien-und-studenten%27%27-1323667098/)                                                                                   | Jul 30, 07:11      |
|       517    |            48 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/vormerkschein-30.06.2025---gemeindewohnung-top-lage---03.-bezirk---wiener-wohnen-/-wiener-wohnticket---billig---4250%E2%82%AC-abl%C3%B6se---bezugsfertig-944922347/) | Jul 30, 00:56      |
|       594.63 |            45 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/helle-zweizimmer-wohnung-1446598904/)                                                                                                                      | Jul 29, 22:35      |
|       780    |            72 |          3 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/3-zi.-wohnung/-direktvergabe-vms-30.6.24-wienerwohnen-2134266926/)                                                                                                      | Jul 29, 22:18      |
|       790    |            43 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/direkt-bei-u%2Bs-bahn-%7C-raumwunder-%7C-fernblick-%7C-sparsam-1975754256/)                                                                                                | Jul 29, 21:37      |
