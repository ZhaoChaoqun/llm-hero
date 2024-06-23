# 自己实现一个BPE的tokenizer

class BpeTokenizer():

# 词汇表，记录每个Token的词频
    vocabulary = dict()
# 每行的文本
    lines = list()

    def __init__(self, corpus):
        super()
        self.corpus = corpus
        self.preprocess(corpus)
        # 开始循环组合每个词频最高的pair，直到频率最高的pair的频率小于某个阈值（1）
        # for i in range(10):
        while True:
            max_pair = self.count_pairs()
            if max_pair[1] <= 1:
                break
            self.vocabulary[max_pair[0]] = max_pair[1]
            self.merge_pair(max_pair[0])
            # print(f'第{i}次合并: {max_pair[0]}')
            self.inspect_vocabulary()
        # print('合并完成')
        self.inspect_vocabulary()

    def merge_pair(self, pair):
        new_lines = list()
        for line in self.lines:
            new_line = list()
            i = 0
            while i < len(line):
                if i + 1 < len(line) and line[i] + line[i + 1] == pair:
                    new_line.append(pair)
                    self.vocabulary[line[i]] -= 1
                    self.vocabulary[line[i + 1]] -= 1
                    if self.vocabulary[line[i]] == 0:
                        del self.vocabulary[line[i]]
                    if self.vocabulary[line[i + 1]] == 0:
                        del self.vocabulary[line[i + 1]]
                    i += 2
                else:
                    new_line.append(line[i])
                    i += 1
            new_lines.append(new_line)
        self.lines = new_lines
        
    def preprocess(self, corpus):
        # 按行切分
        with open(corpus, 'r', encoding='utf-8') as f:
            for _, line in enumerate(f):
                # 删除空行
                if not line.strip():
                    continue
                # 按字符切分
                words = list(line.strip())
                self.lines.append(words)
                # 统计词频，构建词表
                for word in words:
                    if word not in self.vocabulary:
                        self.vocabulary[word] = 1
                    else:
                        self.vocabulary[word] += 1

        print(f'词表大小: {len(self.vocabulary)}, 语料行数: {len(self.lines)}')
        self.inspect_vocabulary()

    def count_pairs(self):
        pair_token = dict()
        for line in self.lines:
            for i in range(len(line) - 1):
                pair = line[i] + line[i + 1]
                if pair not in pair_token:
                    pair_token[pair] = 1
                else:
                    pair_token[pair] += 1
        sorted_vocabulary = sorted(pair_token.items(), key=lambda x: x[1], reverse=True)
        print(sorted_vocabulary[0])
        return sorted_vocabulary[0]

    def inspect_vocabulary(self):
        # 按照vocabulary的value倒序排列，打印前10个key-value
        sorted_vocabulary = sorted(self.vocabulary.items(), key=lambda x: x[1], reverse=True)
        print(sorted_vocabulary[:10])

#     本文转token
    def encode(self, text):
        return ''

#     token复原文本
    def decode(self, token):
        return ''

bpe = BpeTokenizer('./shediaoyingxiongzhuan.txt')
bpe.inspect_vocabulary()