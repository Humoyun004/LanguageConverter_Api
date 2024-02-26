import re


def transliterate(context: str, from_: str, to: str):
    '''
    context -> str oladi, text kritiladi o'zgartirilishi kerak bo'lgan
    from_ -> str oladi,bu yerga o'zgartirilayotgan til kritiladi
    to -> str oladi u ham, bu yerga esa o'zgartirilishi kerak bo'lgan til kritiladi

    result: ham str holatda qaytadi va yana.
    '''

    cyr_lat = {
        '«': '“',
        '»': '”',
        'А': 'A',
        'Б': 'B',
        'Д': 'D',
        'Э': 'E',
        'Ф': 'F',
        'Г': 'G',
        'Ҳ': 'H',
        'И': 'I',
        'Ж': 'J',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Қ': 'Q',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'В': 'V',
        'Х': 'X',
        'Й': 'Y',
        'З': 'Z',
        'Ў': 'O‘',
        'Ғ': 'G‘',
        'Ш': 'Sh',
        'Ч': 'Ch',
        'а': 'a',
        'б': 'b',
        'д': 'd',
        'e': 'e',
        'Е': 'Е',
        'ф': 'f',
        'г': 'g',
        'ҳ': 'h',
        'и': 'i',
        'ж': 'j',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'қ': 'q',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'в': 'v',
        'х': 'x',
        'й': 'y',
        'з': 'z',
        'ў': 'o‘',
        'ғ': 'g‘',
        'ш': 'sh',
        'ч': 'ch',
        'ъ': '’',
        'ы': 'i',
        'ь': '',
        'я': 'ya',
        'Я': 'YA',
        'Ю': 'YU',
        'ю': 'yu',
        'ё': 'yo',
        'Ё': 'YO',
    }

    lat_cyr = {
        'A': 'А',
        'B': 'Б',
        'D': 'Д',
        'F': 'Ф',
        'G': 'Г',
        'H': 'Ҳ',
        'I': 'И',
        'J': 'Ж',
        'K': 'К',
        'L': 'Л',
        'M': 'М',
        'N': 'Н',
        'O': 'О',
        'P': 'П',
        'Q': 'Қ',
        'R': 'Р',
        'S': 'С',
        'T': 'Т',
        'U': 'У',
        'V': 'В',
        'X': 'Х',
        'Y': 'Й',
        'Z': 'З',
        'a': 'а',
        'b': 'б',
        'd': 'д',
        'f': 'ф',
        'g': 'г',
        'h': 'ҳ',
        'i': 'и',
        'j': 'ж',
        'k': 'к',
        'l': 'л',
        'm': 'м',
        'n': 'н',
        'p': 'п',
        'q': 'қ',
        'r': 'р',
        's': 'с',
        't': 'т',
        'u': 'у',
        'v': 'в',
        'x': 'х',
        'y': 'й',
        'z': 'з',
    }

    result = ""

    if to == "lat":
        letter_replacer = re.sub(r"(НГ|Нг)", "Ng", context)
        letter_replacer = re.sub(r"ЙЮ", "YYU", letter_replacer)
        letter_replacer = re.sub(r"Йю", "Yyu", letter_replacer)
        letter_replacer = re.sub(r"ЙЁ", "YYO", letter_replacer)
        letter_replacer = re.sub(r"Йё", "Yyo", letter_replacer)
        letter_replacer = re.sub(r"ЪЁ", "YO", letter_replacer)
        letter_replacer = re.sub(r"ЪЕ", "YE", letter_replacer)
        letter_replacer = re.sub(r"ЪЯ", "YA", letter_replacer)
        letter_replacer = re.sub(r"ЪЮ", "YU", letter_replacer)
        letter_replacer = re.sub(r"ЬЁ", "YO", letter_replacer)
        letter_replacer = re.sub(r"ЬЕ", "YE", letter_replacer)
        letter_replacer = re.sub(r"ЬЯ", "YA", letter_replacer)
        letter_replacer = re.sub(r"ЬЮ", "YU", letter_replacer)
        letter_replacer = re.sub(r"нг", "ng", letter_replacer)
        letter_replacer = re.sub(r"йю", "yyu", letter_replacer)
        letter_replacer = re.sub(r"йё", "yyo", letter_replacer)
        letter_replacer = re.sub(r"ъё", "yo", letter_replacer)
        letter_replacer = re.sub(r"ъе", "ye", letter_replacer)
        letter_replacer = re.sub(r"ъя", "ya", letter_replacer)
        letter_replacer = re.sub(r"ъю", "yu", letter_replacer)
        letter_replacer = re.sub(r"ьё", "yo", letter_replacer)
        letter_replacer = re.sub(r"ье", "ye", letter_replacer)
        letter_replacer = re.sub(r"ья", "ya", letter_replacer)
        letter_replacer = re.sub(r"ью", "yu", letter_replacer)

        for i in letter_replacer:
            if i in cyr_lat:
                result += cyr_lat[i]
            else:
                result += i
        return result

    elif to == "cyr":
        letter_replacer = re.sub(r"(Oʻ|O'|O‘)", "Ў", context)
        letter_replacer = re.sub(r"(SH|Sh)", "Ш", letter_replacer)
        letter_replacer = re.sub(r"(CH|Ch)", "Ч", letter_replacer)
        letter_replacer = re.sub(r"(NG|Ng)", "НГ", letter_replacer)
        letter_replacer = re.sub(r"NG'", "НҒ", letter_replacer)
        letter_replacer = re.sub(r"(Gʻ|G'|G‘)", "Ғ", letter_replacer)
        letter_replacer = re.sub(r"(YE|Ye)", "E", letter_replacer)
        letter_replacer = re.sub(r"(YO|Yo)", "Ё", letter_replacer)
        letter_replacer = re.sub(r"(YU|Yu)", "Ю", letter_replacer)
        letter_replacer = re.sub(r"(YA|Ya)", "Я", letter_replacer)
        letter_replacer = re.sub(r"(YO'|Yo')", "ЙЎ", letter_replacer)
        letter_replacer = re.sub(r"(oʻ|o'|o‘)", "ў", letter_replacer,)
        letter_replacer = re.sub(r"sh", "ш", letter_replacer)
        letter_replacer = re.sub(r"ch", "ч", letter_replacer)
        letter_replacer = re.sub(r"ng", "нг", letter_replacer)
        letter_replacer = re.sub(r"ng'", "НҒ", letter_replacer)
        letter_replacer = re.sub(r"(gʻ|g'|g‘)", "ғ", letter_replacer,)
        letter_replacer = re.sub(r"( ʻ|'|‘|’)", "ъ", letter_replacer)
        letter_replacer = re.sub(r"(ye)", "е", letter_replacer)
        letter_replacer = re.sub(r"(yo)", "ё", letter_replacer)
        letter_replacer = re.sub(r"(yu)", "ю", letter_replacer)
        letter_replacer = re.sub(r"(ya)", "я", letter_replacer)
        letter_replacer = re.sub(r"yo'", "йў", letter_replacer)

        for i in letter_replacer:
            if i in lat_cyr:
                result += lat_cyr[i]
            else:
                result += i
        return result


