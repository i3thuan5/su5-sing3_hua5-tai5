import json

from flask import Flask
from taihua import ik
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


app = Flask(__name__)


@app.route("/<hunsu>")
def 標記(hunsu):
    return json.dumps(
        ik(
            拆文分析器.分詞句物件(hunsu),
        ),
        indent=2, ensure_ascii=False, sort_keys=True
    )
