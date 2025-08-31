# activate venv
.venv/Scripts/activate

set -e

# 关联远程 gh-pages 分支 到 public
git worktree add -B gh-pages deploy-public origin/gh-pages

# 构建 Hugo
hugo build --themesDir .. --destination deploy-public

# 提交并推送
cd deploy-public
git add --all
git commit -m "Rebuild site"
git push origin gh-pages

cd ..
git worktree remove deploy-public
