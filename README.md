# ClusterClipboard
simple code will help in copy , paste work across Cluster of computer

if you need copy , paste functionality and key based saving function across cluster of machine then this is for you. 

this project will provide helping hand in copy , paste work across cluster . 

this project uses simple Client - Server concept. by using this Server will always keep record of all the copied data , store within itself with user provided 'key'. 

User can use  `clipb` commond line option to save stdin result into make it save in server.  
eg:
`grep "ERROR" | clipb <key>`


When ever User need to get those information , then you can use `vclipb <key>` with assigned key. this will fetch details from the Server for given key and display it into Stdout . 



## setup information 
### SERVER
server.py is server script which is used to record all the copies . 

this should kept in machine from where all the machines can be assible. 

`python server.py`

### CLIENT

clipb   & vclipb both are python script which need to be kept in PATH variable. so that , it can be called from any where. 

example:

`ping google.com  -c 3 | clipb pg`

above command will records 3 ping result and related inforation , and save it in SERVER machine (machine where server.py runs). 
"pg" will act as a key , which can be used to retrive it later. 

to retrive use

 `vclipb pg ` this will do stdout print result into command prompt. 

