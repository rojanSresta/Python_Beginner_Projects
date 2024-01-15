with open("story.txt", 'r') as f:
    story = f.read()

placeholders = set()

PLACEHOLDER_START = '<'
PLACEHOLDER_END = '>'

answers = {}

for index, char in enumerate(story):
    if PLACEHOLDER_START == char:
        PLACEHOLDER_END_index_value = story.find(PLACEHOLDER_END, index + 1)
        placeholder = story[index:PLACEHOLDER_END_index_value + 1]
        placeholders.add(placeholder)

for placeholder in placeholders:
    user_answer = input(f"Enter word for {placeholder}: ")
    answers[placeholder] = user_answer

print(answers)

for placeholder in placeholders:
    story = story.replace(placeholder, answers[placeholder])

print(story)
