from scrapeTiger import multi_page,details_page

multi_page(url="https://quotes.toscrape.com/page/",start_page=1,end_page=3,css_selector= ".quote span a")"""here we passing url then set start_page=1 which will start
scraping from page 1 and also set end_page=3 which will stop scraping after reach page 2. we are grabing href of each items using css_selector"""

details_page(field_one_css='.author-title') #here we are scraping author name from details page of each items.
