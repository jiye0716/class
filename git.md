# Git

git bash 貼上 : Shift+Ins

- 版本控制系統
- 共同開發

### github repo：存放 project 的地方

---

### git config --global user.name "xxxxx"

### git config --global user.email xxxxxxx@example.com

### git init

    (initial)初始化repo

### git pull

    從遠端repo拉取回本地（同步）

### git clone

    從遠端repo複製資料

### git status

    顯示修改檔案清單
    -s：僅會顯示已修改的檔案名稱

### git add .

    git add <檔案名稱>
    將子目錄裡的所有檔案註冊到索引裡

### git commit

    -a : 有修改的檔案(不包括新增的檔案)，將其加入索引並提交。
    -m : 提交訊息

### git push

    從本地推送到遠端
    git push origin master 本地master分支推一份到origin節點
    git push -u origin master 把預設remote都設成origin

### git reset -- <file name>

    把add的檔案unstage回去

### git checkout -- <file>

    把檔案回到上次commit的狀態

### git reset --soft HEAD~1

    往前退一個commit(保留修改的部分）

### git rm

    remove

### git remote add <自訂名稱> <網址>

    把這個網址加到你的remote
    git remote add origin xxx.github

### git remote

    查看所有remote

---

## 設定 ssh 連線

### ssh -keygen

    產生公鑰與私鑰

### cd /c/Users/

### ls -al

    顯示目錄下物件

### cat id_rsa.pub

    顯示內容

---

## 建立電腦端 New repo

### mkdir 建立新資料夾

    code . 開啟vscode

### git init 初始化 repo

### git add .

### git commit(電腦)

### 建立 Github new repo

### git remote add https://github.com/xxx

### git push 推到 github

---

# branch (分支)

## git checkout -b <branch name>

    建立新branch並切換過去

## git branch

    查看電腦上的branch
    git branch -a 查看所有branch(include remote)

---

## Create new branch

### makir

### git clone xxx.com

### git checkout -b <branch name>

### git branch 查看電腦上的 branch

    git branch -a (include remote)

---

## branch 整合回 master ( github 上 merge)

## Pull request

---

### 如果有衝突-不能 automatically merge

### git switch master (東西需做完)

### git pull (origin)

### git switch 新 branch

### git rebase <要 rebase 到哪個分支>

    把目前分支的起始點移到最新進度

### 解衝突

### git rebase --continue

    解完衝突繼續Rebase

### git push -f

    強制push (改變歷史)
    不要在主要master

### merge pull request (github)

### git branch -d <branch name>

    刪除電腦上的branch

---

## 新 branch 整合回 master (在電腦上 merge)

---

### 新 branch commit 完

### 切回 master

### git merge <要整併的分支>

    把目前分支整併到另一分支
    做完後現在的分支會消失

### 如果原本的分支有新版本 merge 完 push 會出現衝突

### git pull

### 解決 confilct

### git commit

### git push

---
