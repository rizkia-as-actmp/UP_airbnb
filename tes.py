from sqlalchemy import create_engine
from models.host import Host

# Assuming you have a SQLAlchemy engine
engine = create_engine("mysql://root:21204444@172.21.0.2:3306/UP_airbnb")

# Create a Connection from the Engine
conn = engine.connect()

# Create a Querier instance
# querier = Querier(conn=conn)

# Example: Create an account
# arg = CreateAccountParams("Khumairah", "umi@gmail.com", "21204444")
# result_create_account = querier.create_account(arg)
# conn.commit()

# Example: Create a HOST
# arg = CreateHostParams(3, "Mountain View Villa", "Rumah indah dengan pemandangan gunung alpen yang dikelilingin hutan taiga", "House", "Desa Minecraft", "Dapur", 300 )
# result_create_account = querier.create_host(arg)
# conn.commit()

# result_get_account = querier.get_host(id=1)
# account_data = result_get_account.fetchone()

# result_get_account = querier.list_host_by_owner(owner_id=3)
# account_data = result_get_account.fetchall()

# result_get_account = querier.delete_host(id=1)
# account_data = result_get_account.fetchall()
# conn.commit()

host = Host(conn, 3, "Coastal Resort", "Resort indah dipesisir pantai dengan pemandangan lautan dan pulau terlarang", "Resort", "Coastal Village, Plain Region", "Wifi", 30)
host.createHost()

host = Host(conn)
result = host.getHost(4)
hostData = result.fetchone()
print(hostData)


# Do something with the results...
# print(account_data.description)
# for data in account_data:
#     print(data.description)
