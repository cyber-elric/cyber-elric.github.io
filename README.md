# Github Page

1. 创建新仓库，名字叫**username.github.io**(username指你的GitHub账号名)。添加README.md
这样命名，网页的域名就是：**https://username.github.io**
若命名不是上面那种，那网页域名就会是**https://username.github.io/RepositoryName**



2. 在仓库的Settings里设置GitHub page。



3. 上传网页文件到仓库。GitHub page会自动识别index.html文件
若没有index.html，网页就会显示README.md的内容
GitHub page只支持静态网页。



## GitHub action

1. 在仓库的Actions新建一个workflow。

运行时的文件目录默认应该就是GitHub的仓库的第一层

```
# This is a basic workflow to help you get started with Actions

name: bing_daily_wallpaper

# Controls when the action will run. 
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  # push:
    # branches: [ main ]
  # pull_request:
    # branches: [ main ]
  schedule:
    # minute hour day month week
    - cron: '1 16 * * *'

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest
    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
      
      # set up python environment
      - uses: actions/setup-python@v1
        with:
          python-version: 3.8
      
      - name: requirements
        run: 
          # cd img
          pip install -r requirements.txt
          
      - name: py
        run: 
          # cd img
          python bing.py
          
      - name: commit
        run: |
          git config --local user.email yourEmail@gmail.com
          git config --local user.name yourName
          git add .
          git commit -m 'bing daily wallpaper' -a
     
      # push changes to github    
      - uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

好像每个仓库的workflow自带GITHUB_TOKEN,直接这样用就行，不用自己新建。

如果不行就试一下到仓库的Settings的Secrets新建一个secret名字叫GITHUB_TOKEN
或到个人界面的Settings里的Developer Settings新建一个Personal Access Token,勾选必要的选项，名字叫GITHUB_TOKEN。
