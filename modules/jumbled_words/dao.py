from modules.common.word_dictionary import word_dictionary

def get_all_words_for_level(level,set_lang,target_lang):
    words = word_dictionary[level]
    words_for_level = {}
    if target_lang == 'en':
        for word in words:
            words_for_level[word['meanings'][set_lang]] = word['english_word']
    elif set_lang == 'en':
        for word in words:
            words_for_level[word['english_word']] = word['meanings'][target_lang]
    else:
        for word in words:
            words_for_level[word['meanings'][set_lang]] = word['meanings'][target_lang]
    return words_for_level

print(get_all_words_for_level(level='1',set_lang='mr',target_lang='hi'))











