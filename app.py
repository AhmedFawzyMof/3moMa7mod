from flask import Flask, render_template
from gtts import gTTS 
import os,glob
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


with open('./data/Chinese.json', encoding="utf-8") as Chinese:
    Chinese_Lessons = Chinese.read()

Chinese = json.loads(Chinese_Lessons)

with open('./data/Korean.json', encoding="utf-8") as Korean:
    Korean_Lessons = Korean.read()

Korean = json.loads(Korean_Lessons)

with open('./data/Russian.json', encoding="utf-8") as Russian:
    Russian_Lessons = Russian.read()

Russian = json.loads(Russian_Lessons)

with open('./data/Spanish.json', encoding="utf-8") as Spanish:
    Spanish_Lessons = Spanish.read()

Spanish = json.loads(Spanish_Lessons)

with open('./data/Turkish.json', encoding="utf-8") as Turkish:
    Turkish_Lessons = Turkish.read()

Turkish = json.loads(Turkish_Lessons)

with open('./data/French.json', encoding="utf-8") as French:
    French_Lessons = French.read()

French = json.loads(French_Lessons)

with open('./data/German.json', encoding="utf-8") as German:
    German_Lessons = German.read()

German = json.loads(German_Lessons)

with open('./data/Italian.json', encoding="utf-8") as Italian:
    Italian_Lessons = Italian.read()

Italian = json.loads(Italian_Lessons)

russia_flag =  "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/800px-Flag_of_Russia.svg.png?20120812153731";
german_flag =  "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/800px-Flag_of_Germany.svg.png?20111003033442";
china_flag =  "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/255px-Flag_of_the_People%27s_Republic_of_China.svg.png";
france_flag =  "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/250px-Flag_of_France.svg.png";
italy_flag =  "https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/255px-Flag_of_Italy.svg.png";
korea_flag =  "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/255px-Flag_of_South_Korea.svg.png";
spain_flag =  "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Bandera_de_Espa%C3%B1a.svg/200px-Bandera_de_Espa%C3%B1a.svg.png";
turkey_flag =  "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/220px-Flag_of_Turkey.svg.png";


Language = [
  { 'code': "de", 'lang': "German", 'flag': german_flag },
  { 'code': "ru", 'lang': "Russian", 'flag': russia_flag },
  { 'code': "zh-cn", 'lang': "Chinese", 'flag': china_flag },
  { 'code': "fr", 'lang': "French", 'flag': france_flag },
  { 'code': "it", 'lang': "Italian", 'flag': italy_flag },
  { 'code': "ko", 'lang': "Korean", 'flag': korea_flag },
  { 'code': "es", 'lang': "Spanish", 'flag': spain_flag },
  { 'code': "tr", 'lang': "Turkish", 'flag': turkey_flag },
]

app = Flask(__name__)

@app.route("/")
def Languages():
    languages = Language
    return render_template('html/Languages/index.html', languages = languages, len = len(Language))

@app.route('/<lang>')
def Lessons(lang):
    lessons = []
    if lang == 'German':
        for lesson in German:
            lessons.append(lesson['title'])
    
    if lang == 'Russian':
        for lesson in Russian:
            lessons.append(lesson['title'])

    if lang == 'Chinese':
        for lesson in Chinese:
            lessons.append(lesson['title'])
 
    if lang == 'French':
        for lesson in French:
            lessons.append(lesson['title'])
    
    if lang == 'Italian':
        for lesson in Italian:
            lessons.append(lesson['title'])
          
    if lang == 'Korean':
        for lesson in Korean:
            lessons.append(lesson['title'])

    if lang == 'Spanish':
        for lesson in Spanish:
            lessons.append(lesson['title'])

    if lang == 'Turkish':
        for lesson in Turkish:
            lessons.append(lesson['title'])
    
    return render_template('html/Lessons/index.html', lessons = lessons, len = len(lessons), lang = lang)


@app.route('/<lang>/<lesson>')
def Lesson(lang=None,lesson=None):
    lessonNum = int(lesson)
    Thelesson = {}
    code = ''

    if lang == 'German':
       Thelesson = German[lessonNum]
       code = 'de'
    
    if lang == 'Russian':
        Thelesson = Russian[lessonNum]
        code = 'ru'


    if Thelesson == 'Chinese':
        Thelesson = Chinese[lessonNum]
        code = 'zh-CN'

 
    if lang == 'French':
        Thelesson = French[lessonNum]
        code = 'fr'

    
    if lang == 'Italian':
        Thelesson = Italian[lessonNum]
        code = 'it'

          
    if lang == 'Korean':
        Thelesson = Korean[lessonNum]
        code = 'ko'


    if lang == 'Spanish':
        Thelesson = Spanish[lessonNum]
        code = 'es'


    if lang == 'Turkish':
        Thelesson = Turkish[lessonNum]
        code = 'tr'

    conversation = Thelesson['conversation']
    translation = Thelesson['translation']
    arabic = Thelesson['arabic']

    for line in conversation:
        conversationMp3 = gTTS(text=line, lang='en')   
        title = Thelesson['title']
        conversationMp3.save(f'{ROOT_DIR}/static/audio/{title}{conversation.index(line)}(en).mp3')    
    
    for line in translation:
        translationMp3 = gTTS(text=line, lang=code)
        title = Thelesson['title']
        translationMp3.save(f'{ROOT_DIR}/static/audio/{title}{translation.index(line)}({code}).mp3')    


    for line in arabic:
        arabicMp3 = gTTS(text=line, lang='ar')
        title = Thelesson['title']
        arabicMp3.save(f'{ROOT_DIR}/static/audio/{title}{arabic.index(line)}(ar).mp3')

    Tlesson = json.dumps(Thelesson)
    return render_template('html/Lesson/Index.html', lesson = Tlesson, lang = lang, code = code,title=Thelesson['title'])


@app.route('/remove',methods = ['POST'])
def remove():
    print('ok i will remove it')

    files = glob.glob(f'{ROOT_DIR}/static/audio/*')
    for f in files:
        os.remove(f)

    return 
    

    

app.run()