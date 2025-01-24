import time
import os
import subprocess
# Здесь должен быть ваш реальный код проверки
# 1. Конвертация
# например: jupyter nbconvert --to python <файл>.ipynb
# 2. Разделение
# 3. Фидбек
# 4. Советы
def get_result_string(feedback_list):
   return "\n".join([f"Блок: {index}, Отзыв: {feedback}" for index, feedback in enumerate(feedback_list)])

# Пример вызова
feedback_list = ["Отлично", "Хорошо", "Есть недочеты"]

result_string = get_result_string(feedback_list)

time.sleep(5) # Задержка для демонстрации
print("Проверка запущена. Результаты будут в комментариях к Pull Request.")
print(f"Результаты:\n {result_string}")
print("Совет: Подумайте над улучшением.")
