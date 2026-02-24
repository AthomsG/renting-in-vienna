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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District   | Link                                                                                                                                                                                                                  | 📅 Published Date   |
|-------------:|--------------:|-----------:|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       538    |            50 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/wohnung-gemeinde-2008342070/)                                                                                                     | Feb 24, 19:37      |
|       557.04 |            48 |          2 | 17. Hernals   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1170-hernals/pezzlgasse/rosensteingasse/postsportverein:-ruhige-erdgescho%C3%9Fwohnung-mit-innenhofmitbenutzung-1345053628/)                    | Feb 24, 18:55      |
|       780    |            42 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/privatvermietung-g-am-haydnpark---helle-zimmer-neubau-lift-1339898870/)                                                           | Feb 24, 16:19      |
|       556.27 |            53 |          2 | 14. Penzing   | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/%22direktvergabe%22---2-zimmer-gemeindewohnung-%2853m2%29-in-randlage-im-hugo-breitner-hof-1140-wien-1799230342/)                  | Feb 24, 16:11      |
|       787.86 |            60 |          3 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/unbefristete-altbauwohnung-der-fernkorngasse-1576437102/)                                                                        | Feb 24, 15:20      |
|       573.7  |            55 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/2-zimmer-gemeindewohnung-am-wienerberg%21-vormerkschein-bis-31.12.2025-1159323993/)                                              | Feb 24, 14:11      |
|       796.37 |            43 |          2 | 12. Meidling  | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1120-meidling/attraktive-2-zimmer-wohnung---u-bahn-fu%C3%9Fl%C3%A4ufig-erreichbar%21-2041565188/)                                               | Feb 24, 11:53      |
|       659    |            48 |          2 | 16. Ottakring | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1160-ottakring/provisionsfrei-&-unbefristet%21-wohnung-in-ruhiger-lage-1698701761/)                                                             | Feb 24, 10:28      |
|       749    |            51 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/s%C3%BCdlich-ausgerichtete-2---zimmer-wohnung-inkl.-neuer-einbauk%C3%BCche-mit-optimaler-infrastruktur-933175927/)               | Feb 24, 09:28      |
|       558.82 |            57 |          2 | 10. Favoriten | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gemeindewohnung-1100-wien-57m%C2%B2-direktvergabe-mit-abl%C3%B6se-f%C3%BCr-vormerkschein-bis-31.01.2026-2-r%C3%A4ume-801237623/) | Feb 24, 09:26      |
