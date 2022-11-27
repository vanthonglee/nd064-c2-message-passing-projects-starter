import faker
import grpc
import location_pb2
import location_pb2_grpc

"""
A sample gRPC client implementation demonstrates how to communicate with gRPC from a mobile device.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("127.0.0.1:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Existing people
preloaded_person_ids = [1, 5, 6, 8, 9]
# Non-existing people
non_existing_person_ids = [987, 56]

fake = faker.Faker()

def random_float_str():
    return str(fake.pyfloat(1))

# Send the chosen payload to both existing and non-existing people
payloads = [location_pb2.LocationMessage(person_id=y, latitude=random_float_str(), longitude=random_float_str()) for x in [preloaded_person_ids, non_existing_person_ids] for y in x]

for location in payloads:
    response = stub.Create(location)
    print(f"The gRPC server's response: {response}")