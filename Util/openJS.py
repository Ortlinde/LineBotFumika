# open javaScript file
def js_from_file(file_name):
    """
    讀取js檔案
    :return:
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result