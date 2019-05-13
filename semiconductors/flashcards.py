import random
import re
import textwrap
# ENTER "pip install textwrap3" into command line


def find_questions_and_answers(filename):
	with open(filename,encoding="utf8") as f:
		entire_text = f.read()
	questions = re.findall(r'\$\$\$\n(.+?)\n£££', entire_text,re.DOTALL)
	answers = re.findall(r'£££\n(.+?)###', entire_text,re.DOTALL)
	q_a = []
	for i,q in enumerate(questions):
		q_a.append( (q,answers[i]) )
	return q_a

	
def quiz(questions_and_answers,shuffle=False,reverse=False):
	if shuffle:
		random.shuffle(questions_and_answers)
	elif reverse:
		questions_and_answers.reverse()
	corrects = 0
	wrongs = 0
	total = len(questions_and_answers)
	updated_questions_and_answers = []
	for i,q_a in enumerate(questions_and_answers):
		lines = q_a[0].splitlines()
		for l in lines:
			print(textwrap.fill(l) + '\n')
		right_wrong = input()
		print('\n')
		if right_wrong == '': #correct condition
			corrects += 1
		else:
			wrongs += 1
			updated_questions_and_answers.append(q_a)
			if q_a[1] != '\n': # If there is correct answer to reference in the text file
				print('The correct answer is:\n' + textwrap.fill(q_a[1]) + '\n\n\n')
				lines = q_a[1].splitlines()
				for l in lines:
					print(textwrap.fill(l) + '\n')	
	print('\nCorrect Answers: {}/{}\nIncorrect Answers: {}/{}\n\n'.format(corrects,total,wrongs,total))
	if wrongs == 0:
		print('You have successfully answered all of the flashcards correctly!')
	else:
		input('Press [Enter] to try again at wrong answers.\n')
		quiz(updated_questions_and_answers)


if __name__ == '__main__':
	
	print(textwrap.fill('Pressing [Enter] signifies a correct answer.\nAnything else signifies a wrong answer.')+'\n\n\n')

	QUESTIONS_AND_ANSWERS_1 = find_questions_and_answers('Q1.txt')
	QUESTIONS_AND_ANSWERS_LPE = find_questions_and_answers('lpe.txt')
	QUESTIONS_AND_ANSWERS_VL = find_questions_and_answers('vegard.txt')
	QUESTIONS_AND_ANSWERS_SEM = find_questions_and_answers('sem.txt')
	
	CHAPTER_1 = find_questions_and_answers('ch1.txt')
	CHAPTER_2 = find_questions_and_answers('ch2.txt')
	CHAPTER_3 = find_questions_and_answers('ch3.txt')
	CHAPTER_5 = find_questions_and_answers('ch5.txt')
	
	quiz(QUESTIONS_AND_ANSWERS_1,shuffle=False,reverse=False)
	quiz(QUESTIONS_AND_ANSWERS_LPE,shuffle=False,reverse=False)
	quiz(QUESTIONS_AND_ANSWERS_VL,shuffle=False,reverse=False)
	quiz(QUESTIONS_AND_ANSWERS_SEM,shuffle=False,reverse=False)
	quiz(CHAPTER_1,shuffle=False,reverse=False)
	quiz(CHAPTER_2,shuffle=False,reverse=False)
	quiz(CHAPTER_3,shuffle=False,reverse=False)
	quiz(CHAPTER_5,shuffle=False,reverse=False)

	quit()

