# リポジトリの概要
2020年度ロボットシステム学の課題2の提出用リポジトリです。  
今日の運勢を占います。
# 動作環境
ubuntu 20.04.1 LTS
# 使用したもの
Raspberry Pi 4
# デモ動画へのリンク
<https://youtu.be/Flp1p2mdYuQ>
# 実行までの流れ
- インストール方法
```
cd ~/catkin_ws/src
git clone https://github.com/Yyoshinuma/mypkg.git
cd ..
catkin_make
source /opt/ros/noetic/setup.bash
```
- 実行方法
```
roslaunch mypkg mypkg.launch
```
# ライセンス
BSD 2-Clause License
