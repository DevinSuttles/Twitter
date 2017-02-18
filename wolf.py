""""
Created on Fri Oct 25 21:51:08 2017
@author: Devin Suttles
"""

import wolframalpha

wolf_ID="KQP6LU-6GU23P4A6L"

client = wolframalpha.Client(wolf_ID)

res = client.query("iubawgiub")

#for pod in res.pods:
    #do_something_with(pod)
first = next(res.results, None)
if first:
    print(first.text)
