# -*- coding:utf-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os.path
from framework.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = Logger(logger='BasePage').getlogger()

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info(f"wait for {seconds} seconds." )
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error(f"Failed to quit the browser with {e}" )
    def get_windows_img(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath('.')),'screenshots')
        rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        file_name = rq + '.png'
        screen_name = os.path.join(file_path,file_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)

    def find_element(self,selector):
        driver = self.driver
        element = None
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                #element = driver.find_element_by_id(selector_value)
                element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,selector_value)))
                logger.info(f'Had find the element "{element.text}" successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'n' or selector_by == 'name':
            try:
                #element = driver.find_element_by_name(selector_value)
                element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, selector_value)))
                logger.info(
                f'Had find the element "{element.text}" successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 't' or selector_by == 'tag' or selector_by == 'tag_name':
            try:
                #element = driver.find_element_by_tag_name(selector_value)
                element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, selector_value)))
                logger.info(
                f'Had find the element "{element.text}" successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'c' or selector_by == 'class' or selector_by == 'class_name':
            try:
                #element = driver.find_element_by_class_name(selector_value)
                element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, selector_value)))
                logger.info(
                f'Had find the element "{element.text}" successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'l' or selector_by == 'link_text':
            try:
                #element = driver.find_element_by_link_text(selector_value)
                element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, selector_value)))
                logger.info(
                f'Had find the element "{element.text}" successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            try:
                #element = driver.find_element_by_partial_link_text(selector_value)
                element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)))
                logger.info(
                f'Had find the element "{element.text}" successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                #element = driver.find_element_by_xpath(selector_value)
                element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector_value)))
                logger.info(
                f'Had find the element "{element.text}" successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'css' or selector_by == 'css_selector':
            try:
                #element = driver.find_element_by_css_selector(selector_value)
                element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector_value)))
                logger.info(
                f'Had find the element "{element.text}" successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    def find_elements(self,selector):
        elements = None
        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                elements = self.driver.find_elements_by_id(selector_value)
                logger.info(f'Had find the elements successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'n' or selector_by == 'name':
            try:
                elements = self.driver.find_elements_by_name(selector_value)
                logger.info(
                f'Had find the elements successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 't' or selector_by == 'tag_name' or selector_by == 'tag':
            try:
                elements = self.driver.find_elements_by_tag_name(selector_value)
                logger.info(
                f'Had find the elements successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'c' or selector_by == 'class_name' or selector_by == 'class':
            try:
                elements = self.driver.find_elements_by_class_name(selector_value)
                logger.info(
                f'Had find the elements successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'l' or selector_by == 'link_text' or selector_by == 'link':
            try:
                elements = self.driver.find_elements_by_link_text(selector_value)
                logger.info(
                f'Had find the elements successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'p' or selector_by == 'partial_link_text' or selector_by == 'partial':
            try:
                elements = self.driver.find_elements_by_partial_link_text(selector_value)
                logger.info(
                f'Had find the elements successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                elements = self.driver.find_elements_by_xpath(selector_value)
                logger.info(
                f'Had find the elements successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        elif selector_by == 'css' or selector_by == 'css_selector':
            try:
                elements = self.driver.find_elements_by_css_selector(selector_value)
                logger.info(
                f'Had find the elements successful. by {selector_by} via value: {selector_value}')
            except NoSuchElementException as e:
                logger.error(f"NoSuchElementException: {e}")
                self.get_windows_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return elements

    def type(self,selector,text):
        if isinstance(selector,str):
            el = self.find_element(selector)
        else:
            el = selector

        #el.clear()
        try:
            el.send_keys(Keys.CONTROL + "a")
            el.send_keys(text)
            logger.info(f"Had type \' {text} \' in inputBox" )
        except NameError as e:
            logger.error(f"Failed to type in input box with {e}")
            self.get_windows_img()

    def clear(self,selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing." )
        except NameError as e:
            logger.error(f'Failed to clear in input box with {e}')
            self.get_windows_img()

    def click(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info(f"The element was clicked.")
        except NameError as e:
            logger.error(f"Failed to click the element with {e}")

    def get_page_title(self):
        logger.info(f"Current page title is {self.driver.title}" )
        return  self.driver.title

    def move_to_ele(self,selector):
        el = self.find_element(selector)
        try:
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info(f"The element was moved.")
        except Exception as e:
            logger.error(f"Failed {e}")

    #判断元素是否存在
    def isElementExist(self,selector):
        driver = self.driver
        if '=>' not in selector:
            try:
                driver.find_element_by_id(selector)
                #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                return True
            except NoSuchElementException:
                return False
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                driver.find_element_by_id(selector_value)
                #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, selector_value)))
                return True
            except NoSuchElementException:
                return False
        elif selector_by == 'n' or selector_by == 'name':
            try:
                driver.find_element_by_name(selector_value)
                #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, selector_value)))
                return True
            except NoSuchElementException:
                return False

        elif selector_by == 't' or selector_by == 'tag' or selector_by == 'tag_name':
            try:
                driver.find_element_by_tag_name(selector_value)
                #WebDriverWait(driver, 5).until(
                #   EC.visibility_of_element_located((By.TAG_NAME, selector_value)))
                return True
            except NoSuchElementException:
                return False

        elif selector_by == 'c' or selector_by == 'class' or selector_by == 'class_name':
            try:
                driver.find_element_by_class_name(selector_value)
                # WebDriverWait(driver, 5).until(
                #     EC.visibility_of_element_located((By.CLASS_NAME, selector_value)))
                return True
            except NoSuchElementException:
                return False
        elif selector_by == 'l' or selector_by == 'link_text':
            try:
                driver.find_element_by_link_text(selector_value)
                # WebDriverWait(driver, 5).until(
                #     EC.visibility_of_element_located((By.LINK_TEXT, selector_value)))
                return True
            except NoSuchElementException:
                return False
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            try:
                driver.find_element_by_partial_link_text(selector_value)
                # WebDriverWait(driver, 5).until(
                #     EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)))
                return True
            except NoSuchElementException:
                return False
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                driver.find_element_by_xpath(selector_value)
                #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector_value)))
                return True
            except NoSuchElementException:
                return False
        elif selector_by == 'css' or selector_by == 'css_selector':
            try:
                driver.find_element_by_css_selector(selector_value)
                # WebDriverWait(driver, 5).until(
                #     EC.visibility_of_element_located((By.CSS_SELECTOR, selector_value)))
                return True
            except NoSuchElementException:
                return False
        else:
            return False

    def exe_js(self,js):
        '''执行js'''
        self.driver.execute_script(js)
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info(f"Sleep for {seconds} seconds")