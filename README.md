Simplic-Cdn API for Python
===

Using this library you can easily access all simplic-cdn functions using `python` and `ironpython`.

For more information how to use the api, just take a look at http://simplic-cdn-com/doc/api/python

## Accessing the API

This example shows, how easy it is, to access the appi.

```
from simpliccdn import SimplicCdnApi

# Create instance
cdn = SimplicCdnApi()

# Login
cdn.login('admin', 'admin')

# Write some data
cdn.set_data('your_path', 'your-data-as-base-64')

# Request some data
data = cdn.get_data('your_path')
```