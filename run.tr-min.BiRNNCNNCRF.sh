python main.py \ 
    --train=/content/targer/data/NER/tr-min/train.txt \
    --dev=/content/targer/data/NER/tr-min/dev.txt \
    --test=data/NER/tr-min/test.txt \
    --model=BiRNNCNNCRF \
    --elm-fn=/content/targer/embeddings/newscor.lower.vec \
    --elm-dim=200 \
    --epoch-num=10 
