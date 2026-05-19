# Python Orienté Objet

## Introduction

>[!DÉFINITION]
L'Orienté Objet un **paradigme** qui à pour but d'évité les codes redondant en utilisant différent **Objets** pour coder de façon plus **dynamique**
L'idée ça sera de déterminer comment concevoir un **objet réel ou imaginaire** (un plan de construction d'un élément).

Chaque objets possedera des `attrubuts` et des `méthodes`.

|Programation Procedural          |Programation Orienté Objet               |
|---------------------------------|-----------------------------------------|
|Impose des répétition            |Facile à maintenir (moins de répétitions)|
|Utile quand le le code est court |Utile quand le le code est long          |

Les principes fondamenteau de l'oo sont l'encapsulation, l'héritage, et le polymorphisme qui vont permettre d'isolé et de concetualiser les objets qu'on crée.

## Structures

>Quand on programme en OO il est omportant de struturer le code : Il faut mettre touts nos fichier dna sun dossier `Models`

```
Models
    model_1.py
    model_2.py
    model_3.py
main.py
```
Les fichiers du Models vont contenir les objets qui seront à importer dans le fichier main.

L'intruction `from Models.model_1 import model_1` va permettre d'importer une classe ou une fonction dans le répertoire Models.

En utilisant `test = model_1()` on crée directement une instance de ce qu'on a importé.

- Quand Python exécute un fichier directement, il donne à la variable `__name__` la valeur `"__main__"`.
- Ça permet de protéger du code pour qu'il ne s'exécute **que si le fichier est lancé directement**, et pas s'il est importé ailleurs.

```python
def fonction_principale():
    print("Code exécuté uniquement si le fichier est le point d'entrée")

if __name__ == "__main__":
    fonction_principale()
```


>[!BONNE-PRATIQUE]
- Utiliser des noms décriptifs
- Éviter les abréviations pas claire
- Respecter la concontion de nommage PascalCase
- Un seul concept par classe
- Documenter les classes

## Classes et Objets

>[!DÉFINITION] Une clase est un modèles (un plan de construction) utiliser pour faire un, deux, ou trois objet qui aurons le même comportement.

La syntaxe est symple on utilise le mot-clé `class` suivi du nom de la classe en **PascalCase** (chaque mot commence par une majuscule), puis deux-points et un bloc indenté.

``` Python
class Voiture
    pass
```
### Instanciation

Pour créer un objet à partir d'une classe, on utilise le nom de la classe suivi de parenthèses.

```python
from Voiture import Voiture

voiture1 = Voiture()
```

### Attributs

Les attributs représentent les caractéristiques d'un objet. Ils se déclarent dans la classe et peuvent être lus ou modifiés.

```python
class Voiture:
    marque = None
    modele = "Corolla"
    vitesse_actuelle = 0

ma_voiture = Voiture()
print("Marque :", ma_voiture.marque)
print("Modèle :", ma_voiture.modele)
print("Vitesse actuelle :", ma_voiture.vitesse_actuelle)
```

### Méthodes

Les méthodes définissent les **comportements** d'un objet — ce qu'il peut faire.

Elles encapsulent le comportement de l'objet, offrant ainsi une interface cohérente pour manipuler et interagir avec lui.

```python
class Voiture:
    marque = None
    modele = "Corolla"
    vitesse_actuelle = 0

    def accelerer(self, acceleration):
        self.vitesse_actuelle += acceleration

    def freiner(self, deceleration):
        self.vitesse_actuelle -= deceleration

    def afficher_info(self):
        print("Modèle :", self.modele)
        print("Vitesse actuelle :", self.vitesse_actuelle)

ma_voiture = Voiture()
ma_voiture.accelerer(20)
ma_voiture.afficher_info()
```
---

>[!TIPS]Dans notre dossier Models, on peut pour être éfficace ajouter un `__init__.py`. Ce fichier va permettre de lister les différent models qu'on va vouloir appeller dans une liste.

```Python
from .voiture import Voiture
from .garage import Garage

__all__ = [
    "Voiture",
    "Garage"
]
```