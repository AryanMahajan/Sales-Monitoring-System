import matplotlib.pyplot as plt
import csv
import os 

os.system("cls")

def Data_entry():
    print('Which type of data do you want to enter:')
    print('1 => Daily')
    print('2 => Weekly')
    print('3 => Monthly')
    inp=input('Enter here:-> ')
    if inp=='1':
        print('For how many days are there for entry: ')
        time=int(input('Enter here:-> '))
        for a in range (1,time+1):
            print('Enter the data of day',a)
            inpp=int(input('Enter here:-> '))
            print('Enter the date (in dd.mm.yyy form)')
            inppp=input('Enter here:-> ')
            list=[inpp,inppp]
            with open('daily.csv','a',newline='\n') as f:
                writer=csv.writer(f)
                writer.writerow(list)
            a=a+1
        print('Your data have been saved.')
        user_password(user,password)
    elif inp=='2':
        print('For how many weeks are there for entry: ')
        time=int(input('Enter here:-> '))
        for a in range (1,time+1):
            print('Enter the data of week',a)
            inpp=int(input('Enter here:-> '))
            print('Enter the week (in w.mm.yyyy form)')
            inppp=input('Enter here:-> ')
            list=[inpp,inppp]
            with open('weekly.csv','a',newline='\n') as f:
                writer=csv.writer(f)
                writer.writerow(list)
            a=a+1
        print('Your data have been saved.')
        user_password(user,password)
    elif inp=='3':
        print('For how many months are there for entry: ')
        time=int(input('Enter here:-> '))
        for a in range (1,time+1):
            print('Enter the data of month',a)
            inpp=int(input('Enter here:-> '))
            print('Enter the month (in mm.yyyy form)')
            inppp=input('Enter here:-> ')
            list=[inpp,inppp]
            with open('monthly.csv','a',newline='\n') as f:
                writer=csv.writer(f)
                writer.writerow(list)
            a=a+1
        print('Your data have been saved.')
        user_password(user,password)
    else:
        print('Wrong choice')
        user_password(user,password)

def Data_visualisation():
    print('Which type of data do you want to visualise:')
    print('1 => Daily')
    print('2 => Weekly')
    print('3 => Monthly')
    inp=input('Enter here:-> ')
    if inp=='1':
        print('Which type of graph do you want to display:')
        print('1 Bar graph')
        print('2 Line graph')
        inpp=input('Enter here:-> ')
        if inpp=='1':
            x = []
            y = []
            with open('daily.csv','r') as csvfile:
                plots = csv.reader(csvfile, delimiter = ',')
                for row in plots:
                    y.append(int(row[0]))
                    x.append(row[1])
                plt.bar(x, y, color = 'b', width = 0.72, label = "Sales")
                plt.xlabel('Dates')
                plt.ylabel('Total Sales')
                plt.title('Sales Visualisation')
                plt.legend()
                plt.show()
            user_password(user,password)
        elif inpp=='2':
            x= []
            y = []
            with open('daily.csv','r') as csvfile:
                plots = csv.reader(csvfile, delimiter = ',')
                for row in plots:
                    y.append(int(row[0]))
                    x.append(row[1])
                plt.plot(x,y,color='b',label='Sales')
                plt.xlabel('Dates')
                plt.ylabel('Total Sales')
                plt.title('Sales Visualisation')
                plt.legend()
                plt.show()
            user_password(user,password)
        else:
            print('Wrong choice')
            user_password(user,password)

    elif inp=='2':
        print('Which type of graph do you want to display:')
        print('1 Bar graph')
        print('2 Line graph')
        inpp=input('Enter here:-> ')
        if inpp=='1':
            x = []
            y = []
            with open('weekly.csv','r') as csvfile:
                plots = csv.reader(csvfile, delimiter = ',')
                for row in plots:
                    y.append(int(row[0]))
                    x.append(row[1])
                plt.bar(x, y, color = 'b', width = 0.72, label = "Sales")
                plt.xlabel('Weeks')
                plt.ylabel('Total Sales')
                plt.title('Sales Visualisation')
                plt.legend()
                plt.show()
            user_password(user,password)
        elif inpp=='2':
            x= []
            y = []
            with open('weekly.csv','r') as csvfile:
                plots = csv.reader(csvfile, delimiter = ',')
                for row in plots:
                    y.append(int(row[0]))
                    x.append(row[1])
                plt.plot(x,y,color='b',label='Sales')
                plt.xlabel('Weeks')
                plt.ylabel('Total Sales')
                plt.title('Sales Visualisation')
                plt.legend()
                plt.show()
            user_password(user,password)
        else:
            print('Wrong choice')
            user_password(user,password)

    elif inp=='3':
        print('Which type of graph do you want to display:')
        print('1 Bar graph')
        print('2 Line graph')
        inpp=input('Enter here:-> ')
        if inpp=='1':
            x = []
            y = []
            with open('monthly.csv','r') as csvfile:
                plots = csv.reader(csvfile, delimiter = ',')
                for row in plots:
                    y.append(int(row[0]))
                    x.append(row[1])
                plt.bar(x, y, color = 'b', width = 0.72, label = "Sales")
                plt.xlabel('Months')
                plt.ylabel('Total Sales')
                plt.title('Sales Visualisation')
                plt.legend()
                plt.show()
            user_password(user,password)
        elif inpp=='2':
            x= []
            y = []
            with open('monthly.csv','r') as csvfile:
                plots = csv.reader(csvfile, delimiter = ',')
                for row in plots:
                    y.append(int(row[0]))
                    x.append(row[1])
                plt.plot(x,y,color='b',label='Sales')
                plt.xlabel('Months')
                plt.ylabel('Total Sales')
                plt.title('Sales Visualisation')
                plt.legend()
                plt.show()
            user_password(user,password)
        else:
            print('Wrong choice')
            user_password(user,password)

    else:
        print('Wrong choice')
        user_password(user,password)

def user_password(user,password):
    with open('user_password.csv', 'r') as f:
        for line in f:
            words = line.split('/')
            usr=words[0]
            pswd=words[1]
            if usr==user and pswd==password:
                print('+---------------------------------------------------+')
                print('|  Select from the following (enter either 1 or 2): |')
                print('+---+-----------------------------------------------+')
                print('| 1 |                Sales Entry                    |')
                print('+---------------------------------------------------+')
                print('| 2 |             Sales Visualisation               |')
                print('+---+-----------------------------------------------+')
                print('| 3 |                   Exit                        |')
                print('+---+-----------------------------------------------+')
                print('Enter Your Choice:-> ')
                inp=input('Enter here:-> ')
                if inp=='1':
                    Data_entry()
                elif inp=='2':
                    Data_visualisation()
                elif inp=='3':
                    SystemExit()
                else:
                    user_password(user,password)
            else:
                print('Wrong user or password')
                print('Try again')

user=input('Enter username:-> ').lower()
password=input('Enter password:-> ').lower()
user_password(user,password)
