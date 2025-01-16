
import grpc
from concurrent import futures
import time
import pickle  # For loading the pre-trained model

# Import generated classes
import catalyst_service_pb2
import catalyst_service_pb2_grpc

# Load pre-trained model (example: model.pkl)
MODEL_PATH = "model.pkl"
try:
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    model = None
    print("Model file not found. Ensure 'model.pkl' is in the service directory.")


# Catalyst Service Implementation
class CatalystService(catalyst_service_pb2_grpc.CatalystServiceServicer):
    def PredictBehavior(self, request, context):
        if model is None:
            return catalyst_service_pb2.CatalystResponse(
                status="Error", efficiency=0.0
            )
        # Predict catalyst behavior using the loaded model
        efficiency = model.predict([request.parameters])[0]
        return catalyst_service_pb2.CatalystResponse(status="Success", efficiency=efficiency)


# Start the gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    catalyst_service_pb2_grpc.add_CatalystServiceServicer_to_server(CatalystService(), server)
    server.add_insecure_port('[::]:50051')
    print("Catalyst Service with AI is running on port 50051...")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
