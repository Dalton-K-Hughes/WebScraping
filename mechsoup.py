import mechanicalsoup

# Create a variable called browser to represent an object of Browser from mechanicalsoup
browser = mechanicalsoup.Browser()

# Create a variable called url to hold a string of the url for the website
url = "http://olympus.realpython.org/login"

# Create a response object called login_page that stores the response from the requesting url
login_page = browser.get(url)

# Parse the html from the request with beautiful soup
login_html = login_page.soup

# Get the html of the first form in the webpage
form = login_html.select('form')[0]

# Select the username input and assign it to their respective value to login
form.select('input')[0]['value'] = 'zeus'

# Select the password input and assign it to their respective value to login
form.select('input')[1]['value'] = 'ThunderDude'

# Submit the form with the two arguments, the form with the values we inserted and the url of the login page
profiles_page = browser.submit(form, login_page.url)

links = profiles_page.soup.select('a')

base_url = "http://olympus.realpython.org"
for link in links:
    address = base_url + link['href']
    text = link.text
    print(f'{text}: {address}')