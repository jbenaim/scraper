from get_image_links import search_and_download
DRIVER_PATH = './chromedriver 2'

search_term = 'dog'

search_and_download(
  search_term=search_term, 
  driver_path=DRIVER_PATH
)