import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
# 画像読み込みのために必要
import time


# プログレスバーとは、少しずつバーが伸びていって進捗がわかるやつ（読み込みとかに使う）
# プログレスバーのfor文が完成するまでは、それ以降の処理は行われない
st.write("プログレスバーの表示")
"Start!"

lastest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    lastest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    # progressは進んでいく動きを表す
    time.sleep(0.1)
    # sleepは、その秒数だけ間隔を置く（休止する）という意味

"Done!!"


st.title("streamlit 超入門")

st.write("Data Frame")

df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=2000, height=1000)
# st.writeでもいけるが、長さなどは指定できない
# st.tableを使うと、静的なただの表を表すことができる（長さは指定できない）
# pandasに用意されているhighlightなども使用できる
# axis=0 は列、axis=１は行を指定する際に用いる


# マジックコマンド
"""

# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd 
```

"""

df1 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)

st.map(df1)

# line_chartを用いると、折れ線グラフになる
# area_chartを用いると、折れ線グラフのエリアを塗ってくれる
# bar_chartを用いると、棒グラフになる
# mapを用いると、地図が表示される


st.write("Display Image")

# checkboxを用いて条件分岐をするだけで、checkがあるとtrue,ないとfalseを返してくれる
if st.checkbox("Show Image"):
    # この書き方で画像を呼び出せる　Image .open("画像の場所")
    img = Image.open("sample-author1.jpg")

    st.image(img, caption="Someone", use_column_width=True)
    # use_column_width=Trueこれを使用すると、ページの大きさに合わせて最適な大きさに変更してくれる
    # これと同じような形で、video,audioなども簡単に作成できる


st.sidebar.write("Interactive Widgets")

option = st.sidebar.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1, 11))
)

"あなたの好きな数字は" + str(option) + "です"
# streamlitを使用した場合、printだとターミナルに出力されてしまうのでst.writeを用いる（何もなしでもうまく出力できちゃう）

# .sidebarを指定するだけで、サイドバーに持って来れる
text = st.sidebar.text_input("あなたの趣味を教えてください")

condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
# 最小値、最大値、デフォルト値の順番で値を書く

"あなたの趣味は：", text
"コンディション：", condition


left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を出力する")
if button:
    right_column.write("ボタンが押されました！！")


expander1 = st.expander("問い合わせ１")
expander1.write("問い合わせに対する回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせに対する回答")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせに対する回答")
