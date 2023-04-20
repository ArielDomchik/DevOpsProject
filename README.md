terraform apply to provision vpc and cluster
Dont forget to manually attach AmazonEBSCSIPolicy! (need to find a way to provision this with terraform)
update-kubeconfig context to use provisioned cluster api server
label node in az us-east-1a "vol=pers" (kubectl label node <node> vol=pers)
run pipeline 

Need to do :
- Make the application as a helm bundle

