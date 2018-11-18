# SERVINGS
TF Servings Template


### Docker Container + TF Servings

Here is a snippet to launch a serving container. The container is listening on port 8501 and looking for POST REST API call.
```
docker run -p 8501:8501 \
  --mount type=bind,source=/Users/whiterabbit/Desktop/custom_api/model,target=/models/custom_api \
  -e MODEL_NAME=custom_api -t tensorflow/serving &
```

The best method would be to automate this with a *Dockerfile*.
### Making Rest API Calls example

A client needs to make a *POST* request to the server with the following properties: `curl -d '{"instances": [0.0]}' -X POST 127.0.0.1:8501/v1/models/custom_api:predict`

Here is another example making a request to version 3 of the model:
`curl -d '{"instances": {"x_in":[2]}}' -X POST 127.0.0.1:8501/v1/models/cusom_api/version/3:predict`

The input *{"instances": {"x_in":[2]}}* dictionary format is established by Tensorflow and may not be easily modified. This still seems like a good method for even highly complex datasets.
