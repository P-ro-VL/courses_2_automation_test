import os
import subprocess

def run_feature_file(feature_path, max_attempts=2):
    attempt = 1
    while attempt <= max_attempts:
        print(f"\nAttempt {attempt} running: {feature_path}")
        result = subprocess.run(['behave', feature_path], capture_output=True, text=True)
        print(result.stdout)
        
        if result.returncode == 0:
            print(f"✅ Tests passed for: {feature_path}")
            break
        else:
            print(f"❌ Tests failed on attempt {attempt} for: {feature_path}")
            attempt += 1

    print('-' * 60)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    features_dir = os.path.join(base_dir, 'features', 'templates')

    # List all .feature files in the templates directory
    for file_name in os.listdir(features_dir):
        if file_name.endswith('.feature'):
            feature_path = os.path.join('features', 'templates', file_name)
            run_feature_file(feature_path)

if __name__ == "__main__":
    main()
