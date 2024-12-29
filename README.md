# How to install #

1. mkdir bot
2. cd bot
3. # Install miniconda ##
   A. __Linux__
      mkdir -p ~/miniconda3
      wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
      bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
      rm ~/miniconda3/miniconda.sh
      source ~/miniconda3/bin/activate```
   
   B. __Windows__
      curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
      start /wait "" .\miniconda.exe /S
      del miniconda.exe
   Add the path to the miniconda executable to the windows PATH 

   
4. git clone https://github.com/IIEleven11/tg_ai_bot.git
5. cd tg_ai_bot
6. conda create --name bot python==3.10
7. conda activate tg_ai_bot
8. pip install -r requirements.txt
9. download the LLM and insert its location into the my_bot.py script
10. python my_bot.py
