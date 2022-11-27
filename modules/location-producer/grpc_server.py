import grpc
import location_pb2
import location_pb2_grpc

from concurrent import futures

from utils import publish_location, logger

class LocationProducerServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        payload = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude
        }

        print(f"Request Payload:{payload} ")
        logger.info("Request Payload: ", payload)

        publish_location(payload)
        return location_pb2.LocationMessage(**payload)

# Intiialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationProducerServicer(), server)

print("Starting gRPC server on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

# Keep thread alive
server.wait_for_termination()