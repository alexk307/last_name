# Name Suggester

Suggests valid names that sound similar to a given name.
Based on the double metaphone algorithm (https://en.wikipedia.org/wiki/Metaphone#Double_Metaphone).

# Install it
`pip install name_suggestor`

# Usage
```
from name_suggestor import name
>>> name.suggest_name('Alex')
[('ALEX', 0), ('ALLEX', 1), ('ALEXA', 1), ('ALIX', 1), ('ALEXY', 1), ('ELIX', 2), ('OLEXY', 2), ('ALEXIE', 2), ('OLEXA', 2), ('ALEIXO', 2), ('ELKS', 3), ('ALEKSA', 3), ('ELKES', 3), ...]
```

the `suggest_name` method returns a list of tuples, each with an alternative name, and its levenshtein distance from the original name.
