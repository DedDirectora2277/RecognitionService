import pytesseract
from PIL import Image
from langdetect import detect


def extract_text_from_image(image):
    img = Image.open(image)

    # text_lang = detect_language(img)
    # if text_lang == 'en':
    #     lang_file = '--oem 1 --psm 3 -l eng'
    # elif text_lang == 'ru':
    #     lang_file = '--oem 1 --psm 3 -l rus'
    # else:
    #     lang_file = '--oem 1 --psm 3 -l eng+rus'
    lang_file = '--oem 1 --psm 3 -l eng+rus'

    text = pytesseract.image_to_string(img, config=lang_file)

    # Удаление изображения после обработки
    image.close()  # Закрываем файл, чтобы он мог быть удален
    return text


def detect_language(image):
    text_lang = detect(pytesseract.image_to_string(image))
    return text_lang