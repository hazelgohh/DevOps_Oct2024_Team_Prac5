from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# =========================
#  🚀 SETUP AND LOGIN STEPS
# =========================
@given('I open the login page')
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('I enter a valid username and password')
def step_enter_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")

@when('I click the login button')
def step_click_login(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('I should be redirected to the homepage')
def step_verify_login(context):
    try:
        WebDriverWait(context.driver, 5).until(EC.url_contains("inventory.html"))
        assert "inventory.html" in context.driver.current_url, f"Expected 'inventory.html' in {context.driver.current_url}"
    except:
        print(f"❌ ERROR: Expected 'inventory.html' but got {context.driver.current_url}")
    finally:
        context.driver.quit()

# =========================
#  🛒 CHECKOUT STEPS
# =========================
@given('I am logged into the website')
def step_logged_into_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # Allow time for login

@when('I add a product to the cart')
def step_add_product_to_cart(context):
    context.driver.find_element(By.CLASS_NAME, "inventory_item").click()
    context.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

@when('I proceed to checkout')
def step_proceed_to_checkout(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    context.driver.find_element(By.ID, "checkout").click()

@when('I enter my shipping details')
def step_enter_shipping_details(context):
    context.driver.find_element(By.ID, "first-name").send_keys("John")
    context.driver.find_element(By.ID, "last-name").send_keys("Doe")
    context.driver.find_element(By.ID, "postal-code").send_keys("12345")
    context.driver.find_element(By.ID, "continue").click()

@when('I confirm the purchase')
def step_confirm_purchase(context):
    context.driver.find_element(By.ID, "finish").click()

@then('I should see a confirmation message')
def step_see_confirmation_message(context):
    success_text = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you" in success_text
    context.driver.quit()

# =========================
#  🌍 NAVIGATION STEPS
# =========================
@given('I am on the homepage')
def step_on_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('I click on the "Products" page')
def step_click_products_page(context):
    try:
        product_link = WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))  # Change if needed
        )
        product_link.click()
    except:
        print("❌ ERROR: Could not find Products page link")
        context.driver.quit()

@then('I should be redirected to the products page')
def step_redirected_to_products_page(context):
    try:
        WebDriverWait(context.driver, 5).until(EC.url_contains("inventory.html"))
        assert "inventory.html" in context.driver.current_url, f"Expected 'inventory.html' in {context.driver.current_url}"
    except:
        print(f"❌ ERROR: Expected 'inventory.html' but got {context.driver.current_url}")
    finally:
        context.driver.quit()

@when('I click on the "Login" button')
def step_click_login_button(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('I should be redirected to the login page')
def step_redirected_to_login_page(context):
    try:
        WebDriverWait(context.driver, 5).until(EC.url_contains("inventory.html"))
        assert "inventory.html" in context.driver.current_url, f"Expected 'inventory.html' in {context.driver.current_url}"
    except:
        print(f"❌ ERROR: Expected 'inventory.html' but got {context.driver.current_url}")
    finally:
        context.driver.quit()

# =========================
#  🔍 SEARCH FUNCTIONALITY
# =========================
@when('I enter "{search_term}" into the search bar')
def step_enter_search(context, search_term):
    try:
        search_box = WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.NAME, "search"))  # Change if needed
        )
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
    except:
        print("❌ ERROR: Search box not found")
        context.driver.quit()

@when('I click the search button')
def step_click_search_button(context):
    try:
        search_btn = WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "search-button"))  # Change if needed
        )
        search_btn.click()
    except:
        print("❌ ERROR: Search button not found")
        context.driver.quit()

@then('I should see results related to "{search_term}"')
def step_see_search_results(context, search_term):
    try:
        results = WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-results"))  # Change if needed
        ).text
        assert search_term in results, f"Expected '{search_term}' in search results, but got {results}"
    finally:
        context.driver.quit()

@then('I should see a "No results found" message')
def step_see_no_results(context):
    try:
        no_results_text = WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "no-results"))  # Change if needed
        ).text
        assert "No results found" in no_results_text
    finally:
        context.driver.quit()
