from flask import Blueprint, redirect, render_template, request, url_for
import os
import openai


bp = Blueprint("ai", __name__, url_prefix="/ai")


openai.api_key = "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"


@bp.route("/main", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        programming_topic = request.form["programming_topic"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(programming_topic),
            temperature=0.6,
            max_tokens=500  # 设置生成的最大标记数量
        )
        return redirect(url_for("ai.main", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(programming_topic):
    return """Generate a code example related to {}.

Topic: {}
Code:""".format(
        programming_topic,
        programming_topic.capitalize()
    )
