

def summary():
  for x in range(0,4):
    file=input("Would you like the summary of current contracts or the archive ")
    # i haven't done the archive
    answers=['CURRENT','CURRENT CONTRACTS','CURRENT CONTRACT','ARCHIVE']
    if file.upper() not in answers:
      if x == 0 :
        print('Please select a valid contract. 3 attemps left')
      elif x == 1:
        print('Please select a valid contract. 2 attemps left')
      elif x == 2:
        print('Please select a valid contract. 1 attemps left')
      elif x == 3:
        return('')
    else:
      break
  if answers[0] in file.upper():
    with open ('I:/Downloads/summary.txt','r+') as file:
      print('There is currently ' + str(len(file.readlines())) + ' contracts' )
      file.close()
    with open('I:/Downloads/summary.txt') as file:
      contents=file.read()
      count=contents.count('Unlimited')
      count2=contents.count('High')
      total=count + count2
      print('There is ',total,' contracts with either high or unlimted data bundles')
      #Need to put the lines with large packages into arrays so i cann make average cost
  return('')


def month_sum():
  for x in range(0,4):
    file=input("Would you like the summary of current contracts or the archive ")
    answers=['CURRENT','CURRENT CONTRACTS','CURRENT CONTRACT','ARCHIVE']
    if file.upper() not in answers:
      if x == 0 :
        print('Please select a valid contract. 3 attemps left')
      elif x == 1:
        print('Please select a valid contract. 2 attemps left')
      elif x == 2:
        print('Please select a valid contract. 1 attemps left')
      else:
        return('')
    else:
      months=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUEST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
      for x in range(0,4):
        month=input('Select your month ')
        if month.upper() not in months:
          if x == 0:
            print('Enter a valid month. 3 attemps left ')
          elif x == 1:
            print('Enter a valid month. 2 attemps left ')
          elif x == 2:
            print('Enter a valid month. 1 attemps left ')
          else:
            return('')
        else:
          return('')

def find():
  for x in range(0,4):
    file=input("Would you like the summary of current contracts or the archive ")
    answers=['CURRENT','CURRENT CONTRACTS','CURRENT CONTRACT','ARCHIVE']
    if file.upper() not in answers:
      if x == 0 :
        print('Please select a valid contract. 3 attemps left')
      elif x == 1:
        print('Please select a valid contract. 2 attemps left')
      elif x == 2:
        print('Please select a valid contract. 1 attemps left')
      else:
        return('')
    else:
      search=input('Enter text ')
      return ('')


loop=True
while loop == True :
    print ("""
    1.Enter new Contract
    2.Display Summary of Contracts
    3.Display Summary of Contracts for Selected Month
    4.Find and display Contract
    0.Exit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      print(new()) 
    elif ans=="2":
      print(summary()) 
    elif ans=="3":
      print(month_sum())
    elif ans=="4":
      print(find()) 
    elif ans=='0':
      loop=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 
