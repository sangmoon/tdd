from selenium import webdriver


browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. she goes
# to check out its homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

# She tpyes "Buy peacock feathers" into a text box (Edith's hobby
# is typing fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. she
# enters "Use peacock feaatherss to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her lists. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do lists is still there.

# Satisfied, she goes back to sleep.

browser.quit()
