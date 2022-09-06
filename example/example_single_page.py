from scrapeTiger import single_page,details_page

single_page(url="https://quotes.toscrape.com/",css_selector= ".quote span a") #here we are giving url and aslo grabing href of each items using css_selector. 

details_page(field_one_css='.author-title') #here we are scraping author name from details page of each items.



