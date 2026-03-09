import json

api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''
data = json.loads(api_response)
request_id = data["id"]
status = data["status"]
text_result = data["result"]["text"]
confidence_score = data["result"]["confidence"]

print("Request ID:", request_id)
print("Status:", status)
print("Text Result:", text_result)
print("Confidence Score:", confidence_score)


if confidence_score < 0.9:
    print("Warning: Confidence score is low")

json_result = {
    "original_request_id": request_id,
    "processed": True,
    "message": "processing completed",
    "confidence_checked": confidence_score >= 0.9
}
json_output = json.dumps(json_result, indent=2)
with open("response.json", "w") as file:
    file.write(json_output)

print("\nJSON written to response.json")