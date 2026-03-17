from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/second', methods=['GET', 'POST'])
def second_page():
    if request.method == 'POST':
        user_goal = request.form.get('goal')
        # Записываем цель в файл (режим 'a' - append, добавить в конец)
        with open("goals.txt", "a", encoding="utf-8") as f:
            f.write(user_goal + "\n")
    
    # Читаем все цели из файла, чтобы вывести их списком
    all_goals = []
    try:
        with open("goals.txt", "r", encoding="utf-8") as f:
            all_goals = f.readlines()
    except FileNotFoundError:
        all_goals = ["Ancora nessun obiettivo"]

    now = datetime.now().strftime("%H:%M:%S")
    return render_template('home_page.html', goals=all_goals, current_time=now)

if __name__ == '__main__':
    app.run(debug=True)