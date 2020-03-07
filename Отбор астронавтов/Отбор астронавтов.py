from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 class="text-center">Анкета претендента</h1>
                            <h3 class="text-center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                
                                    <input class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input class="form-control" id="surname" placeholder="Введите Фамилию" name="surname">
                                    </br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="obrSelect">Какое у вас образование</label>
                                        <select class="form-control" id="obrSelect" name="obr">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <label for="obrSelect">Какие у вас есть профессии</label>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="professia" id="isl" value="isl">
                                          <label class="form-check-label" for="isl">
                                            Инженер-исследователь
                                          </label>
                                    </div>
                                    
                                    <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="professia" id="stro" value="stro">
                                          <label class="form-check-label" for="stro">
                                            Инженер-строитель
                                          </label>
                                    </div>
                                    
                                    <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="professia" id="pil" value="pil">
                                          <label class="form-check-label" for="pil">
                                            Пилот
                                          </label>
                                    </div>
                                    
                                    <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="professia" id="met" value="met">
                                          <label class="form-check-label" for="met">
                                            Метеоролог
                                          </label>
                                    </div>
                                    
                                    <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="professia" id="zizn" value="zizn">
                                          <label class="form-check-label" for="zizn">
                                            Инженер по жизнеобеспечиванию
                                          </label>
                                    </div>
                                    
                                    <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="professia" id="rad" value="rad">
                                          <label class="form-check-label" for="rad">
                                            Инженер по радиационной защите
                                          </label>
                                    </div>
                                    
                                    <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="professia" id="vr" value="vr">
                                          <label class="form-check-label" for="vr">
                                            Врач
                                          </label>
                                    </div>
                                    
                                    <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="professia" id="ekz" value="ekz">
                                          <label class="form-check-label" for="ekz">
                                            Экзобиолог
                                          </label>
                                    </div>
                                     
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['professia'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')