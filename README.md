# tg_ai_bot

1. mkdir bot
2. cd bot
3. Install miniconda linux
   1. mkdir -p ~/miniconda3
      wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
      bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
      rm ~/miniconda3/miniconda.sh
      source ~/miniconda3/bin/activate
4. git clone
5. cd tg_ai_bot
6. conda create --name bot python==3.10
7. conda activate tg_ai_bot
8. pip install -r requirements.txt
9. download the LLM and insert its location into the my_bot.py script
10. python my_bot.py
