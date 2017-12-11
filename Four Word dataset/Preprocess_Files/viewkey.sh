#!/bin/bash 
sed 's/.*%//g' $1/$2/$3.key > Temp/tmpkey
perl -pe 's|.*?:||' Temp/tmpkey > tmp2
#perl -pe 's|.*?:||' tmp2 > Temp/tmpkey 
rm tmp2
#sed -i 's/:://g' Temp/tmpkey
python viewkey.py $3
cd ../

