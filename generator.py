import requests

def fetch_models():
    response = requests.get("https://huggingface.co/api/models")
    if response.status_code == 200:
        models = response.json()
        top_models = sorted(models, key=lambda x: x.get('downloads', 0), reverse=True)[:10]
        return top_models
    else:
        print("Failed to fetch models")
        return []

def generate_report():
    top_models = fetch_models()
    print("Top 10 Downloaded Models on Hugging Face:")
    for i, model in enumerate(top_models, start=1):
        print(f"{i}. {model['modelId']} - {model.get('downloads', 0)} downloads")

if __name__ == "__main__":
    generate_report()

