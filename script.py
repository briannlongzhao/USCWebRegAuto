from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = ""
password = "$"
term = "Fall 2022"
browser = "Chrome"  # Chrome, Edge, IE, Firefox, or Safari

if browser == "Chrome":
	options = webdriver.ChromeOptions()
	driver = webdriver.Chrome(options=options)
elif browser == "Edge":
	options = webdriver.EdgeOptions()
	driver = webdriver.Edge(options=options)
elif browser == "IE":  # Only runs on Windows
	options = webdriver.IEOptions()
	driver = webdriver.Ie(options=options)
elif browser == "Firefox":
	options = webdriver.FirefoxOptions()
	driver = webdriver.Firefox(options=options)
elif browser == "Safari":  # Only runs on MacOS
	driver = webdriver.Safari()

wait = WebDriverWait(driver, 180)
driver.get("https://my.usc.edu")
wait.until(EC.presence_of_element_located((By.NAME, "j_username"))).send_keys(username)
wait.until(EC.presence_of_element_located((By.NAME, "j_password"))).send_keys(password)
driver.find_element(By.CLASS_NAME, "form-button").click()
driver.switch_to.frame(driver.find_element(By.ID, "duo_iframe"))
driver.find_element(By.CLASS_NAME, "push-label").click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Web Registration"))).click()
wait.until(EC.number_of_windows_to_be(2))
for window_handle in driver.window_handles:
	if window_handle != driver.current_window_handle:
		driver.switch_to.window(window_handle)
		break
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, term))).click()
while True:
	wait.until(EC.element_to_be_clickable((By.ID, "mItReg"))).click()
	wait.until(EC.element_to_be_clickable((By.ID, "SubmitButton"))).click()
	try:
		wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Registration"))
		response = driver.find_element(By.CSS_SELECTOR, ".content-wrapper-regconfirm").text
		if ("Failed" in response):
			continue
		elif ("successful" in response):
			print("Success")
			break
		else:
			driver.refresh()
	except selenium.common.exceptions.TimeoutException:
		driver.refresh()
driver.quit()
