# Journal.vim

## What it does
This plugin lets you organize your daily journal.<br>
It lets you open a day specific journal and manages the files all behind the scenes.

## Setup and Config
```vim
let g:journals_directory = "/path/to/journals_directory"

" Set by default
let g:journals_date_format = '%b-%d-%Y'

" Set by default
let g:journals_title_template = 'Journal entry {date}'
```

## Commands
| Command               | Description                 |
|-----------------------|-----------------------------|
| :Journal              | Open the journal for today  |
| :JournalSearch <word> | Keyword search for journals |

## Future features
- A search by date or relative date (ex. "last friday")
