# DOCUMENTATION:
#  https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# TUTORIAL:
#  https://www.youtube.com/watch?v=4UcqECQe5Kc

def introduction():
    from bs4 import BeautifulSoup
    html_doc = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <title>Scraping Sandbox</title>
                <link href="./css/bootstrap.min.css" rel="stylesheet">
                <link href="./css/main.css" rel="stylesheet">
            </head>
            <body>
                <div class="container">
                    <div class="row">
                        <div class="col-md-1"></div>
                        <div class="col-md-10 well">
                            <img class="logo" src="img/sh-logo.png" width="200px">
                            <h1 class="text-right">Web Scraping Sandbox</h1>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-1"></div>
                        <div class="col-md-10">
                            <h2>Books</h2>
                            <p>A <a href="http://books.toscrape.com">fictional bookstore</a> that desperately wants to be scraped. It's a safe place for beginners learning web scraping and for developers validating their scraping technologies as well. Available at: <a href="http://books.toscrape.com">books.toscrape.com</a></p>
                            <div class="col-md-6">
                                <a href="http://books.toscrape.com"><img src="./img/books.png" class="img-thumbnail"></a>
                            </div>
                            <div class="col-md-6">
                                <table class="table table-hover">
                                    <tr><th colspan="2">Details</th></tr>
                                    <tr><td>Amount of items </td><td>1000</td></tr>
                                    <tr><td>Pagination </td><td>&#10004;</td></tr>
                                    <tr><td>Items per page </td><td>max 20</td></tr>
                                    <tr><td>Requires JavaScript </td><td>&#10008;</td></tr>
                                </table>
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-1"></div>
                        <div class="col-md-10">
                            <h2>Quotes</h2>
                            <p><a href="http://quotes.toscrape.com/">A website</a> that lists quotes from famous people. It has many endpoints showing the quotes in many different ways, each of them including new scraping challenges for you, as described below.</p>
                            <div class="col-md-6">
                                <a href="http://quotes.toscrape.com"><img src="./img/quotes.png" class="img-thumbnail"></a>
                            </div>
                            <div class="col-md-6">
                                <table class="table table-hover">
                                    <tr><th colspan="2">Endpoints</th></tr>
                                    <tr><td><a href="http://quotes.toscrape.com/">Default</a></td><td>Microdata and pagination</td></tr>
                                    <tr><td><a href="http://quotes.toscrape.com/scroll">Scroll</a> </td><td>infinite scrolling pagination</td></tr>
                                    <tr><td><a href="http://quotes.toscrape.com/js">JavaScript</a> </td><td>JavaScript generated content</td></tr>
                                    <tr><td><a href="http://quotes.toscrape.com/tableful">Tableful</a> </td><td>a table based messed-up layout</td></tr>
                                    <tr><td><a href="http://quotes.toscrape.com/login">Login</a> </td><td>login with CSRF token (any user/passwd works)</td></tr>
                                    <tr><td><a href="http://quotes.toscrape.com/search.aspx">ViewState</a> </td><td>an AJAX based filter form with ViewStates</td></tr>
                                    <tr><td><a href="http://quotes.toscrape.com/random">Random</a> </td><td>a single random quote</td></tr>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </body>
        </html>
    """

    # Instantiate soup object with html parser to parse html_doc
    soup = BeautifulSoup(html_doc, 'html.parser')
    print()

    # === SEARCH ===
    # Primitively search for first tags
    print(soup.head.title)
    print(soup.head.link)
    print()

    # find() - Most recommended way to search for elements by tag name, ids, classes, etc.
    link = soup.find('link')            # Tag name
    print(link)
    row = soup.find(class_='row')       # Class
    print(row)
    href = soup.find(attrs={"href":"http://books.toscrape.com"})
    print(href)
    print()

    # findAll() - Retrieve list of every match. Identical parameters to find()
    links = soup.findAll('link')        # Tag name
    print(links)
    rows = soup.findAll(class_='row')   # Class
    print(rows)
    hrefs = soup.findAll(attrs={"href":"http://books.toscrape.com"})
    print(hrefs)
    print()

    # select() - OR INSTEAD USE CSS SELECTORS! ~ findAll()
    # https://www.w3schools.com/cssref/css_selectors.asp
    # https://www.w3schools.com/css/css_combinators.asp
    link = soup.select('link')
    print(links)
    row = soup.select('.row')
    print(row)
    href = soup.select('*[href="http://books.toscrape.com"]')
    print(href)
    print()

    # === TEXT EXTRACTION ===
    # Afterwards retrieve text from tags
    print(row[0].getText())
    # Using the strip() function is suggested to remove all surrounding whitespace
    print(row[0].getText().strip())
    print()

    # === NAVIGATION ===
    href_contents = [h.contents for h in href]
    print(href_contents)
    row_siblings = [r.find_next_sibling('p') for r in row]
    print(row_siblings)
    row_siblings = [r.find_previous_sibling('p') for r in row]
    print(row_siblings)
    print()


def introductoryExample():
    import requests
    from bs4 import BeautifulSoup
    from csv import writer

    # Web scraping exercise: http://toscrape.com/

    # GET request to website
    response = requests.get('http://quotes.toscrape.com/')

    # Instantiate soup object from GET request's response
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.select('div.quote')

    with open('tutorial.csv', 'w', newline='') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['Quote', 'Author', 'Tags']
        csv_writer.writerow(headers)

        for quote in quotes:
            # Finding first class text, extracting its text and stripping it
            text = quote.select('span.text')[0].getText().strip()[1:-1]
            author = quote.select('small.author')[0].getText().strip()
            tags = ','.join([tag.getText().strip() for tag in quote.select('a.tag')])

            csv_writer.writerow([text, author, tags])










def main():
    introductoryExample()


if __name__ == "__main__":
    main()
