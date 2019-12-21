python main.py \ 
    --train=/content/targer/data/NER/tr-min/train.txt \
    --dev=/content/targer/data/NER/tr-min/dev.txt \
    --test=/content/targer/data/NER/tr-min/test.txt \
    --model=BiRNNCNNCRF \
    --emb-type=elmo \
    --elm-fn=/content/targer/embeddings/newscor.lower.vec \
    --elm-dim=1024 \
    --epoch-num=10 
