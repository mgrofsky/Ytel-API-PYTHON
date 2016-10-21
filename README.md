#

## How to Build


You must have Python greater than 2.7 installed in your system to build and run your SDK files. 
The generated code has dependencies over external libraries like nose, jsonpickle, etc. These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, we use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

The paths of Python and PIP must be properly set in the environment variables. Open command prompt and type ```pip --version```.
This should display the current version of the PIP Dependency Manager installed if the installation was successful.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](http://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Message360-Python)


## How to Use

The following section explains how to use the Message360 library in a new project.

### 1. Open Project in an IDE

Open an IDE for Python like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

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
from message360lib.message360_client import *
```

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Message360-Python&libraryName=message360lib.message360_client&projectName=message360)

After this you can add code to initialize the client library and acquire the instance of a Controller class. Sample code to initialize the client library and using controller methods is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](http://apidocs.io/illustration/python?step=runProject&workspaceFolder=Message360-Python&libraryName=message360lib.message360_client&projectName=message360)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'nosetests'

## Initialization

### Authentication and Initialization
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
* [TranscriptionController](#transcription_controller)
* [PhoneNumberController](#phone_number_controller)
* [UsageController](#usage_controller)
* [EmailController](#email_controller)
* [SMSController](#sms_controller)
* [AccountController](#account_controller)
* [RecordingController](#recording_controller)
* [CallController](#call_controller)
* [CarrierController](#carrier_controller)

### <a name="conference_controller"></a>![Class: ](http://apidocs.io/img/class.png ".ConferenceController") ConferenceController

#### Get controller instance

An instance of the ``` ConferenceController ``` class can be accessed from the API Client.

```python
 conference_client = client.conference
```

#### <a name="create_view_participant"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.create_view_participant") create_view_participant

> View Participant

```python
def create_view_participant(self,
                                conference_sid,
                                participant_sid,
                                response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | unique conference sid |
| participantSid |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
conference_sid = 'ConferenceSid'
participant_sid = 'ParticipantSid'
response_type = 'json'

result = conference_client.create_view_participant(conference_sid, participant_sid, response_type)

```


#### <a name="create_list_participant"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.create_list_participant") create_list_participant

> List Participant

```python
def create_list_participant(self,
                                conference_sid,
                                page = None,
                                pagesize = None,
                                muted = None,
                                deaf = None,
                                response_type = 'json')
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
conference_sid = 'ConferenceSid'
page = 12
pagesize = 12
muted = False
deaf = False
response_type = 'json'

result = conference_client.create_list_participant(conference_sid, page, pagesize, muted, deaf, response_type)

```


#### <a name="add_participant"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.add_participant") add_participant

> Add Participant in conference 

```python
def add_participant(self,
                        conferencesid,
                        participantnumber,
                        tocountrycode,
                        muted = None,
                        deaf = None,
                        response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferencesid |  ``` Required ```  | Unique Conference Sid |
| participantnumber |  ``` Required ```  | Particiant Number |
| tocountrycode |  ``` Required ```  | TODO: Add a parameter description |
| muted |  ``` Optional ```  | TODO: Add a parameter description |
| deaf |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
conferencesid = 'conferencesid'
participantnumber = 'participantnumber'
tocountrycode = 176
muted = True
deaf = True
response_type = 'json'

result = conference_client.add_participant(conferencesid, participantnumber, tocountrycode, muted, deaf, response_type)

```


#### <a name="create_view_conference"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.create_view_conference") create_view_conference

> View Conference

```python
def create_view_conference(self,
                               conferencesid,
                               response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferencesid |  ``` Required ```  | The unique identifier of each conference resource |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
conferencesid = 'conferencesid'
response_type = 'json'

result = conference_client.create_view_conference(conferencesid, response_type)

```


#### <a name="create_list_conference"></a>![Method: ](http://apidocs.io/img/method.png ".ConferenceController.create_list_conference") create_list_conference

> List Conference

```python
def create_list_conference(self,
                               page = None,
                               page_size = None,
                               friendly_name = None,
                               status = None,
                               date_created = None,
                               date_updated = None,
                               response_type = 'json')
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
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
page = 176
page_size = 176
friendly_name = 'FriendlyName'
status = InterruptedCallStatus.CANCELED
date_created = 'DateCreated'
date_updated = 'DateUpdated'
response_type = 'json'

result = conference_client.create_list_conference(page, page_size, friendly_name, status, date_created, date_updated, response_type)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="transcription_controller"></a>![Class: ](http://apidocs.io/img/class.png ".TranscriptionController") TranscriptionController

#### Get controller instance

An instance of the ``` TranscriptionController ``` class can be accessed from the API Client.

```python
 transcription_client = client.transcription
```

#### <a name="create_list_transcription"></a>![Method: ](http://apidocs.io/img/method.png ".TranscriptionController.create_list_transcription") create_list_transcription

> Get All transcriptions

```python
def create_list_transcription(self,
                                  page = None,
                                  page_size = None,
                                  status = None,
                                  date_transcribed = None,
                                  response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | TODO: Add a parameter description |
| pageSize |  ``` Optional ```  | TODO: Add a parameter description |
| status |  ``` Optional ```  | TODO: Add a parameter description |
| dateTranscribed |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
page = 176
page_size = 176
status = Status.INPROGRESS
date_transcribed = 'DateTranscribed'
response_type = 'json'

result = transcription_client.create_list_transcription(page, page_size, status, date_transcribed, response_type)

```


#### <a name="create_recording_transcription"></a>![Method: ](http://apidocs.io/img/method.png ".TranscriptionController.create_recording_transcription") create_recording_transcription

> Recording Transcriptions

```python
def create_recording_transcription(self,
                                       recording_sid,
                                       response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | Unique Recording sid |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
recording_sid = 'RecordingSid'
response_type = 'json'

result = transcription_client.create_recording_transcription(recording_sid, response_type)

```


#### <a name="create_view_transcription"></a>![Method: ](http://apidocs.io/img/method.png ".TranscriptionController.create_view_transcription") create_view_transcription

> View Specific Transcriptions

```python
def create_view_transcription(self,
                                  transcription_sid,
                                  response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| transcriptionSid |  ``` Required ```  | Unique Transcription ID |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
transcription_sid = 'TranscriptionSid'
response_type = 'json'

result = transcription_client.create_view_transcription(transcription_sid, response_type)

```


#### <a name="create_audio_url_transcription"></a>![Method: ](http://apidocs.io/img/method.png ".TranscriptionController.create_audio_url_transcription") create_audio_url_transcription

> Audio URL Transcriptions

```python
def create_audio_url_transcription(self,
                                       audio_url,
                                       response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| audioUrl |  ``` Required ```  | Audio url |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
audio_url = 'AudioUrl'
response_type = 'json'

result = transcription_client.create_audio_url_transcription(audio_url, response_type)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="phone_number_controller"></a>![Class: ](http://apidocs.io/img/class.png ".PhoneNumberController") PhoneNumberController

#### Get controller instance

An instance of the ``` PhoneNumberController ``` class can be accessed from the API Client.

```python
 phone_number_client = client.phone_number
```

#### <a name="create_available_phone_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_available_phone_number") create_available_phone_number

> Available Phone Number

```python
def create_available_phone_number(self,
                                      number_type,
                                      area_code,
                                      page_size = None,
                                      response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| numberType |  ``` Required ```  | Number type either SMS,Voice or all |
| areaCode |  ``` Required ```  | Phone Number Area Code |
| pageSize |  ``` Optional ```  | Page Size |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
number_type = 'NumberType'
area_code = 'AreaCode'
page_size = 176
response_type = 'json'

result = phone_number_client.create_available_phone_number(number_type, area_code, page_size, response_type)

```


#### <a name="create_list_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_list_number") create_list_number

> List Account's Phone number details

```python
def create_list_number(self,
                           page = None,
                           page_size = None,
                           number_type = None,
                           friendly_name = None,
                           response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| numberType |  ``` Optional ```  | TODO: Add a parameter description |
| friendlyName |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
page = 176
page_size = 176
number_type = 'NumberType'
friendly_name = 'FriendlyName'
response_type = 'json'

result = phone_number_client.create_list_number(page, page_size, number_type, friendly_name, response_type)

```


#### <a name="create_release_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_release_number") create_release_number

> Release number from account

```python
def create_release_number(self,
                              phone_number,
                              response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Phone number to be relase |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
phone_number = 'PhoneNumber'
response_type = 'json'

result = phone_number_client.create_release_number(phone_number, response_type)

```


#### <a name="create_buy_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_buy_number") create_buy_number

> Buy Phone Number 

```python
def create_buy_number(self,
                          phone_number,
                          response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Phone number to be purchase |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
phone_number = 'PhoneNumber'
response_type = 'json'

result = phone_number_client.create_buy_number(phone_number, response_type)

```


#### <a name="create_view_number_details"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.create_view_number_details") create_view_number_details

> Get Phone Number Details

```python
def create_view_number_details(self,
                                   phone_number,
                                   response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Get Phone number Detail |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
phone_number = 'PhoneNumber'
response_type = 'json'

result = phone_number_client.create_view_number_details(phone_number, response_type)

```


#### <a name="update_phone_number"></a>![Method: ](http://apidocs.io/img/method.png ".PhoneNumberController.update_phone_number") update_phone_number

> Update Phone Number Details

```python
def update_phone_number(self,
                            phone_number,
                            friendly_name = None,
                            voice_url = None,
                            voice_method = None,
                            voice_fallback_url = None,
                            voice_fallback_method = None,
                            hangup_callback = None,
                            hangup_callback_method = None,
                            heartbeat_url = None,
                            heartbeat_method = None,
                            sms_url = None,
                            sms_method = None,
                            sms_fallback_url = None,
                            sms_fallback_method = None,
                            response_type = 'json')
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
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
phone_number = 'PhoneNumber'
friendly_name = 'FriendlyName'
voice_url = 'VoiceUrl'
voice_method = HttpMethod.GET
voice_fallback_url = 'VoiceFallbackUrl'
voice_fallback_method = HttpMethod.GET
hangup_callback = 'HangupCallback'
hangup_callback_method = HttpMethod.GET
heartbeat_url = 'HeartbeatUrl'
heartbeat_method = HttpMethod.GET
sms_url = 'SmsUrl'
sms_method = HttpMethod.GET
sms_fallback_url = 'SmsFallbackUrl'
sms_fallback_method = HttpMethod.GET
response_type = 'json'

result = phone_number_client.update_phone_number(phone_number, friendly_name, voice_url, voice_method, voice_fallback_url, voice_fallback_method, hangup_callback, hangup_callback_method, heartbeat_url, heartbeat_method, sms_url, sms_method, sms_fallback_url, sms_fallback_method, response_type)

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
                          product_code,
                          start_date,
                          end_date,
                          response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| productCode |  ``` Required ```  ``` DefaultValue ```  | Product Code |
| startDate |  ``` Required ```  ``` DefaultValue ```  | Start Usage Date |
| endDate |  ``` Required ```  ``` DefaultValue ```  | End Usage Date |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
product_code = '0'
start_date = '2016-09-06'
end_date = '2016-09-06'
response_type = 'json'

result = usage_client.create_list_usage(product_code, start_date, end_date, response_type)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="email_controller"></a>![Class: ](http://apidocs.io/img/class.png ".EmailController") EmailController

#### Get controller instance

An instance of the ``` EmailController ``` class can be accessed from the API Client.

```python
 email_client = client.email
```

#### <a name="create_send_email"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_send_email") create_send_email

> Send out an email

```python
def create_send_email(self,
                          to,
                          mfrom,
                          mtype,
                          subject,
                          message,
                          cc = None,
                          bcc = None,
                          attachment = None,
                          response_type = 'json')
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
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
to = 'to'
mfrom = 'from'
mtype = SendEmailAs.HTML
subject = 'subject'
message = 'message'
cc = 'cc'
bcc = 'bcc'
attachment = 'attachment'
response_type = 'json'

result = email_client.create_send_email(to, mfrom, mtype, subject, message, cc, bcc, attachment, response_type)

```


#### <a name="create_delete_unsubscribes"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_delete_unsubscribes") create_delete_unsubscribes

> Delete emails from the unsubscribe list

```python
def create_delete_unsubscribes(self,
                                   email,
                                   response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email to remove from the unsubscribe list |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
email = 'email'
response_type = 'json'

result = email_client.create_delete_unsubscribes(email, response_type)

```


#### <a name="create_list_unsubscribes"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_unsubscribes") create_list_unsubscribes

> List all unsubscribed email addresses

```python
def create_list_unsubscribes(self,
                                 response_type = 'json',
                                 offset = None,
                                 limit = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |
| offset |  ``` Optional ```  | Starting record of the list |
| limit |  ``` Optional ```  | Maximum number of records to be returned |



#### Example Usage

```python
response_type = 'json'
offset = 'offset'
limit = 'limit'

result = email_client.create_list_unsubscribes(response_type, offset, limit)

```


#### <a name="add_unsubscribes"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.add_unsubscribes") add_unsubscribes

> Add an email to the unsubscribe list

```python
def add_unsubscribes(self,
                         email,
                         response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email to add to the unsubscribe list |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
email = 'email'
response_type = 'json'

result = email_client.add_unsubscribes(email, response_type)

```


#### <a name="create_delete_spam"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_delete_spam") create_delete_spam

> Deletes a email address marked as spam from the spam list

```python
def create_delete_spam(self,
                           email,
                           response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | Email address |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
email = 'email'
response_type = 'json'

result = email_client.create_delete_spam(email, response_type)

```


#### <a name="create_delete_block"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_delete_block") create_delete_block

> Deletes a blocked email

```python
def create_delete_block(self,
                            email,
                            response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | Email address to remove from block list |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
email = 'email'
response_type = 'json'

result = email_client.create_delete_block(email, response_type)

```


#### <a name="create_list_invalid"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_invalid") create_list_invalid

> List out all invalid email addresses

```python
def create_list_invalid(self,
                            response_type = 'json',
                            offet = None,
                            limit = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |
| offet |  ``` Optional ```  | Starting record for listing out emails |
| limit |  ``` Optional ```  | Maximum number of records to return |



#### Example Usage

```python
response_type = 'json'
offet = 'offet'
limit = 'limit'

result = email_client.create_list_invalid(response_type, offet, limit)

```


#### <a name="create_delete_bounces"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_delete_bounces") create_delete_bounces

> Delete an email address from the bounced address list

```python
def create_delete_bounces(self,
                              email,
                              response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email address to remove from the bounce list |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
email = 'email'
response_type = 'json'

result = email_client.create_delete_bounces(email, response_type)

```


#### <a name="create_list_bounces"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_bounces") create_list_bounces

> List out all email addresses that have bounced

```python
def create_list_bounces(self,
                            response_type = 'json',
                            offset = None,
                            limit = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |
| offset |  ``` Optional ```  | The record to start the list at |
| limit |  ``` Optional ```  | The maximum number of records to return |



#### Example Usage

```python
response_type = 'json'
offset = 'offset'
limit = 'limit'

result = email_client.create_list_bounces(response_type, offset, limit)

```


#### <a name="create_list_spam"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_spam") create_list_spam

> List out all email addresses marked as spam

```python
def create_list_spam(self,
                         response_type,
                         offset = None,
                         limit = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response format, xml or json |
| offset |  ``` Optional ```  | The record number to start the list at |
| limit |  ``` Optional ```  | Maximum number of records to return |



#### Example Usage

```python
response_type = 'json'
offset = 'offset'
limit = 'limit'

result = email_client.create_list_spam(response_type, offset, limit)

```


#### <a name="create_list_blocks"></a>![Method: ](http://apidocs.io/img/method.png ".EmailController.create_list_blocks") create_list_blocks

> Outputs email addresses on your blocklist

```python
def create_list_blocks(self,
                           offset = None,
                           limit = None,
                           response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| offset |  ``` Optional ```  | Where to start in the output list |
| limit |  ``` Optional ```  | Maximum number of records to return |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
offset = 'offset'
limit = 'limit'
response_type = 'json'

result = email_client.create_list_blocks(offset, limit, response_type)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="sms_controller"></a>![Class: ](http://apidocs.io/img/class.png ".SMSController") SMSController

#### Get controller instance

An instance of the ``` SMSController ``` class can be accessed from the API Client.

```python
 sms_client = client.sms
```

#### <a name="create_send_sms"></a>![Method: ](http://apidocs.io/img/method.png ".SMSController.create_send_sms") create_send_sms

> Send an SMS from a message360 number

```python
def create_send_sms(self,
                        fromcountrycode,
                        mfrom,
                        tocountrycode,
                        to,
                        body,
                        method = None,
                        messagestatuscallback = None,
                        response_type = 'json')
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
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
fromcountrycode = 1
mfrom = 'from'
tocountrycode = 1
to = 'to'
body = 'body'
method = HttpMethod.GET
messagestatuscallback = 'messagestatuscallback'
response_type = 'json'

result = sms_client.create_send_sms(fromcountrycode, mfrom, tocountrycode, to, body, method, messagestatuscallback, response_type)

```


#### <a name="create_view_sms"></a>![Method: ](http://apidocs.io/img/method.png ".SMSController.create_view_sms") create_view_sms

> View Particular SMS

```python
def create_view_sms(self,
                        messagesid,
                        response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messagesid |  ``` Required ```  | Message sid |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
messagesid = 'messagesid'
response_type = 'json'

result = sms_client.create_view_sms(messagesid, response_type)

```


#### <a name="create_list_sms"></a>![Method: ](http://apidocs.io/img/method.png ".SMSController.create_list_sms") create_list_sms

> List All SMS

```python
def create_list_sms(self,
                        page = None,
                        pagesize = None,
                        mfrom = None,
                        to = None,
                        datesent = None,
                        response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pagesize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | Messages sent from this number |
| to |  ``` Optional ```  | Messages sent to this number |
| datesent |  ``` Optional ```  | Only list SMS messages sent in the specified date range |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
page = 218
pagesize = 218
mfrom = 'from'
to = 'to'
datesent = 'datesent'
response_type = 'json'

result = sms_client.create_list_sms(page, pagesize, mfrom, to, datesent, response_type)

```


#### <a name="create_list_inbound_sms"></a>![Method: ](http://apidocs.io/img/method.png ".SMSController.create_list_inbound_sms") create_list_inbound_sms

> List All Inbound SMS

```python
def create_list_inbound_sms(self,
                                page = None,
                                pagesize = None,
                                mfrom = None,
                                to = None,
                                response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pagesize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | From Number to Inbound SMS |
| to |  ``` Optional ```  | To Number to get Inbound SMS |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
page = 218
pagesize = 'pagesize'
mfrom = 'from'
to = 'to'
response_type = 'json'

result = sms_client.create_list_inbound_sms(page, pagesize, mfrom, to, response_type)

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
                            date,
                            response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| date |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
date = 'date'
response_type = 'json'

result = account_client.create_view_account(date, response_type)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="recording_controller"></a>![Class: ](http://apidocs.io/img/class.png ".RecordingController") RecordingController

#### Get controller instance

An instance of the ``` RecordingController ``` class can be accessed from the API Client.

```python
 recording_client = client.recording
```

#### <a name="create_delete_recording"></a>![Method: ](http://apidocs.io/img/method.png ".RecordingController.create_delete_recording") create_delete_recording

> Delete Recording Record

```python
def create_delete_recording(self,
                                recording_sid,
                                response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | Unique Recording Sid to be delete |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
recording_sid = 'RecordingSid'
response_type = 'json'

result = recording_client.create_delete_recording(recording_sid, response_type)

```


#### <a name="create_view_recording"></a>![Method: ](http://apidocs.io/img/method.png ".RecordingController.create_view_recording") create_view_recording

> View a specific Recording

```python
def create_view_recording(self,
                              recording_sid,
                              response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | Search Recording sid |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
recording_sid = 'RecordingSid'
response_type = 'json'

result = recording_client.create_view_recording(recording_sid, response_type)

```


#### <a name="create_list_recording"></a>![Method: ](http://apidocs.io/img/method.png ".RecordingController.create_list_recording") create_list_recording

> List out Recordings

```python
def create_list_recording(self,
                              page = None,
                              page_size = None,
                              date_created = None,
                              call_sid = None,
                              response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| dateCreated |  ``` Optional ```  | TODO: Add a parameter description |
| callSid |  ``` Optional ```  | TODO: Add a parameter description |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
page = 218
page_size = 218
date_created = 'DateCreated'
call_sid = 'CallSid'
response_type = 'json'

result = recording_client.create_list_recording(page, page_size, date_created, call_sid, response_type)

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
                         callsid,
                         response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callsid |  ``` Required ```  | Call Sid id for particular Call |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
callsid = 'callsid'
response_type = 'json'

result = call_client.create_view_call(callsid, response_type)

```


#### <a name="create_make_call"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_make_call") create_make_call

> You can experiment with initiating a call through Message360 and view the request response generated when doing so and get the response in json

```python
def create_make_call(self,
                         from_country_code,
                         mfrom,
                         to_country_code,
                         to,
                         url,
                         method = None,
                         status_call_back_url = None,
                         status_call_back_method = None,
                         fall_back_url = None,
                         fall_back_method = None,
                         heart_beat_url = None,
                         heart_beat_method = None,
                         timeout = None,
                         play_dtmf = None,
                         hide_caller_id = None,
                         record = None,
                         record_call_back_url = None,
                         record_call_back_method = None,
                         transcribe = None,
                         transcribe_call_back_url = None,
                         if_machine = None,
                         response_type = 'json')
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
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
from_country_code = 'FromCountryCode'
mfrom = 'From'
to_country_code = 'ToCountryCode'
to = 'To'
url = 'Url'
method = HttpMethod.GET
status_call_back_url = 'StatusCallBackUrl'
status_call_back_method = HttpMethod.GET
fall_back_url = 'FallBackUrl'
fall_back_method = HttpMethod.GET
heart_beat_url = 'HeartBeatUrl'
heart_beat_method = True
timeout = 218
play_dtmf = 'PlayDtmf'
hide_caller_id = True
record = True
record_call_back_url = 'RecordCallBackUrl'
record_call_back_method = HttpMethod.GET
transcribe = True
transcribe_call_back_url = 'TranscribeCallBackUrl'
if_machine = IfMachine.CONTINUE
response_type = 'json'

result = call_client.create_make_call(from_country_code, mfrom, to_country_code, to, url, method, status_call_back_url, status_call_back_method, fall_back_url, fall_back_method, heart_beat_url, heart_beat_method, timeout, play_dtmf, hide_caller_id, record, record_call_back_url, record_call_back_method, transcribe, transcribe_call_back_url, if_machine, response_type)

```


#### <a name="create_play_audio"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_play_audio") create_play_audio

> Play Dtmf and send the Digit

```python
def create_play_audio(self,
                          length,
                          direction,
                          loop,
                          mix,
                          call_sid = None,
                          audio_url = None,
                          response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| length |  ``` Required ```  | Time limit in seconds for audio play back |
| direction |  ``` Required ```  | The leg of the call audio will be played to |
| loop |  ``` Required ```  | Repeat audio playback indefinitely |
| mix |  ``` Required ```  | If false, all other audio will be muted |
| callSid |  ``` Optional ```  | The unique identifier of each call resource |
| audioUrl |  ``` Optional ```  | URL to sound that should be played. You also can add more than one audio file using semicolons e.g. http://example.com/audio1.mp3;http://example.com/audio2.wav |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
length = 218
direction = Direction.IN
loop = True
mix = True
call_sid = 'CallSid'
audio_url = 'AudioUrl'
response_type = 'json'

result = call_client.create_play_audio(length, direction, loop, mix, call_sid, audio_url, response_type)

```


#### <a name="create_record_call"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_record_call") create_record_call

> Record a Call

```python
def create_record_call(self,
                           call_sid,
                           record,
                           direction = None,
                           time_limit = None,
                           call_back_url = None,
                           fileformat = None,
                           response_type = 'json')
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
call_sid = 'CallSid'
record = True
direction = Direction.IN
time_limit = 218
call_back_url = 'CallBackUrl'
fileformat = AudioFormat.MP3
response_type = 'json'

result = call_client.create_record_call(call_sid, record, direction, time_limit, call_back_url, fileformat, response_type)

```


#### <a name="create_voice_effect"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_voice_effect") create_voice_effect

> Voice Effect

```python
def create_voice_effect(self,
                            call_sid,
                            audio_direction = None,
                            pitch_semi_tones = None,
                            pitch_octaves = None,
                            pitch = None,
                            rate = None,
                            tempo = None,
                            response_type = 'json')
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
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
call_sid = 'CallSid'
audio_direction = AudioDirection.IN
pitch_semi_tones = 218.210384905436
pitch_octaves = 218.210384905436
pitch = 218.210384905436
rate = 218.210384905436
tempo = 218.210384905436
response_type = 'json'

result = call_client.create_voice_effect(call_sid, audio_direction, pitch_semi_tones, pitch_octaves, pitch, rate, tempo, response_type)

```


#### <a name="create_send_digit"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_send_digit") create_send_digit

> Play Dtmf and send the Digit

```python
def create_send_digit(self,
                          call_sid,
                          play_dtmf,
                          play_dtmf_direction = None,
                          response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| playDtmf |  ``` Required ```  | DTMF digits to play to the call. 0-9, #, *, W, or w |
| playDtmfDirection |  ``` Optional ```  | The leg of the call DTMF digits should be sent to |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
call_sid = 'CallSid'
play_dtmf = 'PlayDtmf'
play_dtmf_direction = Direction.IN
response_type = 'json'

result = call_client.create_send_digit(call_sid, play_dtmf, play_dtmf_direction, response_type)

```


#### <a name="create_interrupted_call"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_interrupted_call") create_interrupted_call

> Interrupt the Call by Call Sid

```python
def create_interrupted_call(self,
                                call_sid,
                                url = None,
                                method = None,
                                status = None,
                                response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | Call SId |
| url |  ``` Optional ```  | URL the in-progress call will be redirected to |
| method |  ``` Optional ```  | The method used to request the above Url parameter |
| status |  ``` Optional ```  | Status to set the in-progress call to |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
call_sid = 'CallSid'
url = 'Url'
method = HttpMethod.GET
status = InterruptedCallStatus.CANCELED
response_type = 'json'

result = call_client.create_interrupted_call(call_sid, url, method, status, response_type)

```


#### <a name="create_list_calls"></a>![Method: ](http://apidocs.io/img/method.png ".CallController.create_list_calls") create_list_calls

> A list of calls associated with your Message360 account

```python
def create_list_calls(self,
                          page = None,
                          page_size = None,
                          to = None,
                          mfrom = None,
                          date_created = None,
                          response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  | Number of individual resources listed in the response per page |
| to |  ``` Optional ```  | Only list calls to this number |
| mfrom |  ``` Optional ```  | Only list calls from this number |
| dateCreated |  ``` Optional ```  | Only list calls starting within the specified date range |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
page = 'Page'
page_size = 'PageSize'
to = 'To'
mfrom = 'From'
date_created = 'DateCreated'
response_type = 'json'

call_client.create_list_calls(page, page_size, to, mfrom, date_created, response_type)

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
                              phonenumber,
                              response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phonenumber |  ``` Required ```  | The number to lookup |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
phonenumber = 'phonenumber'
response_type = 'json'

result = carrier_client.create_carrier_lookup(phonenumber, response_type)

```


#### <a name="create_carrier_lookup_list"></a>![Method: ](http://apidocs.io/img/method.png ".CarrierController.create_carrier_lookup_list") create_carrier_lookup_list

> Get the All Purchase Number's Carrier lookup

```python
def create_carrier_lookup_list(self,
                                   page = None,
                                   pagesize = None,
                                   response_type = 'json')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Optional ```  | Page Number |
| pagesize |  ``` Optional ```  | Page Size |
| responseType |  ``` Optional ```  ``` DefaultValue ```  | Response format, xml or json |



#### Example Usage

```python
page = 'page'
pagesize = 'pagesize'
response_type = 'json'

result = carrier_client.create_carrier_lookup_list(page, pagesize, response_type)

```


[Back to List of Controllers](#list_of_controllers)



