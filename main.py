import pyfiglet
from rich.console import Console 
import time
from tqdm import tqdm


ascii_art = pyfiglet.figlet_format("Hello python class!")
print(ascii_art)

fonts = ['slant', '3-d', 'block', 'bubble', 'digital', 'ivrit','bulbhead', 'dotmatrix']
for font in fonts:
    print(pyfiglet.figlet_format("Hello python class!", font=font))


console = Console()
ascii_art = pyfiglet.figlet_format("Colorful!")
console.print(ascii_art, style="bold blue")


for i in range(1, 6):
    print(pyfiglet.figlet_format(f"Step {i}", font="isometric1"))
    time.sleep(0.5)
   