## Building

Build the lambda by changing to this working directory and running:

`mkdir build && pip install -r requirements.txt --target build && cp lambda_function.py build && cd build && zip -r lambda.zip . && cd .. && mv build/lambda.zip . && rm -rf build`

The output file, `lambda.zip`, can then be uploaded to AWS.

## Some curl commands for testing

Run the Twilio SMS flow.

```
curl -X POST https://subscriptions.bugalert.org/runsms \ 
-H 'Content-Type: application/json' \
-H 'Origin: https://bugalert.org' \
-d '{"api_key":"REMOVED", "email": "nobody@example.com", "category":"dev", "message": "Bug Alert: This is a test of new Bug Alert capabilities. You can ignore this test. https://bugalert.org/?src=s"}'
```

Run the Twilio phone call flow.

```
curl -X POST https://subscriptions.bugalert.org/runtel \
-H 'Content-Type: application/json' \
-H 'Origin: https://bugalert.org' \
-d '{"api_key":"REMOVED", "email": "nobody@example.com", "category":"dev", "message": "This is a test of new Bug Alert capabilities. You can ignore this test."}'
```

Run the email contacts update flow.
```
curl -X POST https://subscriptions.bugalert.org/listup \
-H 'Content-Type: application/json' \
-H 'Origin: https://bugalert.org' \
-d '{"api_key":"REMOVED", "email": "nobody@example.com", "category":"dev"}'
```

