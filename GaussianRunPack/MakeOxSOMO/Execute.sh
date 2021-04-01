#!/bin/bash
python CreateCom.py
bash RunGaussian.sh
python MakeOxInfo.py > ./OxInfo.json
