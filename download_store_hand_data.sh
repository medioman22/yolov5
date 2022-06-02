#!/bin/bash

# hands dataset 

curl -L -q "https://public.roboflow.com/ds/L4HgyEQXXH?key=eZpjwNJLf1" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip

mkdir images
mkdir images/test
mkdir images/train
mkdir images/valid

mkdir labels
mkdir labels/test
mkdir labels/train
mkdir labels/valid

mv test/images/* images/test
mv train/images/* images/train
mv valid/images/* images/valid

mv test/labels/* labels/test
mv train/labels/* labels/train
mv valid/labels/* labels/valid

rm -rf test
rm -rf train
rm -rf valid


ws_dir='/workspace'

mkdir $ws_dir
mkdir $ws_dir/datasets

mkdir $ws_dir/datasets/hand_detect
mv labels $ws_dir/datasets/hand_detect
mv images $ws_dir/datasets/hand_detect