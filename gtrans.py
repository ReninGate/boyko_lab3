from lab3Package import googletransModule as gtm

lang = "en"
text = "Створити віртуальне оточення (ім'я оточення - прізвище студента). В цьому оточенні створити проект Python"

print("Оригінальний текст: " + text)
translation = gtm.transLate(text, lang)
print("Переклад:"  + translation)
translationLang = gtm.langDetect(translation, lang)
print("Код мови перекладу: " + str(translationLang))
print("Мова перекладу: " + gtm.codeLang(translationLang.lang))
print("Всі мови та переклад на них тексту:")
print(gtm.languageList("screen", text))
