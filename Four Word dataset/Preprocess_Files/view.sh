cd ./Preprocess_Files/
rm -rf ./Preprocess_Files/Temp/
sed 's/ [  ]*<.*>//g' < $1/$2/$3.xml > tmp2
tr '\n' '_' < tmp2 > tmp
sed -i 's/____/\n/g' tmp
sed -i 's/_/ /g' tmp
tail -n +2 tmp > tmp2 
mv tmp2 tmp
head -n -1 tmp > tmp2

if [ ! -d Temp  ]; then
    mkdir Temp
fi

mv tmp2 Temp/tmp
rm -f tmp*

./viewkey.sh $1 $2 $3 
