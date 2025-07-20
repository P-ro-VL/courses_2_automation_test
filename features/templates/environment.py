import requests

def before_scenario(context, scenario):
  print("------ PREPARING SCENARIO ------")
  print(f"Starting scenario: {scenario.name}")

  print("Deleting all test templates...")
  delete_all_test_templates()

  print("------ SCENARIO PREPARATION DONE ------\n")

# -------------------------------------------- #

def delete_all_test_templates():
    template_name = "[Auto Test] Quy trình tạo ngành mới trường Công nghệ - Đại học Kinh tế Quốc dân"

    response = requests.get('https://courses-admin.neu.edu.vn/backend/templates')
    data = response.json()

    objects = data['object']

    for obj in objects:
        if obj['name'] == template_name:
            template_id = obj['templateId']
            delete_response = requests.delete(f'https://courses-admin.neu.edu.vn/backend/templates/{template_id}')
            if delete_response.status_code == 200:
                print(f"Deleted template: {template_name}")
            else:
                print(f"Failed to delete template: {template_name}, Status Code: {delete_response.status_code}")

