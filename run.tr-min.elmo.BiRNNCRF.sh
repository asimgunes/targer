python main.py \ 
    --train data/NER/tr-min/train.txt \
    --dev data/NER/tr-min/dev.txt \
    --test data/NER/tr-min/test.txt \
    --model BiRNNCRF \
    --emb-type elmo \
    --elm-fn embeddings/newscor.lower.vec \
    --elm-dim 200 \
    --epoch-num 10 
