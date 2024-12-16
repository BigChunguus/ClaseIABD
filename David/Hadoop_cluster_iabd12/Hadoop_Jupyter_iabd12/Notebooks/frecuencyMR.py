#!/usr/bin/python3

from mrjob.job import MRJob
from mrjob.step import MRStep
from collections import Counter
import re

WORD_RE = re.compile(r"[\w']+")


class MRMustUsedWord(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_frecuency)
        ]

    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner_count_words(self, word, counts):
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        yield None, (sum(counts), word)
        
    def reducer_frecuency(self, _, counts):
        sorted_freqs = sorted(counts, key=lambda t: t[0], reverse=True)
        yield None, list(sorted_freqs[0:10])



if __name__ == '__main__':
    MRMustUsedWord.run()
