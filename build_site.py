import json, html, os, shutil
E=html.escape
OUT='/workspace/observatoire'
CDC="https://www.ccomptes.fr/sites/default/files/2025-09/20250923-S2025-1126-1-France-Televisions.pdf"
CDCO="Cour des comptes, « France Télévisions, exercices 2017-2024 » (S2025-1126-1), publié le 23/09/2025"
A3="https://audiovisuel-public.com/le-rapport/chapitre/axe-iii-masse-salariale/"
A2="https://audiovisuel-public.com/le-rapport/chapitre/axe-ii-conflits-interets/"
RAP="Commission d'enquête sur l'audiovisuel public, rapport de M. Charles Alloncle, 05/05/2026 (miroir citoyen non officiel, pages PDF ; texte officiel : https://www.assemblee-nationale.fr/dyn/17/rapports/ceaudio/l17b2698-t1_rapport-enquete)"
FTV="https://static.francetelevisions.fr/inline-images/20260513%20R%C3%A9ponse%20FTV%20Rapport%20CE%20v2.pdf"
FTVO="France Télévisions, Réponse au rapport de la commission d'enquête, 13/05/2026"
def S(o,d,p,u): return {"organisme":o,"document":d,"page":p,"url":u}
F=[]
F.append(dict(id="cse-14-2m", titre="Comités sociaux : 14,2 M€ de subventions en 2024 (dont piscine de 1 M€ au domaine de Lalinde)",
 montant="14,2 M€ (2024) ; 13,6 M€ (2019)", date="2025-09-23", tags=["CSE-avantages"], statut="Confirmé",
 source=S("Cour des comptes",CDCO,"p. 104 (page PDF)",CDC),
 faits=["La Cour écrit : « de 13,6 M€ en 2019, elle s'élève à 14,2 M€ en 2024, couvrant notamment l'activité de restauration. »",
  "Le même passage décrit un « château de Lalinde doté d'un parc de 115 hectares et d'une piscine qui a coûté 1 M€ ».",
  "63 % du financement des activités sociales et culturelles va au comité interentreprises (ex CI-ORTF) (même page)."],
 reponse_ftv="Réponse de FTV du 13/05/2026 : aucun passage sur le CSE retrouvé par recherche de mots-clés (CSE, ASC, comité d'entreprise). À compléter.",
 reserves=["Le montant est une charge récurrente fixée par accord et par assiette de calcul (la Cour parle de « constance des taux »), pas une dérive ponctuelle.","Le 1 M€ de la piscine est un coût passé (année non précisée dans l'extrait lu)."]))
F.append(dict(id="salaire-moyen", titre="Salaire moyen par tête à France Télévisions : 73 690 € en 2024",
 montant="73 690 € brut (2024) ; 71 490 € (2023)", date="2025-09-23", tags=["salaires"], statut="Nuancé",
 source=S("Cour des comptes",CDCO,"p. 98 (page PDF), tableau n° 38",CDC),
 faits=["Le SMPT (salaire moyen brut comptable par tête) passe de 68 580 € (2021) à 73 690 € (2024).","Comparaison de la Cour : culture 48 900 €, audiovisuel 66 700 €."],
 reponse_ftv="FTV (13/05/2026) : le SMPT « intègre les éléments variables » (heures supplémentaires, nuit, indexation outre-mer, indemnités de départ) ; « Il ne s'agit donc en aucun cas d'un salaire contractuel moyen », qui est de « 61k€ annuels brut ». Ancienneté moyenne : 20,6 ans.",
 reserves=["Le SMPT inclut des éléments non récurrents : ne pas le lire comme un salaire contractuel.","Les deux chiffres (73 690 € et 61 k€) sont sourcés mais ne mesurent pas la même chose."]))
F.append(dict(id="frais-mission-46m", titre="Frais de mission : 46 M€ en 2024 (année des JO)",
 montant="46 M€ (2024) ; 42,8 M€ en moyenne annuelle hors covid", date="2025-09-23", tags=["gouvernance"], statut="Confirmé",
 source=S("Cour des comptes",CDCO,"p. 75 (page PDF), §3.2.1.2.4",CDC),
 faits=["« Parmi les charges d'exploitation figurent les frais de mission (compte 625) […] pesant pour plus de 42,8 M€ en moyenne annuelle hors période de covid, avec un maximum de 46 M€ atteint en 2024, année des Jeux olympiques et paralympiques. »","Réponse commune Bercy/Comptes publics (04/09/2025) : « les frais de mission, dont le montant avait déjà été souligné par la Cour en 2016, ont continué de croître » (https://www.ccomptes.fr/sites/default/files/2025-09/20250923-S2025-1126-1-France-Televisions-rep-commune-MEFSIN-MCP.pdf)."],
 reponse_ftv="Réponse spécifique de FTV sur les frais de mission : non retrouvée dans le document du 13/05/2026.",
 reserves=["Le pic 2024 est lié aux JO (couverture sportive) : la Cour le dit elle-même."]))
F.append(dict(id="indemnites-depart-232m", titre="Indemnités de départ : 232 M€ cumulés de 2015 à 2025",
 montant="232 M€ (2015-2025) ; 22,5 M€ en 2025 ; 143 M€ pour les indemnités > 100 000 € (2017-2025)", date="2026-05-05", tags=["salaires","gouvernance"], statut="Confirmé (données FTV)",
 source=S("Assemblée nationale – commission d'enquête",RAP,"p. 389 (PDF)",A3),
 faits=["Le rapport (tableau fourni par FTV) : « le total annuel a oscillé entre 14,8 millions d'euros en 2020 et 29,4 millions d'euros en 2015, pour s'établir à 22,5 millions d'euros en 2025, soit un cumul égal à 232 millions d'euros sur la période. »","« Le montant des indemnités supérieurs 100 000 euros s'élève à 143 M€ entre 2017 et 2025, soit 62 % du montant total » ; FTV évalue à 141 le nombre d'indemnités supérieures à 100 000 € depuis 2015.","FTV rattache ces montants à « l'accord d'entreprise de 2013 en lien avec un critère d'ancienneté »."],
 reponse_ftv="FTV (13/05/2026, rec. 60) : peut transmettre la ventilation au CGEFI et au Parlement. Dans ses réponses sur les résultats, FTV rattache les coûts de départs à la rupture conventionnelle collective 2018-2023 menée « avec l'accord de l'Etat » (opération qualifiée de non récurrente).",
 reserves=["Les 232 M€ incluent des indemnités légales, conventionnelles et transactionnelles (départs en retraite compris) : tout n'est pas « parachute ».","Aucune indemnité individuelle supérieure à 500 000 € n'a été retrouvée dans le rapport (voir page non vérifié)."]))
F.append(dict(id="hauts-salaires-31", titre="31 salariés gagnent plus que le chef de l'État (rémunération « super brute »)",
 montant="10,813 M€ bruts/an pour 31 salariés (vs 8,525 M€ au tarif du président, 275 000 € × 31)", date="2026-05-05", tags=["salaires"], statut="Nuancé",
 source=S("Assemblée nationale – commission d'enquête",RAP,"chapitre Axe III, pp. 380-407 (PDF)",A3),
 faits=["« France Télévisions ayant fourni à votre rapporteur, à sa demande, la liste des 10 % des salaires bruts les plus élevés de l'entreprise, votre rapporteur y a compté 31 salariés gagnant plus que le chef de l'État » (dont 17 directeurs au siège parisien, selon le rapport).","« La somme de la rémunération « super brute » de ces 31 salariés atteint 10,813 millions d'euros bruts par an, contre 8,525 millions d'euros si l'on multiplie par 31 la rémunération annuelle super brute du Président de la République (275 000 euros). »"],
 reponse_ftv="FTV (13/05/2026) : les salaires > 100 k€ font l'objet d'avis du contrôleur d'État ; la liste des 10 plus hauts salaires est transmise chaque année au Parlement. Sur la citation de Mme Ernotte (« quelques figures d'antenne et directeurs ultramarins »), FTV précise qu'elle ne portait que sur les 10 plus hauts salaires, pas sur les 31, et que le rapport l'a tronquée.",
 reserves=["Ordre de grandeur de l'écart : 2,3 M€ par an (10,813 − 8,525), pour 31 personnes.","L'indexation outre-mer et les cachets d'antenne figurent dans l'assiette."]))
F.append(dict(id="cannes-majestic", titre="Festival de Cannes : ≈ 6 M€/an et suites au Majestic à 1 899 € la nuit (2024)",
 montant="≈ 6 M€/an (rapport) ; 3,2 M€ net en 2025 (FTV) ; 1 899 €/nuit (2024)", date="2026-05-05", tags=["gouvernance","conflits d'intérêts"], statut="Nuancé",
 source=S("Assemblée nationale – commission d'enquête",RAP,"pp. 393-394 (PDF)",A3),
 faits=["Rapport : « La présence de France Télévisions au Festival de Cannes représente une dépense annuelle de l'ordre de 6 millions d'euros, en progression de 15 % sur les trois dernières années ».","Rapport : « en 2024, les nuitées réservées pour la présidente et le directeur général délégué au Majestic ont ainsi été facturées 1 899 euros par nuit ».","Une information judiciaire (abus de biens sociaux, recel, détournement de biens publics) est ouverte à Paris sur l'édition 2023 (20 Minutes/AFP, 11/02/2026 : https://www.20minutes.fr/arts-stars/medias/4200976-20260211-somme-extravagante-juge-interesse-frais-hotel-dirigeants-france-televisions-cannes). Facture 2023 : 112 123 € TTC, chambres à 1 599 € et 1 199 € (Liberta Press, 13/03/2026, source secondaire)."],
 reponse_ftv="FTV (via La Lettre / audition n° 12) : hébergement obtenu par « barter » via un intermédiaire, sans argent public ; Mme Sitbon-Gomez : « À ma connaissance, pas un euro d'argent public n'a été dépensé pour ces frais d'hôtel à Cannes. » Selon FTV (AFP, 11-12/02/2026), le barter est une « pratique courante, légale et utilisée par tous les médias ». Coût net Cannes 2025 : 3,2 M€, en baisse de 700 k€ sur 2024 (FTV).",
 reserves=["Présomption d'innocence : l'information judiciaire n'est pas une condamnation.","Le « 1 700 €/nuit » souvent cité est le chiffre de 2023 (Marianne) ; le rapport donne 1 899 € pour 2024.","L'absence de décaissement (barter) est une affirmation de FTV non contredite par un document primaire lu ici ; le rapport relève que le barter n'est utilisé que « depuis 2022 »."]))
F.append(dict(id="nopl-250m", titre="« N'oubliez pas les paroles » : environ 250 M€ versés sur dix ans (2015-2025)",
 montant="≈ 250 M€ sur 2015-2025 (≈ 25 M€/an)", date="2026-05-05", tags=["production privée","conflits d'intérêts"], statut="Nuancé",
 source=S("Assemblée nationale – commission d'enquête",RAP,"p. 407 (PDF)",A3),
 faits=["Rapport : « Sur dix ans, entre 2015 et 2025, France Télévisions aura ainsi versé environ 250 millions d'euros pour cette seule émission. »","Contrat : 75 M€ sur trois ans reconductible ; hausse de 20 % du coût unitaire par minute entre 2024-2025 et 2026-2027 alors que l'audience recule de 5 % sur deux ans et 10 % sur cinq ans (rapport p. 407).","Marge de l'émission : 25 % (rapport, Axe III) ; contrats pluriannuels renouvelés en 2021 et 2024 « sans qu'il y ait eu le moindre appel d'offres » (question d'A. Alloncle, audition n° 57, 01/04/2026)."],
 reponse_ftv="FTV (13/05/2026) : « N'oubliez pas les paroles génère des recettes publicitaires significatives et sa diffusion est rentable », « sans peser sur les concours publics ». Productrice (Capital, 2026) : l'émission « génère environ 10% des recettes publicitaires de France Télévisions ».",
 reserves=["Le montant est un coût de production brut : les recettes publicitaires ne sont pas déduites dans le rapport.","« Sans appel d'offres » est la conséquence d'un régime d'exclusion légal (voir fiche marchés publics), pas une irrégularité établie."]))
F.append(dict(id="mediawan-44-111", titre="Mediawan : 44 M€ (2018) → 111 M€ (2024) de chiffre d'affaires avec France Télévisions",
 montant="111 M€ (2024) ; +152 % depuis 2018", date="2026-05-13", tags=["production privée","conflits d'intérêts"], statut="Confirmé (chiffres FTV) / Nuancé (interprétation)",
 source=S("France Télévisions",FTVO,"p. 75 (PDF)",FTV),
 faits=["FTV : « entre 2018 et 2024, le chiffre d'affaires réalisé avec France Télévisions est passé de 44 M€ à 111 M€, soit une augmentation de 152 %, tandis que le nombre de sociétés du groupe contractant avec France Télévisions est passé de 13 à 28 ».","Banijay : 36 M€ → 87 M€ (3 → 14 sociétés).","Rapport Alloncle : marges observées supérieures aux marges des devis (« Ça commence aujourd'hui » 24 %, « N'oubliez pas les paroles » 25 %, « Chacun son Tour » 42 %) (Axe III, p. 403)."],
 reponse_ftv="FTV : Mediawan et Banijay représentent « respectivement 11,6% et 11,4% du chiffre d'affaires réalisé par l'ensemble du secteur de la production avec France Télévisions », ce qui « n'est pas le fruit d'une décision délibérée de l'entreprise » ; les 29 sociétés Mediawan et 17 sociétés Banijay travaillaient « pour la plupart » déjà avec FTV avant leur rachat.",
 reserves=["Comparaison 2018/2024 à périmètre non constant (13 → 28 sociétés du groupe).","Les surfacturations reposent sur « les rares audits » consultés par le rapporteur : échantillon non quantifié."]))
F.append(dict(id="salto-57-7m", titre="Salto : un échec à 57,7 M€ (France Télévisions, TF1, M6)",
 montant="57,7 M€", date="2026-05-05", tags=["gouvernance"], statut="Nuancé",
 source=S("Assemblée nationale – commission d'enquête",RAP,"Axe III, encadré « La plateforme Salto : un échec commercial et stratégique à 57,7 millions d'euros » (pp. 380-407)",A3),
 faits=["Intertitre du rapport : « La plateforme Salto : un échec commercial et stratégique à 57,7 millions d'euros ». Salto, lancée conjointement par FTV, TF1 et M6 en octobre 2020, a été arrêtée le 27/03/2023."],
 reponse_ftv="FTV (13/05/2026) : l'arrêt de Salto est une opération « non récurrente » ; l'issue « était liée à une conjonction de facteurs exogènes » (refus par l'Autorité de la concurrence de la fusion TF1/M6, retrait de TF1 puis de M6) ; FTV dit avoir négocié « une sortie intéressante d'un point de vue financier ».",
 reserves=["Le montant de 57,7 M€ n'a pas été recoupé avec les comptes FTV dans cette version (V1).","Salto était un projet commun à trois groupes : la part supportée par FTV n'est pas isolée dans l'extrait lu."]))
F.append(dict(id="marches-publics-exclusion", titre="Marchés publics et audiovisuel public : les achats de programmes ne sont pas soumis à la mise en concurrence de droit commun",
 montant="864 M€ d'achats de programmes externes (2024, rapport p. 264)", date="2026-05-13", tags=["gouvernance","production privée"], statut="Nuancé",
 source=S("Code de la commande publique (reproduction non officielle ; le texte Légifrance de L2513-1 n'a pas pu être ouvert)","Article L2513-1 (créé par ordonnance n° 2018-1074 du 26/11/2018, en vigueur depuis le 01/04/2019) ; directive 2014/24/UE art. 10 b et considérant 23","—","https://www.code-commande-publique.com/exclusions-autres-marches/marches-publics-conclus-par-un-pouvoir-adjudicateur-exclusions/"),
 faits=["Correction : le fondement est l'art. L2513-1 du code de la commande publique (et non L2512-5) ; le « code des marchés publics » est abrogé.","Texte (L2513-1, lu sur une reproduction non officielle) : « Sont soumis aux règles définies au titre II les marchés publics de services conclus par un pouvoir adjudicateur qui : […] 2° Soit ont pour objet l'achat, le développement, la production ou la coproduction de programmes destinés à la diffusion et qui sont attribués par des éditeurs de services de communication audiovisuelle ou radiophonique. »","Ce n'est pas une exception « œuvre artistique » : c'est l'exclusion des marchés de programmes des éditeurs de médias (directive 2014/24/UE, considérant 23 : « considérations revêtant une importance culturelle et sociale »).","Rapport Alloncle p. 267 : « il ne paraît pas pertinent d'exclure les contrats d'achats de programmes des règles de droit commun pour ce qui concerne la procédure de passation du marché (publicité, mise en concurrence préalable) » ; recommandation n° 21.","Rapport p. 266 : les achats de programmes sont exclus « du fait de l'importance, dans les choix, des critères artistiques et éditoriaux qui laisse une large marge d'appréciation au décideur » (Cour des comptes, octobre 2016, p. 94, cité)."],
 reponse_ftv="FTV (13/05/2026, rec. 21) : l'inclusion dans la commande publique « serait un non-sens, porterait une atteinte majeure à la liberté éditoriale […] et contreviendrait au droit de l'Union européenne » ; « Cette spécificité ne signifie pas absence de concurrence » (appels à projets, appels à concepts) ; plateforme de dépôt des projets annoncée.",
 reserves=["Le contenu des articles L2521-1 à L2521-5 (règles du Titre II) n'a pas été lu : ne pas écrire que ces marchés échappent à toute règle.","Les pages du rapport sont celles du miroir citoyen (FTV cite « p. 273 » pour un passage que le miroir place p. 267).","FTV affirme que « contreviendrait au droit de l'Union européenne » : la directive 2014/24 (art. 10 b) autorise l'exclusion sans l'imposer.","Contrats de « C dans l'air », « C à vous », « Envoyé spécial » (durée, reconduction) : non vérifiés. Détail dans data/fiche_marches_publics.json."],
 detail="fiche_marches_publics.json"))
F.append(dict(id="sm-appel-2024", titre="Syndicat de la magistrature : appel à « se mobiliser contre l'accession au pouvoir de l'extrême droite » (11/06/2024)",
 montant="non chiffré", date="2024-06-11", tags=["Syndicats de fonctionnaires et prises de position politiques","Pluralisme et impartialité des institutions"], statut="Confirmé (texte) / Nuancé (interprétation)",
 source=S("Syndicat de la magistrature","Communiqué du 11/06/2024","1 page","https://www.syndicat-magistrature.fr/documents/173/cp-dissolution-11-juin-2024.pdf"),
 faits=["« Le Syndicat de la magistrature appelle l'ensemble des magistrates et magistrats […] à se mobiliser contre l'accession au pouvoir de l'extrême droite. »","Le texte ne contient pas « faire barrage » et ne cite pas explicitement les législatives.","Élections à la commission d'avancement 2026 (ministère de la Justice, 13/02/2026) : USM 60,99 %, SM 25,03 %, UM 12,51 %."],
 reponse_ftv="Réponse du SM : non retrouvée. Cadre : avis du CSM du 13/12/2023, ordonnance 58-1270 art. 10 et 10-1.",
 reserves=["Fiche sans montant d'argent public : elle relève de la rubrique « Institutions financées sur fonds publics hors de leur rôle neutre ».","Aucune saisine du CSM ni procédure disciplinaire retrouvée.","Détail complet : data/fiche_sm.json."],
 detail="fiche_sm.json"))
F.append(dict(id="le-grand-ecart", titre="Le grand écart : dérives documentées à l'échelle de la dette, du déficit et de l'effort d'économies",
 montant="non chiffré (mise à l'échelle)", date="2026-10-25", tags=["gouvernance","Privatisation des gains / socialisation des pertes"], statut="Nuancé",
 source=S("Insee","Informations rapides n° 239 (29/09/2026) et n° 78 (27/03/2026)","—","https://www.insee.fr/fr/statistiques/9053525"),
 faits=["Dette publique fin T2 2026 : 3 595,5 Md€ = 119,0 % du PIB (Insee, 29/09/2026).","Déficit 2025 : 152,5 Md€ = 5,1 % du PIB (Insee, 27/03/2026).","PLF 2027 : effort de 54 Md€ dont 43 Md€ dans les textes financiers (dossier de presse, octobre 2026).","14,2 M€ de CSE = 0,0093 % du déficit 2025 ; 111 M€ Mediawan = 0,073 % ; 46 M€ de frais de mission = 0,030 %."],
 reponse_ftv="FTV conteste la comparabilité de ces lignes (obligations conventionnelles, droit du travail, production). Voir grand-ecart.html.",
 reserves=["Les montants ne s'additionnent pas (natures et périmètres différents).","Les citations « la France est ruinée » / « plus d'argent » n'ont pas de source datée retrouvée : non vérifié."],
 detail="fiche_grand_ecart.json"))
# livres
F.append(dict(id="livre-alloncle", titre="Livre : Charles Alloncle, « Je jure de dire toute la vérité » (Fayard, 30/09/2026)",
 montant="non chiffré", date="2026-09-30", tags=["livres","gouvernance","production privée"], statut="Nuancé",
 source=S("Éditions Fayard","Fiche livre : 320 p., EAN 9782213736440, 20,90 € (papier), 14,99 € (numérique, EAN 9782213737225)","—","https://www.fayard.fr/livre/je-jure-de-dire-toute-la-verite-9782213736440/"),
 faits=["Date corrigée : le livre est paru le 30/09/2026 (et non 2025). Récit des coulisses de la commission d'enquête, classé « Documents, témoignages ».","Texte de présentation (Fayard) : « J'avais été nommé pour contrôler un service public ; j'avais fini par réveiller tout un système que mes questions dérangeaient. »","Télérama (03/10/2026) : le livre « ne recélait aucune véritable révélation ». L'Obs (02/10/2026) : il vise surtout J. Patrier-Leitus et X. Niel (article tronqué, abonnés).","Passages cités par la presse partisane (Médias-Presse.info) : accusation de parjure contre D. Ernotte (cabinet externe de « briefing »), signalements art. 40 annoncés (CNews, 30/09/2026)."],
 these_auteur="Un « système » de connivence entre dirigeants, producteurs et institutions protège les dépenses de l'audiovisuel public ; le rapport aurait failli être enterré (adopté à une voix près, selon l'auteur).",
 reponse_ftv="FTV/Radio France : aucune réponse au livre retrouvée. L'auteur dénonce un « boycott » (message X du 12/10/2026, CNews/Le Figaro TV Magazine).",
 reserves=["Le texte du livre n'a pas été lu : seules des recensions et extraits de presse l'ont été.","Contrôle des affirmations du message X du 12/10/2026 : voir la page Livres."]))
F.append(dict(id="livre-knafo", titre="Livre : Sarah Knafo, « Le Casse du siècle » (Fayard, 02/09/2026)",
 montant="non chiffré (thèse : 940 500 € prélevés sur une carrière)", date="2026-09-02", tags=["livres","Privatisation des gains / socialisation des pertes"], statut="Nuancé",
 source=S("Éditions Fayard","Fiche livre : 286 p., EAN 9782213733135, 19,90 €","—","https://www.fayard.fr/livre/le-casse-du-siecle-9782213733135/"),
 faits=["Date : 02/09/2026 (JDD, Le Parisien/AFP) ; 63 087 exemplaires vendus selon l'éditeur à la date du 06/09 (Le Parisien/AFP, 08/09/2026).","Preuves publiées par l'autrice : https://sarahknafo.fr/preuves (109 « preuves » numérotées). Page 24 du livre (preuves) : 22 000 × 42,75 = 940 500 € (écart de 1 843 €/mois entre coût employeur 3 922 € et net 2 079 €).","franceinfo « Vrai ou faux » (08/09/2026) a examiné les principaux chiffres du livre ; la fiche de paie est celle d'un salarié fictif (« Nicolas Durand »)."],
 these_auteur="L'État organise un « casse légal » ; 130 Md€ d'économies annuelles ; privatisation de l'audiovisuel public ; suppression de l'Arcom.",
 reponse_ftv="Sans objet (franceinfo, qui vérifie le livre, appartient au groupe France Télévisions : conflit d'intérêts à signaler).",
 reserves=["Le chiffre de 63 000 exemplaires est une déclaration de l'éditeur ; GfK 208 000 au 27/09 (source secondaire) et Edistat 265 714 en six semaines (ActuaLitté) sont des mesures ultérieures.","Pages du livre non vérifiées (le texte intégral n'a pas été lu)."]))
F.append(dict(id="livre-marleix", titre="Livres : Olivier Marleix, « Les Liquidateurs » (2021) et « Dissolution française » (2025)",
 montant="non chiffré", date="2021-02-04", tags=["livres","Privatisation des gains / socialisation des pertes","conflits d'intérêts"], statut="Nuancé",
 source=S("Assemblée nationale","Rapport n° 897 rectifié de la commission d'enquête sur la politique industrielle (Alstom), 19/04/2018, avant-propos du président O. Marleix","avant-propos","https://www.assemblee-nationale.fr/15/pdf/rap-enq/r0897-tI.pdf"),
 faits=["Orthographe : Marleix. « Les Liquidateurs », Robert Laffont, 04/02/2021, 252 p., EAN 9782221251874. « Dissolution française », Robert Laffont, 13/11/2025, 288 p., EAN 9782221283783, préface de Michel Barnier.","Recoupement avec le rapport officiel (fiche Alstom) : la formule « cécité, imprévision et entre soi » et le chiffre de 299 000 € (étude AT Kearney) figurent dans l'avant-propos signé par O. Marleix, président ; l'amende américaine : « près d'1 milliard $ (finalement prononcée à 772 millions $) » ; offre de GE : 12,35 Md€.","Le rapporteur G. Kasbarian conclut différemment dans la partie rapporteur : « L'État a donc joué son rôle en utilisant les leviers à sa disposition »."],
 these_auteur="Une élite aurait « liquidé » des fleurons industriels (quatrième de couverture de l'éditeur) ; un « pacte de corruption » (saisine du PNF selon Breizh-info, source secondaire).",
 reponse_ftv="Sans objet.",
 reserves=["Le prix de cession effectif d'Alstom Énergie et les décisions de justice postérieures à 2018 n'ont pas été recoupés.","Extraits de « Dissolution française » lus uniquement sur un blog : non vérifiés. Texte des livres non lu."]))
F.append(dict(id="livre-jovanovic-2008", titre="Livre : Pierre Jovanovic, « 2008 » (Le Jardin des Livres, 13/06/2025)",
 montant="non chiffré", date="2025-06-13", tags=["livres","Privatisation des gains / socialisation des pertes"], statut="Nuancé",
 source=S("Librairie Gallimard Paris (référencement éditeur)","Fiche livre : « 2008 », Le Jardin des Livres, 13/06/2025, ISBN 9782914569873","—","https://www.librairie-gallimard.com/livre/9782914569873-2008-pierre-jovanovic/"),
 faits=["Titre, éditeur, date : confirmés (libraires Gallimard et Goulard).","Quatrième de couverture : « Les gouvernements n'ont pas eu le choix : ils ont volé l'argent des impôts, l'argent du peuple, pour sauver les banques. »","Recoupement avec les chiffres officiels : plan de soutien aux banques 2008-2009 (19,75 Md€ de fonds propres, 77 Md€ de prêts garantis) : bilan de +2,7 Md€ pour l'État selon le ministère (05/07/2011) ; en revanche Dexia : coût direct de 6,6 Md€ pour les finances publiques françaises (Cour des comptes, 2013). Voir les fiches « banques-2008-2009-bilan » et « dexia-cour-6-6-md ».","Autres titres : « Notre-Dame de l'Apocalypse » (03/10/2008, ISBN 9782914569996) et « 777 » (2009, ISBN 9782914569880) ne portent pas sur l'argent public français."],
 these_auteur="Les gouvernements auraient été contraints par un « chantage » des banques de les sauver avec l'argent des contribuables ; les pertes auraient été socialisées et les profits restés privés (présentation de l'éditeur/librairies).",
 reponse_ftv="Sans objet.",
 reserves=["Pour la France, les chiffres officiels ne confirment pas une perte nette pour l'État sur le plan SFEF/SPPE (bilan positif selon le ministère), mais confirment un coût public sur Dexia ; la thèse est donc partiellement étayée, selon le cas.","Les sauvetages à l'étranger (États-Unis, etc.) n'ont pas été examinés ; le texte du livre n'a pas été lu, donc les chiffres propres au livre ne sont pas vérifiés."]))
exec(open('/workspace/pass2_fiches.py',encoding='utf8').read())
exec(open('/workspace/camps.py',encoding='utf8').read())
for f in F:
    f['camp'],f['camp_pourquoi'],f['camp_resume']=CAMPS[f['id']]
json.dump(F,open(OUT+'/data/fiches.json','w'),ensure_ascii=False,indent=1)
for f in os.listdir('/workspace/observatoire-ajouts'):
    if f.endswith('.json'): shutil.copy('/workspace/observatoire-ajouts/'+f,OUT+'/data/'+f)
TAGS=["salaires","CSE-avantages","production privée","conflits d'intérêts","pluralisme","gouvernance","Syndicats de fonctionnaires et prises de position politiques","Privatisation des gains / socialisation des pertes","Pluralisme et impartialité des institutions","Institutions financées sur fonds publics hors de leur rôle neutre","cabinets de conseil","aides aux entreprises","fraude sociale","associations","opérateurs et agences","immobilier","livres"]
def slug(s): return ''.join(c if c.isalnum() else '-' for c in s.lower())[:40]
def stcls(s): return 'ok' if s.startswith('Confirmé') else ('nu' if s.startswith('Nuancé') else 'nv')
NAV_ITEMS=[("index.html","Accueil"),("grand-ecart.html","Le grand écart"),("livres.html","Livres"),("non-verifie.html","Non vérifié"),("methode.html","Méthode")]
def page(title,body,r='',cur=''):
    nav=''.join(f'<a href="{r}{h}"'+(' aria-current="page"' if h==cur else '')+f'>{l}</a>' for h,l in NAV_ITEMS)
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)} – Observatoire de l'argent public</title><meta name="description" content="Observatoire des dépenses et dérives de l'argent public en France : chaque chiffre est sourcé, daté et assorti d'un statut."><link rel="stylesheet" href="{r}style.css"></head><body><a class="skip" href="#main">Aller au contenu</a>
<header class="site"><div class="wrap bar"><a class="brand" href="{r}index.html"><span class="logo" aria-hidden="true">€</span><span><b>Observatoire de l'argent public</b><small>Chaque chiffre : une source, une date, un statut</small></span></a>
<form class="hsearch" role="search" action="{r}index.html" method="get"><label class="sr" for="hq">Rechercher une fiche</label><input id="hq" type="search" name="q" placeholder="Rechercher : mot-clé, montant, source…" autocomplete="off"><button type="submit">Rechercher</button></form>
<input type="checkbox" id="nt" class="navt" aria-label="Menu"><label for="nt" class="burger">☰ Menu</label><nav class="main" aria-label="Navigation principale">{nav}</nav></div></header>
<main id="main" class="wrap">{body}</main>
<footer class="site"><div class="wrap"><p>Version 2 – 25/10/2026. Les réponses des organismes cités sont reproduites lorsqu'elles ont été retrouvées. Une thèse d'auteur n'est pas un fait établi. <a href="{r}methode.html">Méthode</a> · <a href="{r}non-verifie.html">Non vérifié</a></p><p>Dossier local : rien n'est publié ni diffusé.</p></div></footer>
<script src="{r}search.js"></script></body></html>"""
def li(items): return '<ul>'+''.join(f'<li>{E(i)}</li>' for i in items)+'</ul>'
def link(u): return f'<a href="{E(u)}">{E(u)}</a>'
CAMPS_LIST=["macroniste","extrême gauche","droite/LR","RN","transverse"]
def ccls(c): return 'c-'+{'macroniste':'m','extrême gauche':'x','droite/LR':'d','RN':'r','transverse':'t'}[c]
def cbadges(f): return ''.join(f'<span class="camp {ccls(c)}" title="Camp politique (qualification éditoriale)">{E(c)}</span>' for c in f['camp'])
for f in F:
    s=f['source']
    body=f'<p class="crumb"><a href="../index.html">← toutes les fiches</a></p><h1 class="ft">{E(f["titre"])}</h1><p class="meta"><span class="st {stcls(f["statut"])}">{E(f["statut"])}</span> '+''.join(f'<span class="tag">{E(t)}</span>' for t in f['tags'])+' '+cbadges(f)+f'</p><table><tr><th>Montant</th><td>{E(f["montant"])}</td></tr><tr><th>Date de la source</th><td>{E(f["date"])}</td></tr><tr><th>Source</th><td>{E(s["organisme"])} – {E(s["document"])} – {E(s["page"])}<br>{link(s["url"])}</td></tr></table><h3>Faits établis (citations exactes)</h3>{li(f["faits"])}'
    body+='<div class="why"><h3>Pourquoi ce tag</h3><p><b>Camp(s) : '+E(', '.join(f['camp']))+'.</b> '+E(f['camp_resume'])+'.</p>'+li(f['camp_pourquoi'])+'<p class="small">Qualification éditoriale, contestable, fondée sur les faits listés ci-dessus ; elle n\'établit aucune responsabilité personnelle. Critères : <a href="../methode.html#camp">page Méthode</a>.</p></div>'
    if f.get('these_auteur'): body+=f'<h3>Thèse de l\'auteur (non établie comme fait)</h3><p>{E(f["these_auteur"])}</p>'
    body+=f'<h3>Réponse de l\'organisme</h3><p>{E(f["reponse_ftv"])}</p><h3>Réserves</h3>{li(f["reserves"])}'
    if f.get('liens'): body+='<h3>Autres sources lues</h3><ul>'+''.join(f'<li>{link(u)}</li>' for u in f['liens'])+'</ul>'
    if f.get('detail'): body+=f'<p>Détail : <a href="../data/{f["detail"]}">data/{f["detail"]}</a></p>'
    open(f'{OUT}/fiches/{f["id"]}.html','w').write(page(f['titre'],body,'../'))
import unicodedata
def norm(t): return ''.join(ch for ch in unicodedata.normalize('NFD',t.lower()) if unicodedata.category(ch)!='Mn')
def card(f):
    srch=norm(' '.join([f['titre'],f['montant'],f['date'],f['statut'],' '.join(f['tags']),' '.join(f['camp']),'camp politique',f['source']['organisme'],f['source']['document']]))
    return (f'<article class="card" data-tags="{E("|".join(f["tags"]))}" data-camps="{E("|".join(f["camp"]))}" data-s="{E(srch)}"><div class="cmeta"><span class="st {stcls(f["statut"])}">{E(f["statut"])}</span><span class="date">{E(f["date"])}</span></div>'
      f'<div class="camps">{cbadges(f)}</div><h3><a href="fiches/{f["id"]}.html">{E(f["titre"])}</a></h3><p class="amount">{E(f["montant"])}</p><p class="src">Source : {E(f["source"]["organisme"])}</p><div class="tags">'+''.join(f'<span class="tag">{E(t)}</span>' for t in f['tags'])+'</div></article>')
cards=''.join(card(f) for f in F)
cbtns='<button data-c="" class="on">Tous les camps</button>'+''.join(f'<button data-c="{E(c)}" class="{ccls(c)}">{E(c)} <span class="n">{sum(1 for f in F if c in f["camp"])}</span></button>' for c in CAMPS_LIST)
btns='<button data-t="">Tout</button>'+''.join(f'<button data-t="{E(t)}">{E(t)}</button>' for t in TAGS)
chiffres='''<section class="keys"><div><b>3 595,5 Md€</b><span>dette publique, fin T2 2026 (119,0 % du PIB) – <a href="https://www.insee.fr/fr/statistiques/9053525">Insee, 29/09/2026</a></span></div>
<div><b>152,5 Md€</b><span>déficit public 2025 (5,1 % du PIB) – <a href="https://www.insee.fr/fr/statistiques/8956575">Insee, 27/03/2026</a></span></div>
<div><b>54 Md€</b><span>effort de redressement du PLF 2027 (dont 43 Md€ dans les textes) – <a href="https://solidarites.gouv.fr/sites/solidarite/files/2026-10/DP-BUDGET-2027.pdf">dossier de presse, oct. 2026</a></span></div>
<div><b>14,2 M€ = 0,0093 %</b><span>du déficit 2025 : charge des comités sociaux de FTV en 2024 – <a href="fiches/cse-14-2m.html">fiche</a></span></div>
<div><b>111 M€ = 0,073 %</b><span>du déficit 2025 : CA de Mediawan avec FTV en 2024 (chiffre FTV) – <a href="fiches/mediawan-44-111.html">fiche</a></span></div></section>'''
idx=f'''<h2>Fil rouge : une dette officielle, des dérives documentées, une échelle honnête</h2>
<p>La dette dépasse 3 000 Md€ (confirmé : 3 595,5 Md€). Le déficit 2025 est de 152,5 Md€ (et non « environ 140 Md€ » : ce dernier chiffre n'a pas été retrouvé dans une source officielle). Aucun poste de l'audiovisuel public documenté ici ne dépasse 0,15 % de ce déficit : le débat porte sur la cohérence et la gouvernance, pas sur la résorption de la dette. Voir <a href="grand-ecart.html">Le grand écart</a>.</p>{chiffres}
<h2 id="fiches">Fiches</h2>
<div class="searchbox"><label for="q" class="sr">Rechercher dans les fiches</label><input id="q" type="search" placeholder="Rechercher une fiche : mot-clé, montant, organisme, source…" autocomplete="off" aria-controls="cards"><button type="button" id="qclear" hidden>Effacer</button></div>
<p id="count" class="count" role="status" aria-live="polite"></p>
<p class="frow">Camp politique <a href="methode.html#camp" title="Critères d'attribution">(critères)</a></p><div class="filters camps-f" role="group" aria-label="Filtrer par camp politique">{cbtns}</div><p class="frow">Thème</p><div class="filters tags-f" role="group" aria-label="Filtrer par thème">{btns}</div><div id="cards">{cards}</div><p id="noresult" class="noresult" hidden>Aucun résultat. Essayez un autre mot-clé, ou retirez le thème sélectionné. Les éléments sans source primaire sont sur la page <a href="non-verifie.html">Non vérifié</a>.</p>
<noscript><p>La recherche et le filtre nécessitent JavaScript ; toutes les fiches restent visibles.</p></noscript>
'''
open(OUT+'/index.html','w').write(page('Accueil',idx,'','index.html'))
ech=json.load(open('/workspace/observatoire-ajouts/echelles.json'))
rows=''.join(f'<tr><td>{E(r["poste"])}</td><td>{r["montant_M€"]:g}</td><td>{r["pct_deficit_2025_(152,5 Md€)"]}</td><td>{r["pct_effort_2027_(54 Md€)"]}</td><td>{r["pct_depenses_publiques_2025_(1 714,1 Md€)"]}</td></tr>' for r in ech)
ge=f'''<h2>Le grand écart</h2><p>Chaque montant est rapporté au déficit 2025 (152,5 Md€, Insee 27/03/2026), à l'effort 2027 (54 Md€, gouvernement) et à la dépense publique 2025 (1 714,1 Md€, Insee). Les montants ne s'additionnent pas ; FTV conteste leur comparabilité.</p><table><tr><th>Poste</th><th>M€</th><th>% déficit 2025</th><th>% effort 2027</th><th>% dépenses publiques 2025</th></tr>{rows}</table>
<h3>Repères officiels</h3><ul><li>Dette fin T2 2026 : 3 595,5 Md€ = 119,0 % du PIB ({link("https://www.insee.fr/fr/statistiques/9053525")}).</li><li>Déficit 2025 : 152,5 Md€ = 5,1 % ; dépenses 57,2 % du PIB ; dette fin 2025 : 3 460,5 Md€ = 115,6 % ({link("https://www.insee.fr/fr/statistiques/8956575")}).</li><li>PLF 2027 : effort de 54 Md€, déficit cible 5,0 % ; charge d'intérêts 79,2 → 91,2 Md€ (périmètre non précisé) ({link("https://solidarites.gouv.fr/sites/solidarite/files/2026-10/DP-BUDGET-2027.pdf")}).</li></ul>
<h3>Discours officiel</h3><ul><li>« Il n'y a pas d'argent magique » : attribuée à Philippe Juvin (LR), et non au Premier ministre (URL de la source non conservée dans cette V1 : à recontrôler).</li><li>« La France est ruinée », « plus d'argent » : <b>non vérifié</b>, aucune déclaration datée retrouvée.</li></ul>
<p>Détail : <a href="data/fiche_grand_ecart.json">data/fiche_grand_ecart.json</a>.</p>'''
open(OUT+'/grand-ecart.html','w').write(page('Le grand écart',ge,'','grand-ecart.html'))
lv=f'''<h2>Livres</h2><p>Les métadonnées reçues sont vérifiées, pas reprises. Le texte intégral des livres n'a pas été lu : les passages ne sont cités que s'ils ont été retrouvés dans une source citée.</p>
<h3>Charles Alloncle – « Je jure de dire toute la vérité »</h3><p>Fayard, <b>30/09/2026</b> (et non 2025), 320 p., EAN 9782213736440 – {link("https://www.fayard.fr/livre/je-jure-de-dire-toute-la-verite-9782213736440/")}. Fiche : <a href="fiches/livre-alloncle.html">livre-alloncle</a>.</p>
<table><tr><th>Affirmation (message X de C. Alloncle, 12/10/2026, citée par CNews)</th><th>Verdict</th><th>Source primaire</th></tr>
<tr><td>« des karaokés à 250 millions € »</td><td>Nuancé : ≈ 250 M€ sur 2015-2025 pour une seule émission (« N'oubliez pas les paroles »)</td><td>Rapport p. 407 ; <a href="fiches/nopl-250m.html">fiche</a></td></tr>
<tr><td>« des indemnités de départ de plus de 500 000 € »</td><td>Non vérifié : le rapport donne des agrégats (232 M€, 141 indemnités &gt; 100 000 €) ; 400 000 € cités à l'audition n° 63</td><td>Rapport p. 389 ; <a href="fiches/indemnites-depart-232m.html">fiche</a></td></tr>
<tr><td>« des nuits dans des palaces à 1 700 euros »</td><td>Nuancé : 1 899 € la nuit en 2024 (rapport) ; 1 700 € = chiffre 2023 de Marianne</td><td>Rapport p. 393 ; <a href="fiches/cannes-majestic.html">fiche</a></td></tr>
<tr><td>« des milliards d'euros de contrats conclus en dehors des règles applicables aux marchés publics »</td><td>Nuancé : l'exclusion est légale (L2513-1) ; 864 M€ d'achats externes en 2024 ; total pluriannuel non vérifié</td><td><a href="fiches/marches-publics-exclusion.html">fiche</a></td></tr>
<tr><td>Mediawan</td><td>Confirmé (chiffres FTV : 44 → 111 M€) / Nuancé</td><td><a href="fiches/mediawan-44-111.html">fiche</a></td></tr></table>
<h3>Sarah Knafo – « Le Casse du siècle »</h3><p>Fayard, <b>02/09/2026</b>, 286 p., EAN 9782213733135 – {link("https://www.fayard.fr/livre/le-casse-du-siecle-9782213733135/")}. 63 087 exemplaires en 5 jours : déclaration de l'éditeur (Le Parisien/AFP, 08/09/2026). Fiche : <a href="fiches/livre-knafo.html">livre-knafo</a>.</p>
<table><tr><th>Affirmation</th><th>Verdict</th></tr>
<tr><td>Fiche de paie : coût employeur 3 922 € / net 2 079 € ; 940 500 € sur 42,75 ans</td><td>Nuancé : calcul arithmétique exact (22 000 × 42,75), mais l'écart correspond à des cotisations qui financent des prestations (retraite, santé, famille, chômage) ; sources Insee/Urssaf/DSS non rouvertes</td></tr>
<tr><td>Dépense publique 2025 : 1 714 Md€, 57 % du PIB</td><td>Confirmé (Insee : 1 714,1 Md€, 57,2 %)</td></tr>
<tr><td>Dette : 1 090-1 100 Md€ de hausse 2017-2024</td><td>Nuancé : 3 305 Md€ fin 2024 (preuve n° 60) ; fin 2017 : 2 218 Md€ selon l'autrice, 2 263,3 Md€ selon la série comptespublics.fr : écart de révision à lever</td></tr>
<tr><td>AFD : directeur payé 17 500 €/mois ; siège « près de 1 Md€ »</td><td>Nuancé : siège évalué 840 M€, 924 M€ frais inclus (CIE, cité par la question écrite n° 15786) ; le ministère répond qu'il n'engage « pas de coûts pour l'Etat » ; rémunération : décision du 23/03/2023, DG évoquant jusqu'à 262 000 € bruts/an (Le Parisien)</td></tr>
<tr><td>Audiovisuel public « près de 4 Md€ par an »</td><td>Non vérifié (FTV : 2,506 Md€ de financement public en LFI 2025)</td></tr>
<tr><td>3,7 M d'agents « inutiles » ; 800 000 postes = 40 Md€/an</td><td>Contesté (franceinfo, F. Ecalle/Fipeco : 30-40 Md€ si réalisé, irréaliste sans réorganisation)</td></tr></table>
<h3>Pierre Jovanovic – « 2008 »</h3><p>Le Jardin des Livres, <b>13/06/2025</b>, ISBN 9782914569873 (libraire) : titre/date confirmés. Recoupement avec les chiffres officiels (France) : plan SFEF/SPPE : 19,75 Md€ de fonds propres et 77 Md€ de prêts garantis, <b>bilan positif de 2,7 Md€ pour l'État selon le ministère</b> (05/07/2011) ; Dexia : <b>coût direct de 6,6 Md€</b> (Cour des comptes, 2013). La thèse « les gouvernements ont volé l'argent des impôts pour sauver les banques » n'est donc <b>pas confirmée</b> pour le plan SFEF/SPPE en France, et <b>partiellement étayée</b> pour Dexia. Fiches : <a href="fiches/livre-jovanovic-2008.html">livre</a>, <a href="fiches/banques-2008-2009-bilan.html">banques 2008-2009</a>, <a href="fiches/dexia-cour-6-6-md.html">Dexia</a>.</p>
<h3>Olivier Marleix – « Les Liquidateurs » (2021), « Dissolution française » (13/11/2025)</h3><p>Orthographe confirmée : Marleix. Alstom : rapport n° 897 de la commission d'enquête (19/04/2018), lu dans la version officielle : la formule « cécité, imprévision et entre soi », les 299 000 € de l'étude AT Kearney et la lecture « l'État a failli » sont celles de l'avant-propos du président Marleix ; le rapporteur G. Kasbarian écrit au contraire que « L'État a donc joué son rôle ». Fiches : <a href="fiches/livre-marleix.html">livre-marleix</a>, <a href="fiches/alstom-commission-2018.html">Alstom</a>.</p>
<h3>Éric Denécé</h3><p>Orthographe corrigée (Denécé). Recoupement partiel avec le catalogue de la BnF (premiers résultats seulement : titres, éditeurs, années ; rien d'autre n'est repris). Titres retrouvés : <i>Histoire secrète des forces spéciales : de 1939 à nos jours</i> (Nouveau monde éditions, 2010 et 2019) ; <i>Commandos &amp; forces spéciales</i> (Ouest-France, 2011) ; <i>L'espionnage en 365 citations</i> (Chêne, 2013, réunis par É. Denécé) ; <i>Forces spéciales, l'avenir de la guerre ?</i> (Éditions du Rocher, 2002) ; <i>Le nouveau contexte des échanges et ses règles cachées</i> (L'Harmattan, 2001) ; <i>La face cachée des révolutions arabes</i> (CF2R, sous la direction d'É. Denécé, Ellipses, <b>2013 selon la BnF</b> ; la liste fournie indiquait 2012) ; <i>Chroniques de la guerre en Ukraine</i> (CF2R, depuis 2023, sous sa direction). Les autres titres de la liste de 29 ouvrages restent <b>à vérifier</b>. Ses positions sur l'Ukraine sont des thèses d'auteur ; elles sont hors périmètre de l'argent public sauf coûts publics sourcés. Source : <a href="https://catalogue.bnf.fr/rechercher.do?motRecherche=Denécé&amp;critereRecherche=0&amp;depart=0&amp;facetteModifiee=ok">catalogue.bnf.fr</a> (consulté le 25/10/2026).</p>'''
open(OUT+'/livres.html','w').write(page('Livres',lv,'','livres.html'))
nv=f'''<h2>Non vérifié</h2><p>Éléments exclus des fiches faute de source primaire retrouvée.</p>
<h3>Faits ou slogans</h3><ul>
<li>Indemnité de départ individuelle de plus de 500 000 € (Alloncle) : le rapport lu ne la mentionne pas ; 400 000 € cités en audition n° 63 ; 415 000 € relayés par un post LinkedIn (source secondaire).</li>
<li>« La France est ruinée », « plus d'argent » : aucune déclaration datée et attribuée retrouvée. « Nous ne réduisons pas les dépenses, nous les maîtrisons » (Lecornu, Figaro, 17/09/2026) : relayé par un site secondaire, interview non lue.</li>
<li>Déficit « d'environ 140 Md€ » : chiffre officiel 2025 = 152,5 Md€ ; Knafo cite « 170 Md€ » (via note de lecture) : non vérifié.</li>
<li>Charge d'intérêts 2025 (APU) de 64,7 Md€ (dettedelafrance.fr, source secondaire) ; la ligne PLF 2027 (79,2 → 91,2 Md€) n'a pas un périmètre précisé : ne pas comparer les deux.</li>
<li>Concours publics à l'audiovisuel PLF 2027 (3,82 Md€) et baisse de 219 M€ 2024-2026 annoncée par FTV : non retrouvés dans un document d'État.</li>
<li>Durée, reconduction et mise en concurrence des contrats « C dans l'air », « C à vous », « Envoyé spécial » : aucune source primaire.</li>
<li>Avis du Conseil d'État, de l'Autorité de la concurrence, de l'Arcom sur l'exclusion des programmes : aucun trouvé.</li></ul>
<h3>Fiches A et B : ce qui reste non vérifié</h3><ul>
<li>Fiche A (20 Heures du 18/10/2026) : la formule « images brutes = jeu de l'extrême droite » n'a été retrouvée dans aucune des sources lues (CGT, CFDT, TVmag, Anadolu, La Provence/AFP, Télérama, Le Dauphiné, Voici).</li>
<li>Fiche A : le remplacement d'une interview d'Angèle par ce sujet n'est donné que par un extrait de recherche (Melty), non consulté : non vérifié.</li>
<li>Fiche A : Le JDD, Le Figaro, Contrepoints, Valeurs actuelles, actu.fr n'ont pas été lus sur ce sujet : leur traitement n'est pas résumé.</li>
<li>Fiche B : la vidéo est attribuée à « France 3 Alsace » (Valeurs actuelles, Le JDD) ou à « France 3 Nancy » (SNJ, CGT) : non réconcilié. Aucune réponse publique de France Télévisions retrouvée ; les « 900 000 vues » proviennent d'un mail interne cité par la CGT.</li>
<li>Fiche B : les contenus de Cnews et d'Europe 1 (cités par le SNJ) n'ont pas été consultés.</li></ul>
<h3>Passe 2 : sujets non traités ou non confirmés</h3><ul>
<li>Fraude fiscale chiffrée et « 50 Md€ de fraude sociale » (chiffre contesté) : pas de source primaire retenue ; seul le rapport de la Cour sur les indus (mai 2025) est fiché.</li>
<li>Immobilier de l'État : des extraits de recherche donnent, pour 2025, 365,9 M€ de recettes du compte d'affectation spéciale (dont 239,3 M€ de cessions), 1,987 Md€ de loyers payés et 24,87 m² de bureaux par poste contre une cible de 22,8 m² (Cour des comptes, « Le budget de l'État en 2025 – Gestion du patrimoine immobilier de l'État », avril 2026) : <b>non vérifiés</b>, le PDF n'a pas pu être téléchargé.</li>
<li>Associations : une revue IGF-IGAS (juillet 2025) évoquerait plus de 49 Md€ de financements publics aux associations en 2023 et la Cour 16 Md€ de soutiens de l'État à l'économie sociale et solidaire en 2024 : <b>non vérifiés</b> (documents non lus).</li>
<li>AFP, France Médias Monde, Arte : le seul contrôle de la Cour retrouvé est celui de France Médias Monde (2013-2019, publié le 25/03/2021, 15 recommandations, selon une recherche) ; aucun contrôle retrouvé pour Arte ; non fichés.</li>
<li>Radio France : les réponses de la ministre et de la PDG, publiées avec le rapport de la Cour, n'ont pas été lues.</li>
<li>Gain net budgétaire d'environ 850 M€ du plan bancaire selon la Cour des comptes (2010) : extraits de presse seulement.</li>
<li>HATVP, IGF (revues de dépenses) : non traités dans cette passe.</li></ul>
<h3>Livres</h3><ul>
<li>Pierre Jovanovic : « Révélation : l'argent secret des banques » (ou titre proche) : introuvable (BnF, libraires, presse). Le titre « 2008 » (2025) est identifié ; ses chiffres propres ne sont pas vérifiés (texte non lu).</li>
<li>Éric Denécé : liste de 29 ouvrages : une partie seulement recoupée avec la BnF (voir la page Livres).</li>
<li>Passages des livres de Knafo, Alloncle, Marleix : seuls les extraits de presse ont été lus.</li></ul>'''
open(OUT+'/non-verifie.html','w').write(page('Non vérifié',nv,'','non-verifie.html'))
me='''<h2>Méthode</h2><ul><li>Une fiche n'existe que si une source primaire est identifiée (rapport, décision, texte officiel, publication d'un organisme). Sinon : page « Non vérifié ».</li>
<li>Statuts : <b>Confirmé</b> (chiffre retrouvé à la source), <b>Nuancé</b> (chiffre exact mais périmètre, interprétation ou réponse contestée), <b>Non vérifié</b>.</li>
<li>Les citations sont reproduites mot pour mot ; les pages sont celles des PDF, ou du miroir citoyen audiovisuel-public.com pour le rapport Alloncle (non officiel).</li>
<li>Les réponses des organismes (France Télévisions, 13/05/2026) sont reproduites quand elles existent.</li>
<li>Mise à l'échelle : chaque montant est rapporté au déficit, à l'effort d'économies et à la dépense publique ; les montants ne s'additionnent pas.</li>
<li>Thèse d'un auteur ≠ fait établi : les thèses sont étiquetées comme telles.</li>
<li>Limites : sources secondaires signalées ; textes de livres non lus ; certains rapports de la Cour n'ont été lus que sur leur page de synthèse (le serveur ccomptes.fr refuse le téléchargement des PDF depuis la box) : indiqué dans les réserves de chaque fiche.</li></ul>
<h2 id="camp">Le tag « camp politique »</h2>
<p><b>Qualification éditoriale, contestable, fondée sur les faits listés dans le bloc « Pourquoi ce tag » de chaque fiche.</b> Elle situe où se placent les faits et les acteurs cités ; elle n'établit aucune responsabilité personnelle ni aucune faute, et ne porte aucun jugement de valeur. Une fiche peut avoir plusieurs camps.</p>
<h3>Critères (affichés fiche par fiche)</h3>
<ul><li><b>C1 – Exécutif en place à la date des faits</b> : période couverte par les chiffres ou la décision.</li>
<li><b>C2 – Décision, nomination ou financement</b> attribuable à un exécutif identifié (cité avec sa date).</li>
<li><b>C3 – Acteur politique ou syndical</b> mis en cause ou auteur de la critique, avec l'appartenance déclarée dans la source.</li>
<li><b>C4 – Lecture politique rapportée par les sources</b>, citée entre guillemets ; une lecture citée n'est pas un fait établi.</li></ul>
<h3>Règles d'attribution</h3>
<ul><li><b>macroniste</b> : tous les faits chiffrés datent de la présidence d'Emmanuel Macron (depuis le 14/05/2017) et la décision ou le financement relève de l'exécutif en place ; ou l'acteur mis en cause ou auteur de la lecture appartient au bloc présidentiel (par exemple LREM).</li>
<li><b>droite/LR</b> : faits relevant de l'exécutif Sarkozy-Fillon (UMP, ancêtre de LR), ou acteur LR auteur de la lecture citée.</li>
<li><b>RN</b> : acteur du Rassemblement national auteur de la critique ou mis en cause, avec sa citation.</li>
<li><b>extrême gauche</b> : acteur d'un mouvement ou d'une organisation qualifiés ainsi par une source citée dans la fiche. Aucune fiche n'est actuellement dans ce cas : les syndicats (CGT, CFDT, SNJ, Syndicat de la magistrature) ne sont pas des partis et aucune source lue ne les classe ainsi ; le filtre affiche donc 0.</li>
<li><b>transverse</b> : faits qui traversent plusieurs exécutifs (y compris Hollande, qui n'a pas de valeur propre), lectures de camps différents réunies dans un même document, ou acteur dont le parti n'est pas dans la liste (UDR, Reconquête, groupe communiste du Sénat) ou qui n'est pas un parti (syndicats). En cas de doute : transverse, avec l'explication affichée.</li>
<li>Le camp du rapporteur ou du président d'une commission d'enquête n'est pas, à lui seul, le camp de la fiche lorsque la commission est pluraliste ; il est cité dans la justification.</li>
<li>Limites : les camps sont des étiquettes d'attribution ; une même dépense peut avoir été engagée par des exécutifs différents ; l'appartenance partisane est celle indiquée par la source à la date citée.</li></ul>'''
open(OUT+'/methode.html','w').write(page('Méthode',me,'','methode.html'))
exec(open('/workspace/site_assets.py',encoding='utf8').read())
open(OUT+'/style.css','w',encoding='utf8').write(CSS)
open(OUT+'/search.js','w',encoding='utf8').write(JS)
open(OUT+'/README.md','w').write('''# Observatoire de l'argent public (V2, 25/10/2026)
Site statique, sans dépendance. Ouvrir `index.html`.
- `data/fiches.json` : source de vérité des fiches (le script `build_site.py` régénère `fiches/*.html`).
- `data/fiche_*.json` : détails (marchés publics, SM, grand écart, enquêteurs).
- Pages : index (recherche en direct + filtre de tags, ?q= et ?tag= dans l'URL), grand-ecart, livres, non-verifie, methode.
- Rien n'est publié : le dossier est local.
''')
shutil.copy('/workspace/build_site.py',OUT+'/build_site.py'); shutil.copy('/workspace/pass2_fiches.py',OUT+'/pass2_fiches.py'); shutil.copy('/workspace/site_assets.py',OUT+'/site_assets.py'); shutil.copy('/workspace/camps.py',OUT+'/camps.py')
print(len(F),'fiches')
