# ST4-SFJO24
Problématique :

L’e-réputation du premier ministre anglais Boris Jonhson :
Comment le retour autour du scandale du "partygate" affecte les avis de internautes vis-à-vis de Boris Johnson sur Twitter ?

Cadre : ST4 DATA WEB

Groupe 4 :
- NADALIN Marius
- GARRIGUE Clément
- DE LABOULAYE Bertrand
- KACHA Lotfi
- FRATTAROLI Martin

# Objectif :

Quantifier, interpréter et visualiser l'impact du scandale du "partygate" sur l'e-réputation de Boris Jonhson.

Il s'agira de réaliser un scraping de données sur Twitter, d'analyser les sentiments (positif, négatif ou neutre) dans les tweets avant et après le vote de confiance au Royaume-Uni.

Outils Principaux :
- Python
- API.2 de Twitter ( scraping )
- Base de donnée SQLite ( stockage des tweets )
- Scikit-Learn ( apprentissage et mise en place d'un classifieur : arbre de décision )
- Seaborn ( dataviz )

# Utilisation :

0 ) Création de la base de donnée SQL et entrainement de l'arbre de décision :

Lancer le programme .\SQL_DB\sql_create.py

Depuis le programme tree_classifier.py :
regenerate_classifier(csv_path = '.\csv\db_apprentissage.csv',filename = 'tree_classifier.sav')

1 ) Scrapping et remplissage de la base de donnée SQL:

Depuis le programme scraper.py :
scrapping("Boris Johnson")

2 ) Scoring via le classifieur arbre de décision :

Depuis le programme scoring.py :
score_database()

3 ) Scoring via Sentiwordnet :

Implémentation sur un Collab, non présent sur ce git

4 ) Visualisation des données :

Depuis le programme dataviz.py :

db = STDB.db_to_dataframe()
db_senti = STDB.db_to_dataframe_sentiwordnet()

chart_bar_count(db)
chart_bar_percent(db)
chart_pie(db)

chart_bar_count_senti(db_senti)
chart_bar_percent_senti(db_senti)
chart_pie_senti(db_senti)