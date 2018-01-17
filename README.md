# Getting started

message360 API version 3

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
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

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Message360-Python&libraryName=message_360.message_360_client&projectName=message_360&className=Message360Client)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Message360-Python&libraryName=message_360.message_360_client&projectName=message_360&className=Message360Client)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

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
* [PhoneNumberController](#phone_number_controller)
* [WebRTCController](#web_rtc_controller)
* [TranscriptionController](#transcription_controller)
* [RecordingController](#recording_controller)
* [EmailController](#email_controller)
* [SMSController](#sms_controller)
* [CallController](#call_controller)
* [CarrierController](#carrier_controller)
* [AddressController](#address_controller)
* [SubAccountController](#sub_account_controller)
* [AccountController](#account_controller)
* [UsageController](#usage_controller)
* [ShortCodeController](#short_code_controller)
* [PostCardController](#post_card_controller)
* [LetterController](#letter_controller)
* [AreaMailController](#area_mail_controller)

## <a name="shared_short_code_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SharedShortCodeController") SharedShortCodeController

### Get controller instance

An instance of the ``` SharedShortCodeController ``` class can be accessed from the API Client.

```python
 shared_short_code_controller = client.shared_short_code
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
| templateId |  ``` Required ```  | The unique identifier for a template object |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

template_id = uuid.uuid4()
collect['template_id'] = template_id

response_type = 'json'
collect['response_type'] = response_type


result = shared_short_code_controller.view_template(collect)

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


result = shared_short_code_controller.view_shared_shortcodes(collect)

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
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| shortcode |  ``` Optional ```  | Only list messages sent from this Short Code |
| to |  ``` Optional ```  | Only list messages sent to this number |
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

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

to = 'to'
collect['to'] = to

datesent = 'datesent'
collect['datesent'] = datesent


result = shared_short_code_controller.list_outbound_shared_shortcodes(collect)

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
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | From Number to Inbound ShortCode |
| shortcode |  ``` Optional ```  | Only list messages sent to this Short Code |
| datecreated |  ``` Optional ```  | Only list messages sent with the specified date |



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

datecreated = 'Datecreated'
collect['datecreated'] = datecreated


result = shared_short_code_controller.list_inbound_shared_shortcodes(collect)

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


result = shared_short_code_controller.send_shared_shortcode(collect)

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


result = shared_short_code_controller.list_templates(collect)

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


result = shared_short_code_controller.view_keyword(collect)

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
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| keyword |  ``` Optional ```  | Only list keywords of keyword |
| shortcode |  ``` Optional ```  | Only list keywords of shortcode |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

keyword = 'Keyword'
collect['keyword'] = keyword

shortcode = 86
collect['shortcode'] = shortcode


result = shared_short_code_controller.list_keyword(collect)

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


result = shared_short_code_controller.view_assignement(collect)

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
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| shortcode |  ``` Optional ```  | Only list keywords of shortcode |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

shortcode = 'Shortcode'
collect['shortcode'] = shortcode


result = shared_short_code_controller.list_assignment(collect)

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


result = shared_short_code_controller.update_assignment(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="conference_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ConferenceController") ConferenceController

### Get controller instance

An instance of the ``` ConferenceController ``` class can be accessed from the API Client.

```python
 conference_controller = client.conference
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


result = conference_controller.deaf_mute_participant(collect)

```


### <a name="view_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.view_participant") view_participant

> Retrieve information about a participant by its ParticipantSid.

```python
def view_participant(self,
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


result = conference_controller.view_participant(collect)

```


### <a name="view_conference"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.view_conference") view_conference

> Retrieve information about a conference by its ConferenceSid.

```python
def view_conference(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier of each conference resource |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

response_type = 'json'
collect['response_type'] = response_type


result = conference_controller.view_conference(collect)

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
| conferenceSid |  ``` Required ```  | The unique identifier for a conference object. |
| participantNumber |  ``` Required ```  | The phone number of the participant to be added. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| muted |  ``` Optional ```  | Specifies if participant should be muted. |
| deaf |  ``` Optional ```  | Specifies if the participant should hear audio in the conference. |



#### Example Usage

```python
collect = {}

conference_sid = 'ConferenceSid'
collect['conference_sid'] = conference_sid

participant_number = 'ParticipantNumber'
collect['participant_number'] = participant_number

response_type = 'json'
collect['response_type'] = response_type

muted = False
collect['muted'] = muted

deaf = False
collect['deaf'] = deaf


result = conference_controller.add_participant(collect)

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
| mfrom |  ``` Required ```  | A valid 10-digit number (E.164 format) that will be initiating the conference call. |
| to |  ``` Required ```  | A valid 10-digit number (E.164 format) that is to receive the conference call. |
| url |  ``` Required ```  | URL requested once the conference connects |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| method |  ``` Optional ```  ``` DefaultValue ```  | Specifies the HTTP method used to request the required URL once call connects. |
| statusCallBackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the conference is finished. |
| statusCallBackMethod |  ``` Optional ```  | Specifies the HTTP methodlinkclass used to request StatusCallbackUrl. |
| fallbackUrl |  ``` Optional ```  | URL requested if the initial Url parameter fails or encounters an error |
| fallbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |
| record |  ``` Optional ```  | Specifies if the conference should be recorded. |
| recordCallBackUrl |  ``` Optional ```  | Recording parameters will be sent here upon completion. |
| recordCallBackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once conference connects. |
| scheduleTime |  ``` Optional ```  | Schedule conference in future. Schedule time must be greater than current time |
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

response_type = 'json'
collect['response_type'] = response_type

method = HttpActionEnum.POST
collect['method'] = method

status_call_back_url = 'StatusCallBackUrl'
collect['status_call_back_url'] = status_call_back_url

status_call_back_method = HttpActionEnum.GET
collect['status_call_back_method'] = status_call_back_method

fallback_url = 'FallbackUrl'
collect['fallback_url'] = fallback_url

fallback_method = HttpActionEnum.GET
collect['fallback_method'] = fallback_method

record = False
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = HttpActionEnum.GET
collect['record_call_back_method'] = record_call_back_method

schedule_time = 'ScheduleTime'
collect['schedule_time'] = schedule_time

timeout = 44
collect['timeout'] = timeout


result = conference_controller.create_conference(collect)

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


result = conference_controller.hangup_participant(collect)

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


result = conference_controller.play_conference_audio(collect)

```


### <a name="list_participant"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.list_participant") list_participant

> Retrieve a list of participants for an in-progress conference.

```python
def list_participant(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| conferenceSid |  ``` Required ```  | The unique identifier for a conference. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response format, xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| muted |  ``` Optional ```  | Specifies if participant should be muted. |
| deaf |  ``` Optional ```  | Specifies if the participant should hear audio in the conference. |



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


result = conference_controller.list_participant(collect)

```


### <a name="list_conference"></a>![Method: ](https://apidocs.io/img/method.png ".ConferenceController.list_conference") list_conference

> Retrieve a list of conference objects.

```python
def list_conference(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| friendlyName |  ``` Optional ```  | Only return conferences with the specified FriendlyName |
| dateCreated |  ``` Optional ```  | Conference created date |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

date_created = 'DateCreated'
collect['date_created'] = date_created


result = conference_controller.list_conference(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="phone_number_controller"></a>![Class: ](https://apidocs.io/img/class.png ".PhoneNumberController") PhoneNumberController

### Get controller instance

An instance of the ``` PhoneNumberController ``` class can be accessed from the API Client.

```python
 phone_number_controller = client.phone_number
```

### <a name="available_phone_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.available_phone_number") available_phone_number

> Retrieve a list of available phone numbers that can be purchased and used for your message360 account.

```python
def available_phone_number(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| numbertype |  ``` Required ```  | Number type either SMS,Voice or all |
| areacode |  ``` Required ```  | Specifies the area code for the returned list of available numbers. Only available for North American numbers. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return. |



#### Example Usage

```python
collect = {}

numbertype = NumberTypeEnum.ALL
collect['numbertype'] = numbertype

areacode = 'areacode'
collect['areacode'] = areacode

response_type = 'json'
collect['response_type'] = response_type

pagesize = 10
collect['pagesize'] = pagesize


result = phone_number_controller.available_phone_number(collect)

```


### <a name="view_number_details"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.view_number_details") view_number_details

> Retrieve the details for a phone number by its number.

```python
def view_number_details(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid message360 10-digit phone number (E.164 format). |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_controller.view_number_details(collect)

```


### <a name="release_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.release_number") release_number

> Remove a purchased message360 number from your account.

```python
def release_number(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid 10-digit message360 number (E.164 format). |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_controller.release_number(collect)

```


### <a name="buy_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.buy_number") buy_number

> Purchase a phone number to be used with your message360 account

```python
def buy_number(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid 10-digit message360 number (E.164 format). |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_controller.buy_number(collect)

```


### <a name="mass_release_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.mass_release_number") mass_release_number

> Remove a purchased message360 number from your account.

```python
def mass_release_number(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid message360 comma separated numbers (E.164 format). |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_controller.mass_release_number(collect)

```


### <a name="update_phone_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.update_phone_number") update_phone_number

> Update properties for a message360 number that has been purchased for your account. Refer to the parameters list for the list of properties that can be updated.

```python
def update_phone_number(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid message360 number (E.164 format). |
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
| smsFallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML from an SMS or at initial request of the SmsUrl. |
| smsFallbackMethod |  ``` Optional ```  | The HTTP method message360 will use when URL requested if the SmsUrl is not available. |



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


result = phone_number_controller.update_phone_number(collect)

```


### <a name="list_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.list_number") list_number

> Retrieve a list of purchased phones numbers associated with your message360 account.

```python
def list_number(self,
                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | Which page of the overall response will be returned. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| numberType |  ``` Optional ```  | The capability supported by the number.Number type either SMS,Voice or all |
| friendlyName |  ``` Optional ```  | A human-readable label added to the number object. |



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


result = phone_number_controller.list_number(collect)

```


### <a name="mass_update_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.mass_update_number") mass_update_number

> Update properties for a message360 numbers that has been purchased for your account. Refer to the parameters list for the list of properties that can be updated.

```python
def mass_update_number(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phoneNumber |  ``` Required ```  | A valid comma(,) separated message360 numbers. (E.164 format). |
| voiceUrl |  ``` Required ```  | The URL returning InboundXML incoming calls should execute when connected. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| friendlyName |  ``` Optional ```  | A human-readable value for labeling the number. |
| voiceMethod |  ``` Optional ```  | Specifies the HTTP method used to request the VoiceUrl once incoming call connects. |
| voiceFallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML on a call or at initial request of the voice url |
| voiceFallbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the VoiceFallbackUrl once incoming call connects. |
| hangupCallback |  ``` Optional ```  | URL that can be requested to receive notification when and how incoming call has ended. |
| hangupCallbackMethod |  ``` Optional ```  | The HTTP method message360 will use when requesting the HangupCallback URL. |
| heartbeatUrl |  ``` Optional ```  | URL that can be used to monitor the phone number. |
| heartbeatMethod |  ``` Optional ```  | The HTTP method message360 will use when requesting the HeartbeatUrl. |
| smsUrl |  ``` Optional ```  | URL requested when an SMS is received. |
| smsMethod |  ``` Optional ```  | The HTTP method message360 will use when requesting the SmsUrl. |
| smsFallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML from an SMS or at initial request of the SmsUrl. |
| smsFallbackMethod |  ``` Optional ```  | The HTTP method message360 will use when URL requested if the SmsUrl is not available. |



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


result = phone_number_controller.mass_update_number(collect)

```


### <a name="get_did_score_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.get_did_score_number") get_did_score_number

> Get DID Score Number

```python
def get_did_score_number(self,
                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phonenumber |  ``` Required ```  | Specifies the multiple phone numbers for check updated spamscore . |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phonenumber = 'Phonenumber'
collect['phonenumber'] = phonenumber

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_controller.get_did_score_number(collect)

```


### <a name="bulk_buy_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.bulk_buy_number") bulk_buy_number

> Purchase a selected number of DID's from specific area codes to be used with your message360 account.

```python
def bulk_buy_number(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| numberType |  ``` Required ```  | The capability the number supports. |
| areaCode |  ``` Required ```  | Specifies the area code for the returned list of available numbers. Only available for North American numbers. |
| quantity |  ``` Required ```  | A positive integer that tells how many number you want to buy at a time. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| leftover |  ``` Optional ```  | If desired quantity is unavailable purchase what is available . |



#### Example Usage

```python
collect = {}

number_type = NumberTypeEnum.ALL
collect['number_type'] = number_type

area_code = 'AreaCode'
collect['area_code'] = area_code

quantity = 'Quantity'
collect['quantity'] = quantity

response_type = 'json'
collect['response_type'] = response_type

leftover = 'Leftover'
collect['leftover'] = leftover


result = phone_number_controller.bulk_buy_number(collect)

```


### <a name="transfer_number"></a>![Method: ](https://apidocs.io/img/method.png ".PhoneNumberController.transfer_number") transfer_number

> Transfer phone number that has been purchased for from one account to another account.

```python
def transfer_number(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| phonenumber |  ``` Required ```  | A valid 10-digit message360 number (E.164 format). |
| fromaccountsid |  ``` Required ```  | A specific Accountsid from where Number is getting transfer. |
| toaccountsid |  ``` Required ```  | A specific Accountsid to which Number is getting transfer. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phonenumber = 'phonenumber'
collect['phonenumber'] = phonenumber

fromaccountsid = 'fromaccountsid'
collect['fromaccountsid'] = fromaccountsid

toaccountsid = 'toaccountsid'
collect['toaccountsid'] = toaccountsid

response_type = 'json'
collect['response_type'] = response_type


result = phone_number_controller.transfer_number(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="web_rtc_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WebRTCController") WebRTCController

### Get controller instance

An instance of the ``` WebRTCController ``` class can be accessed from the API Client.

```python
 web_rtc_controller = client.web_rtc
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


result = web_rtc_controller.check_funds(collect)

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


result = web_rtc_controller.create_token(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="transcription_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TranscriptionController") TranscriptionController

### Get controller instance

An instance of the ``` TranscriptionController ``` class can be accessed from the API Client.

```python
 transcription_controller = client.transcription
```

### <a name="view_transcription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.view_transcription") view_transcription

> Retrieve information about a transaction by its TranscriptionSid.

```python
def view_transcription(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| transcriptionsid |  ``` Required ```  | The unique identifier for a transcription object. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

transcriptionsid = 'transcriptionsid'
collect['transcriptionsid'] = transcriptionsid

response_type = 'json'
collect['response_type'] = response_type


result = transcription_controller.view_transcription(collect)

```


### <a name="recording_transcription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.recording_transcription") recording_transcription

> Transcribe a message360 recording by its RecordingSid.

```python
def recording_transcription(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingSid |  ``` Required ```  | The unique identifier for a recording object. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

recording_sid = 'recordingSid'
collect['recording_sid'] = recording_sid

response_type = 'json'
collect['response_type'] = response_type


result = transcription_controller.recording_transcription(collect)

```


### <a name="audio_url_transcription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.audio_url_transcription") audio_url_transcription

> Transcribe an audio recording from a file.

```python
def audio_url_transcription(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| audiourl |  ``` Required ```  | URL pointing to the location of the audio file that is to be transcribed. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

audiourl = 'audiourl'
collect['audiourl'] = audiourl

response_type = 'json'
collect['response_type'] = response_type


result = transcription_controller.audio_url_transcription(collect)

```


### <a name="list_transcription"></a>![Method: ](https://apidocs.io/img/method.png ".TranscriptionController.list_transcription") list_transcription

> Retrieve a list of transcription objects for your message360 account.

```python
def list_transcription(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| status |  ``` Optional ```  | The state of the transcription. |
| dateTranscribed |  ``` Optional ```  | The date the transcription took place. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

status = StatusEnum.INPROGRESS
collect['status'] = status

date_transcribed = 'dateTranscribed'
collect['date_transcribed'] = date_transcribed


result = transcription_controller.list_transcription(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="recording_controller"></a>![Class: ](https://apidocs.io/img/class.png ".RecordingController") RecordingController

### Get controller instance

An instance of the ``` RecordingController ``` class can be accessed from the API Client.

```python
 recording_controller = client.recording
```

### <a name="view_recording"></a>![Method: ](https://apidocs.io/img/method.png ".RecordingController.view_recording") view_recording

> Retrieve the recording of a call by its RecordingSid. This resource will return information regarding the call such as start time, end time, duration, and so forth.

```python
def view_recording(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingsid |  ``` Required ```  | The unique identifier for the recording. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

recordingsid = 'recordingsid'
collect['recordingsid'] = recordingsid

response_type = 'json'
collect['response_type'] = response_type


result = recording_controller.view_recording(collect)

```


### <a name="delete_recording"></a>![Method: ](https://apidocs.io/img/method.png ".RecordingController.delete_recording") delete_recording

> Remove a recording from your message360 account.

```python
def delete_recording(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| recordingsid |  ``` Required ```  | The unique identifier for a recording. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

recordingsid = 'recordingsid'
collect['recordingsid'] = recordingsid

response_type = 'json'
collect['response_type'] = response_type


result = recording_controller.delete_recording(collect)

```


### <a name="list_recording"></a>![Method: ](https://apidocs.io/img/method.png ".RecordingController.list_recording") list_recording

> Retrieve a list of recording objects.

```python
def list_recording(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| datecreated |  ``` Optional ```  | Filter results by creation date |
| callsid |  ``` Optional ```  | The unique identifier for a call. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

datecreated = 'Datecreated'
collect['datecreated'] = datecreated

callsid = 'callsid'
collect['callsid'] = callsid


result = recording_controller.list_recording(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="email_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EmailController") EmailController

### Get controller instance

An instance of the ``` EmailController ``` class can be accessed from the API Client.

```python
 email_controller = client.email
```

### <a name="delete_spam"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_spam") delete_spam

> Remove an email from the spam email list.

```python
def delete_spam(self,
                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| email |  ``` Required ```  | A valid email address that is to be remove from the spam list. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

email = 'Email'
collect['email'] = email


result = email_controller.delete_spam(collect)

```


### <a name="delete_block"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_block") delete_block

> Remove an email from blocked emails list.

```python
def delete_block(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email address to be remove from the blocked list. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'Email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_controller.delete_block(collect)

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
| email |  ``` Required ```  | A valid email address that is to be added to the unsubscribe list |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_controller.add_unsubscribes(collect)

```


### <a name="send_email"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.send_email") send_email

> Create and submit an email message to one or more email addresses.

```python
def send_email(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| to |  ``` Required ```  | A valid address that will receive the email. Multiple addresses can be separated by using commas. |
| mtype |  ``` Required ```  ``` DefaultValue ```  | Specifies the type of email to be sent |
| subject |  ``` Required ```  | The subject of the mail. Must be a valid string. |
| message |  ``` Required ```  | The email message that is to be sent in the text. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| mfrom |  ``` Optional ```  | A valid address that will send the email. |
| cc |  ``` Optional ```  | Carbon copy. A valid address that will receive the email. Multiple addresses can be separated by using commas. |
| bcc |  ``` Optional ```  | Blind carbon copy. A valid address that will receive the email. Multiple addresses can be separated by using commas. |
| attachment |  ``` Optional ```  | A file that is attached to the email. Must be less than 7 MB in size. |



#### Example Usage

```python
collect = {}

to = 'To'
collect['to'] = to

mtype = SendEmailAsEnum.HTML
collect['mtype'] = mtype

subject = 'Subject'
collect['subject'] = subject

message = 'Message'
collect['message'] = message

response_type = 'json'
collect['response_type'] = response_type

mfrom = 'From'
collect['mfrom'] = mfrom

cc = 'Cc'
collect['cc'] = cc

bcc = 'Bcc'
collect['bcc'] = bcc

attachment = 'Attachment'
collect['attachment'] = attachment


result = email_controller.send_email(collect)

```


### <a name="delete_unsubscribes"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_unsubscribes") delete_unsubscribes

> Remove an email address from the list of unsubscribed emails.

```python
def delete_unsubscribes(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | A valid email address that is to be remove from the unsubscribe list. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

email = 'email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_controller.delete_unsubscribes(collect)

```


### <a name="list_unsubscribes"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_unsubscribes") list_unsubscribes

> Retrieve a list of email addresses from the unsubscribe list.

```python
def list_unsubscribes(self,
                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| offset |  ``` Optional ```  | The starting point of the list of unsubscribed emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.list_unsubscribes(collect)

```


### <a name="list_invalid"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_invalid") list_invalid

> Retrieve a list of invalid email addresses.

```python
def list_invalid(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| offset |  ``` Optional ```  | The starting point of the list of invalid emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.list_invalid(collect)

```


### <a name="delete_bounces"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_bounces") delete_bounces

> Remove an email address from the bounced list.

```python
def delete_bounces(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| email |  ``` Required ```  | The email address to be remove from the bounced email list. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

email = 'Email'
collect['email'] = email


result = email_controller.delete_bounces(collect)

```


### <a name="list_bounces"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_bounces") list_bounces

> Retrieve a list of emails that have bounced.

```python
def list_bounces(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| offset |  ``` Optional ```  | The starting point of the list of bounced emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.list_bounces(collect)

```


### <a name="list_spam"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_spam") list_spam

> Retrieve a list of emails that are on the spam list.

```python
def list_spam(self,
                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| offset |  ``` Optional ```  | The starting point of the list of spam emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.list_spam(collect)

```


### <a name="list_blocks"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.list_blocks") list_blocks

> Retrieve a list of emails that have been blocked.

```python
def list_blocks(self,
                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| offset |  ``` Optional ```  | The starting point of the list of blocked emails that should be returned. |
| limit |  ``` Optional ```  | The count of results that should be returned. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

offset = 'Offset'
collect['offset'] = offset

limit = 'Limit'
collect['limit'] = limit


result = email_controller.list_blocks(collect)

```


### <a name="delete_invalid"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.delete_invalid") delete_invalid

> Remove an email from the invalid email list.

```python
def delete_invalid(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | A valid email address that is to be remove from the invalid email list. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

email = 'Email'
collect['email'] = email

response_type = 'json'
collect['response_type'] = response_type


result = email_controller.delete_invalid(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sms_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SMSController") SMSController

### Get controller instance

An instance of the ``` SMSController ``` class can be accessed from the API Client.

```python
 sms_controller = client.sms
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
| mfrom |  ``` Required ```  | The 10-digit SMS-enabled message360 number (E.164 format) in which the message is sent. |
| to |  ``` Required ```  | The 10-digit phone number (E.164 format) that will receive the message. |
| body |  ``` Required ```  | The body message that is to be sent in the text. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once SMS sent. |
| messageStatusCallback |  ``` Optional ```  | URL that can be requested to receive notification when SMS has Sent. A set of default parameters will be sent here once the SMS is finished. |
| smartsms |  ``` Optional ```  ``` DefaultValue ```  | Check's 'to' number can receive sms or not using Carrier API, if wireless = true then text sms is sent, else wireless = false then call is recieved to end user with audible message. |
| deliveryStatus |  ``` Optional ```  ``` DefaultValue ```  | Delivery reports are a method to tell your system if the message has arrived on the destination phone. |



#### Example Usage

```python
collect = {}

mfrom = 'From'
collect['mfrom'] = mfrom

to = 'To'
collect['to'] = to

body = 'Body'
collect['body'] = body

response_type = 'json'
collect['response_type'] = response_type

method = HttpActionEnum.GET
collect['method'] = method

message_status_callback = 'MessageStatusCallback'
collect['message_status_callback'] = message_status_callback

smartsms = False
collect['smartsms'] = smartsms

delivery_status = False
collect['delivery_status'] = delivery_status


result = sms_controller.send_sms(collect)

```


### <a name="view_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.view_sms") view_sms

> Retrieve a single SMS message object by its SmsSid.

```python
def view_sms(self,
                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageSid |  ``` Required ```  | The unique identifier for a sms message. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

message_sid = 'MessageSid'
collect['message_sid'] = message_sid

response_type = 'json'
collect['response_type'] = response_type


result = sms_controller.view_sms(collect)

```


### <a name="list_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.list_sms") list_sms

> Retrieve a list of Outbound SMS message objects.

```python
def list_sms(self,
                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | Filter SMS message objects from this valid 10-digit phone number (E.164 format). |
| to |  ``` Optional ```  | Filter SMS message objects to this valid 10-digit phone number (E.164 format). |
| dateSent |  ``` Optional ```  | Only list SMS messages sent in the specified date range |



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

to = 'To'
collect['to'] = to

date_sent = 'DateSent'
collect['date_sent'] = date_sent


result = sms_controller.list_sms(collect)

```


### <a name="list_inbound_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.list_inbound_sms") list_inbound_sms

> Retrieve a list of Inbound SMS message objects.

```python
def list_inbound_sms(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| mfrom |  ``` Optional ```  | Filter SMS message objects from this valid 10-digit phone number (E.164 format). |
| to |  ``` Optional ```  | Filter SMS message objects to this valid 10-digit phone number (E.164 format). |
| dateSent |  ``` Optional ```  | Filter sms message objects by this date. |



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

to = 'To'
collect['to'] = to

date_sent = 'DateSent'
collect['date_sent'] = date_sent


result = sms_controller.list_inbound_sms(collect)

```


### <a name="view_detail_sms"></a>![Method: ](https://apidocs.io/img/method.png ".SMSController.view_detail_sms") view_detail_sms

> Retrieve a single SMS message object with details by its SmsSid.

```python
def view_detail_sms(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageSid |  ``` Required ```  | The unique identifier for a sms message. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

message_sid = 'MessageSid'
collect['message_sid'] = message_sid

response_type = 'json'
collect['response_type'] = response_type


result = sms_controller.view_detail_sms(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="call_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CallController") CallController

### Get controller instance

An instance of the ``` CallController ``` class can be accessed from the API Client.

```python
 call_controller = client.call
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
| mfrom |  ``` Required ```  | A valid message360 Voice enabled number (E.164 format) that will be initiating the phone call. |
| to |  ``` Required ```  | To number |
| url |  ``` Required ```  | URL requested once the call connects |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once call connects. |
| statusCallBackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
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

timeout = 227
collect['timeout'] = timeout

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

hide_caller_id = True
collect['hide_caller_id'] = hide_caller_id

record = True
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = HttpActionEnum.GET
collect['record_call_back_method'] = record_call_back_method

transcribe = True
collect['transcribe'] = transcribe

transcribe_call_back_url = 'TranscribeCallBackUrl'
collect['transcribe_call_back_url'] = transcribe_call_back_url

if_machine = IfMachineEnum.CONTINUE
collect['if_machine'] = if_machine

if_machine_url = 'IfMachineUrl'
collect['if_machine_url'] = if_machine_url

if_machine_method = HttpActionEnum.GET
collect['if_machine_method'] = if_machine_method

feedback = True
collect['feedback'] = feedback

survey_id = 'SurveyId'
collect['survey_id'] = survey_id


result = call_controller.make_call(collect)

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

length = 227
collect['length'] = length

direction = DirectionEnum.IN
collect['direction'] = direction

mix = True
collect['mix'] = mix


result = call_controller.play_audio(collect)

```


### <a name="record_call"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.record_call") record_call

> Start or stop recording of an in-progress voice call.

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

record = True
collect['record'] = record

response_type = 'json'
collect['response_type'] = response_type

direction = DirectionEnum.IN
collect['direction'] = direction

time_limit = 227
collect['time_limit'] = time_limit

call_back_url = 'CallBackUrl'
collect['call_back_url'] = call_back_url

fileformat = AudioFormatEnum.MP3
collect['fileformat'] = fileformat


result = call_controller.record_call(collect)

```


### <a name="voice_effect"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.voice_effect") voice_effect

> Add audio voice effects to the an in-progress voice call.

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
| pitchSemiTones |  ``` Optional ```  | Set the pitch in semitone (half-step) intervals. Value between -14 and 14 |
| pitchOctaves |  ``` Optional ```  | Set the pitch in octave intervals.. Value between -1 and 1 |
| pitch |  ``` Optional ```  | Set the pitch (lowness/highness) of the audio. The higher the value, the higher the pitch. Value greater than 0 |
| rate |  ``` Optional ```  | Set the rate for audio. The lower the value, the lower the rate. value greater than 0 |
| tempo |  ``` Optional ```  | Set the tempo (speed) of the audio. A higher value denotes a faster tempo. Value greater than 0 |



#### Example Usage

```python
collect = {}

call_sid = 'CallSid'
collect['call_sid'] = call_sid

response_type = 'json'
collect['response_type'] = response_type

audio_direction = AudioDirectionEnum.IN
collect['audio_direction'] = audio_direction

pitch_semi_tones = 227.569347430286
collect['pitch_semi_tones'] = pitch_semi_tones

pitch_octaves = 227.569347430286
collect['pitch_octaves'] = pitch_octaves

pitch = 227.569347430286
collect['pitch'] = pitch

rate = 227.569347430286
collect['rate'] = rate

tempo = 227.569347430286
collect['tempo'] = tempo


result = call_controller.voice_effect(collect)

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


result = call_controller.send_digit(collect)

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
| callSid |  ``` Required ```  | The unique identifier for voice call that is in progress. |
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


result = call_controller.interrupted_call(collect)

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
| statusCallBackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
| statusCallBackMethod |  ``` Optional ```  | Specifies the HTTP methodlinkclass used to request StatusCallbackUrl. |
| fallBackUrl |  ``` Optional ```  | URL requested if the initial Url parameter fails or encounters an error |
| fallBackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |
| heartBeatUrl |  ``` Optional ```  | URL that can be requested every 60 seconds during the call to notify of elapsed time and pass other general information. |
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

timeout = 227
collect['timeout'] = timeout

play_dtmf = 'PlayDtmf'
collect['play_dtmf'] = play_dtmf

hide_caller_id = 'HideCallerId'
collect['hide_caller_id'] = hide_caller_id

record = True
collect['record'] = record

record_call_back_url = 'RecordCallBackUrl'
collect['record_call_back_url'] = record_call_back_url

record_call_back_method = HttpActionEnum.GET
collect['record_call_back_method'] = record_call_back_method

transcribe = True
collect['transcribe'] = transcribe

transcribe_call_back_url = 'TranscribeCallBackUrl'
collect['transcribe_call_back_url'] = transcribe_call_back_url


result = call_controller.group_call(collect)

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
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| to |  ``` Optional ```  | Filter calls that were sent to this 10-digit number (E.164 format). |
| mfrom |  ``` Optional ```  | Filter calls that were sent from this 10-digit number (E.164 format). |
| dateCreated |  ``` Optional ```  | Return calls that are from a specified date. |



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


result = call_controller.list_calls(collect)

```


### <a name="send_ringless_vm"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.send_ringless_vm") send_ringless_vm

> Initiate an outbound Ringless Voicemail through message360.

```python
def send_ringless_vm(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mfrom |  ``` Required ```  | A valid message360 Voice enabled number (E.164 format) that will be initiating the phone call. |
| rVMCallerId |  ``` Required ```  | A required secondary Caller ID for RVM to work. |
| to |  ``` Required ```  | A valid number (E.164 format) that will receive the phone call. |
| voiceMailURL |  ``` Required ```  | The URL requested once the RVM connects. A set of default parameters will be sent here. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| method |  ``` Optional ```  ``` DefaultValue ```  | Specifies the HTTP method used to request the required URL once call connects. |
| statusCallBackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
| statsCallBackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required StatusCallBackUrl once call connects. |



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


result = call_controller.send_ringless_vm(collect)

```


### <a name="view_call"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.view_call") view_call

> Retrieve a single voice call’s information by its CallSid.

```python
def view_call(self,
                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callsid |  ``` Required ```  | The unique identifier for the voice call. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

callsid = 'callsid'
collect['callsid'] = callsid

response_type = 'json'
collect['response_type'] = response_type


result = call_controller.view_call(collect)

```


### <a name="view_call_detail"></a>![Method: ](https://apidocs.io/img/method.png ".CallController.view_call_detail") view_call_detail

> Retrieve a single voice call’s information by its CallSid.

```python
def view_call_detail(self,
                         call_sid,
                         response_type)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| callSid |  ``` Required ```  | The unique identifier for the voice call. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
call_sid = 'callSid'
response_type = 'json'

result = call_controller.view_call_detail(call_sid, response_type)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="carrier_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CarrierController") CarrierController

### Get controller instance

An instance of the ``` CarrierController ``` class can be accessed from the API Client.

```python
 carrier_controller = client.carrier
```

### <a name="carrier_lookup_list"></a>![Method: ](https://apidocs.io/img/method.png ".CarrierController.carrier_lookup_list") carrier_lookup_list

> Retrieve a list of carrier lookup objects.

```python
def carrier_lookup_list(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size


result = carrier_controller.carrier_lookup_list(collect)

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
| phoneNumber |  ``` Required ```  | A valid 10-digit number (E.164 format). |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

phone_number = 'PhoneNumber'
collect['phone_number'] = phone_number

response_type = 'json'
collect['response_type'] = response_type


result = carrier_controller.carrier_lookup(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="address_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AddressController") AddressController

### Get controller instance

An instance of the ``` AddressController ``` class can be accessed from the API Client.

```python
 address_controller = client.address
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


result = address_controller.create_address(collect)

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
| addressid |  ``` Required ```  | The identifier of the address to be retrieved. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

addressid = 'addressid'
collect['addressid'] = addressid

response_type = 'json'
collect['response_type'] = response_type


result = address_controller.view_address(collect)

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
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | How many results to return, default is 10, max is 100, must be an integer |
| addressid |  ``` Optional ```  | addresses Sid |
| dateCreated |  ``` Optional ```  | date created address. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

addressid = 'addressid'
collect['addressid'] = addressid

date_created = 'dateCreated'
collect['date_created'] = date_created


result = address_controller.list_address(collect)

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
| addressid |  ``` Required ```  | The identifier of the address to be verified. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type either json or xml |



#### Example Usage

```python
collect = {}

addressid = 'addressid'
collect['addressid'] = addressid

response_type = 'json'
collect['response_type'] = response_type


result = address_controller.verify_address(collect)

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
| addressid |  ``` Required ```  | The identifier of the address to be deleted. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type either json or xml |



#### Example Usage

```python
collect = {}

addressid = 'addressid'
collect['addressid'] = addressid

response_type = 'json'
collect['response_type'] = response_type


result = address_controller.delete_address(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sub_account_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SubAccountController") SubAccountController

### Get controller instance

An instance of the ``` SubAccountController ``` class can be accessed from the API Client.

```python
 sub_account_controller = client.sub_account
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


result = sub_account_controller.delete_sub_account(collect)

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


result = sub_account_controller.suspend_sub_account(collect)

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
| friendlyName |  ``` Required ```  | Descriptive name of the sub account |
| password |  ``` Required ```  | The password of the sub account.  Please make sure to make as password that is at least 8 characters long, contain a symbol, uppercase and a number. |
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

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

password = 'Password'
collect['password'] = password

response_type = 'json'
collect['response_type'] = response_type


result = sub_account_controller.create_sub_account(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="account_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AccountController") AccountController

### Get controller instance

An instance of the ``` AccountController ``` class can be accessed from the API Client.

```python
 account_controller = client.account
```

### <a name="view_account"></a>![Method: ](https://apidocs.io/img/method.png ".AccountController.view_account") view_account

> Retrieve information regarding your message360 account by a specific date. The response object will contain data such as account status, balance, and account usage totals.

```python
def view_account(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| date |  ``` Required ```  | Filter account information based on date. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

date = 'Date'
collect['date'] = date

response_type = 'json'
collect['response_type'] = response_type


result = account_controller.view_account(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="usage_controller"></a>![Class: ](https://apidocs.io/img/class.png ".UsageController") UsageController

### Get controller instance

An instance of the ``` UsageController ``` class can be accessed from the API Client.

```python
 usage_controller = client.usage
```

### <a name="list_usage"></a>![Method: ](https://apidocs.io/img/method.png ".UsageController.list_usage") list_usage

> Retrieve usage metrics regarding your message360 account. The results includes inbound/outbound voice calls and inbound/outbound SMS messages as well as carrier lookup requests.

```python
def list_usage(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| productCode |  ``` Optional ```  ``` DefaultValue ```  | Filter usage results by product type. |
| startDate |  ``` Optional ```  ``` DefaultValue ```  | Filter usage objects by start date. |
| endDate |  ``` Optional ```  ``` DefaultValue ```  | Filter usage objects by end date. |
| includeSubAccounts |  ``` Optional ```  | Will include all subaccount usage data |



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

include_sub_accounts = 'IncludeSubAccounts'
collect['include_sub_accounts'] = include_sub_accounts


result = usage_controller.list_usage(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="short_code_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ShortCodeController") ShortCodeController

### Get controller instance

An instance of the ``` ShortCodeController ``` class can be accessed from the API Client.

```python
 short_code_controller = client.short_code
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
| method |  ``` Optional ```  | Specifies the HTTP method used to request the required URL once the Short Code message is sent.GET or POST |
| messagestatuscallback |  ``` Optional ```  | URL that can be requested to receive notification when Short Code message was sent. |



#### Example Usage

```python
collect = {}

shortcode = 185
collect['shortcode'] = shortcode

to = 185.846174203719
collect['to'] = to

body = 'body'
collect['body'] = body

response_type = 'json'
collect['response_type'] = response_type

method = HttpActionEnum.GET
collect['method'] = method

messagestatuscallback = 'messagestatuscallback'
collect['messagestatuscallback'] = messagestatuscallback


result = short_code_controller.send_dedicated_shortcode(collect)

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


result = short_code_controller.view_shortcode(collect)

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

date_sent = 'DateSent'
collect['date_sent'] = date_sent

page = 1
collect['page'] = page

page_size = 10
collect['page_size'] = page_size


result = short_code_controller.list_shortcode(collect)

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
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | Number of individual resources listed in the response per page |
| mfrom |  ``` Optional ```  | Only list SMS messages sent from this number |
| shortcode |  ``` Optional ```  | Only list SMS messages sent to Shortcode |
| datecreated |  ``` Optional ```  | Only list SMS messages sent in the specified date MAKE REQUEST |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

mfrom = 'From'
collect['mfrom'] = mfrom

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

datecreated = 'Datecreated'
collect['datecreated'] = datecreated


result = short_code_controller.list_inbound_shortcode(collect)

```


### <a name="view_dedicated_shortcode_assignment"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.view_dedicated_shortcode_assignment") view_dedicated_shortcode_assignment

> Retrieve a single Short Code object by its shortcode assignment.

```python
def view_dedicated_shortcode_assignment(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | List of valid Dedicated Short Code to your message360 account |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |



#### Example Usage

```python
collect = {}

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

response_type = 'json'
collect['response_type'] = response_type


result = short_code_controller.view_dedicated_shortcode_assignment(collect)

```


### <a name="update_dedicated_short_code_assignment"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.update_dedicated_short_code_assignment") update_dedicated_short_code_assignment

> Update a dedicated shortcode.

```python
def update_dedicated_short_code_assignment(self,
                                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| shortcode |  ``` Required ```  | List of valid dedicated shortcode to your message360 account. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| friendlyName |  ``` Optional ```  | User generated name of the dedicated shortcode. |
| callbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required StatusCallBackUrl once call connects. |
| callbackUrl |  ``` Optional ```  | URL that can be requested to receive notification when call has ended. A set of default parameters will be sent here once the call is finished. |
| fallbackMethod |  ``` Optional ```  | Specifies the HTTP method used to request the required FallbackUrl once call connects. |
| fallbackUrl |  ``` Optional ```  | URL used if any errors occur during execution of InboundXML or at initial request of the required Url provided with the POST. |



#### Example Usage

```python
collect = {}

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

response_type = 'json'
collect['response_type'] = response_type

friendly_name = 'FriendlyName'
collect['friendly_name'] = friendly_name

callback_method = 'CallbackMethod'
collect['callback_method'] = callback_method

callback_url = 'CallbackUrl'
collect['callback_url'] = callback_url

fallback_method = 'FallbackMethod'
collect['fallback_method'] = fallback_method

fallback_url = 'FallbackUrl'
collect['fallback_url'] = fallback_url


result = short_code_controller.update_dedicated_short_code_assignment(collect)

```


### <a name="list_short_code_assignment"></a>![Method: ](https://apidocs.io/img/method.png ".ShortCodeController.list_short_code_assignment") list_short_code_assignment

> Retrieve a list of Short Code assignment associated with your message360 account.

```python
def list_short_code_assignment(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response type format xml or json |
| shortcode |  ``` Optional ```  | Only list Short Code Assignment sent from this Short Code |
| page |  ``` Optional ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  | The count of objects to return per page. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

shortcode = 'Shortcode'
collect['shortcode'] = shortcode

page = 'page'
collect['page'] = page

pagesize = 'pagesize'
collect['pagesize'] = pagesize


result = short_code_controller.list_short_code_assignment(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="post_card_controller"></a>![Class: ](https://apidocs.io/img/class.png ".PostCardController") PostCardController

### Get controller instance

An instance of the ``` PostCardController ``` class can be accessed from the API Client.

```python
 post_card_controller = client.post_card
```

### <a name="view_postcard"></a>![Method: ](https://apidocs.io/img/method.png ".PostCardController.view_postcard") view_postcard

> Retrieve a postcard object by its PostcardId.

```python
def view_postcard(self,
                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| postcardid |  ``` Required ```  | The unique identifier for a postcard object. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

postcardid = 'postcardid'
collect['postcardid'] = postcardid

response_type = 'json'
collect['response_type'] = response_type


result = post_card_controller.view_postcard(collect)

```


### <a name="create_postcard"></a>![Method: ](https://apidocs.io/img/method.png ".PostCardController.create_postcard") create_postcard

> Create, print, and mail a postcard to an address. The postcard front must be supplied as a PDF, image, or an HTML string. The back can be a PDF, image, HTML string, or it can be automatically generated by supplying a custom message.

```python
def create_postcard(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| to |  ``` Required ```  | The AddressId or an object structured when creating an address by addresses/Create. |
| mfrom |  ``` Required ```  | The AddressId or an object structured when creating an address by addresses/Create. |
| attachbyid |  ``` Required ```  | Set an existing postcard by attaching its PostcardId. |
| front |  ``` Required ```  | A 4.25"x6.25" or 6.25"x11.25" image to use as the front of the postcard.  This can be a URL, local file, or an HTML string. Supported file types are PDF, PNG, and JPEG. |
| back |  ``` Required ```  | A 4.25"x6.25" or 6.25"x11.25" image to use as the back of the postcard, supplied as a URL, local file, or HTML string.  This allows you to customize your back design, but we will still insert the recipient address for you. |
| message |  ``` Required ```  | The message for the back of the postcard with a maximum of 350 characters. |
| setting |  ``` Required ```  | Code for the dimensions of the media to be printed. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |
| description |  ``` Optional ```  | A description for the postcard. |
| htmldata |  ``` Optional ```  | A string value that contains HTML markup. |



#### Example Usage

```python
collect = {}

to = 'to'
collect['to'] = to

mfrom = 'from'
collect['mfrom'] = mfrom

attachbyid = 'attachbyid'
collect['attachbyid'] = attachbyid

front = 'front'
collect['front'] = front

back = 'back'
collect['back'] = back

message = 'message'
collect['message'] = message

setting = 'setting'
collect['setting'] = setting

response_type = 'json'
collect['response_type'] = response_type

description = 'description'
collect['description'] = description

htmldata = 'htmldata'
collect['htmldata'] = htmldata


result = post_card_controller.create_postcard(collect)

```


### <a name="list_postcards"></a>![Method: ](https://apidocs.io/img/method.png ".PostCardController.list_postcards") list_postcards

> Retrieve a list of postcard objects. The postcards objects are sorted by creation date, with the most recently created postcards appearing first.

```python
def list_postcards(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| postcardid |  ``` Optional ```  | The unique identifier for a postcard object. |
| dateCreated |  ``` Optional ```  | The date the postcard was created. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

postcardid = 'postcardid'
collect['postcardid'] = postcardid

date_created = 'dateCreated'
collect['date_created'] = date_created


result = post_card_controller.list_postcards(collect)

```


### <a name="delete_postcard"></a>![Method: ](https://apidocs.io/img/method.png ".PostCardController.delete_postcard") delete_postcard

> Remove a postcard object.

```python
def delete_postcard(self,
                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| postcardid |  ``` Required ```  | The unique identifier of a postcard object. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

postcardid = 'postcardid'
collect['postcardid'] = postcardid

response_type = 'json'
collect['response_type'] = response_type


result = post_card_controller.delete_postcard(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="letter_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LetterController") LetterController

### Get controller instance

An instance of the ``` LetterController ``` class can be accessed from the API Client.

```python
 letter_controller = client.letter
```

### <a name="view_letter"></a>![Method: ](https://apidocs.io/img/method.png ".LetterController.view_letter") view_letter

> Retrieve a letter object by its LetterSid.

```python
def view_letter(self,
                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| lettersid |  ``` Required ```  | The unique identifier for a letter object. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

lettersid = 'lettersid'
collect['lettersid'] = lettersid

response_type = 'json'
collect['response_type'] = response_type


result = letter_controller.view_letter(collect)

```


### <a name="create_letter"></a>![Method: ](https://apidocs.io/img/method.png ".LetterController.create_letter") create_letter

> Create, print, and mail a letter to an address. The letter file must be supplied as a PDF or an HTML string.

```python
def create_letter(self,
                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| to |  ``` Required ```  | The AddressId or an object structured when creating an address by addresses/Create. |
| mfrom |  ``` Required ```  | The AddressId or an object structured when creating an address by addresses/Create. |
| attachbyid |  ``` Required ```  | Set an existing letter by attaching its LetterId. |
| file |  ``` Required ```  | File can be a 8.5"x11" PDF uploaded file or URL that links to a file. |
| color |  ``` Required ```  | Specify if letter should be printed in color. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |
| description |  ``` Optional ```  | A description for the letter. |
| extraservice |  ``` Optional ```  | Add an extra service to your letter. Options are "certified" or "registered". Certified provides tracking and delivery confirmation for domestic destinations and is an additional $5.00. Registered provides tracking and confirmation for international addresses and is an additional $16.50. |
| doublesided |  ``` Optional ```  | Specify if letter should be printed on both sides. |
| template |  ``` Optional ```  | Boolean that defaults to true. When set to false, this specifies that your letter does not follow the m360 address template. In this case, a blank address page will be inserted at the beginning of your file and you will be charged for the extra page. |
| htmldata |  ``` Optional ```  | A string value that contains HTML markup. |



#### Example Usage

```python
collect = {}

to = 'to'
collect['to'] = to

mfrom = 'from'
collect['mfrom'] = mfrom

attachbyid = 'attachbyid'
collect['attachbyid'] = attachbyid

file = 'file'
collect['file'] = file

color = 'color'
collect['color'] = color

response_type = 'json'
collect['response_type'] = response_type

description = 'description'
collect['description'] = description

extraservice = 'extraservice'
collect['extraservice'] = extraservice

doublesided = 'doublesided'
collect['doublesided'] = doublesided

template = 'template'
collect['template'] = template

htmldata = 'htmldata'
collect['htmldata'] = htmldata


result = letter_controller.create_letter(collect)

```


### <a name="list_letters"></a>![Method: ](https://apidocs.io/img/method.png ".LetterController.list_letters") list_letters

> Retrieve a list of letter objects. The letter objects are sorted by creation date, with the most recently created letters appearing first.

```python
def list_letters(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| lettersid |  ``` Optional ```  | The unique identifier for a letter object. |
| dateCreated |  ``` Optional ```  | The date the letter was created. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

lettersid = 'lettersid'
collect['lettersid'] = lettersid

date_created = 'dateCreated'
collect['date_created'] = date_created


result = letter_controller.list_letters(collect)

```


### <a name="delete_letter"></a>![Method: ](https://apidocs.io/img/method.png ".LetterController.delete_letter") delete_letter

> Remove a letter object by its LetterId.

```python
def delete_letter(self,
                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| lettersid |  ``` Required ```  | The unique identifier for a letter object. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

lettersid = 'lettersid'
collect['lettersid'] = lettersid

response_type = 'json'
collect['response_type'] = response_type


result = letter_controller.delete_letter(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="area_mail_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AreaMailController") AreaMailController

### Get controller instance

An instance of the ``` AreaMailController ``` class can be accessed from the API Client.

```python
 area_mail_controller = client.area_mail
```

### <a name="create_area_mail"></a>![Method: ](https://apidocs.io/img/method.png ".AreaMailController.create_area_mail") create_area_mail

> Create a new AreaMail object.

```python
def create_area_mail(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| routes |  ``` Required ```  | List of routes that AreaMail should be delivered to.  A single route can be either a zipcode or a carrier route.List of routes that AreaMail should be delivered to.  A single route can be either a zipcode or a carrier route. A carrier route is in the form of 92610-C043 where the carrier route is composed of 5 numbers for zipcode, 1 letter for carrier route type, and 3 numbers for carrier route code. Delivery can be sent to mutliple routes by separating them with a commas. Valid Values: 92656, 92610-C043 |
| attachbyid |  ``` Required ```  | Set an existing areamail by attaching its AreamailId. |
| front |  ``` Required ```  | The front of the AreaMail item to be created. This can be a URL, local file, or an HTML string. Supported file types are PDF, PNG, and JPEG. Back required |
| back |  ``` Required ```  | The back of the AreaMail item to be created. This can be a URL, local file, or an HTML string. Supported file types are PDF, PNG, and JPEG. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |
| description |  ``` Optional ```  | A string value to use as a description for this AreaMail item. |
| targettype |  ``` Optional ```  | The delivery location type. |
| htmldata |  ``` Optional ```  | A string value that contains HTML markup. |



#### Example Usage

```python
collect = {}

routes = 'routes'
collect['routes'] = routes

attachbyid = 'attachbyid'
collect['attachbyid'] = attachbyid

front = 'front'
collect['front'] = front

back = 'back'
collect['back'] = back

response_type = 'json'
collect['response_type'] = response_type

description = 'description'
collect['description'] = description

targettype = 'targettype'
collect['targettype'] = targettype

htmldata = 'htmldata'
collect['htmldata'] = htmldata


result = area_mail_controller.create_area_mail(collect)

```


### <a name="view_area_mail"></a>![Method: ](https://apidocs.io/img/method.png ".AreaMailController.view_area_mail") view_area_mail

> Retrieve an AreaMail object by its AreaMailId.

```python
def view_area_mail(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| areamailid |  ``` Required ```  | The unique identifier for an AreaMail object. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

areamailid = 'areamailid'
collect['areamailid'] = areamailid

response_type = 'json'
collect['response_type'] = response_type


result = area_mail_controller.view_area_mail(collect)

```


### <a name="list_area_mail"></a>![Method: ](https://apidocs.io/img/method.png ".AreaMailController.list_area_mail") list_area_mail

> Retrieve a list of AreaMail objects.

```python
def list_area_mail(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |
| page |  ``` Optional ```  ``` DefaultValue ```  | The page count to retrieve from the total results in the collection. Page indexing starts at 1. |
| pagesize |  ``` Optional ```  ``` DefaultValue ```  | The count of objects to return per page. |
| areamailsid |  ``` Optional ```  | The unique identifier for an AreaMail object. |
| dateCreated |  ``` Optional ```  | The date the AreaMail was created. |



#### Example Usage

```python
collect = {}

response_type = 'json'
collect['response_type'] = response_type

page = 1
collect['page'] = page

pagesize = 10
collect['pagesize'] = pagesize

areamailsid = 'areamailsid'
collect['areamailsid'] = areamailsid

date_created = 'dateCreated'
collect['date_created'] = date_created


result = area_mail_controller.list_area_mail(collect)

```


### <a name="delete_area_mail"></a>![Method: ](https://apidocs.io/img/method.png ".AreaMailController.delete_area_mail") delete_area_mail

> Remove an AreaMail object by its AreaMailId.

```python
def delete_area_mail(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| areamailid |  ``` Required ```  | The unique identifier for an AreaMail object. |
| responseType |  ``` Required ```  ``` DefaultValue ```  | Response Type either json or xml |



#### Example Usage

```python
collect = {}

areamailid = 'areamailid'
collect['areamailid'] = areamailid

response_type = 'json'
collect['response_type'] = response_type


result = area_mail_controller.delete_area_mail(collect)

```


[Back to List of Controllers](#list_of_controllers)



