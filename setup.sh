export LOGMOJI_PATH=$PWD
echo "alias mlog='git log | python $LOGMOJI_PATH/logmoji.py'" >> ~/.zshrc
source ~/.zshrc
