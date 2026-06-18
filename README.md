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

|   💰 Rent (€) |   📏 Size (m²) |   🛏️ Rooms | 🏙️ District              | Link                                                                                                                                                                                                        | 📅 Published Date   |
|-------------:|--------------:|-----------:|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|       648.56 |            78 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/gro%C3%9Fz%C3%BCgige-2-zimmer-altbauwohnung-mit-78-m%C2%B2---n%C3%A4he-u1-keplerplatz-1778570131/)                     | Jun 18, 14:05      |
|       775    |            33 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/modernes-single-apartment-mit-terrasse---erstbezug-1965841874/)                                                        | Jun 18, 13:48      |
|       730    |            56 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/jagdgasse:-gepflegte-helle-2-zimmerwohnung---gute-infrastruktur-und-verkehrsanbindung-1636511241/)                     | Jun 18, 12:09      |
|       776.54 |            53 |          2 | 15. Rudolfsheim-Fünfhaus | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1150-rudolfsheim-f%C3%BCnfhaus/generalsanierte-2-zimmer-wohnung-%28unbefristet%29-n%C3%A4he-u4-meidling-hauptstra%C3%9Fe-1343321989/) | Jun 18, 09:49      |
|       634.34 |            40 |          2 | 10. Favoriten            | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1100-favoriten/ideale-2-zimmer-neubauwohnung---zwischen-quellenstra%C3%9Fe-und-gudrunstra%C3%9Fe-1970495564/)                         | Jun 18, 08:28      |
|       450    |            42 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/unbefristete-altbauwohnung-in-der-fenzlgasse-841244967/)                                                                 | Jun 18, 07:15      |
|       570    |            54 |          2 | 14. Penzing              | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1140-penzing/gemeinde-wohnung-1726125471/)                                                                                            | Jun 17, 18:53      |
|       698    |            41 |          2 | 07. Neubau               | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1070-neubau/vermiete-nette-freundliche-altbauwohnung-mit-hof--und-gartenmitbenutzung-in-der-westbahnstra%C3%9Fe-44-1183326995/)       | Jun 17, 18:38      |
|       750    |            42 |          2 | 02. Leopoldstadt         | [🔗](https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/wien-1020-leopoldstadt/privat:-2-zi.-bei-praterstern&volkertmarkt-innenhof-sehr-ruhig-english-speaker-578274601/)                          | Jun 17, 15:45      |
