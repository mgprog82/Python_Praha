import matplotlib.pyplot as plt

#Добавляем формулу
formula = r'$2^2 = 2 + 2 = 4$'
plt.text(0, 0, formula, fontsize=12)

# Прячем оси
#fig = plt.gca()
#fig.axes.get_xaxis().set_visible(False)
#fig.axes.get_yaxis().set_visible(False)

# Сохраняем как картинку
plt.savefig('filename.png')