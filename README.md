# Getting started

message360 API version 3

## How to Build


You must have Python 2 >=2.7.9 or Python 3 >=3.4 installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Message360-Python)


## How to Use

The following section explains how to use the Message360 SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Message360-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Message360-Python&projectName=message_360)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Message360-Python&projectName=message_360)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Message360-Python&projectName=message_360)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from message_360.message_360_client import Message360Client
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Message360-Python&libraryName=message_360.message_360_client&projectName=message_360)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Message360-Python&libraryName=message_360.message_360_client&projectName=message_360)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'pip install -r test-requirements.txt'
  3. Invoke 'nosetests'

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| basic_auth_user_name | The username to use with basic authentication |
| basic_auth_password | The password to use with basic authentication |



API client can be initialized as following.

```python
# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

client = Message360Client(basic_auth_user_name, basic_auth_password)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [SharedShortCodeController](#shared_short_code_controller)
* [ConferenceController](#conference_controller)
* [TranscriptionController](#transcription_controller)
* [PhoneNumberController](#phone_number_controller)
* [UsageController](#usage_controller)
* [WebRTCController](#web_rtc_controller)
* [RecordingController](#recording_controller)
* [EmailController](#email_controller)
* [SMSController](#sms_controller)
* [CallController](#call_controller)
* [CarrierController](#carrier_controller)
* [AddressController](#address_controller)
* [SubAccountController](#sub_account_controller)
* [AccountController](#account_controller)
* [ShortCodeController](#short_code_controller)

## <a name="shared_short_code_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SharedShortCodeController") SharedShortCodeController

### Get controller instance

An instance of the ``` SharedShortCodeController ``` class can be accessed from the API Client.

```python
 shared_short_code_client = client.shared_short_code
```

### <a name="view_template"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.view_template") view_template

> View a Shared ShortCode Template

```python
def view_template(self,
                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| templateid |  ``` Required ```  | The unique identifier for a template object |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

templateid = uuid.uuid4()
collect['templateid'] = templateid

response_type = 'json'
collect['response_type'] = response_type


result = shared_short_code_client.view_template(collect)

```


### <a name="view_shared_shortcodes"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.view_shared_shortcodes") view_shared_shortcodes

> View a ShortCode Message

```python
def view_shared_shortcodes(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messagesid |  ``` Required ```  | Message sid |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

messagesid = 'messagesid'
collect['messagesid'] = messagesid

response_type = 'json'
collect['response_type'] = response_type


result = shared_short_code_client.view_shared_shortcodes(collect)

```


### <a name="list_outbound_shared_shortcodes"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.list_outbound_shared_shortcodes") list_outbound_shared_shortcodes

> List ShortCode Messages

```python
def list_outbound_shared_shortcodes(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | Messages sent from this number |
| to |  ``` Optional ```  | Messages sent to this number |
| datesent |  ``` Optional ```  | Only list SMS messages sent in the specified date range |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

mfrom = 'from'
collect['mfrom'] = mfrom

to = 'to'
collect['to'] = to

datesent = 'datesent'
collect['datesent'] = datesent


result = shared_short_code_client.list_outbound_shared_shortcodes(collect)

```


### <a name="list_inbound_shared_shortcodes"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.list_inbound_shared_shortcodes") list_inbound_shared_shortcodes

> List All Inbound ShortCode

```python
def list_inbound_shared_shortcodes(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | From Number to Inbound ShortCode |
| shortcode |  ``` Optional ```  | Only list messages sent to this Short Code |
| dateReceived |  ``` Optional ```  | Only list messages sent with the specified date |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

mfrom = 'from'
collect['mfrom'] = mfrom

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

date_received = 'DateReceived'
collect['date_received'] = date_received


result = shared_short_code_client.list_inbound_shared_shortcodes(collect)

```


### <a name="send_shared_shortcode"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.send_shared_shortcode") send_shared_shortcode

> Send an SMS from a message360 ShortCode

```python
def send_shared_shortcode(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | The Short Code number that is the sender of this message |
| to |  ``` Required ```  | A valid 10-digit number that should receive the message |
| templateid |  ``` Required ```  | The unique identifier for the template used for the message |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| data |  ``` Required ```  | format of your data, example: {companyname}:test,{otpcode}:1234 |
| method |  ``` Optional ```  ``` DefaultValue ```  | Specifies the HTTP method used to request the required URL once the Short Code message is sent. |
| messageStatusCallback |  ``` Optional ```  | URL that can be requested to receive notification when Short Code message was sent. |



#### Example Usage

```python
collect = {}

shortcode = 'shortcode'
collect['shortcode'] = shortcode

to = 'to'
collect['to'] = to

templateid = uuid.uuid4()
collect['templateid'] = templateid

response_type = 'json'
collect['response_type'] = response_type

data = 'data'
collect['data'] = data

method = HttpActionEnum.GET
collect['method'] = method

message_status_callback = 'MessageStatusCallback'
collect['message_status_callback'] = message_status_callback


result = shared_short_code_client.send_shared_shortcode(collect)

```


### <a name="list_templates"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.list_templates") list_templates

> List Shortcode Templates by Type

```python
def list_templates(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| mtype |  ``` Optional ```  ``` DefaultValue ```  | The type (category) of template Valid values: marketing, authorization |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| shortcode |  ``` Optional ```  | Only list templates of type |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

mtype = 'authorization'
collect['mtype'] = mtype

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

shortcode = 'Shortcode'
collect['shortcode'] = shortcode


result = shared_short_code_client.list_templates(collect)

```


### <a name="view_keyword"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.view_keyword") view_keyword

> View a set of properties for a single keyword.

```python
def view_keyword(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| keywordid |  ``` Required ```  | The unique identifier of each keyword |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

keywordid = 'Keywordid'
collect['keywordid'] = keywordid

response_type = 'json'
collect['response_type'] = response_type


result = shared_short_code_client.view_keyword(collect)

```


### <a name="list_keyword"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.list_keyword") list_keyword

> Retrieve a list of keywords associated with your message360 account.

```python
def list_keyword(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| keyword |  ``` Optional ```  | Only list keywords of keyword |
| shortcode |  ``` Optional ```  | Only list keywords of shortcode |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

keyword = 'Keyword'
collect['keyword'] = keyword

shortcode = 71
collect['shortcode'] = shortcode


result = shared_short_code_client.list_keyword(collect)

```


### <a name="view_assignement"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.view_assignement") view_assignement

> The response returned here contains all resource properties associated with the given Shortcode.

```python
def view_assignement(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | List of valid Shortcode to your message360 account |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

response_type = 'json'
collect['response_type'] = response_type


result = shared_short_code_client.view_assignement(collect)

```


### <a name="list_assignment"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.list_assignment") list_assignment

> Retrieve a list of shortcode assignment associated with your message360 account.

```python
def list_assignment(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| shortcode |  ``` Optional ```  | Only list keywords of shortcode |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

shortcode = 'Shortcode'
collect['shortcode'] = shortcode


result = shared_short_code_client.list_assignment(collect)

```


### <a name="update_assignment"></a>![Method: ](https://apidocs.io/img/method.png ".SharedShortCodeController.update_assignment") update_assignment

> TODO: Add a method description

```python
def update_assignment(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | List of valid shortcode to your message360 account |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| friendlyName |  ``` Optional ```  | User generated name of the shortcode |
| callbackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
| callbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required StatusCallBackUrl once call connects. |
| fallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML or at initial request of the required Url provided with the POST. |
| fallbackUrlMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |



#### Example Usage

```python
collect = {}

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

response_type = 'json'
collect['response_type'] = response_type

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

callback_url = 'CallbackUrl'
collect['callback_url'] = callback_url

callback_method = HttpActionEnum.GET
collect['callback_method'] = callback_method

fallback_url = 'FallbackUrl'
collect['fallback_url'] = fallback_url

fallback_url_method = HttpActionEnum.GET
collect['fallback_url_method'] = fallback_url_method


result = shared_short_code_client.update_assignment(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="conference_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ConferenceController") ConferenceController

### Get controller instance

An instance of the ``` ConferenceController ``` class can be accessed from the API Client.

```python
 conference_client = client.conference
```

### <a name="deaf_mute_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.deaf_mute_participant") deaf_mute_participant

> Deaf Mute Participant

```python
def deaf_mute_participant(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | ID of the active conference |
| participantSid |  ``` Required ```  | ID of an active participant |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |
| muted |  ``` Optional ```  | Mute a participant |
| deaf |  ``` Optional ```  | Make it so a participant cant hear |



#### Example Usage

```python
collect = {}

conference_sid = 'conferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid

response_type = 'json'
collect['response_type'] = response_type

muted = False
collect['muted'] = muted

deaf = False
collect['deaf'] = deaf


result = conference_client.deaf_mute_participant(collect)

```


### <a name="view_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.view_participant") view_participant

> View Participant

```python
def view_participant(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | unique conference sid |
| participantSid |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.view_participant(collect)

```


### <a name="add_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.add_participant") add_participant

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
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| muted |  ``` Optional ```  | add muted |
| deaf |  ``` Optional ```  | add without volume |



#### Example Usage

```python
collect = {}

conferencesid = 'conferencesid'
collect['conferencesid'] = conferencesid

participantnumber = 'participantnumber'
collect['participantnumber'] = participantnumber

response_type = 'json'
collect['response_type'] = response_type

muted = False
collect['muted'] = muted

deaf = False
collect['deaf'] = deaf


result = conference_client.add_participant(collect)

```


### <a name="view_conference"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.view_conference") view_conference

> View Conference

```python
def view_conference(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferencesid |  ``` Required ```  | The unique identifier of each conference resource |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

conferencesid = 'conferencesid'
collect['conferencesid'] = conferencesid

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.view_conference(collect)

```


### <a name="create_conference"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.create_conference") create_conference

> Here you can experiment with initiating a conference call through message360 and view the request response generated when doing so.

```python
def create_conference(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | This number to display on Caller ID as calling |
| to |  ``` Required ```  | To number |
| url |  ``` Required ```  | URL requested once the call connects |
| method |  ``` Required ```  ``` DefaultValue ```  | Specifies the HTTP method used to request the required URL once call connects. |
| recordCallbackUrl |  ``` Required ```  | Recording parameters will be sent here upon completion. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| statusCallBackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the conference is finished. |
| statusCallBackMethod |  ``` Optional ```  | Specifies the HTTP methodlinkclass used to request StatusCallbackUrl. |
| fallBackUrl |  ``` Optional ```  | URL requested if the initial Url parameter fails or encounters an error |
| fallBackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |
| record |  ``` Optional ```  | Specifies if the conference should be recorded. |
| recordCallbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once conference connects. |
| schdeuleTime |  ``` Optional ```  | Schedule conference in future. Schedule time must be greater than current time |
| timeout |  ``` Optional ```  | The number of seconds the call stays on the line while waiting for an answer. The max time limit is 999 and the default limit is 60 seconds but lower times can be set. |



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

url = 'Url'
collect['url'] = url

method = HttpActionEnum.POST
collect['method'] = method

record_callback_url = 'RecordCallbackUrl'
collect['record_callback_url'] = record_callback_url

response_type = 'json'
collect['response_type'] = response_type

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

status_call_back_method = HttpActionEnum.GET
collect['status_call_back_method'] = status_call_back_method

fall_back_url = 'FallBackUrl'
collect['fall_back_url'] = fall_back_url

fall_back_method = HttpActionEnum.GET
collect['fall_back_method'] = fall_back_method

record = False
collect['record'] = record

record_callback_method = HttpActionEnum.GET
collect['record_callback_method'] = record_callback_method

schdeule_time = 'SchdeuleTime'
collect['schdeule_time'] = schdeule_time

timeout = 71
collect['timeout'] = timeout


result = conference_client.create_conference(collect)

```


### <a name="hangup_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.hangup_participant") hangup_participant

> Remove a participant from a conference.

```python
def hangup_participant(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier for a conference object. |
| participantSid |  ``` Required ```  | The unique identifier for a participant object. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.hangup_participant(collect)

```


### <a name="play_conference_audio"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.play_conference_audio") play_conference_audio

> Play an audio file during a conference.

```python
def play_conference_audio(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier for a conference object. |
| participantSid |  ``` Required ```  | The unique identifier for a participant object. |
| audioUrl |  ``` Required ```  | The URL for the audio file that is to be played during the conference. Multiple audio files can be chained by using a semicolon. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

participant_sid = 'ParticipantSid'
collect['participant_sid'] = participant_sid

audio_url = AudioFormatEnum.MP3
collect['audio_url'] = audio_url

response_type = 'json'
collect['response_type'] = response_type


result = conference_client.play_conference_audio(collect)

```


### <a name="list_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.list_participant") list_participant

> List Participant

```python
def list_participant(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | unique conference sid |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response format, xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | page number |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Amount of records to return per page |
| muted |  ``` Optional ```  | Participants that are muted |
| deaf |  ``` Optional ```  | Participants cant hear |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

muted = False
collect['muted'] = muted

deaf = False
collect['deaf'] = deaf


result = conference_client.list_participant(collect)

```


### <a name="list_conference"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.list_conference") list_conference

> List Conference

```python
def list_conference(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| friendlyName |  ``` Optional ```  | Only return conferences with the specified FriendlyName |
| dateCreated |  ``` Optional ```  | Conference created date |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

date_created = 'DateCreated'
collect['date_created'] = date_created


result = conference_client.list_conference(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="transcription_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TranscriptionController") TranscriptionController

### Get controller instance

An instance of the ``` TranscriptionController ``` class can be accessed from the API Client.

```python
 transcription_client = client.transcription
```

### <a name="list_transcription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.list_transcription") list_transcription

> Get All transcriptions

```python
def list_transcription(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | page number |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Amount of data per page |
| status |  ``` Optional ```  | Transcription status |
| dateTranscribed |  ``` Optional ```  | Transcription date |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

status = StatusEnum.INPROGRESS
collect['status'] = status

date_transcribed = 'DateTranscribed'
collect['date_transcribed'] = date_transcribed


result = transcription_client.list_transcription(collect)

```


### <a name="view_transcription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.view_transcription") view_transcription

> View Specific Transcriptions

```python
def view_transcription(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| transcriptionSid |  ``` Required ```  | Unique Transcription ID |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

transcription_sid = 'TranscriptionSid'
collect['transcription_sid'] = transcription_sid

response_type = 'json'
collect['response_type'] = response_type


result = transcription_client.view_transcription(collect)

```


### <a name="recording_transcription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.recording_transcription") recording_transcription

> Recording Transcriptions

```python
def recording_transcription(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | Unique Recording sid |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

recording_sid = 'RecordingSid'
collect['recording_sid'] = recording_sid

response_type = 'json'
collect['response_type'] = response_type


result = transcription_client.recording_transcription(collect)

```


### <a name="audio_url_transcription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.audio_url_transcription") audio_url_transcription

> Audio URL Transcriptions

```python
def audio_url_transcription(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| audioUrl |  ``` Required ```  | Audio url |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

audio_url = 'AudioUrl'
collect['audio_url'] = audio_url

response_type = 'json'
collect['response_type'] = response_type


result = transcription_client.audio_url_transcription(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="phone_number_controller"></a>![Class: ](https://apidocs.io/img/class.png ".PhoneNumberController") PhoneNumberController

### Get controller instance

An instance of the ``` PhoneNumberController ``` class can be accessed from the API Client.

```python
 phone_number_client = client.phone_number
```

### <a name="available_phone_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.available_phone_number") available_phone_number

> Available Phone Number

```python
def available_phone_number(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| numberType |  ``` Required ```  | Number type either SMS,Voice or all |
| areaCode |  ``` Required ```  | Phone Number Area Code |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Page Size |



#### Example Usage

```python
collect = {}

number_type = NumberTypeEnum.ALL
collect['number_type'] = number_type

area_code = 'AreaCode'
collect['area_code'] = area_code

response_type = 'json'
collect['response_type'] = response_type

page_size = 10
collect['page_size'] = page_size


result = phone_number_client.available_phone_number(collect)

```


### <a name="list_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.list_number") list_number

> List Account's Phone number details

```python
def list_number(self,
                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| numberType |  ``` Optional ```  | SMS or Voice |
| friendlyName |  ``` Optional ```  | Friendly name of the number |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

number_type = NumberTypeEnum.ALL
collect['number_type'] = number_type

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name


result = phone_number_client.list_number(collect)

```


### <a name="view_number_details"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.view_number_details") view_number_details

> Get Phone Number Details

```python
def view_number_details(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Get Phone number Detail |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_client.view_number_details(collect)

```


### <a name="release_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.release_number") release_number

> Release number from account

```python
def release_number(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Phone number to be relase |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_client.release_number(collect)

```


### <a name="buy_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.buy_number") buy_number

> Buy Phone Number 

```python
def buy_number(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | Phone number to be purchase |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_client.buy_number(collect)

```


### <a name="update_phone_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.update_phone_number") update_phone_number

> Update Phone Number Details

```python
def update_phone_number(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | The phone number to update |
| voiceUrl |  ``` Required ```  | URL requested once the call connects |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| friendlyName |  ``` Optional ```  | Phone number friendly name description |
| voiceMethod |  ``` Optional ```  | Post or Get |
| voiceFallbackUrl |  ``` Optional ```  | URL requested if the voice URL is not available |
| voiceFallbackMethod |  ``` Optional ```  | Post or Get |
| hangupCallback |  ``` Optional ```  | callback url after a hangup occurs |
| hangupCallbackMethod |  ``` Optional ```  | Post or Get |
| heartbeatUrl |  ``` Optional ```  | URL requested once the call connects |
| heartbeatMethod |  ``` Optional ```  | URL that can be requested every 60 seconds during the call to notify of elapsed time |
| smsUrl |  ``` Optional ```  | URL requested when an SMS is received |
| smsMethod |  ``` Optional ```  | Post or Get |
| smsFallbackUrl |  ``` Optional ```  | URL requested once the call connects |
| smsFallbackMethod |  ``` Optional ```  | URL requested if the sms URL is not available |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

voice_url = 'VoiceUrl'
collect['voice_url'] = voice_url

response_type = 'json'
collect['response_type'] = response_type

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

voice_method = HttpActionEnum.GET
collect['voice_method'] = voice_method

voice_fallback_url = 'VoiceFallbackUrl'
collect['voice_fallback_url'] = voice_fallback_url

voice_fallback_method = HttpActionEnum.GET
collect['voice_fallback_method'] = voice_fallback_method

hangup_callback = 'HangupCallback'
collect['hangup_callback'] = hangup_callback

hangup_callback_method = HttpActionEnum.GET
collect['hangup_callback_method'] = hangup_callback_method

heartbeat_url = 'HeartbeatUrl'
collect['heartbeat_url'] = heartbeat_url

heartbeat_method = HttpActionEnum.GET
collect['heartbeat_method'] = heartbeat_method

sms_url = 'SmsUrl'
collect['sms_url'] = sms_url

sms_method = HttpActionEnum.GET
collect['sms_method'] = sms_method

sms_fallback_url = 'SmsFallbackUrl'
collect['sms_fallback_url'] = sms_fallback_url

sms_fallback_method = HttpActionEnum.GET
collect['sms_fallback_method'] = sms_fallback_method


result = phone_number_client.update_phone_number(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="usage_controller"></a>![Class: ](https://apidocs.io/img/class.png ".UsageController") UsageController

### Get controller instance

An instance of the ``` UsageController ``` class can be accessed from the API Client.

```python
 usage_client = client.usage
```

### <a name="list_usage"></a>![Method: ](https://apidocs.io/img/method.png ".UsageController.list_usage") list_usage

> Get all usage 

```python
def list_usage(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| productCode |  ``` Optional ```  ``` DefaultValue ```  | Product Code |
| startDate |  ``` Optional ```  ``` DefaultValue ```  | Start Usage Date |
| endDate |  ``` Optional ```  ``` DefaultValue ```  | End Usage Date |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

product_code = ProductCodeEnum.ALL
collect['product_code'] = product_code

start_date = '2016-09-06'
collect['start_date'] = start_date

end_date = '2016-09-06'
collect['end_date'] = end_date


result = usage_client.list_usage(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="web_rtc_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WebRTCController") WebRTCController

### Get controller instance

An instance of the ``` WebRTCController ``` class can be accessed from the API Client.

```python
 web_rtc_client = client.web_rtc
```

### <a name="check_funds"></a>![Method: ](https://apidocs.io/img/method.png ".WebRTCController.check_funds") check_funds

> TODO: Add a method description

```python
def check_funds(self,
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


result = web_rtc_client.check_funds(collect)

```


### <a name="create_token"></a>![Method: ](https://apidocs.io/img/method.png ".WebRTCController.create_token") create_token

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
| username |  ``` Required ```  | WebRTC username authentication |
| password |  ``` Required ```  | WebRTC password authentication |



#### Example Usage

```python
collect = {}

account_sid = 'account_sid'
collect['account_sid'] = account_sid

auth_token = 'auth_token'
collect['auth_token'] = auth_token

username = 'username'
collect['username'] = username

password = 'password'
collect['password'] = password


result = web_rtc_client.create_token(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="recording_controller"></a>![Class: ](https://apidocs.io/img/class.png ".RecordingController") RecordingController

### Get controller instance

An instance of the ``` RecordingController ``` class can be accessed from the API Client.

```python
 recording_client = client.recording
```

### <a name="view_recording"></a>![Method: ](https://apidocs.io/img/method.png ".RecordingController.view_recording") view_recording

> View a specific Recording

```python
def view_recording(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | Search Recording sid |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

recording_sid = 'RecordingSid'
collect['recording_sid'] = recording_sid

response_type = 'json'
collect['response_type'] = response_type


result = recording_client.view_recording(collect)

```


### <a name="delete_recording"></a>![Method: ](https://apidocs.io/img/method.png ".RecordingController.delete_recording") delete_recording

> Delete Recording Record

```python
def delete_recording(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | Unique Recording Sid to be delete |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

recording_sid = 'RecordingSid'
collect['recording_sid'] = recording_sid

response_type = 'json'
collect['response_type'] = response_type


result = recording_client.delete_recording(collect)

```


### <a name="list_recording"></a>![Method: ](https://apidocs.io/img/method.png ".RecordingController.list_recording") list_recording

> List out Recordings

```python
def list_recording(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| dateCreated |  ``` Optional ```  | Recording date |
| callSid |  ``` Optional ```  | Call ID |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

date_created = 'DateCreated'
collect['date_created'] = date_created

call_sid = 'CallSid'
collect['call_sid'] = call_sid


result = recording_client.list_recording(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="email_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EmailController") EmailController

### Get controller instance

An instance of the ``` EmailController ``` class can be accessed from the API Client.

```python
 email_client = client.email
```

### <a name="delete_spam"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_spam") delete_spam

> Deletes a email address marked as spam from the spam list

```python
def delete_spam(self,
                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| email |  ``` Required ```  | Email address |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

email = 'email'
collect['email'] = email


result = email_client.delete_spam(collect)

```


### <a name="delete_block"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_block") delete_block

> Deletes a blocked email

```python
def delete_block(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | Email address to remove from block list |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.delete_block(collect)

```


### <a name="add_unsubscribes"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.add_unsubscribes") add_unsubscribes

> Add an email to the unsubscribe list

```python
def add_unsubscribes(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email to add to the unsubscribe list |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.add_unsubscribes(collect)

```


### <a name="send_email"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.send_email") send_email

> Send out an email

```python
def send_email(self,
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
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| cc |  ``` Optional ```  | CC Email address |
| bcc |  ``` Optional ```  | BCC Email address |
| attachment |  ``` Optional ```  | File to be attached.File must be less than 7MB. |



#### Example Usage

```python
collect = {}

to = 'to'
collect['to'] = to

mfrom = 'from'
collect['mfrom'] = mfrom

mtype = SendEmailAsEnum.HTML
collect['mtype'] = mtype

subject = 'subject'
collect['subject'] = subject

message = 'message'
collect['message'] = message

response_type = 'json'
collect['response_type'] = response_type

cc = 'cc'
collect['cc'] = cc

bcc = 'bcc'
collect['bcc'] = bcc

attachment = 'attachment'
collect['attachment'] = attachment


result = email_client.send_email(collect)

```


### <a name="delete_unsubscribes"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_unsubscribes") delete_unsubscribes

> Delete emails from the unsubscribe list

```python
def delete_unsubscribes(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email to remove from the unsubscribe list |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.delete_unsubscribes(collect)

```


### <a name="list_unsubscribes"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_unsubscribes") list_unsubscribes

> List all unsubscribed email addresses

```python
def list_unsubscribes(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
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


result = email_client.list_unsubscribes(collect)

```


### <a name="list_invalid"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_invalid") list_invalid

> List out all invalid email addresses

```python
def list_invalid(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
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


result = email_client.list_invalid(collect)

```


### <a name="delete_bounces"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_bounces") delete_bounces

> Delete an email address from the bounced address list

```python
def delete_bounces(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| email |  ``` Required ```  | The email address to remove from the bounce list |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

email = 'email'
collect['email'] = email


result = email_client.delete_bounces(collect)

```


### <a name="list_bounces"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_bounces") list_bounces

> List out all email addresses that have bounced

```python
def list_bounces(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
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


result = email_client.list_bounces(collect)

```


### <a name="list_spam"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_spam") list_spam

> List out all email addresses marked as spam

```python
def list_spam(self,
                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
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


result = email_client.list_spam(collect)

```


### <a name="list_blocks"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_blocks") list_blocks

> Outputs email addresses on your blocklist

```python
def list_blocks(self,
                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| offset |  ``` Optional ```  | Where to start in the output list |
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


result = email_client.list_blocks(collect)

```


### <a name="delete_invalid"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_invalid") delete_invalid

> This endpoint allows you to delete entries in the Invalid Emails list.

```python
def delete_invalid(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | Email that was marked invalid |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Json or xml |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_client.delete_invalid(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sms_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SMSController") SMSController

### Get controller instance

An instance of the ``` SMSController ``` class can be accessed from the API Client.

```python
 sms_client = client.sms
```

### <a name="send_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.send_sms") send_sms

> Send an SMS from a message360 number

```python
def send_sms(self,
                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | SMS enabled Message360 number to send this message from |
| to |  ``` Required ```  | Number to send the SMS to |
| body |  ``` Required ```  | Text Message To Send |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once SMS sent. |
| messagestatuscallback |  ``` Optional ```  | URL that can be requested to receive notification when SMS has Sent. A set of default parameters will be sent here once the SMS is finished. |
| smartsms |  ``` Optional ```  ``` DefaultValue ```  | Check's 'to' number can receive sms or not using Carrier API, if wireless = true then text sms is sent, else wireless = false then call is recieved to end user with audible message. |



#### Example Usage

```python
collect = {}

mfrom = 'from'
collect['mfrom'] = mfrom

to = 'to'
collect['to'] = to

body = 'body'
collect['body'] = body

response_type = 'json'
collect['response_type'] = response_type

method = HttpActionEnum.GET
collect['method'] = method

messagestatuscallback = 'messagestatuscallback'
collect['messagestatuscallback'] = messagestatuscallback

smartsms = False
collect['smartsms'] = smartsms


result = sms_client.send_sms(collect)

```


### <a name="view_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.view_sms") view_sms

> View a Particular SMS

```python
def view_sms(self,
                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messagesid |  ``` Required ```  | Message sid |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

messagesid = 'messagesid'
collect['messagesid'] = messagesid

response_type = 'json'
collect['response_type'] = response_type


result = sms_client.view_sms(collect)

```


### <a name="list_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.list_sms") list_sms

> List All SMS

```python
def list_sms(self,
                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | Messages sent from this number |
| to |  ``` Optional ```  | Messages sent to this number |
| datesent |  ``` Optional ```  | Only list SMS messages sent in the specified date range |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

mfrom = 'from'
collect['mfrom'] = mfrom

to = 'to'
collect['to'] = to

datesent = 'datesent'
collect['datesent'] = datesent


result = sms_client.list_sms(collect)

```


### <a name="list_inbound_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.list_inbound_sms") list_inbound_sms

> List All Inbound SMS

```python
def list_inbound_sms(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | From Number to Inbound SMS |
| to |  ``` Optional ```  | To Number to get Inbound SMS |
| dateSent |  ``` Optional ```  | Filter sms message objects by this date. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

mfrom = 'from'
collect['mfrom'] = mfrom

to = 'to'
collect['to'] = to

date_sent = 'DateSent'
collect['date_sent'] = date_sent


result = sms_client.list_inbound_sms(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="call_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CallController") CallController

### Get controller instance

An instance of the ``` CallController ``` class can be accessed from the API Client.

```python
 call_client = client.call
```

### <a name="make_call"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.make_call") make_call

> You can experiment with initiating a call through Message360 and view the request response generated when doing so and get the response in json

```python
def make_call(self,
                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | This number to display on Caller ID as calling |
| to |  ``` Required ```  | To number |
| url |  ``` Required ```  | URL requested once the call connects |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
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
| ifMachineUrl |  ``` Optional ```  | URL requested when IfMachine=continue |
| ifMachineMethod |  ``` Optional ```  | Method used to request the IfMachineUrl. |
| feedback |  ``` Optional ```  | Specify if survey should be enable or not |
| surveyId |  ``` Optional ```  | The unique identifier for the survey. |



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

url = 'Url'
collect['url'] = url

response_type = 'json'
collect['response_type'] = response_type

method = HttpActionEnum.GET
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

status_call_back_method = HttpActionEnum.GET
collect['status_call_back_method'] = status_call_back_method

fall_back_url = 'FallBackUrl'
collect['fall_back_url'] = fall_back_url

fall_back_method = HttpActionEnum.GET
collect['fall_back_method'] = fall_back_method

heart_beat_url = 'HeartBeatUrl'
collect['heart_beat_url'] = heart_beat_url

heart_beat_method = HttpActionEnum.GET
collect['heart_beat_method'] = heart_beat_method

timeout = 121
collect['timeout'] = timeout

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

hide_caller_id = False
collect['hide_caller_id'] = hide_caller_id

record = False
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = HttpActionEnum.GET
collect['record_call_back_method'] = record_call_back_method

transcribe = False
collect['transcribe'] = transcribe

transcribe_call_back_url = 'TranscribeCallBackUrl'
collect['transcribe_call_back_url'] = transcribe_call_back_url

if_machine = IfMachineEnum.CONTINUE
collect['if_machine'] = if_machine

if_machine_url = 'IfMachineUrl'
collect['if_machine_url'] = if_machine_url

if_machine_method = HttpActionEnum.GET
collect['if_machine_method'] = if_machine_method

feedback = False
collect['feedback'] = feedback

survey_id = 'SurveyId'
collect['survey_id'] = survey_id


result = call_client.make_call(collect)

```


### <a name="play_audio"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.play_audio") play_audio

> Play Dtmf and send the Digit

```python
def play_audio(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| audioUrl |  ``` Required ```  | URL to sound that should be played. You also can add more than one audio file using semicolons e.g. http://example.com/audio1.mp3;http://example.com/audio2.wav |
| sayText |  ``` Required ```  | Valid alphanumeric string that should be played to the In-progress call. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| length |  ``` Optional ```  | Time limit in seconds for audio play back |
| direction |  ``` Optional ```  | The leg of the call audio will be played to |
| mix |  ``` Optional ```  | If false, all other audio will be muted |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

audio_url = 'AudioUrl'
collect['audio_url'] = audio_url

say_text = 'SayText'
collect['say_text'] = say_text

response_type = 'json'
collect['response_type'] = response_type

length = 121
collect['length'] = length

direction = DirectionEnum.IN
collect['direction'] = direction

mix = False
collect['mix'] = mix


result = call_client.play_audio(collect)

```


### <a name="record_call"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.record_call") record_call

> Record a Call

```python
def record_call(self,
                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| record |  ``` Required ```  | Set true to initiate recording or false to terminate recording |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response format, xml or json |
| direction |  ``` Optional ```  | The leg of the call to record |
| timeLimit |  ``` Optional ```  | Time in seconds the recording duration should not exceed |
| callBackUrl |  ``` Optional ```  | URL consulted after the recording completes |
| fileformat |  ``` Optional ```  | Format of the recording file. Can be .mp3 or .wav |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

record = False
collect['record'] = record

response_type = 'json'
collect['response_type'] = response_type

direction = DirectionEnum.IN
collect['direction'] = direction

time_limit = 121
collect['time_limit'] = time_limit

call_back_url = 'CallBackUrl'
collect['call_back_url'] = call_back_url

fileformat = AudioFormatEnum.MP3
collect['fileformat'] = fileformat


result = call_client.record_call(collect)

```


### <a name="voice_effect"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.voice_effect") voice_effect

> Voice Effect

```python
def voice_effect(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier for the in-progress voice call. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| audioDirection |  ``` Optional ```  | The direction the audio effect should be placed on. If IN, the effects will occur on the incoming audio stream. If OUT, the effects will occur on the outgoing audio stream. |
| pitchSemiTones |  ``` Optional ```  | value between -14 and 14 |
| pitchOctaves |  ``` Optional ```  | value between -1 and 1 |
| pitch |  ``` Optional ```  | value greater than 0 |
| rate |  ``` Optional ```  | value greater than 0 |
| tempo |  ``` Optional ```  | value greater than 0 |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

response_type = 'json'
collect['response_type'] = response_type

audio_direction = AudioDirectionEnum.IN
collect['audio_direction'] = audio_direction

pitch_semi_tones = 121.51357696695
collect['pitch_semi_tones'] = pitch_semi_tones

pitch_octaves = 121.51357696695
collect['pitch_octaves'] = pitch_octaves

pitch = 121.51357696695
collect['pitch'] = pitch

rate = 121.51357696695
collect['rate'] = rate

tempo = 121.51357696695
collect['tempo'] = tempo


result = call_client.voice_effect(collect)

```


### <a name="send_digit"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.send_digit") send_digit

> Play Dtmf and send the Digit

```python
def send_digit(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier of each call resource |
| playDtmf |  ``` Required ```  | DTMF digits to play to the call. 0-9, #, *, W, or w |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| playDtmfDirection |  ``` Optional ```  | The leg of the call DTMF digits should be sent to |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

response_type = 'json'
collect['response_type'] = response_type

play_dtmf_direction = DirectionEnum.IN
collect['play_dtmf_direction'] = play_dtmf_direction


result = call_client.send_digit(collect)

```


### <a name="interrupted_call"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.interrupted_call") interrupted_call

> Interrupt the Call by Call Sid

```python
def interrupted_call(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | Call SId |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| url |  ``` Optional ```  | URL the in-progress call will be redirected to |
| method |  ``` Optional ```  | The method used to request the above Url parameter |
| status |  ``` Optional ```  | Status to set the in-progress call to |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

response_type = 'json'
collect['response_type'] = response_type

url = 'Url'
collect['url'] = url

method = HttpActionEnum.GET
collect['method'] = method

status = InterruptedCallStatusEnum.CANCELED
collect['status'] = status


result = call_client.interrupted_call(collect)

```


### <a name="group_call"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.group_call") group_call

> Group Call

```python
def group_call(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | This number to display on Caller ID as calling |
| to |  ``` Required ```  | Please enter multiple E164 number. You can add max 10 numbers. Add numbers separated with comma. e.g : 1111111111,2222222222 |
| url |  ``` Required ```  | URL requested once the call connects |
| responseType |  ``` Required ```  ``` DefaultValue ```  | TODO: Add a parameter description |
| groupConfirmKey |  ``` Required ```  | Define the DTMF that the called party should send to bridge the call. Allowed Values : 0-9, #, * |
| groupConfirmFile |  ``` Required ```  | Specify the audio file you want to play when the called party picks up the call |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once call connects. |
| statusCallBackUrl |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once call connects. |
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



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

url = 'Url'
collect['url'] = url

response_type = 'json'
collect['response_type'] = response_type

group_confirm_key = 'GroupConfirmKey'
collect['group_confirm_key'] = group_confirm_key

group_confirm_file = AudioFormatEnum.MP3
collect['group_confirm_file'] = group_confirm_file

method = HttpActionEnum.GET
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

status_call_back_method = HttpActionEnum.GET
collect['status_call_back_method'] = status_call_back_method

fall_back_url = 'FallBackUrl'
collect['fall_back_url'] = fall_back_url

fall_back_method = HttpActionEnum.GET
collect['fall_back_method'] = fall_back_method

heart_beat_url = 'HeartBeatUrl'
collect['heart_beat_url'] = heart_beat_url

heart_beat_method = HttpActionEnum.GET
collect['heart_beat_method'] = heart_beat_method

timeout = 121
collect['timeout'] = timeout

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

hide_caller_id = 'HideCallerId'
collect['hide_caller_id'] = hide_caller_id

record = False
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = HttpActionEnum.GET
collect['record_call_back_method'] = record_call_back_method

transcribe = False
collect['transcribe'] = transcribe

transcribe_call_back_url = 'TranscribeCallBackUrl'
collect['transcribe_call_back_url'] = transcribe_call_back_url


result = call_client.group_call(collect)

```


### <a name="list_calls"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.list_calls") list_calls

> A list of calls associated with your Message360 account

```python
def list_calls(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| to |  ``` Optional ```  | Only list calls to this number |
| mfrom |  ``` Optional ```  | Only list calls from this number |
| dateCreated |  ``` Optional ```  | Only list calls starting within the specified date range |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

to = 'To'
collect['to'] = to

mfrom = 'From'
collect['mfrom'] = mfrom

date_created = 'DateCreated'
collect['date_created'] = date_created


result = call_client.list_calls(collect)

```


### <a name="send_ringless_vm"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.send_ringless_vm") send_ringless_vm

> API endpoint used to send a Ringless Voicemail

```python
def send_ringless_vm(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | This number to display on Caller ID as calling |
| rVMCallerId |  ``` Required ```  | Alternate caller ID required for RVM |
| to |  ``` Required ```  | To number |
| voiceMailURL |  ``` Required ```  | URL to an audio file |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| method |  ``` Optional ```  ``` DefaultValue ```  | Not currently used in this version |
| statusCallBackUrl |  ``` Optional ```  | URL to post the status of the Ringless request |
| statsCallBackMethod |  ``` Optional ```  | POST or GET |



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

rvm_caller_id = 'RVMCallerId'
collect['rvm_caller_id'] = rvm_caller_id

to = 'To'
collect['to'] = to

voice_mail_url = 'VoiceMailURL'
collect['voice_mail_url'] = voice_mail_url

response_type = 'json'
collect['response_type'] = response_type

method = HttpActionEnum.GET
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

stats_call_back_method = HttpActionEnum.GET
collect['stats_call_back_method'] = stats_call_back_method


result = call_client.send_ringless_vm(collect)

```


### <a name="view_call"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.view_call") view_call

> View Call Response

```python
def view_call(self,
                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callsid |  ``` Required ```  | Call Sid id for particular Call |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

callsid = 'callsid'
collect['callsid'] = callsid

response_type = 'json'
collect['response_type'] = response_type


result = call_client.view_call(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="carrier_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CarrierController") CarrierController

### Get controller instance

An instance of the ``` CarrierController ``` class can be accessed from the API Client.

```python
 carrier_client = client.carrier
```

### <a name="carrier_lookup_list"></a>![Method: ](https://apidocs.io/img/method.png ".CarrierController.carrier_lookup_list") carrier_lookup_list

> Get the All Purchase Number's Carrier lookup

```python
def carrier_lookup_list(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Page Number |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Page Size |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize


result = carrier_client.carrier_lookup_list(collect)

```


### <a name="carrier_lookup"></a>![Method: ](https://apidocs.io/img/method.png ".CarrierController.carrier_lookup") carrier_lookup

> Get the Carrier Lookup

```python
def carrier_lookup(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phonenumber |  ``` Required ```  | The number to lookup |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phonenumber = 'phonenumber'
collect['phonenumber'] = phonenumber

response_type = 'json'
collect['response_type'] = response_type


result = carrier_client.carrier_lookup(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="address_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AddressController") AddressController

### Get controller instance

An instance of the ``` AddressController ``` class can be accessed from the API Client.

```python
 address_client = client.address
```

### <a name="create_address"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.create_address") create_address

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
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type either json or xml |
| description |  ``` Optional ```  | Description of addresses. |
| email |  ``` Optional ```  | Email Id of user. |
| phone |  ``` Optional ```  | Phone number of user. |



#### Example Usage

```python
collect = {}

name = 'Name'
collect['name'] = name

address = 'Address'
collect['address'] = address

country = 'Country'
collect['country'] = country

state = 'State'
collect['state'] = state

city = 'City'
collect['city'] = city

zip = 'Zip'
collect['zip'] = zip

response_type = 'json'
collect['response_type'] = response_type

description = 'Description'
collect['description'] = description

email = 'email'
collect['email'] = email

phone = 'Phone'
collect['phone'] = phone


result = address_client.create_address(collect)

```


### <a name="view_address"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.view_address") view_address

> View Address Specific address Book by providing the address id

```python
def view_address(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| addressSID |  ``` Required ```  | The identifier of the address to be retrieved. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

address_sid = 'AddressSID'
collect['address_sid'] = address_sid

response_type = 'json'
collect['response_type'] = response_type


result = address_client.view_address(collect)

```


### <a name="list_address"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.list_address") list_address

> List All Address 

```python
def list_address(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |
| page |  ``` Optional ```  ``` DefaultValue ```  | Return requested # of items starting the value, default=0, must be an integer |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | How many results to return, default is 10, max is 100, must be an integer |
| addressSID |  ``` Optional ```  | addresses Sid |
| dateCreated |  ``` Optional ```  | date created address. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

address_sid = 'AddressSID'
collect['address_sid'] = address_sid

date_created = 'DateCreated'
collect['date_created'] = date_created


result = address_client.list_address(collect)

```


### <a name="verify_address"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.verify_address") verify_address

> Validates an address given.

```python
def verify_address(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| addressSID |  ``` Required ```  | The identifier of the address to be verified. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type either json or xml |



#### Example Usage

```python
collect = {}

address_sid = 'AddressSID'
collect['address_sid'] = address_sid

response_type = 'json'
collect['response_type'] = response_type


result = address_client.verify_address(collect)

```


### <a name="delete_address"></a>![Method: ](https://apidocs.io/img/method.png ".AddressController.delete_address") delete_address

> To delete Address to your address book

```python
def delete_address(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| addressSID |  ``` Required ```  | The identifier of the address to be deleted. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type either json or xml |



#### Example Usage

```python
collect = {}

address_sid = 'AddressSID'
collect['address_sid'] = address_sid

response_type = 'json'
collect['response_type'] = response_type


result = address_client.delete_address(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sub_account_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SubAccountController") SubAccountController

### Get controller instance

An instance of the ``` SubAccountController ``` class can be accessed from the API Client.

```python
 sub_account_client = client.sub_account
```

### <a name="delete_sub_account"></a>![Method: ](https://apidocs.io/img/method.png ".SubAccountController.delete_sub_account") delete_sub_account

> Delete sub account or merge numbers into parent

```python
def delete_sub_account(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subAccountSID |  ``` Required ```  | The SubaccountSid to be deleted |
| mergeNumber |  ``` Required ```  ``` DefaultValue ```  | 0 to delete or 1 to merge numbers to parent account. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

sub_account_sid = 'SubAccountSID'
collect['sub_account_sid'] = sub_account_sid

merge_number = MergeNumberStatusEnum.DELETE
collect['merge_number'] = merge_number

response_type = 'json'
collect['response_type'] = response_type


result = sub_account_client.delete_sub_account(collect)

```


### <a name="suspend_sub_account"></a>![Method: ](https://apidocs.io/img/method.png ".SubAccountController.suspend_sub_account") suspend_sub_account

> Suspend or unsuspend

```python
def suspend_sub_account(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subAccountSID |  ``` Required ```  | The SubaccountSid to be activated or suspended |
| activate |  ``` Required ```  ``` DefaultValue ```  | 0 to suspend or 1 to activate |
| responseType |  ``` Required ```  ``` DefaultValue ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

sub_account_sid = 'SubAccountSID'
collect['sub_account_sid'] = sub_account_sid

activate = ActivateStatusEnum.DEACTIVATE
collect['activate'] = activate

response_type = 'json'
collect['response_type'] = response_type


result = sub_account_client.suspend_sub_account(collect)

```


### <a name="create_sub_account"></a>![Method: ](https://apidocs.io/img/method.png ".SubAccountController.create_sub_account") create_sub_account

> Create a sub user account under the parent account

```python
def create_sub_account(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| firstName |  ``` Required ```  | Sub account user first name |
| lastName |  ``` Required ```  | sub account user last name |
| email |  ``` Required ```  | Sub account email address |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

first_name = 'FirstName'
collect['first_name'] = first_name

last_name = 'LastName'
collect['last_name'] = last_name

email = 'Email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = sub_account_client.create_sub_account(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="account_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AccountController") AccountController

### Get controller instance

An instance of the ``` AccountController ``` class can be accessed from the API Client.

```python
 account_client = client.account
```

### <a name="view_account"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.view_account") view_account

> Display Account Description

```python
def view_account(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| date |  ``` Required ```  | TODO: Add a parameter description |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

date = 'Date'
collect['date'] = date

response_type = 'json'
collect['response_type'] = response_type


result = account_client.view_account(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="short_code_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ShortCodeController") ShortCodeController

### Get controller instance

An instance of the ``` ShortCodeController ``` class can be accessed from the API Client.

```python
 short_code_client = client.short_code
```

### <a name="send_dedicated_shortcode"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.send_dedicated_shortcode") send_dedicated_shortcode

> TODO: Add a method description

```python
def send_dedicated_shortcode(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | Your dedicated shortcode |
| to |  ``` Required ```  | The number to send your SMS to |
| body |  ``` Required ```  | The body of your message |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| method |  ``` Optional ```  | Callback status method, POST or GET |
| messagestatuscallback |  ``` Optional ```  | Callback url for SMS status |



#### Example Usage

```python
collect = {}

shortcode = 213
collect['shortcode'] = shortcode

to = 213.008858858612
collect['to'] = to

body = 'body'
collect['body'] = body

response_type = 'json'
collect['response_type'] = response_type

method = HttpActionEnum.GET
collect['method'] = method

messagestatuscallback = 'messagestatuscallback'
collect['messagestatuscallback'] = messagestatuscallback


result = short_code_client.send_dedicated_shortcode(collect)

```


### <a name="view_shortcode"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.view_shortcode") view_shortcode

> View a single Sms Short Code message.

```python
def view_shortcode(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageSid |  ``` Required ```  | The unique identifier for the sms resource |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

message_sid = 'MessageSid'
collect['message_sid'] = message_sid

response_type = 'json'
collect['response_type'] = response_type


result = short_code_client.view_shortcode(collect)

```


### <a name="list_shortcode"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.list_shortcode") list_shortcode

> Retrieve a list of Short Code message objects.

```python
def list_shortcode(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| shortcode |  ``` Optional ```  | Only list messages sent from this Short Code |
| to |  ``` Optional ```  | Only list messages sent to this number |
| dateSent |  ``` Optional ```  | Only list messages sent with the specified date |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

to = 'To'
collect['to'] = to

date_sent = datetime.now()
collect['date_sent'] = date_sent

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size


result = short_code_client.list_shortcode(collect)

```


### <a name="list_inbound_shortcode"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.list_inbound_shortcode") list_inbound_shortcode

> Retrive a list of inbound Sms Short Code messages associated with your message360 account.

```python
def list_inbound_shortcode(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Zero indexed |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | Only list SMS messages sent from this number |
| shortcode |  ``` Optional ```  | Only list SMS messages sent to Shortcode |
| dateReceived |  ``` Optional ```  | Only list SMS messages sent in the specified date MAKE REQUEST |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size

mfrom = 'From'
collect['mfrom'] = mfrom

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

date_received = 'DateReceived'
collect['date_received'] = date_received


result = short_code_client.list_inbound_shortcode(collect)

```


[Back to List of Controllers](#list_of_controllers)



