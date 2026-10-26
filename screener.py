import time
import os
from datetime import datetime
import mss

save_dir = "screenshots"
os.makedirs(save_dir, exist_ok=True)

with mss.mss() as sct:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        filename = f"{save_dir}/screenshot_{timestamp}.png"

        # Сразу сохраняем скриншот в файл (без промежуточных PIL-объектов)
        sct.shot(output=filename)

        time.sleep(5)