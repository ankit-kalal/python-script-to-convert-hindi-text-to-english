isRightTurnVowel = False
isZPronunciation = False
isUpDot = False

hindiText = "ग़ज़ब ख़ास मेरे साथिया सागर मातृत्व अनिरुद्ध पुष्पा कृष्णा गृहस्थाश्रम"

englishText = []

hindiToEnglishMap = {
    'अ': 'a',
    'आ': 'aa',
    'इ': 'i',
    'ई': 'yi',
    'उ': 'u',
    'ऊ': 'oo',
    'ऋ': 'ri',
    'ॠ': 'ree',
    'ए': 'e',
    'ऐ': 'ai',
    'ओ': 'o',
    'औ': 'au',
    'अं': 'am',
    'अः': 'ah',
    'ॐ': 'om',
    'ऑ': 'a',
    'ा': 'aa',
    'ि': 'i',
    'ी': 'ee',
    'ु': 'u',
    'ू': 'oo',
    'े': 'e',
    'ै': 'ai',
    'ो': 'o',
    'ौ': 'au',
    'ं': 'n',
    'ः': 'ah',
    'ँ': 'n',
    'ृ': 'ru',
    '्': '_',
    '़': '_',
    'क': 'ka',
    'ख': 'kha',
    'ग': 'ga',
    'घ': 'gha',
    'ङ': 'nga',
    'च': 'cha',
    'छ': 'chha',
    'ज': 'ja',
    'झ': 'jha',
    'ञ': 'nya',
    'ट': 'ta',
    'ठ': 'tha',
    'ड': 'da',
    'ढ': 'dha',
    'ण': 'na',
    'त': 'ta',
    'थ': 'tha',
    'द': 'da',
    'ध': 'dha',
    'न': 'na',
    'प': 'pa',
    'फ': 'pha',
    'ब': 'ba',
    'भ': 'bha',
    'म': 'ma',
    'य': 'ya',
    'र': 'ra',
    'ल': 'la',
    'व': 'va',
    'श': 'sha',
    'ष': 'sha',
    'स': 'sa',
    'ह': 'ha',
    'ळ': 'la',
    'क्ष': 'ksa',
    'श्र': 'sra',
    ' ': ' '
}

hindiToEnglishVowelsMap = {
    'ा': 'aa',
    'ि': 'i',
    'ी': 'ee',
    'ु': 'u',
    'ू': 'oo',
    'े': 'e',
    'ै': 'ai',
    'ो': 'o',
    'ौ': 'au',
    'ं': 'n',
    'ः': 'ah',
    'ँ': 'n',
    'ृ': 'ru',
    '्': '_',
    '़': '_',
    'क': 'k',
    'ख': 'kh',
    'ग': 'g',
    'घ': 'gh',
    'ङ': 'ng',
    'च': 'ch',
    'छ': 'chh',
    'ज': 'j',
    'झ': 'jh',
    'ञ': 'ny',
    'ट': 't',
    'ठ': 'th',
    'ड': 'd',
    'ढ': 'dh',
    'ण': 'n',
    'त': 't',
    'थ': 'th',
    'द': 'd',
    'ध': 'dh',
    'न': 'n',
    'प': 'p',
    'फ': 'ph',
    'ब': 'b',
    'भ': 'bh',
    'म': 'm',
    'य': 'y',
    'र': 'r',
    'ल': 'l',
    'व': 'v',
    'श': 'sh',
    'ष': 'sh',
    'स': 's',
    'ह': 'h',
    'ळ': 'l',
    'क्ष': 'ks',
    'श्र': 'sr',
    'अ': 'a',
    'आ': 'aa',
    'इ': 'i',
    'ई': 'yi',
    'उ': 'u',
    'ऊ': 'oo',
    'ऋ': 'ri',
    'ॠ': 'ree',
    'ए': 'e',
    'ऐ': 'ai',
    'ओ': 'o',
    'औ': 'au',
    'अं': 'am',
    'अः': 'ah',
    'ॐ': 'om',
    'ऑ': 'a',
    ' ': ' '
}

rightSlipVowelConvert = {
    'ी': 'i',
    'ू': 'u',
    'ा': 'a',
    'ि': 'i',
    'ु': 'u',
    'े': 'e',
    'ै': 'ai',
    'ो': 'o',
    'ौ': 'au',
    'ं': 'n',
    'ः': 'ah',
    'ँ': 'n',
    'ृ': 'ru',
    '्': '_',
    '़': '_',
    'क': 'k',
    'ख': 'kh',
    'ग': 'g',
    'घ': 'gh',
    'ङ': 'ng',
    'च': 'ch',
    'छ': 'chh',
    'ज': 'j',
    'झ': 'jh',
    'ञ': 'ny',
    'ट': 't',
    'ठ': 'th',
    'ड': 'd',
    'ढ': 'dh',
    'ण': 'n',
    'त': 't',
    'थ': 'th',
    'द': 'd',
    'ध': 'dh',
    'न': 'n',
    'प': 'p',
    'फ': 'ph',
    'ब': 'b',
    'भ': 'bh',
    'म': 'm',
    'य': 'y',
    'र': 'r',
    'ल': 'l',
    'व': 'v',
    'श': 'sh',
    'ष': 'sh',
    'स': 's',
    'ह': 'h',
    'ळ': 'l',
    'क्ष': 'ks',
    'श्र': 'sr',
    'अ': 'a',
    'आ': 'aa',
    'इ': 'i',
    'ई': 'yi',
    'उ': 'u',
    'ऊ': 'oo',
    'ऋ': 'ri',
    'ॠ': 'ree',
    'ए': 'e',
    'ऐ': 'ai',
    'ओ': 'o',
    'औ': 'au',
    'अं': 'am',
    'अः': 'ah',
    'ॐ': 'om',
    'ऑ': 'a',
    ' ': ' '
}

zPronunciationConvert = {
    '़': 'a',
    'ं': 'an',
    'ी': 'i',
    'ू': 'u',
    'ा': 'a',
    'ि': 'i',
    'ु': 'u',
    'े': 'e',
    'ै': 'ai',
    'ो': 'o',
    'ौ': 'au',
    'ः': 'ah',
    'ँ': 'n',
    'ृ': 'ru',
    '्': '_',
    'क': 'q',
    'ख': 'kh',
    'ग': 'gh',
    'घ': 'gh',
    'ङ': 'ng',
    'च': 'ch',
    'छ': 'chh',
    'ज': 'z',
    'झ': 'zh',
    'ञ': 'ny',
    'ट': 't',
    'ठ': 'th',
    'ड': 'd',
    'ढ': 'dh',
    'ण': 'n',
    'त': 't',
    'थ': 'th',
    'द': 'd',
    'ध': 'dha',
    'न': 'n',
    'प': 'p',
    'फ': 'f',
    'ब': 'b',
    'भ': 'bh',
    'म': 'm',
    'य': 'y',
    'र': 'r',
    'ल': 'l',
    'व': 'v',
    'श': 'sh',
    'ष': 'sh',
    'स': 's',
    'ह': 'h',
    'ळ': 'l',
    'क्ष': 'ks',
    'श्र': 'sr',
    'अ': 'a',
    'आ': 'aa',
    'इ': 'i',
    'ई': 'yi',
    'उ': 'u',
    'ऊ': 'oo',
    'ऋ': 'ri',
    'ॠ': 'ree',
    'ए': 'e',
    'ऐ': 'ai',
    'ओ': 'o',
    'औ': 'au',
    'अं': 'am',
    'अः': 'ah',
    'ॐ': 'om',
    'ऑ': 'a',
    ' ': ' '
}

upDotConvert = {
    'ं': 'n',
    '़': 'a',
    'ी': 'i',
    'ू': 'u',
    'ा': 'a',
    'ि': 'i',
    'ु': 'u',
    'े': 'e',
    'ै': 'ai',
    'ो': 'o',
    'ौ': 'au',
    'ः': 'ah',
    'ँ': 'n',
    'ृ': 'ru',
    '्': '_',
    'क': 'ka',
    'ख': 'kha',
    'ग': 'ga',
    'घ': 'gha',
    'ङ': 'ng',
    'च': 'cha',
    'छ': 'chha',
    'ज': 'za',
    'झ': 'zha',
    'ञ': 'nya',
    'ट': 'ta',
    'ठ': 'tha',
    'ड': 'da',
    'ढ': 'dha',
    'ण': 'na',
    'त': 'ta',
    'थ': 'tha',
    'द': 'da',
    'ध': 'dha',
    'न': 'na',
    'प': 'pa',
    'फ': 'fa',
    'ब': 'ba',
    'भ': 'bha',
    'म': 'ma',
    'य': 'ya',
    'र': 'ra',
    'ल': 'la',
    'व': 'va',
    'श': 'sha',
    'ष': 'sha',
    'स': 'sa',
    'ह': 'ha',
    'ळ': 'la',
    'क्ष': 'ksa',
    'श्र': 'sra',
    'अ': 'a',
    'आ': 'aa',
    'इ': 'i',
    'ई': 'yi',
    'उ': 'u',
    'ऊ': 'oo',
    'ऋ': 'ri',
    'ॠ': 'ree',
    'ए': 'e',
    'ऐ': 'ai',
    'ओ': 'o',
    'औ': 'au',
    'अं': 'am',
    'अः': 'ah',
    'ॐ': 'om',
    'ऑ': 'a',
    ' ': ' '
}




# Dictionary for Hindi characters transliteration
hindi_to_english_characters = {
    'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ii', 'उ': 'u', 'ऊ': 'uu', 'ऋ': 'r', 'ॠ': 'rr', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
    'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ng', 'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny', 'ट': 't', 'ठ': 'th',
    'ड': 'd', 'ढ': 'dh', 'ण': 'n', 'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n', 'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh',
    'म': 'm', 'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh', 'ष': 'ss', 'स': 's', 'ह': 'h', 'ळ': 'l', 'क्ष': 'ksh', 'ज्ञ': 'gy',
    'ं': 'ng', 'ः': 'h', '्': '', '।': '|', '॥': '||'
}

# Dictionary for Hindi matras (vowel marks) transliteration
hindi_to_english_matras = {
    'ा': 'aa', 'ि': 'i', 'ी': 'ii', 'ु': 'u', 'ू': 'uu', 'ृ': 'ru', 'ॄ': 'rr', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', 'ं': 'ng', 'ः': 'h', '्': ''
}



def hindi_to_english_transliteration(hindi_text):
    english_text = ''
    hindi_text.replace('्', '').replace('़', '').replace('_', '')

    i = 0
    n = len(hindi_text)
  
    while i < len(hindi_text):
        next_char = None
        char = hindi_text[i]

        if char in ('्','़','_'):
            i += 1
            continue

        if char == ' ':
            english_text += ' '
            i += 1
            continue

        try:
            next_char = hindi_text[i+1]
            if next_char not in ('्','़','_'):
                pass
            else:
                next_char = hindi_text[i+2]
                i = i + 1
        except IndexError:
            pass
        
        english_text += hindi_to_english_characters[char]

        if next_char and next_char in hindi_to_english_matras.keys():
            english_text += hindi_to_english_matras[next_char]
            next_char = None
            i = i + 1
        else:
            if i < n-1 and next_char != ' ':
                english_text += 'a'

        i = i + 1

    return english_text

input_text = "ग़ज़ब ख़ास मेरे साथिया सागर मातृत्व अनिरुद्ध पुष्पा कृष्णा गृहस्थाश्रम"
input_text = "ग़ज़ब ख़ास मेरे साथिया सागर मातृत्व अनिरुद्ध पुष्पा कृष्णा गृहस्थाश्रम "
output_text = hindi_to_english_transliteration(input_text)
print("Input:  ", input_text)
print("Output: ", output_text)
