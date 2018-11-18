FROM tensorflow/serving:nightly

ENV model_name=sneed

COPY ./${model_name} /models/${model_name}

RUN apt update \
  && apt upgrade \
  && tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=${model_name} --model_base_path=/models/${model_name}

EXPOSE 8501
EXPOSE 8500
