from selenium import webdriver


if __name__ == '__main__':
  path_to_driver = 'chromedriver'
  browser = webdriver.Chrome('./chromedriver')

  browser.get('https://authoraditiagarwal.com/leadership/')
  # ch = browser.find_element_by_class_name('sow-headline')
  browser.find_element_by_link_text('Leadership Agility: What You Need to Know').click()
  # print(ch)
  browser.close()