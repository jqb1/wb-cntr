# WebsiteButtonCounter

This script provies you with a website `<button>` tag counter 

It accepts this type of buttons:
- html tag <button>:
`<button> Click me! </button>`
- types submit, reset, button:
```
<input type="submit" value="Submit button”>
<input type="reset" value="Reset button”>
<input type="button" value="Button button”>
```
- button class - any CSS class that contain button or btn keywords, case insensitive:
```
<a href="#" class="btn btn-small">Enter here!</a>
<a href="#" class="myCustomButton">Enter here!</a>
```

## Requirements:
Firstly install essential tools:
```
pip install -r requirements.txt
```
### Running script
example:
```
buttonz-counter.py files_with_websites.csv counted_websites.csv
```
*You can change:  files_with_websites.csv (file with web addresses)

*counted_websites.csv: name of the output file

To analyze html on localhost go to `/Button-counter/template` paste your code to file `localhost_template.html`

To run localhost type: `python -m http.server`
