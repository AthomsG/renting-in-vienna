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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       773.38 |            66 |          3 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/neu-sanierte-3-zimmer-altbau-wohnung-fussl%C3%A4ufig-zur-mariahilferstra%C3%9Fe%21-887474195/)                                                                                         | Dec 02, 09:26      |
|       790    |            46 |          2 | 21. Floridsdorf          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1210-floridsdorf/stammersdorfer-wohntr%C3%A4ume-erleben:-mietwohnungen-mit-option-auf-zuk%C3%BCnftigen-kauf-739383800/)                                                                                               | Dec 02, 08:56      |
|       599.44 |            55 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/erstbezug---betreutes-wohnen-%28ab-dem-60.-lebensjahr%29-in-1220-wien-1340139211/)                                                                                                                    | Dec 02, 08:25      |
|       753.02 |            40 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/2-zimmer-wohnung-mit-balkon-n%C3%A4he-u-bahn-ab-j%C3%A4nner-verf%C3%BCgbar%21-1636009287/)                                                                                                              | Dec 02, 06:56      |
|       645    |            67 |          3 | 19. Döbling              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1190-d%C3%B6bling/helle-und-ruhige-3-zimmer-wiener-wohnen-gemeindewohnung-%28direktvergabe%29-s%C3%BCdseitiger-balkon-und-eine-sch%C3%B6ne-aussicht-%28vormerkschein/-wohnticket-bis-inkl.-31.10.2024%29-1101475972/) | Dec 01, 20:11      |
|       659    |            40 |          2 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/%2Aneues-projekt%2A-urbanes-wohnen-im-wildgarten-ab-01.02.2025-981871639/)                                                                                                                              | Dec 01, 19:32      |
|       650    |            38 |          2 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/1220-wien---s%C3%BC%C3%9Fenbrunner-str.-11---provisionfrei---neubau---ab-1.-dezember-1353931234/)                                                                                                     | Dec 01, 19:29      |
|       780    |            77 |          2 | 20. Brigittenau          | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1200-brigittenau/2--zimmerwohnung-nur-mit-wohnticket-1500%E2%82%AC-abl%C3%B6se-2069896053/)                                                                                                                           | Dec 01, 18:26      |
|       650    |            83 |          3 | 12. Meidling             | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/nur-zimmer-zu-vermieten-generalsanierte-neubau-all-inclusive-wg-zimmer-/-provisionsfrei-1621439857/)                                                                                                    | Dec 01, 17:24      |
|       748    |            48 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/sch%C3%B6ne-2-zimmer-wohnung-1701311299/)                                                                                                                                                              | Dec 01, 17:23      |
|       479    |            45 |          2 | 03. Landstraße           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1030-landstra%C3%9Fe/gemeindewohnung-zur-direktvergabe-nur-mit-wohnticket-bis-30.06.2024-1235327178/)                                                                                                                 | Dec 01, 16:55      |
|       658    |            62 |          3 | 22. Donaustadt           | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1220-donaustadt/gemeinde-wohnung-direkt-vergabe-kaiserm%C3%BChlen-neben-u1-833386502/)                                                                                                                                | Dec 01, 16:07      |
|       611    |            47 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/helle-2-zimmer-wohnung-in-1070-wien-nachmieter-gesucht%21-924079937/)                                                                                                                                     | Dec 01, 14:32      |
|       598    |            58 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/gemeindewohnung-2-zimmer-1110-wien-1124888707/)                                                                                                                                                        | Dec 01, 11:37      |
|       749.71 |            42 |          2 | 11. Simmering            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1110-simmering/ina---p%C3%A4rchenwohnung-mit-freifl%C3%A4che-n%C3%A4he-wasserspielplatz-leberberg-1904606435/)                                                                                                        | Dec 01, 10:24      |
