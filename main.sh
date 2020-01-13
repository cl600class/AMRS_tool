for DIRECTORY in output summary
do
    if [ ! -d "$DIRECTORY" ]; then
        mkdir $DIRECTORY
    else
        rm -rf $DIRECTORY/*
    fi
done
echo "Start..."
python3 record.py
python3 convert.py
python3 summarize.py
echo "Finish..."