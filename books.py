# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import getpass
import csv
import os
import json
import selenium
import  urllib.request


href_default = "https://walmart.com/browse/books/3920"


def Books():

    driver = webdriver.Chrome(ChromeDriverManager().install())

    data = []
    list_href_depart = []
    list_href_depart_0 = []
    str_cat_0 = ""
    str_cat_1 = ""
    str_cat_2 = ""
    str_cat_3 = ""
    str_cat_4 = ""
    str_cat_5 = ""

    with open('books.csv', 'w') as csvfile:
        fieldnames = ["name", "description", "category", "pricing", "image", "image_id"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


    driver.get(href_default)
    driver.find_element_by_xpath("//button[@class='button facet-see-more button--link']").click()
    department_all_0 = driver.find_elements_by_xpath("//li[contains(@class, 'department-single-level')]/a")

    for department_0 in department_all_0:
        href_depart_0 = department_0.get_attribute('href')
        # str_cat_0 = department_0.text
        # print(str_cat_0)
        list_href_depart_0.append(href_depart_0)

    for href_0 in list_href_depart_0:
        driver.get(href_0)
        driver.find_element_by_xpath("//button[@class='button facet-see-more button--link']").click()
        department_all_1 = driver.find_elements_by_xpath("//li[contains(@class, 'department-single-level')]/a")
        list_href_depart_1 = []
        list_str_depart_1 = []
        for department_1 in department_all_1:
            href_depart_1 = department_1.get_attribute('href')
            str_cat_1 = department_1.text
            list_href_depart_1.append(href_depart_1)
            list_str_depart_1.append(str_cat_1)

        for href_1 in list_href_depart_1:
            driver.get(href_1)
            driver.find_element_by_xpath("//button[@class='button facet-see-more button--link']").click()
            department_all_2 = driver.find_elements_by_xpath("//li[contains(@class, 'department-single-level')]/a")
            list_href_depart_2 = []
            list_str_depart_2 = []
            for department_2 in department_all_2:
                href_depart_2 = department_2.get_attribute('href')
                str_cat_2 = department_2.text
                list_href_depart_2.append(href_depart_2)
                list_str_depart_2.append(str_cat_2)
            if (list_str_depart_2[0] == list_str_depart_1[0]):
                continue
            for href_2 in list_href_depart_2:
                try:
                    driver.get(href_2)
                    driver.find_element_by_xpath("//button[@class='button facet-see-more button--link']").click()
                    department_all_3 = driver.find_elements_by_xpath("//li[contains(@class, 'department-single-level')]/a")
                    list_href_depart_3 = []
                    list_str_depart_3 = []
                    for department_3 in department_all_3:
                        href_depart_3 = department_3.get_attribute('href')
                        str_cat_3 = department_3.text
                        list_href_depart_3.append(href_depart_3)
                        list_str_depart_3.append(str_cat_3)
                    if (list_str_depart_2[0] == list_str_depart_3[0]):
                        continue

                    for href_3 in list_href_depart_3:
                        try:
                            driver.get(href_3)
                            driver.find_element_by_xpath("//button[@class='button facet-see-more button--link']").click()
                            department_all_4 = driver.find_elements_by_xpath(
                                "//li[contains(@class, 'department-single-level')]/a")
                            list_href_depart_4 = []
                            list_str_depart_4 = []
                            for department_4 in department_all_4:
                                href_depart_4 = department_4.get_attribute('href')
                                str_cat_4 = department_4.text
                                list_href_depart_4.append(href_depart_4)
                                list_str_depart_4.append(str_cat_4)
                            if (list_str_depart_3[0] == list_str_depart_4[0]):
                                continue

                            for href_4 in list_href_depart_4:
                                try:
                                    driver.get(href_4)
                                    driver.find_element_by_xpath(
                                        "//button[@class='button facet-see-more button--link']").click()
                                    department_all_5 = driver.find_elements_by_xpath(
                                        "//li[contains(@class, 'department-single-level')]/a")
                                    list_href_depart_5 = []
                                    list_str_depart_5 = []
                                    for department_5 in department_all_5:
                                        href_depart_5 = department_5.get_attribute('href')
                                        str_cat_5 = department_5.text
                                        list_href_depart_5.append(href_depart_5)
                                        list_str_depart_5.append(str_cat_5)
                                    if (list_str_depart_4[0] == list_str_depart_5[0]):
                                        continue

                                    for href_5 in list_href_depart_5:
                                        try:
                                            driver.get(href_5)
                                            driver.find_element_by_xpath(
                                                "//button[@class='button facet-see-more button--link']").click()
                                            department_all_6 = driver.find_elements_by_xpath(
                                                "//li[contains(@class, 'department-single-level')]/a")
                                            list_href_depart_6 = []
                                            list_str_depart_6 = []
                                            for department_6 in department_all_5:
                                                href_depart_6 = department_6.get_attribute('href')
                                                str_cat_6 = department_6.text
                                                list_href_depart_6.append(href_depart_6)
                                                list_str_depart_6.append(str_cat_6)
                                            if (list_str_depart_5[0] == list_str_depart_6[0]):
                                                continue


                                        except IndexError:
                                            # print(href_4)
                                            data_5 = GetProductsbyCatUrl(href_5)
                                            with open('books.csv', 'a') as csvfile:
                                                fieldnames = ["name", "description", "category", "pricing", "image", "image_id"]
                                                writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                                                        quoting=csv.QUOTE_ALL)
                                                for item_5 in data_5:
                                                    writer.writerow(item_5)
                                            # list_href_depart.append(href_4)
                                            continue
                                        except NoSuchElementException:
                                            continue


                                except IndexError:
                                    #print(href_4)
                                    data_4 = GetProductsbyCatUrl(href_4)
                                    with open('books.csv', 'a') as csvfile:
                                        fieldnames = ["name", "description", "category", "pricing", "image", "image_id"]
                                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                                        for item_4 in data_4:
                                            writer.writerow(item_4)
                                    #list_href_depart.append(href_4)
                                    continue
                                except NoSuchElementException:
                                    continue

                        except IndexError:
                            #print(href_3)
                            data_3 = GetProductsbyCatUrl(href_3)
                            with open('books.csv', 'a') as csvfile:
                                fieldnames = ["name", "description", "category", "pricing", "image", "image_id"]
                                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                                for item_3 in data_3:
                                    writer.writerow(item_3)
                            #list_href_depart.append(href_3)
                            continue
                        except NoSuchElementException:
                            continue

                except IndexError:
                    #print(href_2)
                    data_2 = GetProductsbyCatUrl(href_2)
                    with open('books.csv', 'a') as csvfile:
                        fieldnames = ["name", "description", "category", "pricing", "image", "image_id"]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                        for item_2 in data_2:
                            writer.writerow(item_2)
                    #list_href_depart.append(href_2)
                    continue
                except NoSuchElementException:
                    continue


    driver.close()

def GetProductsbyCatUrl(url):
    data = []
    driver_product = webdriver.Chrome(ChromeDriverManager().install())
    driver_product.get(url)

    i = 1
    while i < 25:

        # if i == 2:
        #     break
        try:
            products = driver_product.find_elements_by_xpath("//a[contains(@class, 'display-block')]")
            imgs = driver_product.find_elements_by_xpath("//a[contains(@class, 'display-block')]/img")
            prices = driver_product.find_elements_by_xpath("//div[contains(@class, 'product-price-with-fulfillment')]/span")
            category = driver_product.find_element_by_xpath("//ol[contains(@class, 'breadcrumb-list')]").text
            titles = driver_product.find_elements_by_xpath("//a[contains(@class, 'product-title-link line-clamp line-clamp-2')]")
            for p in range(0, len(products)):
                if not os.path.exists("images/" + category):
                    os.makedirs("images/" + category)
                list_prices = prices[p].text.split('\n')
                id = GetImageID(imgs[p].get_attribute("data-image-src"))
                img_url = imgs[p].get_attribute("data-image-src").replace("200&", "2000&")
                try:
                    urllib.request.urlretrieve(img_url, "images/" + category + "/" + id)
                except OSError:
                    continue
                time.sleep(3)
                product_data = {
                    "name": titles[p].get_attribute('title'),
                    "description": titles[p].get_attribute('title'),
                    "category": category,
                    "pricing": list_prices[1],
                    "image": img_url,
                    "image_id":id
                }
                print(product_data['name'])
                data.append(product_data)

            button_next = driver_product.find_element_by_xpath("//button[@class='elc-icon paginator-hairline-btn paginator-btn"
                                                               " paginator-btn-next outline']")
            button_next.click()
            time.sleep(3)
            i = i + 1
        except NoSuchElementException:
            break

    driver_product.close()
    return data

def GetImageID(url):
    list_id_0 = url.split('/')
    id = list_id_0[4].split('?')[0]
    return id

Books()
