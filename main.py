import random
import time
skills = {'Sun-Strike': "eee", 'Tornado': 'qww', "EMP":"www", "Ice Wall": "eeq", 'Ghost Walk':'qqw', 'Forge Spirit':'eeq', 'Deafening Blast': 'qwe', 'Cold Snap': 'qqq', 'Alacrity': 'wwe'}

def main():
    i = 0
    start = time.time()
    while True:
        i += 1
        skill, buttons = random.choice(list(skills.items())) 
        print(skill)
        user = input().lower()
        if i >= 10:
            end  = time.time()
            print ("Your Time is : ")
            print  (end - start)
            break
        else:
            if user == skills[skill]:
                continue
            else:
                print('Error, try again')
                end  = time.time()
                print (end - start)
                break


        
    
main()