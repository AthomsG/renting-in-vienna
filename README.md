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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                              | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       499.86 |            44 |          2 | 05. Margareten           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1050-margareten/sanierte-altbauwohnung---1-zimmer-%2B-kabinett-in-ruhiger-lage-in-der-storkgasse-1734443796/)                                               | Sep 11, 15:19      |
|       720    |            48 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-in-ruhelage-zu-vermieten-1625265733/)                                                                                                 | Sep 11, 15:02      |
|       694.36 |            55 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/preiswerte-2-zimmer-wohnung-in-1030-wien-1354789132/)                                                                                  | Sep 11, 14:27      |
|       790    |            47 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/studenten-willkommen---tichy-und-u1-ums-eck-963869023/)                                                                                      | Sep 11, 13:57      |
|       753.13 |            68 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/2-zimmer-wohnung-n%C3%A4he-u3-zu-mieten-in-1110-wien-1925278139/)                                                                            | Sep 11, 12:26      |
|       799    |            45 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/wohlf%C3%BChlen-leicht-gemacht:-2-zimmer-mit-balkon---viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-814857481/)                          | Sep 11, 11:31      |
|       799    |            50 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gro%C3%9Fz%C3%BCgige-2-zimmerwohnung-mit-balkon---viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg-987009303/)                              | Sep 11, 11:30      |
|       799    |            49 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/viola-park---ihre-wohlf%C3%BChloase-am-laaer-berg---2-zimmer-wohnung-mit-balkon-955559017/)                                                  | Sep 11, 11:28      |
|       490    |            47 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/sch%C3%B6ne-zentrale-gemeindewohnung-1030-wien-landstra%C3%9Fe-vormerkschein-31.08.2025-895554242/)                                    | Sep 11, 11:04      |
|       759.99 |            53 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/charmante-vollsanierte-2-zimmer-wohnung-in-1100-wien---ideal-zum-wohlf%C3%BChlen%21-1554200138/)                                             | Sep 11, 10:56      |
|       789    |            31 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/mitten-im-dritten---erstbezug-nahe-u3-s-bahn-und-hervorragender-infrastruktur-mit-hochwertiger-ausstattung%21-1190917268/)             | Sep 11, 09:46      |
|       783.33 |            50 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/b%C3%BCror%C3%A4umlichkeiten-%2A%2A-n%C3%A4he-u3/u4-%2A%2A-zur-befristeten-vermietung-1141195550/)                                            | Sep 11, 01:09      |
|       420.64 |            50 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/%28reserviert%29-direktvergabe-wiener-wohnen-/-neubau-mit-traumhaftem-donau-fernblick-1159522266/)                                        | Sep 10, 20:51      |
|       552    |            49 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/nachmieter-gemeindewohnung-1761149382/)                                                                                                        | Sep 10, 20:37      |
|       779    |            31 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/erstbezug-in-bestlage-nahe-u3-s-bahn-und-hervorragender-infrastruktur-mit-hochwertiger-ausstattung%21---mitten-im-dritten-1983536972/) | Sep 10, 16:56      |
|       430.36 |            65 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/provisionsfrei:-preisg%C3%BCnstige-65m%C2%B2-wohnung-mit-2-zimmern-und-gang-wc---1140-wien-1147613536/)                                        | Sep 10, 16:17      |
|       539    |            50 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/2-zimmer-im-herzen-von-wien-wg-tauglich-direkt-bei-der-u3-2100654093/)                                                       | Sep 10, 15:43      |
