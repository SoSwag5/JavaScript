# scrap using, local files
from bs4 import BeautifulSoup
import requests  #like a real person from a website requestion some information


with open('shop.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
# grabbing specific information that we want to grab
    course_card = soup.find_all('div',class_='product') # to find the product class
    for course in course_card:
        course_name = course.h2.text
        course_price = course.find('p', class_='price').text  # to find the price class

        print(f"{course_name} costs {course_price}")