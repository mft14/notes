# My Python Code Snippets

## Formatting
##### Current date correctly formatte
```
import datetime
now = str(datetime.datetime.now())[0:str(datetime.datetime.now()).find('.')]#gets today's date correctly formatted
```