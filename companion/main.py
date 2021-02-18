answers = {}


q_file = open('questions.txt','r') 
a_file = open('answers.txt','r')

for line in q_file:
    question = line.strip("\n")
    answer = a_file.readline().strip("\n")
    answers[question] = answer
q_file.close()
a_file.close()

while(True):
    question = input("write your question: "+ question+"':")
    answer[question] =answer
print(answers[question])

if question == "bye":
    break
q_file = open('questions.txt','w') 
a_file = open('answers.txt','w')

for question,answer in answers.item():
    q_file.write(question+"/n")
    a_file.write(answers+ "/n")

q_file.close
a_file.close