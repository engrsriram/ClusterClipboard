# ClusterClipboard
simple code will help in copy , paste work across Cluster of compute

this project will provide helping hand in copy , paste work across cluster . 

this project uses simple Client - Server concept. by using this Server will always keep record of all the copied data , store within itself with user provided 'key'. 

User can use  `clipb` commond line option to save stdin result into make it save in server.  
eg:
`grep "ERROR" | clipb <key>`


When ever User need to get those information , then can simple use `vclipb <key>` with privided key. this will fetch details from the Server with given key and display it into Stdout . 

