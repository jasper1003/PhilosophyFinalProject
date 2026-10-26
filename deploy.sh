#!/bin/bash
set -e

PROJECT_DIR="/Users/jasper_1003_/Renpy/Avatar"
WEB_OUT_DIR="/Users/jasper_1003_/Renpy/Avatar-web"
RENPY_SDK="/Applications/renpy-8.5.3-sdk"

echo "=== [1/4] 編譯遊戲至 Web (HTML5/WASM) ==="
"$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" web_build "$PROJECT_DIR" --destination "$WEB_OUT_DIR"

echo "=== [2/4] 提交最新原始碼至 main 分支 ==="
cd "$PROJECT_DIR"
git checkout main
git add .
git commit -m "Update game script and assets: $(date '+%Y-%m-%d %H:%M:%S')" || true

echo "=== [3/4] 更新 gh-pages 網頁部署分支 ==="
git checkout gh-pages
git rm -rf . >/dev/null 2>&1 || true
cp -r "$WEB_OUT_DIR"/* .
git add .
git commit -m "Deploy latest Web build: $(date '+%Y-%m-%d %H:%M:%S')" || true

echo "=== [4/4] 推送更新至 GitHub 雲端 ==="
git push origin main gh-pages
git checkout main

echo "=== [完成] 網頁版已全自動同步完成！組員可於 1 分鐘後重新整理網頁遊玩！ ==="
