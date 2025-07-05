#!/bin/bash

echo "⚙️  Generazione sito con Hugo..."
hugo

echo "🚀 Deploy su GitHub Pages..."
cd public
git init
git add .
git commit -m "Deploy Hugo site"
git branch -M gh-pages
git remote add origin https://github.com/voksDB/esercizio_editoria_EdiNews.git
git push -f origin gh-pages
cd ..

echo "✅ Sito pubblicato su: https://voksdb.github.io/esercizio_editoria_EdiNews/"
