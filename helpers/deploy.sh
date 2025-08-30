# activate venv
.venv/Scripts/activate

# check directory structure
echo "check_docs_frontmatter.py..."
python3 -u helpers/check_docs_frontmatter.py

# generate doc_sidebar.yaml
echo "docs_sidebar.py..."
python3 -u helpers/docs_sidebar.py

# build
hugo build --themesDir .. --destination ../public

git add .
git commit -m "update"
git push origin main
# checkout branch gh-pages
git checkout gh-pages
git rm -rf *
cp -r ../public/* .
git add .
git commit -m "Rebuild site"
git push origin gh-pages --force
# checkout branch main
git checkout main

echo "Deploy to gh-pages complete !"
