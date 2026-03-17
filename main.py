from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# 1. Эта функция обрабатывает ПОЛУЧЕНИЕ данных из формы
@app.route('/second', methods=['GET', 'POST']) # Разрешаем оба метода!
def add_goal():
    if request.method == 'POST':
        user_goal = request.form.get('goal')
        if user_goal:
            with open("goals.txt", "a", encoding="utf-8") as f:
                f.write(user_goal + "\n")
        # После сохранения уходим на страницу со списком
        return redirect('/second_page')
    
    # Если кто-то зашел через GET (ошибка 405 больше не вылетит)
    return redirect('/second_page')

# 2. Эта функция просто ПОКАЗЫВАЕТ список целей
@app.route('/second_page')
def show_goals():
    all_goals = []
    try:
        with open("goals.txt", "r", encoding="utf-8") as f:
            # .strip() убирает лишние переносы строк \n
            all_goals = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        all_goals = []

    now = datetime.now().strftime("%H:%M:%S")
    return render_template('home_page.html', goals=all_goals, current_time=now)

@app.route('/clear', methods=['POST'])
def clear_goals():
    with open("goals.txt", "w", encoding="utf-8") as file:
        file.truncate(0)
    return redirect('/second_page')

if __name__ == '__main__':
    app.run(debug=True)