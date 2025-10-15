from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class BasePage:
    def __init__(self, page):
        self.page = page

    def get_element(self, locator: str):
        """Convert string locator into a Playwright locator object."""
        return self.page.locator(locator)

    def click(self, locator: str, timeout: int = 10000):
        """Click element safely."""
        try:
            element = self.get_element(locator)
            element.wait_for(state="visible", timeout=timeout)
            element.click()
        except PlaywrightTimeoutError:
            raise Exception(f"Element not clickable: {locator}")

    def fill(self, locator: str, value: str, timeout: int = 10000):
        """Fill input field."""
        try:
            if value is None:
              raise ValueError(f"Cannot fill None for locator: {locator}")
            element = self.get_element(locator)
            element.wait_for(state="visible", timeout=timeout)
            element.fill(value)
        except PlaywrightTimeoutError:
            raise Exception(f"Unable to fill input: {locator}")

    def get_text(self, locator: str):
        """Get element text."""
        element = self.get_element(locator)
        return element.inner_text()

    def is_visible(self, locator: str, timeout: int = 5000):
        """Return True if element visible within timeout."""
        try:
            self.page.wait_for_selector(locator, state="visible", timeout=timeout)
            return True
        except PlaywrightTimeoutError:
            return False

    def scroll_into_view(self, locator: str):
        """Scroll until element visible."""
        self.get_element(locator).scroll_into_view_if_needed()
