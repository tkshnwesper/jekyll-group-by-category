# jekyll group by category

If all your posts are located in `_posts` directory, this script will

1. group them by category
2. create a directory for each category
3. add respective posts into a `_posts` directory inside each category directory (`<category>/_posts`)
4. will read text from standard input and replace all occurrances of `{}` with the `category` and add the contents to an `index.html` file at the path `<category>/index.html`
