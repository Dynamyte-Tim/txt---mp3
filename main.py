import gtts  # import the gtts library to convert text to speech
from pathlib import Path  # import Path module from pathlib library to handle file paths
from art import tprint  # import the tprint function from the art library to create ASCII art

# define a function to convert a text file to an MP3 file
def get_file(file_path =r'test.txt', lenguage = 'en'):
    # check if the file exists and has a .txt extension
    if Path(file_path).suffix =='.txt' and Path(file_path).is_file():
        # print message to show that the file is being read
        print(f'The {Path(file_path).stem} file is reading now!')

        # create ASCII art to show the file conversion
        tprint('txt --> mp3', chr_ignore=True)

        # read the text file and replace newline characters with spaces
        with open(file_path, 'r', encoding='utf-8') as file:
            page = file.read()
            pages = page.replace('\n', ' ')

        # get the file_name without the extension
        file_name = Path(file_path).stem

        # use gtts to convert the text to speech and save as an MP3 file
        audio = gtts.gTTS(pages, lang=lenguage)
        audio.save(F'{file_name}.mp3')

        # return message indicating that the file was saved successfully
        return f'File {file_name}.mp3 saved successfully!'

    else:
        # return error message if the file does not exist or does not have a .txt extension
        return 'File isn\'t correct, check path.'

# define a main function to prompt the user for file path and language, and call the get_file function
def main():
    # prompt the user for the file path and language
    print(get_file(input('Write path to your file: '), lenguage=input('Write lenguage for example: en or ru: ')))

# run the main function if this script is being run directly
if __name__ == '__main__':
    main()
