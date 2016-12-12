#Getting started

## How to Build


You must have Python 2 >=2.7.9 or Python 3 >=3.4 installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](http://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Message360-Python)


## How to Use

The following section explains how to use the Message360 SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Message360-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Message360-Python&projectName=message360)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Message360-Python&projectName=message360)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=createFile&workspaceFolder=Message360-Python&projectName=message360)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from message360.message_360_client import *
```

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Message360-Python&libraryName=message360.message_360_client&projectName=message360)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](http://apidocs.io/illustration/python?step=runProject&workspaceFolder=Message360-Python&libraryName=message360.message_360_client&projectName=message360)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'pip install -r test-requirements.txt'
  3. Invoke 'nosetests'

## Initialization

### Authentication and 
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| basic_auth_user_name | The username to use with basic authentication |
| basic_auth_password | The password to use with basic authentication |



API client can be initialized as following.

```python
# Configuration parameters and credentials
basic_auth_user_name = "basic_auth_user_name" # The username to use with basic authentication
basic_auth_password = "basic_auth_password" # The password to use with basic authentication

client = Message360Client(basic_auth_user_name, basic_auth_password)
```

## Class Reference

### <a name="list_of_controllers"></a>List of Controllers

* [ConferenceController](#conference_controller)
* [EmailController](#email_controller)
* [NumberVerificationController](#number_verification_controller)
* [CarrierController](#carrier_controller)
* [CallController](#call_controller)
* [SMSController](#sms_controller)
* [AccountController](#account_controller)
* [WebRTCController](#web_rtc_controller)
* [SubAccountController](#sub_account_controller)
* [AddressController](#address_controller)
* [PhoneNumberController](#phone_number_controller)
* [RecordingController](#recording_controller)
* [TranscriptionController](#transcription_controller)
* [UsageController](#usage_controller)

### <a name="conference_controller"></a>![Class: ](http://apidocs.io/img/class.png ".ConferenceController") ConferenceController

#### Get controller instance

An instance of the ``` ConferenceController ``` class can be accessed from the API Client.

```python
 conference_client = client.conference
```

#### <a name="create_deaf_mute_participant"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.create_deaf_mute_participant") create_deaf_mute_participant

> Deaf Mute Participant

```python
def create_deaf_mute_participant(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | TODO: Add a parameter description |
| participantSid |  ``` Required ```  | TODO: Add a parameter description |
| muted |  ``` Optional ```  | TODO: Add a parameter description |
| deaf |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

conference_sid = 'conferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid

muted = True
collect['muted'] = muted

deaf = True
collect['deaf'] = deaf

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.create_deaf_mute_participant(collect)

```


#### <a name="create_list_conference"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.create_list_conference") create_list_conference

> List Conference

```python
def create_list_conference(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| friendlyName |  ``` Optional ```  | Only return conferences with the specified FriendlyName |
| status |  ``` Optional ```  | TODO: Add a parameter description |
| dateCreated |  ``` Optional ```  | TODO: Add a parameter description |
| dateUpdated |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

page = 186
collect['page'] = page

page_size = 186
collect['page_size'] = page_size

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

status = InterruptedCallStatus.CANCELED
collect['status'] = status

date_created = 'DateCreated'
collect['date_created'] = date_created

date_updated = 'DateUpdated'
collect['date_updated'] = date_updated

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.create_list_conference(collect)

```


#### <a name="create_view_conference"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.create_view_conference") create_view_conference

> View Conference

```python
def create_view_conference(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferencesid |  ``` Required ```  | The unique identifier of each conference resource |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

conferencesid = 'conferencesid'
collect['conferencesid'] = conferencesid

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.create_view_conference(collect)

```


#### <a name="add_participant"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.add_participant") add_participant

> Add Participant in conference 

```python
def add_participant(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferencesid |  ``` Required ```  | Unique Conference Sid |
| participantnumber |  ``` Required ```  | Particiant Number |
| tocountrycode |  ``` Required ```  | TODO: Add a parameter description |
| muted |  ``` Optional ```  | TODO: Add a parameter description |
| deaf |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

conferencesid = 'conferencesid'
collect['conferencesid'] = conferencesid

participantnumber = 'participantnumber'
collect['participantnumber'] = participantnumber

tocountrycode = 186
collect['tocountrycode'] = tocountrycode

muted = True
collect['muted'] = muted

deaf = True
collect['deaf'] = deaf

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.add_participant(collect)

```


#### <a name="create_list_participant"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.create_list_participant") create_list_participant

> List Participant

```python
def create_list_participant(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | unique conference sid |
| page |  ``` Optional ```  | page number |
| pagesize |  ``` Optional ```  | TODO: Add a parameter description |
| muted |  ``` Optional ```  | TODO: Add a parameter description |
| deaf |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

page = 186
collect['page'] = page

pagesize = 186
collect['pagesize'] = pagesize

muted = True
collect['muted'] = muted

deaf = True
collect['deaf'] = deaf

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.create_list_participant(collect)

```


#### <a name="create_view_participant"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.create_view_participant") create_view_participant

> View Participant

```python
def create_view_participant(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | unique conference sid |
| participantSid |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.create_view_participant(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="email_controller"></a>![Class: ](http://apidocs.io/img/class.png ".EmailController") EmailController

#### Get controller instance

An instance of the ``` EmailController ``` class can be accessed from the API Client.

```python
 email_client = client.email
```

#### <a name="create_delete_invalid"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_delete_invalid") create_delete_invalid

> This endpoint allows you to delete entries in the Invalid Emails list.

```python
def create_delete_invalid(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.create_delete_invalid(collect)

```


#### <a name="create_list_blocks"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_blocks") create_list_blocks

> Outputs email addresses on your blocklist

```python
def create_list_blocks(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| offset |  ``` Optional ```  | Where to start in the output list |
| limit |  ``` Optional ```  | Maximum number of records to return |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

offset = 'offset'
collect['offset'] = offset

limit = 'limit'
collect['limit'] = limit

response_type = 'json'
collect['response_type'] = response_type


result = email_client.create_list_blocks(collect)

```


#### <a name="create_list_spam"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_spam") create_list_spam

> List out all email addresses marked as spam

```python
def create_list_spam(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |
| offset |  ``` Optional ```  | The record number to start the list at |
| limit |  ``` Optional ```  | Maximum number of records to return |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

offset = 'offset'
collect['offset'] = offset

limit = 'limit'
collect['limit'] = limit


result = email_client.create_list_spam(collect)

```


#### <a name="create_list_bounces"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_bounces") create_list_bounces

> List out all email addresses that have bounced

```python
def create_list_bounces(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |
| offset |  ``` Optional ```  | The record to start the list at |
| limit |  ``` Optional ```  | The maximum number of records to return |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

offset = 'offset'
collect['offset'] = offset

limit = 'limit'
collect['limit'] = limit


result = email_client.create_list_bounces(collect)

```


#### <a name="create_delete_bounces"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_delete_bounces") create_delete_bounces

> Delete an email address from the bounced address list

```python
def create_delete_bounces(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email address to remove from the bounce list |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.create_delete_bounces(collect)

```


#### <a name="create_list_invalid"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_invalid") create_list_invalid

> List out all invalid email addresses

```python
def create_list_invalid(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |
| offet |  ``` Optional ```  | Starting record for listing out emails |
| limit |  ``` Optional ```  | Maximum number of records to return |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

offet = 'offet'
collect['offet'] = offet

limit = 'limit'
collect['limit'] = limit


result = email_client.create_list_invalid(collect)

```


#### <a name="create_list_unsubscribes"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_unsubscribes") create_list_unsubscribes

> List all unsubscribed email addresses

```python
def create_list_unsubscribes(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |
| offset |  ``` Optional ```  | Starting record of the list |
| limit |  ``` Optional ```  | Maximum number of records to be returned |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

offset = 'offset'
collect['offset'] = offset

limit = 'limit'
collect['limit'] = limit


result = email_client.create_list_unsubscribes(collect)

```


#### <a name="create_delete_unsubscribes"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_delete_unsubscribes") create_delete_unsubscribes

> Delete emails from the unsubscribe list

```python
def create_delete_unsubscribes(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email to remove from the unsubscribe list |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.create_delete_unsubscribes(collect)

```


#### <a name="add_unsubscribes"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.add_unsubscribes") add_unsubscribes

> Add an email to the unsubscribe list

```python
def add_unsubscribes(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email to add to the unsubscribe list |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.add_unsubscribes(collect)

```


#### <a name="create_delete_block"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_delete_block") create_delete_block

> Deletes a blocked email

```python
def create_delete_block(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | Email address to remove from block list |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.create_delete_block(collect)

```


#### <a name="create_delete_spam"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_delete_spam") create_delete_spam

> Deletes a email address marked as spam from the spam list

```python
def create_delete_spam(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | Email address |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.create_delete_spam(collect)

```


#### <a name="create_send_email"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_send_email") create_send_email

> Send out an email

```python
def create_send_email(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| to |  ``` Required ```  | The to email address |
| mfrom |  ``` Required ```  | The from email address |
| mtype |  ``` Required ```  ``` DefaultValue ```  | email format type, html or text |
| subject |  ``` Required ```  | Email subject |
| message |  ``` Required ```  | The body of the email message |
| cc |  ``` Optional ```  | CC Email address |
| bcc |  ``` Optional ```  | BCC Email address |
| attachment |  ``` Optional ```  | File to be attached.File must be less than 7MB. |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

to = 'to'
collect['to'] = to

mfrom = 'from'
collect['mfrom'] = mfrom

mtype = SendEmailAs.HTML
collect['mtype'] = mtype

subject = 'subject'
collect['subject'] = subject

message = 'message'
collect['message'] = message

cc = 'cc'
collect['cc'] = cc

bcc = 'bcc'
collect['bcc'] = bcc

attachment = 'attachment'
collect['attachment'] = attachment

response_type = 'json'
collect['response_type'] = response_type


result = email_client.create_send_email(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="number_verification_controller"></a>![Class: ](http://apidocs.io/img/class.png ".NumberVerificationController") NumberVerificationController

#### Get controller instance

An instance of the ``` NumberVerificationController ``` class can be accessed from the API Client.

```python
 number_verification_client = client.number_verification
```

#### <a name="create_verify_number"></a>![Method: ](http://apidocs.io/img/method.png ".NumberVerificationController.create_verify_number") create_verify_number

> Number Verification

```python
def create_verify_number(self,
                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phonenumber |  ``` Required ```  | TODO: Add a parameter description |
| mtype |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

phonenumber = 'phonenumber'
collect['phonenumber'] = phonenumber

mtype = 'type'
collect['mtype'] = mtype

response_type = 'json'
collect['response_type'] = response_type


result = number_verification_client.create_verify_number(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="carrier_controller"></a>![Class: ](http://apidocs.io/img/class.png ".CarrierController") CarrierController

#### Get controller instance

An instance of the ``` CarrierController ``` class can be accessed from the API Client.

```python
 carrier_client = client.carrier
```

#### <a name="create_carrier_lookup"></a>![Method: ](http://apidocs.io/img/method.png ".CarrierController.create_carrier_lookup") create_carrier_lookup

> Get the Carrier Lookup

```python
def create_carrier_lookup(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phonenumber |  ``` Required ```  | The number to lookup |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phonenumber = 'phonenumber'
collect['phonenumber'] = phonenumber

response_type = 'json'
collect['response_type'] = response_type


result = carrier_client.create_carrier_lookup(collect)

```


#### <a name="create_carrier_lookup_list"></a>![Method: ](http://apidocs.io/img/method.png ".CarrierController.create_carrier_lookup_list") create_carrier_lookup_list

> Get the All Purchase Number's Carrier lookup

```python
def create_carrier_lookup_list(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Page Number |
| pagesize |  ``` Optional ```  | Page Size |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

page = 22
collect['page'] = page

pagesize = 22
collect['pagesize'] = pagesize

response_type = 'json'
collect['response_type'] = response_type


result = carrier_client.create_carrier_lookup_list(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="call_controller"></a>![Class: ](http://apidocs.io/img/class.png ".CallController") CallController

#### Get controller instance

An instance of the ``` CallController ``` class can be accessed from the API Client.

```python
 call_client = client.call
```

#### <a name="create_view_call"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_view_call") create_view_call

> View Call Response

```python
def create_view_call(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callsid |  ``` Required ```  | Call Sid id for particular Call |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

callsid = 'callsid'
collect['callsid'] = callsid

response_type = 'json'
collect['response_type'] = response_type


result = call_client.create_view_call(collect)

```


#### <a name="create_group_call"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_group_call") create_group_call

> Group Call

```python
def create_group_call(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| fromCountryCode |  ``` Required ```  ``` DefaultValue ```  | TODO: Add a parameter description |
| mfrom |  ``` Required ```  | TODO: Add a parameter description |
| toCountryCode |  ``` Required ```  ``` DefaultValue ```  | TODO: Add a parameter description |
| to |  ``` Required ```  | TODO: Add a parameter description |
| url |  ``` Required ```  | TODO: Add a parameter description |
| method |  ``` Optional ```  | TODO: Add a parameter description |
| statusCallBackUrl |  ``` Optional ```  | TODO: Add a parameter description |
| statusCallBackMethod |  ``` Optional ```  | TODO: Add a parameter description |
| fallBackUrl |  ``` Optional ```  | TODO: Add a parameter description |
| fallBackMethod |  ``` Optional ```  | TODO: Add a parameter description |
| heartBeatUrl |  ``` Optional ```  | TODO: Add a parameter description |
| heartBeatMethod |  ``` Optional ```  | TODO: Add a parameter description |
| timeout |  ``` Optional ```  | TODO: Add a parameter description |
| playDtmf |  ``` Optional ```  | TODO: Add a parameter description |
| hideCallerId |  ``` Optional ```  | TODO: Add a parameter description |
| record |  ``` Optional ```  | TODO: Add a parameter description |
| recordCallBackUrl |  ``` Optional ```  | TODO: Add a parameter description |
| recordCallBackMethod |  ``` Optional ```  | TODO: Add a parameter description |
| transcribe |  ``` Optional ```  | TODO: Add a parameter description |
| transcribeCallBackUrl |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

from_country_code = '1'
collect['from_country_code'] = from_country_code

mfrom = 'From'
collect['mfrom'] = mfrom

to_country_code = '1'
collect['to_country_code'] = to_country_code

to = 'To'
collect['to'] = to

url = 'Url'
collect['url'] = url

method = HttpAction.GET
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

status_call_back_method = HttpAction.GET
collect['status_call_back_method'] = status_call_back_method

fall_back_url = 'FallBackUrl'
collect['fall_back_url'] = fall_back_url

fall_back_method = HttpAction.GET
collect['fall_back_method'] = fall_back_method

heart_beat_url = 'HeartBeatUrl'
collect['heart_beat_url'] = heart_beat_url

heart_beat_method = HttpAction.GET
collect['heart_beat_method'] = heart_beat_method

timeout = 22
collect['timeout'] = timeout

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

hide_caller_id = 'HideCallerId'
collect['hide_caller_id'] = hide_caller_id

record = False
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = HttpAction.GET
collect['record_call_back_method'] = record_call_back_method

transcribe = False
collect['transcribe'] = transcribe

transcribe_call_back_url = 'TranscribeCallBackUrl'
collect['transcribe_call_back_url'] = transcribe_call_back_url

response_type = 'json'
collect['response_type'] = response_type


result = call_client.create_group_call(collect)

```


#### <a name="create_voice_effect"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_voice_effect") create_voice_effect

> Voice Effect

```python
def create_voice_effect(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | TODO: Add a parameter description |
| audioDirection |  ``` Optional ```  | TODO: Add a parameter description |
| pitchSemiTones |  ``` Optional ```  | value between -14 and 14 |
| pitchOctaves |  ``` Optional ```  | value between -1 and 1 |
| pitch |  ``` Optional ```  | value greater than 0 |
| rate |  ``` Optional ```  | value greater than 0 |
| tempo |  ``` Optional ```  | value greater than 0 |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

audio_direction = AudioDirection.IN
collect['audio_direction'] = audio_direction

pitch_semi_tones = 22.8361971480009
collect['pitch_semi_tones'] = pitch_semi_tones

pitch_octaves = 22.8361971480009
collect['pitch_octaves'] = pitch_octaves

pitch = 22.8361971480009
collect['pitch'] = pitch

rate = 22.8361971480009
collect['rate'] = rate

tempo = 22.8361971480009
collect['tempo'] = tempo

response_type = 'json'
collect['response_type'] = response_type


result = call_client.create_voice_effect(collect)

```


#### <a name="create_record_call"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_record_call") create_record_call

> Record a Call

```python
def create_record_call(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| record |  ``` Required ```  | Set true to initiate recording or false to terminate recording |
| direction |  ``` Optional ```  | The leg of the call to record |
| timeLimit |  ``` Optional ```  | Time in seconds the recording duration should not exceed |
| callBackUrl |  ``` Optional ```  | URL consulted after the recording completes |
| fileformat |  ``` Optional ```  | Format of the recording file. Can be .mp3 or .wav |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

record = False
collect['record'] = record

direction = Direction.IN
collect['direction'] = direction

time_limit = 22
collect['time_limit'] = time_limit

call_back_url = 'CallBackUrl'
collect['call_back_url'] = call_back_url

fileformat = AudioFormat.MP3
collect['fileformat'] = fileformat

response_type = 'json'
collect['response_type'] = response_type


result = call_client.create_record_call(collect)

```


#### <a name="create_play_audio"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_play_audio") create_play_audio

> Play Dtmf and send the Digit

```python
def create_play_audio(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| audioUrl |  ``` Required ```  | URL to sound that should be played. You also can add more than one audio file using semicolons e.g. http://example.com/audio1.mp3;http://example.com/audio2.wav |
| length |  ``` Optional ```  | Time limit in seconds for audio play back |
| direction |  ``` Optional ```  | The leg of the call audio will be played to |
| loop |  ``` Optional ```  | Repeat audio playback indefinitely |
| mix |  ``` Optional ```  | If false, all other audio will be muted |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

audio_url = 'AudioUrl'
collect['audio_url'] = audio_url

length = 22
collect['length'] = length

direction = Direction.IN
collect['direction'] = direction

loop = False
collect['loop'] = loop

mix = False
collect['mix'] = mix

response_type = 'json'
collect['response_type'] = response_type


result = call_client.create_play_audio(collect)

```


#### <a name="create_list_calls"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_list_calls") create_list_calls

> A list of calls associated with your Message360 account

```python
def create_list_calls(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| to |  ``` Optional ```  | Only list calls to this number |
| mfrom |  ``` Optional ```  | Only list calls from this number |
| dateCreated |  ``` Optional ```  | Only list calls starting within the specified date range |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

page = 22
collect['page'] = page

page_size = 22
collect['page_size'] = page_size

to = 'To'
collect['to'] = to

mfrom = 'From'
collect['mfrom'] = mfrom

date_created = 'DateCreated'
collect['date_created'] = date_created

response_type = 'json'
collect['response_type'] = response_type


result = call_client.create_list_calls(collect)

```


#### <a name="create_interrupted_call"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_interrupted_call") create_interrupted_call

> Interrupt the Call by Call Sid

```python
def create_interrupted_call(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | Call SId |
| url |  ``` Optional ```  | URL the in-progress call will be redirected to |
| method |  ``` Optional ```  | The method used to request the above Url parameter |
| status |  ``` Optional ```  | Status to set the in-progress call to |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

url = 'Url'
collect['url'] = url

method = HttpAction.GET
collect['method'] = method

status = InterruptedCallStatus.CANCELED
collect['status'] = status

response_type = 'json'
collect['response_type'] = response_type


result = call_client.create_interrupted_call(collect)

```


#### <a name="create_send_digit"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_send_digit") create_send_digit

> Play Dtmf and send the Digit

```python
def create_send_digit(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| playDtmf |  ``` Required ```  | DTMF digits to play to the call. 0-9, #, *, W, or w |
| playDtmfDirection |  ``` Optional ```  | The leg of the call DTMF digits should be sent to |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

play_dtmf_direction = Direction.IN
collect['play_dtmf_direction'] = play_dtmf_direction

response_type = 'json'
collect['response_type'] = response_type


result = call_client.create_send_digit(collect)

```


#### <a name="create_make_call"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_make_call") create_make_call

> You can experiment with initiating a call through Message360 and view the request response generated when doing so and get the response in json

```python
def create_make_call(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| fromCountryCode |  ``` Required ```  | from country code |
| mfrom |  ``` Required ```  | This number to display on Caller ID as calling |
| toCountryCode |  ``` Required ```  | To cuntry code number |
| to |  ``` Required ```  | To number |
| url |  ``` Required ```  | URL requested once the call connects |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once call connects. |
| statusCallBackUrl |  ``` Optional ```  | specifies the HTTP methodlinkclass used to request StatusCallbackUrl. |
| statusCallBackMethod |  ``` Optional ```  | Specifies the HTTP methodlinkclass used to request StatusCallbackUrl. |
| fallBackUrl |  ``` Optional ```  | URL requested if the initial Url parameter fails or encounters an error |
| fallBackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |
| heartBeatUrl |  ``` Optional ```  | URL that can be requested every 60 seconds during the call to notify of elapsed tim |
| heartBeatMethod |  ``` Optional ```  | Specifies the HTTP method used to request HeartbeatUrl. |
| timeout |  ``` Optional ```  | Time (in seconds) Message360 should wait while the call is ringing before canceling the call |
| playDtmf |  ``` Optional ```  | DTMF Digits to play to the call once it connects. 0-9, #, or * |
| hideCallerId |  ``` Optional ```  | Specifies if the caller id will be hidden |
| record |  ``` Optional ```  | Specifies if the call should be recorded |
| recordCallBackUrl |  ``` Optional ```  | Recording parameters will be sent here upon completion |
| recordCallBackMethod |  ``` Optional ```  | Method used to request the RecordCallback URL. |
| transcribe |  ``` Optional ```  | Specifies if the call recording should be transcribed |
| transcribeCallBackUrl |  ``` Optional ```  | Transcription parameters will be sent here upon completion |
| ifMachine |  ``` Optional ```  | How Message360 should handle the receiving numbers voicemail machine |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

from_country_code = 'FromCountryCode'
collect['from_country_code'] = from_country_code

mfrom = 'From'
collect['mfrom'] = mfrom

to_country_code = 'ToCountryCode'
collect['to_country_code'] = to_country_code

to = 'To'
collect['to'] = to

url = 'Url'
collect['url'] = url

method = HttpAction.GET
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

status_call_back_method = HttpAction.GET
collect['status_call_back_method'] = status_call_back_method

fall_back_url = 'FallBackUrl'
collect['fall_back_url'] = fall_back_url

fall_back_method = HttpAction.GET
collect['fall_back_method'] = fall_back_method

heart_beat_url = 'HeartBeatUrl'
collect['heart_beat_url'] = heart_beat_url

heart_beat_method = False
collect['heart_beat_method'] = heart_beat_method

timeout = 22
collect['timeout'] = timeout

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

hide_caller_id = False
collect['hide_caller_id'] = hide_caller_id

record = False
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = HttpAction.GET
collect['record_call_back_method'] = record_call_back_method

transcribe = False
collect['transcribe'] = transcribe

transcribe_call_back_url = 'TranscribeCallBackUrl'
collect['transcribe_call_back_url'] = transcribe_call_back_url

if_machine = IfMachine.CONTINUE
collect['if_machine'] = if_machine

response_type = 'json'
collect['response_type'] = response_type


result = call_client.create_make_call(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="sms_controller"></a>![Class: ](http://apidocs.io/img/class.png ".SMSController") SMSController

#### Get controller instance

An instance of the ``` SMSController ``` class can be accessed from the API Client.

```python
 sms_client = client.sms
```

#### <a name="create_view_sms"></a>![Method: ](http://apidocs.io/img/method.png ".SMSController.create_view_sms") create_view_sms

> View Particular SMS

```python
def create_view_sms(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messagesid |  ``` Required ```  | Message sid |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

messagesid = 'messagesid'
collect['messagesid'] = messagesid

response_type = 'json'
collect['response_type'] = response_type


result = sms_client.create_view_sms(collect)

```


#### <a name="create_list_inbound_sms"></a>![Method: ](http://apidocs.io/img/method.png ".SMSController.create_list_inbound_sms") create_list_inbound_sms

> List All Inbound SMS

```python
def create_list_inbound_sms(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pagesize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | From Number to Inbound SMS |
| to |  ``` Optional ```  | To Number to get Inbound SMS |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

page = 114
collect['page'] = page

pagesize = 'pagesize'
collect['pagesize'] = pagesize

mfrom = 'from'
collect['mfrom'] = mfrom

to = 'to'
collect['to'] = to

response_type = 'json'
collect['response_type'] = response_type


result = sms_client.create_list_inbound_sms(collect)

```


#### <a name="create_list_sms"></a>![Method: ](http://apidocs.io/img/method.png ".SMSController.create_list_sms") create_list_sms

> List All SMS

```python
def create_list_sms(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pagesize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | Messages sent from this number |
| to |  ``` Optional ```  | Messages sent to this number |
| datesent |  ``` Optional ```  | Only list SMS messages sent in the specified date range |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

page = 114
collect['page'] = page

pagesize = 114
collect['pagesize'] = pagesize

mfrom = 'from'
collect['mfrom'] = mfrom

to = 'to'
collect['to'] = to

datesent = 'datesent'
collect['datesent'] = datesent

response_type = 'json'
collect['response_type'] = response_type


result = sms_client.create_list_sms(collect)

```


#### <a name="create_send_sms"></a>![Method: ](http://apidocs.io/img/method.png ".SMSController.create_send_sms") create_send_sms

> Send an SMS from a message360 number

```python
def create_send_sms(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| fromcountrycode |  ``` Required ```  ``` DefaultValue ```  | From Country Code |
| mfrom |  ``` Required ```  | SMS enabled Message360 number to send this message from |
| tocountrycode |  ``` Required ```  ``` DefaultValue ```  | To country code |
| to |  ``` Required ```  | Number to send the SMS to |
| body |  ``` Required ```  | Text Message To Send |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once SMS sent. |
| messagestatuscallback |  ``` Optional ```  | URL that can be requested to receive notification when SMS has Sent. A set of default parameters will be sent here once the SMS is finished. |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

fromcountrycode = 1
collect['fromcountrycode'] = fromcountrycode

mfrom = 'from'
collect['mfrom'] = mfrom

tocountrycode = 1
collect['tocountrycode'] = tocountrycode

to = 'to'
collect['to'] = to

body = 'body'
collect['body'] = body

method = HttpAction.GET
collect['method'] = method

messagestatuscallback = 'messagestatuscallback'
collect['messagestatuscallback'] = messagestatuscallback

response_type = 'json'
collect['response_type'] = response_type


result = sms_client.create_send_sms(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="account_controller"></a>![Class: ](http://apidocs.io/img/class.png ".AccountController") AccountController

#### Get controller instance

An instance of the ``` AccountController ``` class can be accessed from the API Client.

```python
 account_client = client.account
```

#### <a name="create_view_account"></a>![Method: ](http://apidocs.io/img/method.png ".AccountController.create_view_account") create_view_account

> Display Account Description

```python
def create_view_account(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| date |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

date = 'date'
collect['date'] = date

response_type = 'json'
collect['response_type'] = response_type


result = account_client.create_view_account(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="web_rtc_controller"></a>![Class: ](http://apidocs.io/img/class.png ".WebRTCController") WebRTCController

#### Get controller instance

An instance of the ``` WebRTCController ``` class can be accessed from the API Client.

```python
 web_rtc_client = client.web_rtc
```

#### <a name="create_check_funds"></a>![Method: ](http://apidocs.io/img/method.png ".WebRTCController.create_check_funds") create_check_funds

> TODO: Add a method description

```python
def create_check_funds(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| accountSid |  ``` Required ```  | Your message360 Account SID |
| authToken |  ``` Required ```  | Your message360 Token |



#### Example Usage

```python
collect = {}

account_sid = 'account_sid'
collect['account_sid'] = account_sid

auth_token = 'auth_token'
collect['auth_token'] = auth_token


result = web_rtc_client.create_check_funds(collect)

```


#### <a name="create_authenticate_number"></a>![Method: ](http://apidocs.io/img/method.png ".WebRTCController.create_authenticate_number") create_authenticate_number

> Authenticate a message360 number for use

```python
def create_authenticate_number(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Phone number to authenticate for use |
| accountSid |  ``` Required ```  | Your message360 Account SID |
| authToken |  ``` Required ```  | Your message360 token |



#### Example Usage

```python
collect = {}

phone_number = 'phone_number'
collect['phone_number'] = phone_number

account_sid = 'account_sid'
collect['account_sid'] = account_sid

auth_token = 'auth_token'
collect['auth_token'] = auth_token


result = web_rtc_client.create_authenticate_number(collect)

```


#### <a name="create_token"></a>![Method: ](http://apidocs.io/img/method.png ".WebRTCController.create_token") create_token

> message360 webrtc

```python
def create_token(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| accountSid |  ``` Required ```  | Your message360 Account SID |
| authToken |  ``` Required ```  | Your message360 Token |



#### Example Usage

```python
collect = {}

account_sid = 'account_sid'
collect['account_sid'] = account_sid

auth_token = 'auth_token'
collect['auth_token'] = auth_token


result = web_rtc_client.create_token(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="sub_account_controller"></a>![Class: ](http://apidocs.io/img/class.png ".SubAccountController") SubAccountController

#### Get controller instance

An instance of the ``` SubAccountController ``` class can be accessed from the API Client.

```python
 sub_account_client = client.sub_account
```

#### <a name="create_sub_account"></a>![Method: ](http://apidocs.io/img/method.png ".SubAccountController.create_sub_account") create_sub_account

> Create Sub account

```python
def create_sub_account(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| firstname |  ``` Required ```  | TODO: Add a parameter description |
| lastname |  ``` Required ```  | TODO: Add a parameter description |
| email |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | ResponseType Format either json or xml |



#### Example Usage

```python
collect = {}

firstname = 'firstname'
collect['firstname'] = firstname

lastname = 'lastname'
collect['lastname'] = lastname

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = sub_account_client.create_sub_account(collect)

```


#### <a name="create_suspend_sub_account"></a>![Method: ](http://apidocs.io/img/method.png ".SubAccountController.create_suspend_sub_account") create_suspend_sub_account

> Suspend or unsuspend

```python
def create_suspend_sub_account(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subaccountsid |  ``` Required ```  | TODO: Add a parameter description |
| activate |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

subaccountsid = 'subaccountsid'
collect['subaccountsid'] = subaccountsid

activate = ActivateStatus.ACTIVATE
collect['activate'] = activate

response_type = 'ResponseType'
collect['response_type'] = response_type


result = sub_account_client.create_suspend_sub_account(collect)

```


#### <a name="create_delete_merge_sub_account"></a>![Method: ](http://apidocs.io/img/method.png ".SubAccountController.create_delete_merge_sub_account") create_delete_merge_sub_account

> Delete or Merge Sub account

```python
def create_delete_merge_sub_account(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subaccountsid |  ``` Required ```  | TODO: Add a parameter description |
| mergenumber |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format either json or xml |



#### Example Usage

```python
collect = {}

subaccountsid = 'subaccountsid'
collect['subaccountsid'] = subaccountsid

mergenumber = MergeNumberStatus.DELETE
collect['mergenumber'] = mergenumber

response_type = 'json'
collect['response_type'] = response_type


result = sub_account_client.create_delete_merge_sub_account(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="address_controller"></a>![Class: ](http://apidocs.io/img/class.png ".AddressController") AddressController

#### Get controller instance

An instance of the ``` AddressController ``` class can be accessed from the API Client.

```python
 address_client = client.address
```

#### <a name="create_address"></a>![Method: ](http://apidocs.io/img/method.png ".AddressController.create_address") create_address

> To add an address to your address book, you create a new address object. You can retrieve and delete individual addresses as well as get a list of addresses. Addresses are identified by a unique random ID.

```python
def create_address(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| name |  ``` Required ```  | Name of user |
| address |  ``` Required ```  | Address of user. |
| country |  ``` Required ```  | Must be a 2 letter country short-name code (ISO 3166) |
| state |  ``` Required ```  | Must be a 2 letter State eg. CA for US. For Some Countries it can be greater than 2 letters. |
| city |  ``` Required ```  | City Name. |
| zip |  ``` Required ```  | Zip code of city. |
| description |  ``` Optional ```  | Description of addresses. |
| email |  ``` Optional ```  | Email Id of user. |
| phone |  ``` Optional ```  | Phone number of user. |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response Type Either json or xml |



#### Example Usage

```python
collect = {}

name = 'name'
collect['name'] = name

address = 'address'
collect['address'] = address

country = 'country'
collect['country'] = country

state = 'state'
collect['state'] = state

city = 'city'
collect['city'] = city

zip = 'zip'
collect['zip'] = zip

description = 'description'
collect['description'] = description

email = 'email'
collect['email'] = email

phone = 'phone'
collect['phone'] = phone

response_type = 'json'
collect['response_type'] = response_type


result = address_client.create_address(collect)

```


#### <a name="create_delete_address"></a>![Method: ](http://apidocs.io/img/method.png ".AddressController.create_delete_address") create_delete_address

> To delete Address to your address book

```python
def create_delete_address(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| addressid |  ``` Required ```  | The identifier of the address to be deleted. |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type either json or xml |



#### Example Usage

```python
collect = {}

addressid = 'addressid'
collect['addressid'] = addressid

response_type = 'json'
collect['response_type'] = response_type


result = address_client.create_delete_address(collect)

```


#### <a name="create_verify_address"></a>![Method: ](http://apidocs.io/img/method.png ".AddressController.create_verify_address") create_verify_address

> Validates an address given.

```python
def create_verify_address(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| addressid |  ``` Required ```  | The identifier of the address to be verified. |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type either JSON or xml |



#### Example Usage

```python
collect = {}

addressid = 'addressid'
collect['addressid'] = addressid

response_type = 'json'
collect['response_type'] = response_type


result = address_client.create_verify_address(collect)

```


#### <a name="create_list_address"></a>![Method: ](http://apidocs.io/img/method.png ".AddressController.create_list_address") create_list_address

> List All Address 

```python
def create_list_address(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  ``` DefaultValue ```  | Return requested # of items starting the value, default=0, must be an integer |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | How many results to return, default=10, max 100, must be an integer |
| addressId |  ``` Optional ```  | addresses Sid |
| dateCreated |  ``` Optional ```  | date created address. |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

address_id = 'addressId'
collect['address_id'] = address_id

date_created = 'dateCreated'
collect['date_created'] = date_created

response_type = 'json'
collect['response_type'] = response_type


result = address_client.create_list_address(collect)

```


#### <a name="create_view_address"></a>![Method: ](http://apidocs.io/img/method.png ".AddressController.create_view_address") create_view_address

> View Address Specific address Book by providing the address id

```python
def create_view_address(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| addressId |  ``` Required ```  | The identifier of the address to be retrieved. |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

address_id = 'addressId'
collect['address_id'] = address_id

response_type = 'json'
collect['response_type'] = response_type


result = address_client.create_view_address(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="phone_number_controller"></a>![Class: ](http://apidocs.io/img/class.png ".PhoneNumberController") PhoneNumberController

#### Get controller instance

An instance of the ``` PhoneNumberController ``` class can be accessed from the API Client.

```python
 phone_number_client = client.phone_number
```

#### <a name="update_phone_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.update_phone_number") update_phone_number

> Update Phone Number Details

```python
def update_phone_number(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | TODO: Add a parameter description |
| friendlyName |  ``` Optional ```  | TODO: Add a parameter description |
| voiceUrl |  ``` Optional ```  | URL requested once the call connects |
| voiceMethod |  ``` Optional ```  | TODO: Add a parameter description |
| voiceFallbackUrl |  ``` Optional ```  | URL requested if the voice URL is not available |
| voiceFallbackMethod |  ``` Optional ```  | TODO: Add a parameter description |
| hangupCallback |  ``` Optional ```  | TODO: Add a parameter description |
| hangupCallbackMethod |  ``` Optional ```  | TODO: Add a parameter description |
| heartbeatUrl |  ``` Optional ```  | URL requested once the call connects |
| heartbeatMethod |  ``` Optional ```  | URL that can be requested every 60 seconds during the call to notify of elapsed time |
| smsUrl |  ``` Optional ```  | URL requested when an SMS is received |
| smsMethod |  ``` Optional ```  | TODO: Add a parameter description |
| smsFallbackUrl |  ``` Optional ```  | URL requested once the call connects |
| smsFallbackMethod |  ``` Optional ```  | URL requested if the sms URL is not available |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

voice_url = 'VoiceUrl'
collect['voice_url'] = voice_url

voice_method = HttpAction.GET
collect['voice_method'] = voice_method

voice_fallback_url = 'VoiceFallbackUrl'
collect['voice_fallback_url'] = voice_fallback_url

voice_fallback_method = HttpAction.GET
collect['voice_fallback_method'] = voice_fallback_method

hangup_callback = 'HangupCallback'
collect['hangup_callback'] = hangup_callback

hangup_callback_method = HttpAction.GET
collect['hangup_callback_method'] = hangup_callback_method

heartbeat_url = 'HeartbeatUrl'
collect['heartbeat_url'] = heartbeat_url

heartbeat_method = HttpAction.GET
collect['heartbeat_method'] = heartbeat_method

sms_url = 'SmsUrl'
collect['sms_url'] = sms_url

sms_method = HttpAction.GET
collect['sms_method'] = sms_method

sms_fallback_url = 'SmsFallbackUrl'
collect['sms_fallback_url'] = sms_fallback_url

sms_fallback_method = HttpAction.GET
collect['sms_fallback_method'] = sms_fallback_method

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_client.update_phone_number(collect)

```


#### <a name="create_buy_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_buy_number") create_buy_number

> Buy Phone Number 

```python
def create_buy_number(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Phone number to be purchase |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_client.create_buy_number(collect)

```


#### <a name="create_release_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_release_number") create_release_number

> Release number from account

```python
def create_release_number(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Phone number to be relase |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_client.create_release_number(collect)

```


#### <a name="create_view_number_details"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_view_number_details") create_view_number_details

> Get Phone Number Details

```python
def create_view_number_details(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Get Phone number Detail |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_client.create_view_number_details(collect)

```


#### <a name="create_list_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_list_number") create_list_number

> List Account's Phone number details

```python
def create_list_number(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| numberType |  ``` Optional ```  | TODO: Add a parameter description |
| friendlyName |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

page = 72
collect['page'] = page

page_size = 72
collect['page_size'] = page_size

number_type = NumberType.ALL
collect['number_type'] = number_type

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_client.create_list_number(collect)

```


#### <a name="create_available_phone_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_available_phone_number") create_available_phone_number

> Available Phone Number

```python
def create_available_phone_number(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| numberType |  ``` Required ```  | Number type either SMS,Voice or all |
| areaCode |  ``` Required ```  | Phone Number Area Code |
| pageSize |  ``` Optional ```  | Page Size |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

number_type = NumberType.ALL
collect['number_type'] = number_type

area_code = 'AreaCode'
collect['area_code'] = area_code

page_size = 72
collect['page_size'] = page_size

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_client.create_available_phone_number(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="recording_controller"></a>![Class: ](http://apidocs.io/img/class.png ".RecordingController") RecordingController

#### Get controller instance

An instance of the ``` RecordingController ``` class can be accessed from the API Client.

```python
 recording_client = client.recording
```

#### <a name="create_list_recording"></a>![Method: ](http://apidocs.io/img/method.png ".RecordingController.create_list_recording") create_list_recording

> List out Recordings

```python
def create_list_recording(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| dateCreated |  ``` Optional ```  | TODO: Add a parameter description |
| callSid |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

page = 72
collect['page'] = page

page_size = 72
collect['page_size'] = page_size

date_created = 'DateCreated'
collect['date_created'] = date_created

call_sid = 'CallSid'
collect['call_sid'] = call_sid

response_type = 'json'
collect['response_type'] = response_type


result = recording_client.create_list_recording(collect)

```


#### <a name="create_delete_recording"></a>![Method: ](http://apidocs.io/img/method.png ".RecordingController.create_delete_recording") create_delete_recording

> Delete Recording Record

```python
def create_delete_recording(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | Unique Recording Sid to be delete |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

recording_sid = 'RecordingSid'
collect['recording_sid'] = recording_sid

response_type = 'json'
collect['response_type'] = response_type


result = recording_client.create_delete_recording(collect)

```


#### <a name="create_view_recording"></a>![Method: ](http://apidocs.io/img/method.png ".RecordingController.create_view_recording") create_view_recording

> View a specific Recording

```python
def create_view_recording(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | Search Recording sid |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

recording_sid = 'RecordingSid'
collect['recording_sid'] = recording_sid

response_type = 'json'
collect['response_type'] = response_type


result = recording_client.create_view_recording(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="transcription_controller"></a>![Class: ](http://apidocs.io/img/class.png ".TranscriptionController") TranscriptionController

#### Get controller instance

An instance of the ``` TranscriptionController ``` class can be accessed from the API Client.

```python
 transcription_client = client.transcription
```

#### <a name="create_audio_url_transcription"></a>![Method: ](http://apidocs.io/img/method.png ".TranscriptionController.create_audio_url_transcription") create_audio_url_transcription

> Audio URL Transcriptions

```python
def create_audio_url_transcription(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| audioUrl |  ``` Required ```  | Audio url |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

audio_url = 'AudioUrl'
collect['audio_url'] = audio_url

response_type = 'json'
collect['response_type'] = response_type


result = transcription_client.create_audio_url_transcription(collect)

```


#### <a name="create_recording_transcription"></a>![Method: ](http://apidocs.io/img/method.png ".TranscriptionController.create_recording_transcription") create_recording_transcription

> Recording Transcriptions

```python
def create_recording_transcription(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | Unique Recording sid |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

recording_sid = 'RecordingSid'
collect['recording_sid'] = recording_sid

response_type = 'json'
collect['response_type'] = response_type


result = transcription_client.create_recording_transcription(collect)

```


#### <a name="create_view_transcription"></a>![Method: ](http://apidocs.io/img/method.png ".TranscriptionController.create_view_transcription") create_view_transcription

> View Specific Transcriptions

```python
def create_view_transcription(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| transcriptionSid |  ``` Required ```  | Unique Transcription ID |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

transcription_sid = 'TranscriptionSid'
collect['transcription_sid'] = transcription_sid

response_type = 'json'
collect['response_type'] = response_type


result = transcription_client.create_view_transcription(collect)

```


#### <a name="create_list_transcription"></a>![Method: ](http://apidocs.io/img/method.png ".TranscriptionController.create_list_transcription") create_list_transcription

> Get All transcriptions

```python
def create_list_transcription(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | TODO: Add a parameter description |
| pageSize |  ``` Optional ```  | TODO: Add a parameter description |
| status |  ``` Optional ```  | TODO: Add a parameter description |
| dateTranscribed |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

page = 72
collect['page'] = page

page_size = 72
collect['page_size'] = page_size

status = Status.INPROGRESS
collect['status'] = status

date_transcribed = 'DateTranscribed'
collect['date_transcribed'] = date_transcribed

response_type = 'json'
collect['response_type'] = response_type


result = transcription_client.create_list_transcription(collect)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="usage_controller"></a>![Class: ](http://apidocs.io/img/class.png ".UsageController") UsageController

#### Get controller instance

An instance of the ``` UsageController ``` class can be accessed from the API Client.

```python
 usage_client = client.usage
```

#### <a name="create_list_usage"></a>![Method: ](http://apidocs.io/img/method.png ".UsageController.create_list_usage") create_list_usage

> Get all usage 

```python
def create_list_usage(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| productCode |  ``` Required ```  ``` DefaultValue ```  | Product Code |
| startDate |  ``` Required ```  ``` DefaultValue ```  | Start Usage Date |
| endDate |  ``` Required ```  ``` DefaultValue ```  | End Usage Date |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

product_code = ProductCode.ALL
collect['product_code'] = product_code

start_date = '2016-09-06'
collect['start_date'] = start_date

end_date = '2016-09-06'
collect['end_date'] = end_date

response_type = 'json'
collect['response_type'] = response_type


result = usage_client.create_list_usage(collect)

```


[Back to List of Controllers](#list_of_controllers)



