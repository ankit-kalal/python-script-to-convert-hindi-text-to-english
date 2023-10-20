hindi_to_english_characters = {
    'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ii', 'उ': 'u', 'ऊ': 'uu', 'ऋ': 'r', 'ॠ': 'rr', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
    'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ng', 'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny', 'ट': 't', 'ठ': 'th',
    'ड': 'd', 'ढ': 'dh', 'ण': 'n', 'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n', 'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh',
    'म': 'm', 'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh', 'ष': 'ss', 'स': 's', 'ह': 'h', 'ळ': 'l', 'क्ष': 'ksh', 'ज्ञ': 'gy',
    'ं': 'ng', 'ः': 'h', '्': '', '।': '|', '॥': '||'
}


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
