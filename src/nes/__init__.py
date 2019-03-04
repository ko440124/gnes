from typing import Iterator, Dict

from .document import BaseDocument
from .encoder import *
from .helper import set_logger
from .indexer import *

__version__ = '0.0.1'


class BaseNES(BaseIndexer):
    def __init__(self, binary_encoder: BaseBinaryEncoder,
                 binary_indexer: BaseBinaryIndexer,
                 text_indexer: BaseTextIndexer,
                 batch_size: int = 128):
        super().__init__()
        self.binary_encoder = binary_encoder
        self.binary_indexer = binary_indexer
        self.text_indexer = text_indexer
        self.batch_size = batch_size

    def _add_batch(self, batch: List[BaseDocument]):
        sents, ids = list(zip(*[(s, d.id) for d in batch for s in d.sentences]))
        bin_vectors = self.binary_encoder.encode(sents)
        self.binary_indexer.add(bin_vectors, ids)
        self.text_indexer.add(batch)

    @TB._as_train_func
    @TB._timeit
    def train(self, iter_doc: Iterator[BaseDocument], is_tokenized=False) -> None:
        sents = [s for d in iter_doc for s in d.sentences]
        self.binary_encoder.train(sents, is_tokenized)

    @TB._train_required
    def add(self, iter_doc: Iterator[BaseDocument]) -> None:
        cur_batch = []
        for doc in iter_doc:
            cur_batch.append(doc)
            if len(cur_batch) == self.batch_size:
                self._add_batch(cur_batch)
                cur_batch.clear()
        if cur_batch:
            self._add_batch(cur_batch)

    @TB._train_required
    def query(self, keys: List[str], top_k: int) -> List[List[Tuple[Dict, float]]]:
        bin_queries = self.binary_encoder.encode(keys)
        result_score = self.binary_indexer.query(bin_queries, top_k)
        all_ids = list(set(d[0] for id_score in result_score for d in id_score if d[0] >= 0))
        result_doc = self.text_indexer.query(all_ids)
        id2doc = {d_id: d_content for d_id, d_content in zip(all_ids, result_doc)}
        return [[(id2doc[d_id], d_score) for d_id, d_score in id_score] for id_score in result_score]


class DummyNES(BaseNES):
    def __init__(self, *args, **kwargs):
        from .indexer.numpyindexer import NumpyIndexer
        from .encoder.bert_binary import BertBinaryEncoder
        from .indexer.leveldb import LVDBIndexer
        binary_encoder = BertBinaryEncoder(*args, **kwargs)
        binary_indexer = NumpyIndexer(*args, **kwargs)
        text_indexer = LVDBIndexer(*args, **kwargs)
        super().__init__(binary_encoder, binary_indexer, text_indexer)
