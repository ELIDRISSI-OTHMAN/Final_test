# Rapport de Stage LaTeX - Documents Séparés

Ce dossier contient le rapport de stage complet divisé en 16 documents LaTeX indépendants.

## Structure des Documents

1. **01_page_titre.tex** - Page de titre
2. **02_introduction.tex** - Introduction générale
3. **03_contexte_problematique.tex** - Contexte et problématique
4. **04_objectifs.tex** - Objectifs du stage
5. **05_analyse_besoins.tex** - Analyse des besoins
6. **06_architecture_technologies.tex** - Architecture et technologies
7. **07_developpement.tex** - Développement de l'application
8. **08_algorithmes.tex** - Algorithmes implémentés
9. **09_interface_utilisateur.tex** - Interface utilisateur
10. **10_tests_validation.tex** - Tests et validation
11. **11_distribution.tex** - Distribution et déploiement
12. **12_resultats.tex** - Résultats et évaluation
13. **13_difficultes.tex** - Difficultés rencontrées
14. **14_apports.tex** - Apports du stage
15. **15_perspectives.tex** - Perspectives d'amélioration
16. **16_conclusion.tex** - Conclusion

## Compilation

### Compilation Automatique
```cmd
compile_all.bat
```

### Compilation Manuelle
Pour compiler un document individuel :
```cmd
pdflatex 01_page_titre.tex
```

## Caractéristiques

- **Packages utilisés** : Uniquement les packages par défaut LaTeX
- **Encodage** : UTF-8 avec support français
- **Format** : A4, 12pt, marges 2.5cm
- **Indépendance** : Chaque document est compilable séparément
- **Pas de caractères spéciaux** : Utilisation de caractères ASCII étendus uniquement

## Personnalisation

Pour personnaliser le rapport :
1. Modifiez la page de titre avec vos informations
2. Adaptez le contenu selon votre contexte spécifique
3. Ajoutez vos propres données et résultats
4. Incluez vos captures d'écran et diagrammes

## Sortie

Chaque compilation génère un fichier PDF indépendant que vous pouvez :
- Utiliser séparément pour des présentations
- Combiner en un seul document
- Imprimer individuellement
- Partager par sections

## Support

Les documents sont conçus pour être compatibles avec :
- MiKTeX
- TeX Live
- Overleaf
- Tout autre distribution LaTeX standard