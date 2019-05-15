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
			print(textwrap.fill(l,width=150))
		right_wrong = input()
		if right_wrong == '': #correct condition
			corrects += 1
		else:
			wrongs += 1
			updated_questions_and_answers.append(q_a)
			if q_a[1] != '\n': # If there is correct answer to reference in the text file
				lines = q_a[1].splitlines()
				print('\nTHE CORRECT ANSWER IS:\n')
				for l in lines:
					print(textwrap.fill(l,width=150))	
		print('\n')
		print('---------------------------------------------------------')
		print('\n')
	print('\nCorrect Answers: {}/{}\nIncorrect Answers: {}/{}\n\n'.format(corrects,total,wrongs,total))
	if wrongs == 0:
		print('You have successfully answered all of the flashcards correctly!')
	else:
		input('Press [Enter] to try again at wrong answers.\n')
		quiz(updated_questions_and_answers)


if __name__ == '__main__':
	
	print(textwrap.fill('Pressing [Enter] signifies a correct answer.\nAnything else signifies a wrong answer.')+'\n\n\n')

	QUESTIONS_AND_ANSWERS_DEBYE_LENGTH = find_questions_and_answers('debye_length.txt')
	QUESTIONS_AND_ANSWERS_LORENTZ_FORCE = find_questions_and_answers('lorentz_force.txt')
	QUESTIONS_AND_ANSWERS_PLASMA_CONDUCTIVITY = find_questions_and_answers('plasma_conductivity.txt')
	QUESTIONS_AND_ANSWERS_DIFFUSION = find_questions_and_answers('diffusion.txt')
	QUESTIONS_AND_ANSWERS_SHEATHS = find_questions_and_answers('sheaths.txt')
	QUESTIONS_AND_ANSWERS_WAVES_IN_PLASMA = find_questions_and_answers('waves_in_plasma.txt')
	
	
	quiz(QUESTIONS_AND_ANSWERS_DEBYE_LENGTH,shuffle=False,reverse=False)
	quiz(QUESTIONS_AND_ANSWERS_LORENTZ_FORCE,shuffle=False,reverse=False)
	quiz(QUESTIONS_AND_ANSWERS_PLASMA_CONDUCTIVITY,shuffle=False,reverse=False)
	quiz(QUESTIONS_AND_ANSWERS_DIFFUSION,shuffle=False,reverse=False)
	quiz(QUESTIONS_AND_ANSWERS_SHEATHS,shuffle=False,reverse=False)
	quiz(QUESTIONS_AND_ANSWERS_WAVES_IN_PLASMA,shuffle=False,reverse=False)


	quit()

