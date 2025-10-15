from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()  # load EMAIL/PASSWORD

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.context = context.browser.new_context()  # create browser context
    context.page = context.context.new_page()        # assign page
    print("Browser and page initialized successfully")

def after_all(context):
    print("After All")
    # context.context.close()  # close context first
    # context.browser.close()
    # context.playwright.stop()
