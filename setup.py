import os

os.system('mode con: cols=80')

print('Трансляция музыки из ВКонтакте в статус Telegram'.center(80))
print('by snowlue'.center(80))
print()
print('===== ВКонтакте ====='.center(80))
print('1. Создайте закрытое сообщество — https://vk.com/groups_create')
print('2. Выберите «Группа по интересам» и тип группы «Закрытая»')
print('3. Скопируйте адрес группы и вставьте ниже (например, https://vk.com/club12345)')
print('4. Откройте раздел «Музыка» — https://vk.com/audio')
print('5. В плеере нажмите «Трансляция аудиозаписей» (третья кнопка с конца)')
print('6. Выберите только что созданное сообщество\n')

link = input('Вставьте адрес сообщества: ')
print('\n')

print('===== Telegram ====='.center(80))
print('1. Перейдите на https://my.telegram.org')
print('2. Залогиньтесь и создайте приложение (нажмите «API development tools»)')
print('3. Скопируйте api_id и api_hash\n')

api_id = input('Введите api_id: ')
api_hash = input('Введите api_hash: ')

status = input('\n\nВведите статус, который будет стоять, если что-то сломается: ')
while len(status) > 70:
    status = input('Введите статус, который будет стоять, если что-то сломается: ')
with open('bd.py', 'w', encoding='utf-8') as file:
    file.write(f'api_id = {api_id}\napi_hash = "{api_hash}"\nstatus = "{status}"\ngroup_link = "{link}"\n')
