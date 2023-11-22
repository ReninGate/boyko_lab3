import googletrans as gt

def transLate(text, dest):
    try:
        result = gt.Translator().translate(text,dest=dest,src="auto").text
    except ValueError:
        result = "Не вдалося перекласти текст через невірно введену мову"
    except:
        result = "Помилка!"
    return result

def langDetect(text,set):
    try:
        if set=="lang":
            result = gt.Translator().detect(text)
            result = result.lang
        elif set =="confidence":
            result = gt.Translator().detect(text)
            result = result.confidence
        else:
            result = gt.Translator().detect(text)
        return result
    except Exception as e:
        return str(e)
def codeLang(lang):
    try:
        result = gt.LANGUAGES[lang]
    except:
        try:
            result = gt.LANGCODES[lang]
        except:
            result = "Немає введеного коду чи мови у списках"
    return result

def languageList(out, text):
    try:
        i = 1
        if (out=="screen"):
            print(f"№   Мова                 Код   Переклад")
            for key, value in gt.LANGUAGES.items():
                print(f"{i:<3} {value:<21} {key:<5} " + transLate(text, key))
                i+=1

        elif(out=="file"):
            with open('languageList.txt', 'w' , encoding='utf-8') as file:
                file.write("№   Мова                  Код   Переклад\n")
                for key, value in gt.LANGUAGES.items():
                    file.write(f"{i:<3} {value:<21} {key:<5} " + transLate(text, key) + "\n")
                    i += 1
        else:
            return "Команда введена невірно"
        return "OK"
    except Exception as e:
        return str(e)