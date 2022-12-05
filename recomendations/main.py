import grpc
from recomendations_pb2_grpc import RecommendationsStub
from recomendations_pb2 import BookCategory, RecommendationRequest

if __name__ == "__main__":
    channel = grpc.insecure_channel("localhost:50051")
    client = RecommendationsStub(channel)

    while True:
        category = input("choose category to recommend (MYSTERY, SCIENCE_FICTION, SELF_HELP):\n\t")
        if category == "exit":
            break

        request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)

        print(client.Recommend(request))
