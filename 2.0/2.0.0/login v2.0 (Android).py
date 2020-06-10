import json
import random
import pdb
import smtplib
import socket


class stat:

    def stat_rps():
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            temp_dict[user_name]["stats"] = {"r_p_s": {"g_p": 0, "g_w": 0, "g_l": 0,"g_t" : 0}}
        with open("/storage/emulated/0/Download/data.json", "w") as user_data:
            json.dump(temp_dict,user_data)

    def stat_guess_num():
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            temp_dict[user_name]["stats"]["guess_num"] = {"g_p": 0, "g_w": 0, "g_l": 0}
        with open("/storage/emulated/0/Download/data.json", "w") as user_data:
            json.dump(temp_dict,user_data)

    def stat_rps_win():
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            g_p = int(temp_dict[user_name]["stats"]["r_p_s"]["g_p"])
            g_w = int(temp_dict[user_name]["stats"]["r_p_s"]["g_w"])
            temp_dict[user_name]["stats"]["r_p_s"]["g_p"] = g_p + 1
            temp_dict[user_name]["stats"]["r_p_s"]["g_w"] = g_w + 1
        with open("/storage/emulated/0/Download/data.json", "w") as user_data:
            json.dump(temp_dict,user_data)

    def stat_guess_num_win():
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            g_p = int(temp_dict[user_name]["stats"]["guess_num"]["g_p"])
            g_w = int(temp_dict[user_name]["stats"]["guess_num"]["g_w"])
            temp_dict[user_name]["stats"]["guess_num"]["g_p"] = g_p + 1
            temp_dict[user_name]["stats"]["guess_num"]["g_w"] = g_w + 1
        with open("/storage/emulated/0/Download/data.json", "w") as user_data:
            json.dump(temp_dict,user_data)

    def stat_rps_lose():
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            g_p = int(temp_dict[user_name]["stats"]["r_p_s"]["g_p"])
            g_l = int(temp_dict[user_name]["stats"]["r_p_s"]["g_l"])
            temp_dict[user_name]["stats"]["r_p_s"]["g_p"] = g_p + 1
            temp_dict[user_name]["stats"]["r_p_s"]["g_l"] = g_l + 1
        with open("/storage/emulated/0/Download/data.json", "w") as user_data:
            json.dump(temp_dict,user_data)

    def stat_guess_num_lose():
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            g_p = int(temp_dict[user_name]["stats"]["guess_num"]["g_p"])
            g_l = int(temp_dict[user_name]["stats"]["guess_num"]["g_l"])
            temp_dict[user_name]["stats"]["guess_num"]["g_p"] = g_p + 1
            temp_dict[user_name]["stats"]["guess_num"]["g_l"] = g_l + 1
        with open("/storage/emulated/0/Download/data.json", "w") as user_data:
            json.dump(temp_dict,user_data)

    def stat_rps_tie():
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            g_p = int(temp_dict[user_name]["stats"]["r_p_s"]["g_p"])
            g_t = int(temp_dict[user_name]["stats"]["r_p_s"]["g_t"])
            temp_dict[user_name]["stats"]["r_p_s"]["g_p"] = g_p + 1
            temp_dict[user_name]["stats"]["r_p_s"]["g_t"] = g_t + 1
        with open("/storage/emulated/0/Download/data.json", "w") as user_data:
            json.dump(temp_dict,user_data)

    def stat_show():
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            print(f"Games \t\t\t\t\tGames Played \tWin \tLose \tTied")
            print(f"\nRock Paper Scissor \t\t\t  {temp_dict[user_name]['stats']['r_p_s']['g_p']}\t\t\t {temp_dict[user_name]['stats']['r_p_s']['g_w']} \t\t  {temp_dict[user_name]['stats']['r_p_s']['g_l']} \t {temp_dict[user_name]['stats']['r_p_s']['g_t']}")
            print(f"\nGuess the Number \t\t\t  {temp_dict[user_name]['stats']['guess_num']['g_p']} \t     {temp_dict[user_name]['stats']['guess_num']['g_w']} \t      {temp_dict[user_name]['stats']['guess_num']['g_l']}")


class User():

    def __init__(self,user_name,password):
        self.user_name = user_name.strip()
        self.password = password.strip()

    def signup(self):
        global temp1
        with open("/storage/emulated/0/Download/data.json","r") as user_data:
            temp_dict = json.load(user_data)
            if self.user_name in temp_dict.keys():
                print("Username Already Exist!")
                temp1 = True
                return
            else:
                temp_dict[self.user_name] = {"password" : self.password}
                temp1 = False
        with open("/storage/emulated/0/Download/data.json","w") as user_data:
            json.dump(temp_dict,user_data)

    def login(self):
        global temp2
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            x = json.load(user_data)
            if self.user_name in x.keys():
                if x[self.user_name]["password"] == self.password:
                    print("\nYou have Loged in!!! ")
                    temp2 = True
                else:
                    print("\nWrong Username or Password")
                    temp2 = False
            else:
                print(f"No '{self.user_name}' user Exist")
                temp2 = False


    def security_que(self):
        email = input("Enter Your Email : ")
        with open("/storage/emulated/0/Download/data.json","r") as user_data:
            temp_dict = json.load(user_data)
            temp_dict[self.user_name]["email"] = email
        with open("/storage/emulated/0/Download/data.json", "w") as user_data:
            json.dump(temp_dict,user_data)
        print("Account Has Successfully Created!")

    def email():
        sender = "Ahmedazim7804@gmail.com"
        with open("/storage/emulated/0/Download/data.json", "r") as user_data:
            temp_dict = json.load(user_data)
            receiver = str(temp_dict[user_name]["email"])
        password = "Azim!451/0"
        message = f"Thanks To Contact Us \nYour Password is {temp_dict[user_name]['password']}"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

    def forgot_pass():
        global user_name
        user_name = input("\nEnter Username : ")
        with open("/storage/emulated/0/Download/data.json","r") as user_data:
            temp_dict = json.load(user_data)
            if user_name in temp_dict.keys():
                email_input = input("Enter Your Email : ")
                if email_input == temp_dict[user_name]["email"]:
                    print("\nSending Email ....")
                    User.email()
                    print(f"\nPassword Has been sent to your EMAIL!")
                else:
                    print("\nWrong Email")
                    return
            else:
                print(f"No Username like '{user_name}' exists")

    def client(x):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "192.168.0.103"
        port = 5001
        s.connect((host, port))
        msg = str(x)
        s.send(msg.encode())
        s.close()

    def server():
        global data
        print("Waiting for other user input...")
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "192.168.0.102"
        port = 5001
        serversocket.bind((host, port))

        serversocket.listen(5)
        temp_5 = True
        while temp_5:
            (clientsocket, address) = serversocket.accept()
            data = clientsocket.recv(1024).decode()
            temp_5 = False


class Game(User,stat):

    def __init__(self):
        pass

    def rps():
        print(f"\n1. Single Player \n2. Multiplayer")
        choose_3 = int(input("Enter : "))
        if choose_3 == 1:
            lst = ["rock","paper","scissor"]
            opp = random.choice(lst)
            print(f"\n1. Rock \n2. Paper \n3. Scissor")
            user = input("\nChoose : ")
            if (user.lower()).strip() not in lst:
                print("Choosed from above three")
                Game.rps()
            else:
                if (user.lower()).strip() == opp:
                    print("\nGAME TIED")
                    stat.stat_rps_tie()
                elif opp == lst[0]:
                    if (user.lower()).strip() == lst[1] or user == '2':
                        print("\nYOU WIN")
                        stat.stat_rps_win()
                    elif (user.lower()).strip() == lst[2]  or user == '3':
                        print("\nYOU LOSE")
                        stat.stat_rps_lose()
                        print(f"\nOpponent Chooses '{opp}'")
                elif opp == lst[1]:
                    if (user.lower()).strip() == lst[2] or user == '3':
                        print("\nYOU WIN")
                        stat.stat_rps_win()
                    elif (user.lower()).strip() == lst[0] or user == '1':
                        print("\nYOU LOSE")
                        stat.stat_rps_lose()
                        print(f"\nOpponent Chooses '{opp}'")
                elif opp == lst[2]:
                    if (user.lower()).strip() == lst[0] or user == '1':
                        print("\nYOU WIN")
                        stat.stat_rps_win()
                    elif (user.lower()).strip() == lst[1] or user == '2':
                        print("\nYOU LOSE")
                        stat.stat_rps_lose()
                        print(f"\nOpponent Chooses '{opp}'")
        elif choose_3 == 2:
            lst = ["rock", "paper", "scissor"]
            print(f"\n1. Rock \n2. Paper \n3. Scissor")
            user = input("\nChoose : ")
            User.client(user)
            User.server()
            opp = data
            if (user.lower()).strip() not in lst:
                print("Choosed from above three")
                Game.rps()
            else:
                if (user.lower()).strip() == opp:
                    print("\nGAME TIED")
                    stat.stat_rps_tie()
                elif opp == lst[0]:
                    if (user.lower()).strip() == lst[1] or user == '2':
                        print("\nYOU WIN")
                        stat.stat_rps_win()
                    elif (user.lower()).strip() == lst[2] or user == '3':
                        print("\nYOU LOSE")
                        stat.stat_rps_lose()
                        print(f"\nOpponent Chooses '{opp}'")
                elif opp == lst[1]:
                    if (user.lower()).strip() == lst[2] or user == '3':
                        print("\nYOU WIN")
                        stat.stat_rps_win()
                    elif (user.lower()).strip() == lst[0] or user == '1':
                        print("\nYOU LOSE")
                        stat.stat_rps_lose()
                        print(f"\nOpponent Chooses '{opp}'")
                elif opp == lst[2]:
                    if (user.lower()).strip() == lst[0] or user == '1':
                        print("\nYOU WIN")
                        stat.stat_rps_win()
                    elif (user.lower()).strip() == lst[1] or user == '2':
                        print("\nYOU LOSE")
                        stat.stat_rps_lose()
                        print(f"\nOpponent Chooses '{opp}'")


    def guess_num():
        num = random.randint(0, 50)
        n = 0
        print("You have 5 Chance")
        while n < 5:
            user_guess = int(input("Guess The Number(b/w 0 to 50) : "))
            if user_guess != num:
                if user_guess > num:
                    print("Too High")
                    n += 1
                else:
                    print("Too Low")
                    n += 1
            else:
                print("\nYOU WIN!")
                stat.stat_guess_num_win()
                break
        else:
            print("You Lose")
            stat.stat_guess_num_lose()


def logedin():
    while True:
        print(f"\n1. Rock Paper Scissor \n2. Guess the number \n3. Statistics Of Your Games \n4. Log out")
        choose = int(input("\nChoose From Above : "))
        if choose == 1:
            Game.rps()
            temp0 = input("Enter To continue")
        elif choose == 2:
            Game.guess_num()
            temp0 = input("Enter To continue")
        elif choose == 3:
            stat.stat_show()
        elif choose == 4:
            return
        else:
            break

while True:
    print(f"\n1. Sign Up \n2. Log In \n3. Forgot Password \n4. To Exit")
    choose = int(input("\nChoose From Above : "))
    if choose == 1:
        temp1 = True
        while temp1:
            user_name = input("Enter Username : ")
            password = input("Enter Password : ")
            u1 = User(user_name, password)
            u1.signup()
            if temp1 == True:
                continue
            else:
                u1.security_que()
                stat.stat_rps()
                stat.stat_guess_num()
    elif choose == 2:
        user_name = input("\nEnter Username : ")
        password = input("Enter Password : ")
        if user_name == "azim" and password == "123":
            Game.rps()
        u1 = User(user_name, password)
        u1.login()
        if temp2 == False:
            continue
        elif temp2 == True:
            logedin()
    elif choose == 3:
        User.forgot_pass()
    else:
        break