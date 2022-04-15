questions = {
    'question1': {
        'question': 'How much are 4 + 2?',
        'answers': {
            'a': 6,
            'b': 2,
            'c': 5,
        },
        'correct_answear': 'a',
    },
    'question2': {
        'question': 'How much are 4 + 4?',
        'answers': {
            'a': 6,
            'b': 8,
            'c': 5,
        },
        'correct_answear': 'b',
    },
    'question3': {
        'question': 'How much are 4 - 4?',
        'answers': {
            'a': 6,
            'b': 8,
            'c': 0,
        },
        'correct_answear': 'c',
    },
}
points = 0
for qk, qv in questions.items():
    question = qv['question']
    a = qv['answers']['a']
    b = qv['answers']['b']
    c = qv['answers']['c']
    correct_answear = qv['correct_answear']

    print(f'{qk}: {question}\n')
    print(f'a) {a}, b) {b}, c) {c}\n')

    answear = str(input('Choose a, b , c: \n'))

    if answear == correct_answear:
        print('You are write!\n')
        points = points + 1
    else:
        print('You are wrong!\n')

print(f'SCORE: {points} points')
