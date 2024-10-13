# Read Me

This series of Python scripts demonstrates how to use the Python [unittest](https://docs.python.org/3/library/unittest.html) module to perform some simple unit tests. This application is meant to be used directly by a *developer* or *tester*, and its simple usage is demonstrated by the following use case diagram.
![alt text](https://raw.githubusercontent.com/wildharpo/Testing_Documentation/refs/heads/main/Python%20Tester%20Use%20Case%20Diagram.jpeg "use case diagram image").

As an example, take a look at the [number_verification_test.py](IntegrationTests/number_verification_test.py) file.

The first thing we have to do is import the unittest module and the os module in order for our Python script to have access to the original classes that it needs. The following portion of the code accomplishes this:

```python
import unittest
import sys, os
sys.path.append(os.path.join(sys.path[0], '../../Client/Helpers'))
sys.path.append(os.path.join(sys.path[0], '../../Client/Services'))
from number_formatter import *
from number_verification_api import *
```

Our number_verification_test.py file is two folders below the directory we need to import in order to have access to the files we want to test. The Python sys module allows us to append values to our environment variable path in order to get that access. We need the [number_verification_api](Client/Services/number_verification_api.py) file in order to test its logic for adherance to our expected number verification functionality, and it leverages the [number_formatter](Client/Helpers/number_formatter.py) file for a portion of its workflow.
