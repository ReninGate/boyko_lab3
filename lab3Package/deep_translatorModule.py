import deep_translator as dt
import langdetect


def transLate(text, dest):
    return dt.GoogleTranslator("auto", dest).translate(text)

def langDetect(text,set):
    try:
        lang_info = langdetect.detect_langs(text)
        if(set=="lang"):
            return lang_info[0].lang
        elif(set=="confidence"):
            return lang_info[0].prob
        elif(set=="all"):
            return lang_info
        else:
            return "Не вірно введена команда"
    except Exception as e:
        return str(e)

def codeLang(lang):

    try:
        if(dt.GoogleTranslator().__dict__['_languages'].get(lang)!=None):
            return dt.GoogleTranslator().__dict__['_languages'].get(lang)
        else:
            for key in dt.GoogleTranslator().__dict__['_languages']:
                if( dt.GoogleTranslator().__dict__['_languages'].get(key) == lang):
                    return key
    except Exception as e:
        return str(e)

def languageList(out, text):
    try:
        i = 1
        if (out=="screen"):
            print(f"№   Мова                 Код   Переклад")
            for key, value in dt.GoogleTranslator().__dict__['_languages'].items():
                print(f"{i:<3} {key:<21} {value:<5} " + transLate(text, key))
                i+=1

        elif(out=="file"):
            with open('languageList.txt', 'w' , encoding='utf-8') as file:
                file.write("№   Мова                  Код   Переклад\n")
                for key, value in dt.GoogleTranslator().__dict__['_languages'].items():
                    file.write(f"{i:<3} {key:<21} {value:<5} " + transLate(text, key) + "\n")
                    i += 1
        else:
            return "Команда введена невірно"
        return "OK"
    except Exception as e:
        return str(e)