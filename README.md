# RASA CHATBOT

### The following points are mentioned in this description.
- About the Chatbot and its framework.
- Aim of this Chatbot
- Machine Configuration on which the bot is deployed


#### About the Chatbot and its framework
This chatbot project is created using Rasa Open Source Framework.

- Rasa Open Source is an open-source conversational AI platform that allows you to understand and hold conversations and connect to messaging channels and third-party systems through a set of APIs. It supplies the 	building blocks for creating virtual (digital) assistants or chatbots

- More details can be viewed on  https://rasa.com/docs/rasa/  site 

- The installation of the framework is done following the steps mentioned in 	https://rasa.com/docs/rasa/installation/installing-rasa-open-source

- The resulting Rasa assistant is installed on a personal machine and developed locally.
- For some machine learning algorithms, we need to install additional python packages as they aren't installed by default to keep the footprint small.

### Aim of this Chatbot
NX developers (Siemens Digital)  could use the chatbot to solve their nxci-based queries. The chatbot holds various documentation which can come in handy to the developers. 
It could be a storage space for all the nx-related documents, links, and custom queries. Build-related can also be resolved by the same. 

Currently, this project ,has implemented and stored the following documentation and custom actions.
- Checking the Status of Code files  and its rejectors
- Documentation
- FAQs about Change package
- FAQs about build on cp
documentation about static analysis
- Library Definition documentation
- Third Party Integration documentation
- Install Feature Validation documentation
- Dpx Validation documentation
- QXDB2 Tools documentation
- udu_common_tasks documentation

### Machine Configuration on which the bot is deployed
The deployment is done on two machines - Windows machine (PC) and on a Linix Machine. The linux machine was accessed remotely via mobaXterm tool.

#### Configuration of machine 1:-
  - Windows Specification 	
  - Edition  	:  Windows 10 Enterprise	
  - Os Build	: 	19042.2130
  - Device Specifications
  - System Type	:	64-bit operating system, x64-based processor
  - Processor	:	11th Gen Intel(R) Core(TM) i5-1145G7 @ 2.60GHz   1.50 GHz
#### Configuration of machine 2:-
-  PLATFORM			:	x86_64 GNU/Linux
- OSVERSION 			:	CentOS Linux release 7.9.2009 (Core)
- MODEL 				:	x86_64
- TOTAL MEMORY : 	32946296 kB
- PROCESSORS 		: 	4
- COMPILER 			:	gcc-4.8.5-44.el7.x86_64

### Location of Chatbot documentation

A word file named Rasa Documentation and a ppt named Chatbot_ppt is present on 
	\\plm\pnnas\nxdata\build_team\BuildDocs\Chatbot files location

##### These files include details like:-
- Installation
- Deployment
- How to add more documents and custom actions to the bot
- Chatbot basics and types 
- Other chatbot frameworks explored. 
- Reasons to choose the Rasa framework 
- About Rasa framework architecture 

###  Site on which the bot is deployed and its details
The bot is deployed on http://nx-ci-dev:88/
	
All the conversations made with the bot are stored in local database. This could further help in tracking the major queries of developers and other major analysis
#### Tracker store  is used to store the conversations.
#### https://rasa.com/docs/rasa/tracker-stores
#### Server where the models are pulled from.
#### https://rasa.com/docs/rasa/model-storage#fetching-models-from-a-server

 
#### Description of every file in this CP
- config.yml                - 	Contains pipelines and policies required for the bot functioning.
- connections.py         - 	Helps to create a DMS database connection to fetch CP details.
- credentials.yml         - 	Contains the credentials for the voice & chat platforms the bot is using.
- domain.yml              - 	Has all intents(from nlu.yml) , actions(from stories.yml), slots,entities and responses stored
- endpoints.yml          - 	Contains the bot's d.fferent endpoints,server where the models are pulled from.
- readme                    - 	Has details of installation , adding more intents and actions in the bot. 
- status_cp.py             - 	The status of various CPs and display messages for the bot are stored in this file. 
- baseline_actions.py - 	Finds the latest available baseline for SubmitCi. 
- cpstatus_actions.py - 	CP number is taken as input by the user, and its details (status, rejectors) are displayed.
- nlu.yml                     - 	All vital training examples for the bot are stored with the corresponding intents.
- rules.yml                  - 	Rules for the bot's conversation are in this file.
- stories.yml               - 	Dialogue-Flow / Scripts for the bot. 
- test_stories.yml        -  To test stories and ensure the proper functioning of the above file.







