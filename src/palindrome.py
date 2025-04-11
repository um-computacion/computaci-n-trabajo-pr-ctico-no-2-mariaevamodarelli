def is_palindrome(text):
    
    cleaned_text = clean_text(text)

    return compare_characters(cleaned_text)

def clean_text(text):
   
    text = text.lower()

    
    text = text.replace("á", "a").replace("é", "e").replace("í", "i")
    text = text.replace("ó", "o").replace("ú", "u")
    text = text.replace("ü", "u")

    
    cleaned = ""
    for caracter in text:
        if caracter.isalpha():  
            cleaned += caracter

    return cleaned

