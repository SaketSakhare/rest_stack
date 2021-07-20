# rest_stack
# Run the FastApi server
* cd app
* uvicorn  main:app --reload

# Download and install goreplay to store http trafic 
* https://github.com/buger/goreplay/releases
* dpkg --force-all -i gor_v1.3.0_RC5_amd64.deb
* gor --input-raw :8000 --output-file test.text

# Replay the stored test data on api server
* gor --input-file test_0.text  --output-http http://localhost:8000
