# activate venv
.venv/Scripts/activate

set -e

# 关联远程 gh-pages 分支 到 public
git worktree add -B gh-pages public origin/gh-pages

# 构建 Hugo
rm -rf public/*
hugo build --themesDir .. --destination public

# 提交并推送
cd public
git add --all
git commit -m "Rebuild site"
git push origin gh-pages

cd ..
git worktree remove public
