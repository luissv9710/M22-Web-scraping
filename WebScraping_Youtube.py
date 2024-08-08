from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de opciones para el navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Abre el navegador en pantalla completa

# Configuración del controlador
service = Service(ChromeDriverManager().install())

# Inicializa el navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Paso 1: Abre el canal específico en YouTube
    driver.get("https://www.youtube.com/@noteduermas3128")

    # Espera a que la página del canal se cargue completamente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Paso 2: Usa el cuadro de búsqueda dentro del canal para buscar el video
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))
    )

    search_box.send_keys("El huésped de Drácula | Relatos para no dormir T1 Ep. 1")
    search_box.submit()

    # Espera a que aparezcan los resultados y haz clic en el video
    video_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='El huésped de Drácula | Relatos para no dormir T1 Ep. 1']"))
    )
    video_link.click()

finally:
    # Mantén el navegador abierto
    input("Presiona Enter para cerrar el navegador...")

    driver.quit()