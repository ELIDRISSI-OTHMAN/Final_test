@echo off
echo Compilation de tous les documents LaTeX du rapport de stage
echo.

REM Liste des fichiers LaTeX a compiler
set files=01_page_titre 02_introduction 03_contexte_problematique 04_objectifs 05_analyse_besoins 06_architecture_technologies 07_developpement 08_algorithmes 09_interface_utilisateur 10_tests_validation 11_distribution 12_resultats 13_difficultes 14_apports 15_perspectives 16_conclusion

REM Compilation de chaque fichier
for %%f in (%files%) do (
    echo Compilation de %%f.tex...
    pdflatex %%f.tex
    if errorlevel 1 (
        echo Erreur lors de la compilation de %%f.tex
    ) else (
        echo %%f.pdf genere avec succes
    )
    echo.
)

REM Nettoyage des fichiers temporaires
echo Nettoyage des fichiers temporaires...
del *.aux *.log *.out 2>nul

echo.
echo Compilation terminee. Tous les PDF sont prets.
pause