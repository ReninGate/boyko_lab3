from lab3Package import deep_translatorModule as dtm

lang = "en"
text = "Створити віртуальне оточення (ім'я оточення - прізвище студента). В цьому оточенні створити проект Python"

print("Оригінальний текст: " + text)
translation = dtm.transLate(text, lang)
print("Переклад:"  + translation)
translationLang = dtm.langDetect(translation, "lang")
print("Код мови перекладу: " + translationLang)
print("Мова перекладу: " + dtm.codeLang(translationLang))
print("Всі мови та переклад на них тексту:")
print(dtm.languageList("screen", text))
