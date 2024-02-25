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
        'Нг': 'Ng',
        'НГ': 'NG',
        'ЙЮ': 'YYU',
        'Йю': 'Yyu',
        'ЙЁ': 'YYO',
        'Йё': 'Yyo',
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
        'нг': 'ng',
        'ъ': '’',
        'ы': 'i',
        'йю': 'yyu',
        'йё': 'yyo',
        'ь': '',
        'ЪЕ': 'YE',
        'ЪЁ': 'YO',
        'ЪЯ': 'YA',
        'ЪЮ': 'YU',
        'ЬЕ': 'YE',
        'ЬЁ': 'YO',
        'ЬЯ': 'YA',
        'ЬЮ': 'YU',
        'ъе': 'ye',
        'ъё': 'yo',
        'ё': 'yo',
        'Ё': 'YO',
        'ъя': 'ya',
        'ъю': 'yu',
        'ье': 'ye',
        'ьё': 'yo',
        'ья': 'ya',
        'я': 'ya',
        'Я': 'YA',
        'Ю': 'YU',
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
        'O‘': 'Ў',
        'G‘': 'Ғ',
        'SH': 'Ш',
        'Sh': 'Ш',
        'CH': 'Ч',
        'Ch': 'Ч',
        'NG': 'НГ',
        'Ng': 'Нг',
        'NG‘': 'НҒ',
        'Ng‘': 'Нғ',
        'YE': 'Е',
        'YO': 'Ё',
        'YU': 'Ю',
        'YA': 'Я',
        'YO‘': 'ЙЎ',
        'Ye': 'Е',
        'Yo': 'Ё',
        'Yu': 'Ю',
        'Ya': 'Я',
        'Yo‘': 'Йў',
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
        'o': 'о',
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
        'o‘': 'ў',
        'g‘': 'ғ',
        'sh': 'ш',
        'ch': 'ч',
        'ng': 'нг',
        'ng‘': 'нғ',
        'ʼ': 'ъ',
        'ye': 'е',
        'yo': 'ё',
        'yu': 'ю',
        'ya': 'я',
        'yo‘': 'йў',
    }

    result = ""

    if to == "lat":
        letter_replacer = context.replace('Нг','Ng').replace('НГ','NG').replace('ЙЮ','YYU').replace('Йю','Yyu'). \
            replace('ЙЁ','YYO').replace('Йё','Yyo').replace('нг','ng').replace('ъ','’').replace('ы','i'). \
            replace('йю','yyu').replace('йё','yyo').replace('ь','').replace('ЪЕ','YE').replace('ЪЁ','YO'). \
            replace('ЪЯ','YA').replace('ЪЮ','YU').replace('ЬЕ','YE').replace('ЬЁ','YO').replace('ЬЯ','YA'). \
            replace('ЬЮ','YU').replace('ъе','ye').replace('ъё','yo').replace('ъя','ya').replace('ъю','yu').\
            replace('ье','ye').replace('ьё','yo').replace('ья','ya').replace('ю','yu')

        for i in letter_replacer:
            if i in cyr_lat:
                result += cyr_lat[i]
            else:
                result += i
        return result

    elif to == "cyr":
        letter_replacer = context.replace('Oʻ', 'Ў').replace('G‘', 'Ғ').replace('SH', 'Ш').replace('Sh', 'Ш'). \
            replace('CH', 'Ч').replace('Ch', 'Ч').replace('NG', 'НГ').replace('Ng', 'Нг').replace('NG‘', 'НҒ'). \
            replace('Ng‘', 'Нғ').replace('YE', 'Е').replace('YO', 'Ё').replace('YU', 'Ю').replace('YA', 'Я'). \
            replace('YO‘', 'ЙЎ').replace('Ye', 'Е').replace('Yo', 'Ё').replace('Yu', 'Ю').replace('Ya', 'Я'). \
            replace('Yo‘', 'Йў').replace('oʻ', 'ў').replace('gʻ','ғ').replace('sh', 'ш').replace('ch', 'ч').replace('ng', 'нг'). \
            replace('ng‘', 'нғ').replace('ʼ', 'ъ').replace('ye', 'е').replace('yo', 'ё').replace('yu', 'ю'). \
            replace('ya', 'я').replace('yoʻ', 'йў')

        for i in letter_replacer:
            if i in lat_cyr:
                result += lat_cyr[i]
            else:
                result += i
        return result


