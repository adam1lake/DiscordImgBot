from selenium import webdriver
from random import randint
import shutil
import urllib.request
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class ImageGetter:
    # Driver set up
    def __init__(self):
        options = Options()
        # Comment out the line below to disable headless Chrome for debugging
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(2)
        self.cookies_accepted = False

    # Get image using query string. By default, random is off and the first result is returned
    def get_image(self, query, random=False):
        self.driver.get(f"https://www.google.com/search?tbm=isch&q={query}")
        # Sets the index of the image on the page
        if random:
            result_id = randint(1, 50)
        else:
            result_id = 1

        # If cookies have not been accepted, check for "Accept All" button, and click it if it exists
        if not self.cookies_accepted:
            elements = self.driver.find_elements(By.XPATH, "//button[@aria-label='Accept all']")
            if len(elements) > 0:
                elements[0].click()
            self.cookies_accepted = True

        # JavaScript code to get the image using the index and click on it
        self.driver.execute_script("""
        try {
            let element = document.evaluate('(//div[@id="islmp"]//img)[%s]', document, XPathResult.singleNodeValue).iterateNext();
            element.click();
        } catch {
            console.log("Failed to click on element.");
        } 
        """ % result_id)

        # TODO: get a higher resolution image, as the current source gives an image of relatively low resolution
        # Finds multiple images
        elements = self.driver.find_elements(By.XPATH,
                                             "(//img[@class='n3VNCb' and @jsname='HiaYvf' and 'load:XAeZkd;'])")

        url = ""
        print(len(elements))
        # Selects the correct image that has the desired source
        if len(elements) == 0:
            # This occurs when no results are found for the search query
            return "NoResults"
        elif len(elements) == 1 or len(elements) == 2:
            element_id = 0
        elif len(elements) == 3:
            element_id = 1
        else:
            return "Error"

        # Downloads the image
        img = urllib.request.urlopen(elements[element_id].get_attribute("src"))

        # Saves the image to the root directory
        with open("current_image.png", "wb") as f:
            shutil.copyfileobj(img, f)
            print("Image saved.")
            return True
