import pandas as pd

df = pd.read_csv('tested.csv')  # читаем файл и кладем его в датафрейм

# Получаем список всех числовых столбцов
numeric_columns = df.select_dtypes(include=['number']).columns  # ищем столбцы с типом 'число'
print("Числовые столбцы:", list(numeric_columns))

print("\nСтроки с пропусками и подробностями по каждому пропуску:")

# Фильтруем строки, где есть хотя бы один пропуск null (NaN/None) или empty (пустая строка)
missing_rows = df[df.isnull().any(axis=1) | (df == '').any(axis=1)]
# df.isnull() — создаём таблицу, где True для каждой ячейки, если она пустая (null)
# .any(axis=1) — для строки: True, если хоть одна ячейка пустая (null)
# (df == '') — создаём таблицу, где True в ячейке, если она пустая строка
# .any(axis=1) — для строки: True, если хоть одна ячейка пустая строка (empty)
# выбираем строки, где хотя бы один пропуск любого типа

for idx, row in missing_rows.iterrows():  # перебираем каждую строку с пропусками
    messages = []  # сюда будем собирать информацию о найденных пропусках в строке
    for col in df.columns:  # перебираем все столбцы по очереди
        val = row[col]  # значение ячейки в текущей строке и столбце
        if pd.isnull(val):  # если ячейка — пропуск (null, NaN, None)
            messages.append(f"{col}: null")  # записываем столбец и тип пропуска
        elif val == '':  # если ячейка — пустая строка
            messages.append(f"{col}: empty")  # записываем столбец и тип пропуска
    if messages:  # если нашлись пропуски
        # выводим номер строки и подробности: в каких столбцах и какой тип пропуска
        print(f"Строка {idx + 1} — пропуск(и): {', '.join(messages)}")

print("\nВсего строк с пропусками:", len(missing_rows))

fare = df['Fare']  # выбираем столбец стоимости

print("\nБазовая статистика по стоимости ('Fare'):")

print(f"Среднее значение: {fare.mean()}")
print(f"Медиана: {fare.median()}")
print(f"Максимум: {fare.max()}")
print(f"Минимум: {fare.min()}")
print(f"Мода: {fare.mode().values}")
print(f"Сумма: {fare.sum()}")
print(f"\nСтандартное отклонение: {fare.std()}")
print(f"Количество пропусков: {fare.isnull().sum()}")
# Сохраняем строки, где ИЗНАЧАЛЬНО был пропуск в "Fare"
missing_fare_before = df[df['Fare'].isnull()].copy()

# Заполняем пропуски по среднему для класса
df['Fare'] = df.groupby('Pclass')['Fare'].transform(lambda x: x.fillna(x.mean()))

# Получаем индексы тех строк, где раньше был пропуск
missing_indices = missing_fare_before.index

# Выводим обновлённые строки с ранее заполненным пропуском
print("\nСтроки, где 'Fare' был пропуском, и теперь заполнен:")
print(df.loc[missing_indices])