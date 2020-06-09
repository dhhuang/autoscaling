import json
import tmpvalidate_lambda


fake_event = '''
{
    "StackId": "arn:aws:cloudformation:us-west-2:000000000000:stack/llf-55/2eceb8f0-6373-11ea-a475-02e60452d3a4",
    "ResponseURL": "https://cloudformation-custom-resource-response-uswest2.s3-us-west-2.amazonaws.com/arn%3Aaws%3Acloudformation%3Aus-west-2%3A209770520358%3Astack/llf-55/2eceb8f0-6373-11ea-a475-02e60452d3a4%7CcallValidateParameters%7C133d4a13-dc1e-448c-8e96-e434fb45ad47?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200311T083520Z&X-Amz-SignedHeaders=host&X-Amz-Expires=7200&X-Amz-Credential=AKIA54RCMT6SCLH6XNBN%2F20200311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=d055d160b31d6682550bdeb8995d83fcfe44178fa05e3936c80eed0616434b0a",
    "ResourceProperties": {
        "FortiWebAsgMinSize": "3",
        "FortiWebElasticIP": "1.1.2",
        "AddNewElasticIPorNot": "no",
        "ServiceToken": "arn:aws:lambda:us-west-2:000000000000:function:11-lfFwb-2eceb8f0",
        "FortiWebVersionShow": "1.1",
        "FortiWebAsgMaxSize": "4",
        "FortiWebAsgDesiredCapacity": "3",
        "FortiWebAsgScaleOutThreshold": "4",
        "FortiWebAsgScaleInThreshold": "3"
    },
    "RequestType": "Create",
    "ServiceToken": "arn:aws:lambda:us-west-2:000000000000:function:11-lfFwb-2eceb8f0",
    "ResourceType": "AWS::CloudFormation::CustomResource",
    "RequestId": "133d4a13-dc1e-448c-8e96-e434fb45ad47",
    "LogicalResourceId": "callValidateParameters"
}
'''

class fake_context():
    def __init__(self):
        self.log_group_name = 'fake-test-group_name'
        self.log_stream_name = 'fake-test-stream_name'
        self.get_remaining_time_in_millis = self.get_left_time_millis
    def get_left_time_millis(self):
        return 10*60*1000


event = json.loads(fake_event)
#print(type(event),event)

context = fake_context()
#print(context.log_group_name, context.log_stream_name, context.get_remaining_time_in_millis())

tmpvalidate_lambda.handler(event, context)


