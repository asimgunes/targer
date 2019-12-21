python main.py \ 
    --train=/content/targer/data/NER/tr-full/train.txt \
    --dev=/content/targer/data/NER/tr-full/dev.txt \
    --test=/content/targer/data/NER/tr-full/test.txt \
    --model=BiRNNCNNCRF \
    --elm-fn=/content/targer/embeddings/newscor.lower.vec \
    --elm-dim=200 \
    --epoch-num=10 
