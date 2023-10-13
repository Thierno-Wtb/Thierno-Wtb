----------------------------------------------------------------------------
---------- Table dimensionnelle : "dwh_sdp_ventes"."DIM_CALENDRIER" ---------
----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS D_CALENDRIER(
ID_DIM_CALENDRIER 	INTEGER NOT NULL PRIMARY KEY,
DT_JOUR DATE NOT NULL,
NB_ANNEE INTEGER NOT NULL,
NB_SEMESTRE INTEGER NOT NULL,
NB_TRIMESTRE INTEGER NOT NULL,
NB_MOIS INTEGER NOT NULL,
NB_JOUR_ANNEE INTEGER NOT NULL,
NB_JOUR_MOIS INTEGER NOT NULL,
NB_JOUR_SEMAINE INTEGER NOT NULL,
NB_SEMAINE_ANNEE INTEGER NOT NULL,
LB_MOIS VARCHAR(100) NOT NULL,
LB_JOUR VARCHAR(100) NOT NULL,
BL_DERNIER_JOUR_MOIS INTEGER NOT NULL,
BL_BISSEXTILE INTEGER NOT NULL,
BL_WEEK_END INTEGER NOT NULL,
BL_JOUR_FERIE INTEGER NOT NULL,
LB_JOUR_FERIE VARCHAR(100)
); 

----------------------------------------------------------------------------
---------- Table dimensionnelle : "dwh_sdp_ventes"."DWH_d_e_commerce_produit" ---------
----------------------------------------------------------------------------
/*DROP TABLE DWH_D_E_COMMERCE_PRODUIT;*/

CREATE TABLE IF NOT EXISTS DWH_D_E_COMMERCE_PRODUIT(
ID_PRODUIT	NUMERIC NOT NULL PRIMARY KEY,
REF_PRODUIT VARCHAR(255),
DATE_ADD DATETIME,
TYPE_PRODUIT VARCHAR(255),
PRIX_ACHAT FLOAT,
PRIX_VENTE FLOAT,
ECO_TAXE FLOAT,
PRODUIT_CATEGORIE VARCHAR(255),
PRODUIT_TYPE VARCHAR(255),
DT_INSERTION DATETIME,
DT_MAJ DATETIME,
ACTIF INT);


---------------------------------------------------------------------------------
-------- CREATION DE LA TABLE DES FAITS "DWH_F_E_COMMERCE_COMMANDES"---------------
-------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS DWH_F_E_COMMERCE_COMMANDES(id_order numeric not null, id_dim_calendrier numeric not null, ID_CLIENT numeric not null, ID_PRODUIT numeric not null,
reference VARCHAR(255), mode_paiement varchar(255), module_paiement varchar(255), montant_reduction FLOAT, montant_payer FLOAT, taux_impot FLOAT,
delais_livraison NUMERIC, commande_valide NUMERIC, date_inscription DATETIME, date_maj DATETIME, note TEXT);
