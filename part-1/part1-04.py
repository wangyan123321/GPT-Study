import numpy as np
import gensim

print("加载fasttext模型中...")
model = gensim.models.fasttext.load_facebook_model('cc.en.300.bin.gz')
print("加载fasttext模型完成")


def gen_fasttext_vetor(line):
    print("正在生成fasttext向量")
    vector = np.zeros(300)
    for word in line.split():
        vector += model.wv[word]
    vector /= len(line.split())
    print("生成fasttext向量完成")
    return vector


positive_text = """
Wanted to save some to bring to my Chicago family but my North Carolina family ate all 4 boxes before I could pack.
 These are excellent...could serve to anyone
 """
positive_example_in_fasttext = gen_fasttext_vetor(positive_text)

print(positive_example_in_fasttext)
