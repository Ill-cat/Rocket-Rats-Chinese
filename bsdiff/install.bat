@echo off
chcp 65001 > nul
title Rocket Rats 汉化补丁安装工具
echo 正在安装汉化补丁...
if not exist "data.win" (
    echo 错误：请将此补丁放在游戏目录下（和 data.win 同目录）！
    pause
    exit
)

echo 备份原版 data.win...
copy "data.win" "data.win.bak"

echo 正在应用汉化补丁...
bspatch.exe data.win data.win data.patch
echo 汉化完成！按任意键退出...
pause >nul