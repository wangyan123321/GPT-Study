import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")
COMPLETION_MODEL = "text-davinci-003"

prompt = """
商品描述:工厂现货PVC充气青蛙夜市地摊热卖充气玩具发光蛙儿童水上玩具
1.根据商品描述给出商品的一个售卖的标题
2.根据商品描述给出三点商品买点说明
3.根据商品描述预测商品可售卖的价格

将所有描述翻译成中文输出出来
"""


def get_response(prompt) :
    completions = openai.Completion.create(
        engine=COMPLETION_MODEL,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.0,
    )
    message = completions.choices[0].text
    return message

print(get_response(prompt))