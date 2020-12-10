echo BD103 Personal Package
echo Enter CMD

read cmd

if [ $cmd == "build" ]; then
  bash cmd/build.sh
fi

if [ $cmd == "rm" ]; then
  bash cmd/rm.sh
fi

if [ $cmd == "pip" ]; then
  bash cmd/pip.sh
fi

if [ $cmd == "deploy" ]; then
  bash cmd/deploy.sh
fi

if [ $cmd == "test" ]; then
  python3 main.py
fi

if [ $cmd == "newtest" ]; then
  bash cmd/newtest.sh
fi
