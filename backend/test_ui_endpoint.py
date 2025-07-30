import requests
import json

def test_ui_endpoint():
    url = "http://localhost:8000/ui-test"
    payload = {
        "message": "I need name, email, and phone fields"
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            data = response.json()
            if 'content' in data and 'component' in data:
                print("✅ Response structure is correct")
                if data['component'] and isinstance(data['component'], dict):
                    print("✅ Component is a valid object")
                    if 'type' in data['component'] and 'fields' in data['component']:
                        print("✅ Component has required fields")
                    else:
                        print("❌ Component missing required fields")
                else:
                    print("❌ Component is not a valid object")
            else:
                print("❌ Response missing required fields")
        else:
            print("❌ Request failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_ui_endpoint() 