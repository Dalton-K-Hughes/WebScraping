import mechanicalsoup

base_url = 'http://olympus.realpython.org'
browser = mechanicalsoup.Browser()

login_page = browser.get(base_url + '/login')
login_html = login_page.soup

form = login_html.select('form')[0]

form.select('input')[0]['value'] = 'zeus'
form.select('input')[1]['value'] = 'ThunderDude'

profiles_page = browser.submit(form, login_page.url)

title = profiles_page.soup.select('title')[0]
print(title)