# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
#
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
#
# Output: 13

text = "She sells sea shells on the sea shore The shells that she sells are sea shells " \
       "I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells " \
       "are sea shore shells"

text_1 = text.replace(".", " ")
text_2 = text_1.strip(".,!?\n").lower().split()
print(f"В данном отрывке {len(text_2)} слов из них {len(set(text_2))} различных.")


