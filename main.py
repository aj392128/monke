import string
import random
import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

string.ascii_letters
'abcdefghijklmnopqrstuvwxyz'

number = random.randint(0,50)
start_time = time.time()
letter1 = random.choice(string.ascii_letters)
letter2 = random.choice(string.ascii_letters)
letter3 = random.choice(string.ascii_letters)
letter4 = random.choice(string.ascii_letters)
monke = False
list_uwu = [letter1, letter2, letter3, letter4]
file = open('Words.txt')
contents = file.read()
completed_words = 0
completed_sentences = 0
finished_words = []
number_of_words = 0


while monke == False:
 joined = "".join(list_uwu)
 WittSucksAtVideoGames = [' ', joined, ' ']
 joined2 = ''.join(WittSucksAtVideoGames)
       
 if joined2 in contents:
    completed_words = completed_words + 1
    number_of_words = number_of_words + 1
    finished_words.append(joined2)
    print("Found word", number_of_words, joined2)
    letter1 = random.choice(string.ascii_letters)
    letter2 = random.choice(string.ascii_letters)
    letter3 = random.choice(string.ascii_letters)
    letter4 = random.choice(string.ascii_letters)
    number = random.randint(0,50)
    list_uwu = [letter1, letter2, letter3, letter4]

    if number < 30:
      list_uwu = [letter1, letter2, letter3]
    if number == 1:
      list_uwu = [letter1, letter2]

    if (completed_words == 10):
      monke = True
      end_time = time.time()
      time_lapsed = end_time - start_time
      time_convert(time_lapsed)
      im_running_out_of_names = ' '.join(finished_words)
      print(im_running_out_of_names)
      print(time_lapsed)
      completed_words = 0
      with open('Made_words.txt', 'w') as w:
        w.write(im_running_out_of_names)

                  
 else:
    letter1 = random.choice(string.ascii_letters)
    letter2 = random.choice(string.ascii_letters)
    letter3 = random.choice(string.ascii_letters)
    letter4 = random.choice(string.ascii_letters)
    number = random.randint(0,50)
    list_uwu = [letter1, letter2, letter3, letter4]
     
    if number < 15:
      list_uwu = [letter1, letter2, letter3]
    if number == 1:
      list_uwu = [letter1, letter2]
      
        

        
