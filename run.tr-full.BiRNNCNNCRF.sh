python main.py \ 
    --train=data/NER/tr-full/train.txt \
    --dev=data/NER/tr-full/dev.txt \
    --test=data/NER/tr-full/test.txt \
    --model=BiRNNCNNCRF \
    --elm-fn=embeddings/newscor.lower.vec \
    --elm-dim=200 \
    --epoch-num=10 
