# hugging-face-container


Steps:

1. Build the Image   --> docker build -t report-generator .
  
2. Run the Container  --> docker run --rm report-generator
  
3. It will show the logs and get removed.


To automate it we can use crontab on linux or use cronjob in kubernetes. I have added the cronjob.yaml, use below commands to check:

k apply -f cronjob.yaml

k get cj

k get job

k get pods

k logs po <pod-name>
