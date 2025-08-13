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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District      | Link                                                                                                                                                                             | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       635.44 |            47 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-in-1120-wien-1727174830/)                                                   | Aug 13, 06:49      |
|       753    |            41 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/unbefristet%21-hofseitige-2-zimmer-neubauwohnung-mit-balkon-1771171130/)                     | Aug 12, 20:27      |
|       650    |            37 |          2 | 05. Margareten   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/vermiete-wohnung-%2837m%C2%B2%29-im-5.-bezirk-1766664466/)                                 | Aug 12, 19:46      |
|       770    |            48 |          2 | 11. Simmering    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/49m2-im-ruhigen-teil-simmerings-1632409426/)                                                | Aug 12, 19:23      |
|       680    |            58 |          3 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/3-zimmer-gemeindewohnung-mit-wohnticket---58-m%C2%B2---10.-bezirk-910092463/)               | Aug 12, 18:30      |
|       750    |            45 |          2 | 10. Favoriten    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/%28reserviert%29-reserviert%21-ruhige-gr%C3%BCnlage-2-zimmer-beim-reumannplatz-1653457722/) | Aug 12, 18:04      |
|       780.62 |            54 |          2 | 12. Meidling     | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmerwohnung-zentral-begehbar-n%C3%A4he-meidlinger-hauptstra%C3%9Fe-1690329251/)          | Aug 12, 18:00      |
|       720    |            46 |          2 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/perfekt-geschnittene-sonnige-wohnung---vom-eigent%C3%BCmer-1422600724/)                     | Aug 12, 16:24      |
|       687.41 |            52 |          2 | 07. Neubau       | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/%2Aideal-f%C3%BCr-stadtliebhaber%2A-1683672413/)                                               | Aug 12, 15:56      |
|       550    |            60 |          3 | 03. Landstraße   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/zimmer-in-2er-m%C3%A4dchen-wg-an-einzelperson-zu-vergeben-984750401/)                 | Aug 12, 14:33      |
|       546.53 |            48 |          2 | 02. Leopoldstadt | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/direktvergabe-gemeindebau:-1020-2.-bezirk-bei-donau-2-zimmer-mit-balkon-779695420/)      | Aug 12, 11:58      |
|       750    |            55 |          3 | 16. Ottakring    | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/gut-eingeteilte-55m%C2%B2-wohnung-n%C3%A4he-wilhelminenspital-1642244017/)                  | Aug 12, 11:36      |
