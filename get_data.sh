wget http://storage.asmfx.net/nlp/newscor.embeddings.zip
mv newscor.embeddings.zip /embeddings/newscor.embeddings.zip
unzip /embeddings/newscor.embeddings.zip
mkdir data/NER/tr-source
mkdir data/NER/tr-full
mkdir data/NER/tr-min
wget http://storage.asmfx.net/nlp/ner-tr.zip
cp ner-tr.zip data/NER/tr-source/ner-tr.zip
unzip data/NER/tr-source/ner-tr.zip

python create-dataset.py data/NER/tr-source/train.txt data/NER/tr-full/train.txt 0 100000
python create-dataset.py data/NER/tr-source/test.txt data/NER/tr-full/dev.txt 0 500
python create-dataset.py data/NER/tr-source/test.txt data/NER/tr-full/test.txt 501 1000

python create-dataset.py data/NER/tr-source/train.txt data/NER/tr-min/train.txt 0 1000
python create-dataset.py data/NER/tr-source/train.txt data/NER/tr-min/dev.txt 10000 200
python create-dataset.py data/NER/tr-source/train.txt data/NER/tr-min/test.txt 11000 200