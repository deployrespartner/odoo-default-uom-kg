# Default UoM Configuration for Odoo 17

Ce module permet de configurer l'unité de mesure par défaut pour chaque type de produit dans Odoo.

## Fonctionnalités

- Configuration des UoM par défaut pour chaque type de produit :
  - Produits stockables (product)
  - Produits consommables (consu)
  - Services (service)
- Interface de configuration dans les paramètres Odoo
- Mise à jour automatique de l'UoM lors du changement de type de produit
- Valeurs par défaut si non configurées :
  - Kilogramme (kg) pour les produits stockables et consommables
  - Unité pour les services

## Installation

1. Clonez ce dépôt dans votre répertoire addons Odoo :
```bash
git clone https://github.com/deployrespartner/odoo-default-uom-kg.git
```

2. Mettez à jour la liste des modules dans Odoo
3. Installez le module 'Default UoM Kilogram'

## Configuration

1. Allez dans Configuration > Paramètres
2. Dans la section "Inventory", vous trouverez les paramètres suivants :
   - "Default UoM for Storable Products" : UoM par défaut pour les produits stockables
   - "Default UoM for Consumable Products" : UoM par défaut pour les produits consommables
   - "Default UoM for Services" : UoM par défaut pour les services
3. Sélectionnez l'UoM souhaitée pour chaque type de produit
4. Cliquez sur "Sauvegarder" pour appliquer les changements

## Usage

Une fois configuré :
1. Lors de la création d'un nouveau produit, l'UoM sera automatiquement définie selon le type de produit sélectionné
2. Si vous changez le type d'un produit existant, l'UoM sera automatiquement mise à jour selon la configuration

## Notes techniques

- Les paramètres sont stockés dans `ir.config_parameter` sous les clés :
  - `default_uom_kg.default_uom_product`
  - `default_uom_kg.default_uom_consu`
  - `default_uom_kg.default_uom_service`
- Le module surcharge les méthodes suivantes du modèle `product.template` :
  - `_get_default_uom_id` : pour la valeur par défaut à la création
  - `_onchange_detailed_type` : pour la mise à jour lors du changement de type