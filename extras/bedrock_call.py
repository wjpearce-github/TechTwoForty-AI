import boto3, json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

resp = client.invoke_model(
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 200,
        "messages": [{"role": "user", "content": "Summarise what a NAT gateway does."}],
    }),
)

print(json.loads(resp["body"].read())["content"][0]["text"])
