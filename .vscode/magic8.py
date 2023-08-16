import random;

name = "";
question = "";
answer = "";
random_number = random.randint(1,23);
# print("line 7", random_number)

if random_number ==  1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidely so";
elif random_number == 3:
  answer = "Without a doubt";
elif random_number == 4:
  answer = "Reply hazy, try again";
elif random_number == 5:
  answer = "Ask again later";
elif random_number == 6:
  answer = "Better not tell you now";
elif random_number == 7:
  answer = "My sources say no";
elif random_number == 8:
  answer = "Outlook not so good";
elif random_number ==9:
  answer = "Very doubtful";
elif random_number == 10:
  answer="It is certain";
elif random_number == 11:
  answer="Yes definitely";
elif random_number == 12:
  answer="You may rely on it";
elif random_number == 13:
  answer="As I see it, yes";
elif random_number == 14:
  answer="Most likely";
elif random_number == 15:
  answer="Outlook good";
elif random_number == 16:
  answer="Yes";
elif random_number == 17:
  answer="Signs point to yes";
elif random_number == 18:
  answer="Cannot predict now";
elif random_number == 19:
  answer="Concentrate and ask again";
elif random_number == 20:
  answer="Don’t count on it";
elif random_number == 21:
  answer="My reply is no";
elif random_number == 22:
  answer="My sources say no";
elif random_number == 23:
  answer="Don’t count on it";
else:
  answer = "Error";

if name =="" and question =="":
  print("Error: Please provide a question to receive fortune.")
elif name =="":
  print("Question: " + question);
  print("Magic 8-Ball's answer: " + answer)
else: 
  print( name + "asks: " + question);
  print("Magic 8-Ball's answer: " + answer)


 
