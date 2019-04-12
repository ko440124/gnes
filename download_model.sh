#!/usr/bin/env bash

set -e

URL_CHINESE_BERT="https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip"
URL_CHINESE_ELMO="https://gnes-1252847528.cos.ap-guangzhou.myqcloud.com/zhs.model.tar.bz2"
URL_GPT="https://gnes-1252847528.cos.ap-guangzhou.myqcloud.com/openai_gpt.tar.bz2"
URL_GPT2="https://gnes-1252847528.cos.ap-guangzhou.myqcloud.com/openai_gpt2.tar.bz2"
URL_TRANSFORMER_XL="https://gnes-1252847528.cos.ap-guangzhou.myqcloud.com/transformer_xl_wt103.tar.bz2"
URL_WORD2VEC="https://gnes-1252847528.cos.ap-guangzhou.myqcloud.com/sgns.wiki.bigram-char.bz2"

wget ${URL_CHINESE_BERT} -qO temp.zip; unzip temp.zip; rm temp.zip

bz2array=($URL_CHINESE_ELMO $URL_GPT $URL_GPT2 $URL_TRANSFORMER_XL $URL_WORD2VEC)

for url in "${array[@]}"
do
    printf "downloading "%${url}
    wget ${url} -qO tmp.tar.bz2; tar -xvjf tmp.tar.bz2; rm tmp.tar.bz2
done