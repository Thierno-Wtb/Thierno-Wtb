--------------ALIMENTATION DE LA TABLE "DWH_D_E_COMMERCE_CLIENT-------------------------------------

/*SELECT c.id_customer id_client,  c.date_add DATE_INSCRIPTION,  c.lastname NOM, c.firstname PRENOM, c.email E_MAIL, a.address1 ADRESSE, a.postcode CODE_POSTALE, 
a.city VILLE, a.phone TEL_FIXE, a.phone_mobile TEL_MOBILE, a.company NOM_ENTREPRISE, m.message MESSAGE, m.user_agent MOTEUR_RECHERCHE
from ope.ps_customer c
INNER JOIN ope.ps_address a ON a.id_address = c.id_customer
INNER JOIN ope.ps_customer_message m on m.id_customer_message = c.id_customer
Group by c.id_customer;*/
/*select * from dwh_sdp_ventes.dwh_d_e_commerce_client;*/
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
select * from ope.ps_store;
select * from ope.ps_shop;

--------------------ALIMENTATION DE LA TABLE "dwh_sdp_ventes"."DWH_d_e_commerce_produit"

INSERT INTO DWH_d_e_commerce_produit(ID_PRODUIT,REF_PRODUIT, TYPE_PRODUIT, PRIX_ACHAT, PRIX_VENTE,ECO_TAXE, DT_INSERTION, DT_MAJ, ACTIF)
SELECT p.id_product ID_PRODUIT, p.reference REF_PRODUIT, p.product_type TYPE_PRODUIT, a.wholesale_price PRIX_ACHAT, a.price PRIX_VENTE, a.ecotax ECO_TAXE, p.date_add DT_INSERTION, p.date_upd DT_MAJ, p.state ACTIF
from OPE.ps_product p
inner join ope.ps_product_attribute a on a.id_product_attribute = p.id_product;

select * from DWH_d_e_commerce_produit;

