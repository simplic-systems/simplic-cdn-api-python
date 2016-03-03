
# Do imports
from .simpliccdn import SimplicCdnApi



# Create cdn connection
a = SimplicCdnApi('http://localhost:50121')

# Test connection
print  a.ping()

# LOgin
print a.login('admin', 'admin')

# Set blob
for i in range(0, 5000):
    print a.set_data(str(uuid.uuid4()), "YXNkYXNqZGhhdWlzZGggdWlhc2RoIHVpYXNoIGR1aWEgaGR1aWFzaCBkaXVhaHMgZHVpYWhkNzg5MmggdWlhc2Q=")