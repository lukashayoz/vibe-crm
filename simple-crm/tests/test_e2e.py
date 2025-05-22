import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import threading
import time
from simple_crm.app.main import create_app

# Fixture to manage the Flask app lifecycle
@pytest.fixture(scope="session")
def flask_app():
    app = create_app('testing') # Use the testing configuration
    app_context = app.app_context()
    app_context.push()

    # Run the app in a separate thread
    def run_app():
        app.run(host='0.0.0.0', port=5001, use_reloader=False) # Use a different port for testing

    thread = threading.Thread(target=run_app)
    thread.daemon = True
    thread.start()
    
    # Wait a bit for the server to start
    time.sleep(2)

    yield app # Not strictly needed by tests but good practice

    # Teardown: The thread will exit when the main process exits
    # No explicit server stop needed for daemon thread in this simple case.
    app_context.pop()

# Fixture for Selenium WebDriver
@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox") # Recommended for CI environments
    chrome_options.add_argument("--disable-dev-shm-usage") # Recommended for CI environments
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_home_page_e2e(flask_app, browser):
    """
    E2E test for the home page.
    Checks for navigation, hello world message, and footer.
    """
    browser.get("http://127.0.0.1:5001/") # Connect to the test server

    # Check for navigation
    navigation = browser.find_element(By.TAG_NAME, "nav")
    assert navigation.is_displayed()
    assert "Simple CRM" in navigation.text

    # Check for Hello World message
    hello_world_message = browser.find_element(By.XPATH, "//h1[contains(text(), 'Hello World')]")
    assert hello_world_message.is_displayed()

    # Check for footer
    footer = browser.find_element(By.TAG_NAME, "footer")
    assert footer.is_displayed()
    assert "© 2023 Simple CRM. All rights reserved." in footer.text
