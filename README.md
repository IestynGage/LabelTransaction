# Label Transaction

This is a simple python program that labels transactions.

# Running LabelTransaction

1. Create `labels.json` in the top root folder of the project with an array of objects with:
* label with string value
* matches with an array of string

```json
[
    {
        "label": "Shopping",
        "matches": ["supermarket1", "supermarket2"]
    },
    {
        "label": "Transport",
        "matches": ["train"]
    }
]
```
2. Add `.csv` to the projects top root folder that you want to process it must have:
* Date
* Description
* Value

```
Date,Description,Value
"28/01/2022","Shopping", 50
```

3. Run `main.py` file

# Areas to improve

* Filter out date
* Add tests
* Clean up data
* Automatically add things to labels at run time.