from difflib import SequenceMatcher

def string_match(str1, str2):
    matcher = SequenceMatcher(None, str1, str2)
    return matcher.ratio()

str1 = "Тойвонен Е.Б."
str2 = "Тойвенен  Е.Б"

ratio = string_match(str1, str2)
print('Процент совпадения между "{0}" и "{1}" составляет {2}'.format(str1, str2, ratio))