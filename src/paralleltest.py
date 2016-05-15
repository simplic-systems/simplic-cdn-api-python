
# Do imports
from simpliccdn import SimplicCdnApi



# Create cdn connection
a = SimplicCdnApi.SimplicCdnApi('http://localhost:50121')

# Test connection
print  a.ping()

# Login
print a.login('UnitTestUser', 'UnitTestPassword')

# Set blob
#for i in range(0, 5000):
#    print a.set_data(str(uuid.uuid4()), "YXNkYXNqZGhhdWlzZGggdWlhc2RoIHVpYXNoIGR1aWEgaGR1aWFzaCBkaXVhaHMgZHVpYWhkNzg5MmggdWlhc2Q=")

for i in range(0, 2000):
    print a.get_data('00b908bf-7525-472d-88e1-bbc0542e8a50')