import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Создаем DataFrame
df = pd.DataFrame(np.random.random((10, 3)), columns=("col 1", "col 2", "col 3"))

# Преобразуем DataFrame в таблицу
fig, ax = plt.subplots(figsize=(12, 4))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

# Сохраняем PDF файл
pp = PdfPages("foo.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()