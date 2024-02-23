import re


class _CharMapping:
    cyr_lat = {}
    lat_cyr = {}
    cyr_vowel = []
    lat_vowel = []

    def __init__(self):
        self.__initial_data()

    def __initial_data(self):
        self.cyr_vowel = ["а", "и", "э", "у", "ў", "о", "е", "ё", "ю", "я", "А", "И", "Э", "У", "Ў", "О", "Е", "Ё", "Ю", "Я"]
        self.lat_vowel = ["a", "i", "e", "u", "o‘", "o", "A", "I", "E", "U", "O‘", "O"]

        self.cyr_lat = {
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
            'э': 'e',
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
            'ъя': 'ya',
            'ъю': 'yu',
            'ье': 'ye',
            'ьё': 'yo',
            'ья': 'ya',
            'ью': 'yu',
        }

        self.lat_cyr = {
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
            '’': 'ъ',
            'ye': 'е',
            'yo': 'ё',
            'yu': 'ю',
            'ya': 'я',
            'yo‘': 'йў',
        }


class LanguageTransliterator:
    __cmap = {}
    __cyr_vowel = []
    __lat_vowel = []
    __cyr_exwords = {}
    __lat_exwords = {}

    def __init__(self):
        __data = _CharMapping()
        self.__cmap['cyr_lat'] = __data.cyr_lat
        self.__cmap['lat_cyr'] = __data.lat_cyr

        self.__cyr_vowel = __data.cyr_vowel
        self.__lat_vowel = __data.lat_vowel

    def __cyr_rule1(self, word: str, i: int):
        word, i = self.__remove_symbols_starting(word, i)

        e_map1 = {'е': 'e', 'Е': 'E'}
        e_map2 = {'е': 'ye', 'Е': 'Ye'}
        if i == len(word) - 1:
            return e_map1[word[i]]

        if i - 1 >= 0 and i + 1 < len(word):
            if word[i - 1] not in self.__cyr_vowel and word[i + 1] not in self.__cyr_vowel and \
                    word[i - 1] not in ['(', '"', '-', '-', '.', ',', '?', '!']:
                return e_map1[word[i]]

        if i - 1 >= 0:
            if word[i - 1] not in self.__cyr_vowel and word[i - 1] not in ['(', '"', '-', '-', '.', ',', '?', '!']:
                return e_map1[word[i]]

        return e_map2[word[i]]

    def __cyr_rule2(self, word: str, i: int):
        word, i = self.__remove_symbols_starting(word, i)

        s_map1 = {'ц': 'ts', 'Ц': 'TS'}
        s_map2 = {'ц': 's', 'Ц': 'S'}
        if i - 1 >= 0 and i + 1 < len(word):
            if word[i - 1] in self.__cyr_vowel and word[i + 1] in self.__cyr_vowel:
                return s_map1[word[i]]
        return s_map2[word[i]]

    def __cyr_rule3(self, word: str, i: int):
        word, i = self.__remove_symbols_starting(word, i)

        y_map1 = {
            'е': 'е', 'Е': 'E',
            'ё': 'o', 'Ё': 'O',
            'ю': 'u', 'Ю': 'U',
            'я': 'a', 'Я': 'A',
        }
        y_map2 = {
            'е': 'yе', 'Е': 'Ye',
            'ё': 'yo', 'Ё': 'Yo',
            'ю': 'yu', 'Ю': 'Yu',
            'я': 'ya', 'Я': 'Ya',
        }

        if i == len(word) - 1:
            return y_map2[word[i]]

        if i - 1 >= 0 and i != len(word) - 1:
            if word[i] in ['ю', 'Ю', 'я', 'Я'] and word[i - 1] in ['л', 'Л', 'н', 'Н']:
                return y_map2[word[i]]
            if word[i] in ['ё', 'Ё'] and word[i - 1] in ['н', 'Н']:
                return y_map2[word[i]]
            if word[i - 1] not in self.__cyr_vowel:
                return y_map1[word[i]]
        return y_map2[word[i]]

    def __lat_rule1(self, word: str, i: int):
        word, i = self.__remove_symbols_starting(word, i)

        e_map1 = {'e': 'е', 'E': 'Е'}
        e_map2 = {'e': 'э', 'E': 'Э'}

        if i - 1 >= 0 and i + 1 < len(word):
            if not word[i - 1].isalpha():
                return e_map2[word[i]]
            if word[i - 1] not in self.__lat_vowel and word[i + 1] not in self.__lat_vowel:
                return e_map1[word[i]]
            if word[i + 1] in self.__lat_vowel:
                return e_map1[word[i]]
        if i == len(word) - 1:
            return e_map1[word[i]]

        return e_map2[word[i]]

    def __remove_symbols_starting(self, word: str, i: int):
        ni = i
        for ind in range(ni):
            if not word[ind].isalpha():
                i -= 1
                word = word[1:]
            else:
                break
        for ind in range(len(word)-1, i,  -1):
            if not word[ind].isalpha():
                word = word[:-1]
            else:
                break

        return word, i

    def transliterate(self, text, from_: str = 'cyr', to: str = 'lat'):
        sc_map = self.__cmap[from_ + '_' + to]

        if from_ == "lat":
            text = text.replace("g'", "g‘")
            text = text.replace("o'", "o‘")
            text = text.replace("g`", "g‘")
            text = text.replace("o`", "o‘")
            text = text.replace("g’", "g‘")
            text = text.replace("o’", "o‘")
            text = text.replace("gʻ", "g‘")
            text = text.replace("oʻ", "o‘")
            text = text.replace("G'", "G‘")
            text = text.replace("O'", "O‘")
            text = text.replace("G`", "G‘")
            text = text.replace("O`", "O‘")
            text = text.replace("G’", "G‘")
            text = text.replace("O’", "O‘")
            text = text.replace("Gʻ", "G‘")
            text = text.replace("Oʻ", "O‘")
            text = text.replace("'", "’")
            text = text.replace("ʼ", "’")

        tokens = re.findall(r'\S+|\n|\t', text)

        cnv_words = []
        for word in tokens:
            cnv_word = ""
            i = 0
            wl = len(word)

            for c in range(wl):
                i = c
                if word[c].isalpha():
                    break
                else:
                    cnv_word += word[c]

            if i < wl-1:
                for j in range(wl, 2, -1):
                    chunk = word[i:j]

                    if to == "cyr":
                        if chunk.lower() in self.__cyr_exwords:
                            res = self.__cyr_exwords[chunk.lower()]
                            if chunk != chunk.lower():
                                cnv_word += res.capitalize()
                            else:
                                cnv_word += res

                            i = j

                            break

                    if to in ["lat"]:
                        if chunk.lower() in self.__lat_exwords:
                            res = self.__lat_exwords[chunk.lower()]
                            if chunk != chunk.lower():
                                cnv_word += res.capitalize()
                            else:
                                cnv_word += res
                            i += j
                            break

                while i < wl:
                    found = False
                    for j in range(3, 0, -1):
                        chunk = word[i:i+j]

                        if chunk in sc_map:
                            cnv_word += sc_map[chunk]
                            found = True
                            i += j
                            break

                    if not found:
                        catch_in_rule = False
                        if from_ == "cyr":
                            if word[i] in ['е', 'Е']:
                                cnv_word += self.__cyr_rule1(word, i)
                                catch_in_rule = True
                            if word[i] in ['ц', 'Ц']:
                                cnv_word += self.__cyr_rule2(word, i)
                                catch_in_rule = True
                            if word[i] in ['Ё', 'Ю', 'Я', 'ё', 'ю', 'я']:
                                cnv_word += self.__cyr_rule3(word, i)
                                catch_in_rule = True
                        if from_ in ["lat"] and to == "cyr":
                            if word[i] in ['e', 'E']:
                                cnv_word += self.__lat_rule1(word, i)
                                catch_in_rule = True

                        if not catch_in_rule:
                            cnv_word += word[i]

                        i += 1
            cnv_words.append(cnv_word)

        text = ' '.join(cnv_words)

        if from_ == "cyr" and to in ["lat"]:
            text = text.replace(" \*-", "-")
        return text