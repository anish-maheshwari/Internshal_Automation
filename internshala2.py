from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time

# Initialize the driver
driver = webdriver.Chrome()
# Go to the Internshala login page
driver.get("https://internshala.com/login/user")

# Wait for the page to load
time.sleep(3)

# Login
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

# Replace with your login credentials
email.send_keys("letilac898@merotx.com")
password.send_keys("anish@123")
password.send_keys(Keys.RETURN)

# Wait for the page to load after login
time.sleep(5)

# Go to the internship listing page (modify this URL to your required page)
driver.get("https://internshala.com/internships")

# Wait for internships to load
time.sleep(3)


# Find all internship elements using a generalized XPath
internships = driver.find_elements(By.XPATH, "//div[contains(@id, 'individual_internship')]")

# Initialize a list to store the XPaths dynamically
internship_xpaths = []

# Loop through the found elements to get their XPaths
for internship in internships:
    try:
        # Get the unique ID attribute for each internship
        internship_id = internship.get_attribute("id")
        
        # Construct XPath using the unique ID
        xpath = f"//*[@id='{internship_id}']/div"
        internship_xpaths.append(xpath)
    except Exception as e:
        print(f"Couldn't generate XPath for an internship: {e}")

# Print the dynamically generated XPaths
print("Generated XPaths:")
for xpath in internship_xpaths:
    print(xpath)
for xpath in internship_xpaths[:10]:  # Apply to the first 10 internships
    try:
        # Find the internship using the XPath
        internship = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        internship.click()
        print(f"Clicked on internship: {xpath}")

        # Wait for the "Apply now" button to become visible and clickable
        apply_now_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue_button"))
        )

        # Click the "Apply now" button
        apply_now_button.click()
        print("Clicked on the 'Apply now' button successfully!")

        # Wait for the "Submit" button to become visible and clickable
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )

        # Click the Submit button
        submit_button.click()
        print("Clicked on the 'Submit' button successfully!")

        # Wait for confirmation or the next step
        time.sleep(3)

        # Navigate back to the internships page
        driver.back()
        driver.get("https://internshala.com/internships")
        print(driver.back)
        time.sleep(3)

    except Exception as e:
        print(f"Couldn't apply to internship {xpath}: {e}")
        continue

# Close the browser
driver.quit()