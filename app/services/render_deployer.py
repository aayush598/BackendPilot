import requests

def deploy_to_render(github_repo_url, service_name, workspace_name, workspace_email, render_api_key):
    print("Deploy to Render started")
    try:
        # Step 1: Get ownerId using /v1/owners?name=...&email=...
        headers = {
            "Authorization": f"Bearer {render_api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        owner_url = f"https://api.render.com/v1/owners?name={workspace_name}&email={workspace_email}&limit=1"
        owner_response = requests.get(owner_url, headers=headers)

        if owner_response.status_code != 200:
            return {"success": False, "message": f"Failed to fetch owner info: {owner_response.text}"}

        owners_list = owner_response.json()

        print(f"owners_list : {owners_list[0]['owner']['id']}")

        if not owners_list or not owners_list[0]["owner"] or not owners_list[0]["owner"]["id"]:
            return {"success": False, "message": "Owner ID not found in Render API response."}

        # ✅ Correct extraction
        owner_id = owners_list[0]["owner"]["id"]

        # Step 2: Prepare deployment payload
        payload = {
            "service": {
                "type": "web_service",
                "name": service_name,
                "repo": github_repo_url,
                "branch": "main",
                "rootDir": "",
                "buildCommand": "pip install -r requirements.txt",  # Adjust if needed
                "startCommand": "gunicorn app:app",                # Adjust if needed
                "envVars": [],
                "plan": "free",
                "ownerId": owner_id
            }
        }

        print("Request sending...")

        # Step 3: Deploy service
        response = requests.post(
            "https://api.render.com/v1/services",
            json=payload,
            headers=headers,
            timeout=30  # Timeout after 30 seconds (adjust as necessary)
        )


        print("Response received")
        if response.status_code in [200, 201]:
            return {"success": True, "message": "Deployment triggered successfully.", "details": response.json()}
        else:
            return {"success": False, "message": f"Render API Error: {response.text}"}

    except Exception as e:
        return {"success": False, "message": str(e)}
